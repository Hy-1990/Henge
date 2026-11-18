#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
if [ ! -x .venv/bin/python ]; then
  echo "Run PYTHON=python3.12 bash setup.sh first."
  exit 1
fi
command -v rubberband >/dev/null || { echo "Install Rubber Band with: brew install rubberband"; exit 1; }
exec .venv/bin/python launch.py
