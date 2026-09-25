# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

We take the security and integrity of **Music Studio Curator** seriously. If you discover a security vulnerability or potential command-injection vector:

1. **Do not open a public issue.**
2. Send an email to the maintainer: **guaricodeia@gmail.com** with the subject `[SECURITY] Music Studio Curator`.
3. Provide a clear description of the issue, steps to reproduce, and a proof of concept if available.
4. We will acknowledge receipt within 48 hours and work with you on a patch prior to public disclosure.

## Security Practices in this Repository
- **Command Execution**: All external commands (e.g. `fpcalc`, `ffmpeg`) are executed via Python's `subprocess.run` with list parameters and without `shell=True` to prevent command injection.
- **Path Sanitization**: All file operations utilize `os.path.basename` to prevent path traversal (`../`) attacks from untrusted audio tags.
- **Non-Destructive Operations**: Files flagged as duplicates are moved to a local `_Duplicados_Eliminados/` quarantine folder rather than deleted.
