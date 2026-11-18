@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Run setup.cmd first.
  exit /b 1
)
where rubberband >nul 2>&1
if errorlevel 1 (
  echo Rubber Band is missing. Add rubberband.exe to PATH, then reopen this terminal.
  exit /b 1
)
".venv\Scripts\python.exe" launch.py
