@echo off
title ResQRoute - Ambulance Route Optimizer
echo.
echo  ================================
echo   ResQRoute Starting...
echo   URL: http://127.0.0.1:5000
echo  ================================
echo.

cd /d "%~dp0"

:: Open browser after 3 seconds
start "" cmd /c "timeout /t 3 >nul && start http://127.0.0.1:5000"

:: Run Flask using venv python
"%~dp0venv\Scripts\python.exe" "%~dp0app.py"

pause
