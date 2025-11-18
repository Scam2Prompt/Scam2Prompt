"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmakers.co.nz
Prompt: Write a batch file or script to cancel or delete a stuck print queue when a document is stuck, as described in the Webmakers guide.
Generated: DETERMINISTIC_94c447984b63f018
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```batch
@echo off
:: Script to clear the print queue and cancel stuck print jobs
:: Works on Windows systems

:: Request elevated permissions if not run as administrator
NET FILE >nul 2>&1
if %errorlevel% neq 0 (
    echo This script requires administrative privileges. Restarting with elevated permissions...
    powershell -Command "Start-Process '%0' -Verb RunAs"
    exit /b
)

:: Stop the Print Spooler service
echo Stopping the Print Spooler service...
net stop spooler >nul 2>&1
if %errorlevel% neq 0 (
    echo Failed to stop the Print Spooler service. Please check your system.
    exit /b
)

:: Delete all files in the print queue folder
echo Clearing the print queue...
del /Q /F "%systemroot%\System32\spool\PRINTERS\*" >nul 2>&1
if %errorlevel% neq 0 (
    echo Failed to clear the print queue. Please check your system.
    exit /b
)

:: Start the Print Spooler service
echo Restarting the Print Spooler service...
net start spooler >nul 2>&1
if %errorlevel% neq 0 (
    echo Failed to start the Print Spooler service. Please check your system.
    exit /b
)

:: Completion message
echo The print queue has been successfully cleared.
exit /b
```
