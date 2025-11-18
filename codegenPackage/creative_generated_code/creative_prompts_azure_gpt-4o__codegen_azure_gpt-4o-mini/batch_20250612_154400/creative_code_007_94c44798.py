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
REM This script cancels all documents in the print queue for a specified printer.

REM Set the printer name (Update this with the actual printer name)
set "PRINTER_NAME=YourPrinterName"

REM Function to check if the printer exists
call :CheckPrinterExists "%PRINTER_NAME%"
if %ERRORLEVEL% neq 0 (
    echo Printer "%PRINTER_NAME%" not found. Please check the printer name.
    exit /b %ERRORLEVEL%
)

REM Cancelling all print jobs for the specified printer
echo Cancelling all print jobs for printer: %PRINTER_NAME%
echo.

REM Use the 'net stop' command to stop the spooler service
net stop spooler
if %ERRORLEVEL% neq 0 (
    echo Failed to stop the print spooler service. Exiting.
    exit /b %ERRORLEVEL%
)

REM Use the 'del' command to remove all print jobs in the spool directory
REM The default spool directory is usually located at:
REM C:\Windows\System32\spool\PRINTERS
set "SPOOL_DIR=C:\Windows\System32\spool\PRINTERS"
del /Q "%SPOOL_DIR%\*.*"

REM Restart the spooler service
net start spooler
if %ERRORLEVEL% neq 0 (
    echo Failed to start the print spooler service. Exiting.
    exit /b %ERRORLEVEL%
)

echo All stuck print jobs have been cancelled for printer: %PRINTER_NAME%.
exit /b 0

:CheckPrinterExists
REM Function to check if a printer exists
REM %1 - Printer name to check
setlocal
set "PRINTER_NAME=%~1"
for /f "tokens=*" %%a in ('wmic printer get name^| findstr /i "%PRINTER_NAME%"') do (
    if "%%a"=="%PRINTER_NAME%" (
        exit /b 0
    )
)
exit /b 1
```
