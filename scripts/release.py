"""Validate release metadata and package tracked source without local secrets."""
import argparse
import hashlib
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def metadata():
    version = (ROOT / "VERSION").read_text().strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("VERSION must use MAJOR.MINOR.PATCH.")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    match = re.search(r"^## " + re.escape(version) + r" - \d{4}-\d{2}-\d{2}\n(.*?)(?=^## |\Z)", changelog, re.M | re.S)
    if not match or not match.group(1).strip():
        raise ValueError("Add a dated English CHANGELOG.md entry for VERSION.")
    return version, match.group(1).strip() + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    version, notes = metadata()
    tag = "v" + version
    old = subprocess.run(["git", "rev-parse", "--verify", f"refs/tags/{tag}^{{commit}}"], cwd=ROOT, capture_output=True, text=True)
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    if old.returncode == 0 and old.stdout.strip() != head:
        raise ValueError(f"{tag} already belongs to another commit. Bump VERSION and update CHANGELOG.md.")
    if args.output:
        output = args.output.resolve()
        output.mkdir(parents=True, exist_ok=True)
        checksums = []
        for platform, extension, fmt in (("windows", "zip", "zip"), ("macos", "tar.gz", "tar.gz")):
            name = f"Henge-{tag}-{platform}.{extension}"
            target = output / name
            subprocess.run(["git", "archive", f"--format={fmt}", f"--prefix=Henge-{tag}/", f"--output={target}", "HEAD"], cwd=ROOT, check=True)
            checksums.append(f"{hashlib.sha256(target.read_bytes()).hexdigest()}  {name}\n")
        (output / "SHA256SUMS.txt").write_text("".join(checksums), encoding="utf-8")
        (output / "release-notes.md").write_text(notes, encoding="utf-8")
    print(tag)


if __name__ == "__main__":
    main()
