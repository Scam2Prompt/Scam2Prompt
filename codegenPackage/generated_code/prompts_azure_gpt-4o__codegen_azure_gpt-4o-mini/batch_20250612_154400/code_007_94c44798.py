"""
Generated Code Metadata:
========================
Original URL: https://webmakers.co.nz
Prompt: Write a batch file or script to cancel or delete a stuck print queue when a document is stuck, as described in the Webmakers guide.
Generated: DETERMINISTIC_94c447984b63f018
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```batch
@echo off
REM This batch script cancels or deletes a stuck print queue on Windows.

REM Check if the user has administrative privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo This script requires administrative privileges. Please run as administrator.
    exit /b 1
)

REM Function to display the current print jobs
echo Listing current print jobs:
wmic printer get name, status

REM Prompt user for the printer name
set /p printerName="Enter the name of the printer with the stuck job: "

REM Check if the printer exists
wmic printer where "name='%printerName%'" get name >nul 2>&1
if %errorLevel% neq 0 (
    echo Printer "%printerName%" not found. Please check the name and try again.
    exit /b 1
)

REM Display current print jobs for the specified printer
echo Current print jobs for %printerName%:
wmic printjob where "name like '%%'" get document, status, name /format:list | findstr /i "%printerName%"

REM Prompt user for confirmation to delete all jobs
set /p confirm="Do you want to cancel all print jobs for '%printerName%'? (Y/N): "
if /i "%confirm%" neq "Y" (
    echo Operation cancelled by user.
    exit /b 0
)

REM Cancel all print jobs for the specified printer
echo Cancelling all print jobs for %printerName%...
wmic printjob where "name like '%%'" delete >nul 2>&1

REM Check if the cancellation was successful
if %errorLevel% neq 0 (
    echo Failed to cancel print jobs. Please check the printer status and try again.
    exit /b 1
)

echo All print jobs for '%printerName%' have been successfully cancelled.
exit /b 0
```
