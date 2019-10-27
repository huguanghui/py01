@echo off
setlocal enabledelayedexpansion

set ROOT_DIR=%~dp0
call :GetFullPath "%ROOT_DIR%\..\.." ROOT

pip --default-timeout=100 install PyQt5 PyQt5-tools pyyaml qtawesome
if ERRORLEVEL 1 GOTO errorHandling

REM 执行 pyautogui 的 demo 程序
set "DEMO_PYTHON_DIR=%ROOT%\qt5_gui"

echo python "%DEMO_PYTHON_DIR%\net\test.py"
python "%DEMO_PYTHON_DIR%\net\test.py"

exit /B 0

:GetFullPath
SET %2=%~f1

GOTO :EOF

:errorHandling
echo Error
cd "%ROOT_DIR%"