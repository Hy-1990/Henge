# Release policy

Every fix must ship with a GitHub Release. All release descriptions are in English.

## Before merging

1. Bump `VERSION` using semantic versioning: patch for fixes, minor for backward-compatible features, major for breaking changes.
2. Add a dated section to `CHANGELOG.md` matching that version. Describe the user-visible changes, validation, and known limitations in English.
3. Use an English commit subject. Preserve upstream copyright and attribution.
4. Run the offline checks in the README. Do not submit paid generations as part of CI.

## Automated publication

The `Desktop checks and release` workflow runs the full offline application tests
and JavaScript checks on native Windows and macOS runners. Pull requests run
checks without publishing. A push to `main` publishes only after both jobs succeed.

The release tag is `v` followed by `VERSION`. An already-used tag must point at the
same commit; otherwise validation fails and the version must be bumped. A manual
workflow dispatch or rerun can retry a failed publication at the same commit.
Existing published releases are not overwritten.

Assets:

- `Henge-vX.Y.Z-windows.zip`: tracked source with Windows installation scripts.
- `Henge-vX.Y.Z-macos.tar.gz`: tracked source with macOS installation scripts.
- `SHA256SUMS.txt`: SHA-256 hashes of both archives.

These are source packages, not standalone installers. They do not bundle Python,
Rubber Band, virtual environments, credentials, local runs, or downloaded models.
The archives are created from the exact tested commit, not the runner's directory.

## Checks and limits

Native CI covers dependency installation, credential backend loading, process
locking, mocked provider recovery, source-audio preservation, media compositing,
browser-storage migration, and upload validation. CI does not open a browser,
prompt the user to store real credentials, or submit paid generation tasks.

Optional face-mesh installation and real paid workflow quality still require
separate verification on the target OS. Do not describe a release as fully
end-to-end tested on Windows until a real Windows run has been completed.

If checks or publishing fail, fix the failure and rerun; do not bypass checks or
claim the release has shipped. Users can find the changes for each version in
both its GitHub Release and `CHANGELOG.md`.
