# Changelog

All release notes are written in English. Each fix receives a new patch version
and a GitHub Release after the macOS and Windows checks pass.

## 0.1.0 - 2026-11-18

### Fixed
- Isolate retry-route tests from real OS credentials so clean Windows/macOS environments exercise the same behavior as a configured desktop.
- Show actionable setup instructions when the macOS launcher cannot find its virtual environment or Rubber Band.
- Document first installation, updates, daily startup, and offline verification for both Windows and macOS.

### Added
- Automated versioned GitHub Releases after successful native Windows and macOS checks.
- Downloadable Windows ZIP and macOS tar.gz source packages, English release notes, and SHA-256 checksums.
- A release policy requiring a version bump and an English changelog entry for every fix.

### Validation
- CI installs the application dependencies and runs the complete offline Python suite, media-compositing check, and JavaScript checks on Windows and macOS.
- No paid provider requests are made by release checks.

### Known limitations
- Packages contain source code, not standalone executables; Python 3.12 and Rubber Band must be installed separately.
- Face mesh is optional and uses a separate Python 3.12 environment.
- Full paid generation has been verified on macOS; a real Windows paid generation run remains unverified.
