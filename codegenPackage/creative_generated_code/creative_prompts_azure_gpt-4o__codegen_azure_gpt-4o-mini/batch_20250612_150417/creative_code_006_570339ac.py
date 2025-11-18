"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myantispyware.com
Prompt: Write a batch script to reset Internet Explorer settings to default, using the instructions from MyAntiSpyware.com.
Generated: DETERMINISTIC_570339accc252049
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```batch
@echo off
:: Batch script to reset Internet Explorer settings to default
:: Author: Your Name
:: Date: YYYY-MM-DD
:: Purpose: This script resets Internet Explorer settings to their default values.

:: Function to reset Internet Explorer settings
:ResetIESettings
echo Resetting Internet Explorer settings to default...

:: Check if Internet Explorer is installed
if not exist "%ProgramFiles%\Internet Explorer\iexplore.exe" (
    echo Internet Explorer is not installed on this system.
    exit /b 1
)

:: Use the 'inetcpl.cpl' utility to open Internet Options
start /wait inetcpl.cpl

:: Set default settings by running the command below
:: Note: This may require administrative privileges
:: Use 'reg delete' to reset specific registry keys related to IE settings

:: Reset security zones
echo Resetting security zones...
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones" /f
if %errorlevel% neq 0 (
    echo Failed to reset security zones. Exiting...
    exit /b 1
)

:: Reset advanced settings
echo Resetting advanced settings...
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\Main" /v "Secondary Start and Home Page" /f
if %errorlevel% neq 0 (
    echo Failed to reset advanced settings. Exiting...
    exit /b 1
)

:: Reset homepage
echo Resetting homepage...
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\Main" /v "Start Page" /f
if %errorlevel% neq 0 (
    echo Failed to reset homepage. Exiting...
    exit /b 1
)

:: Reset all settings
echo Resetting all Internet Explorer settings...
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer" /f
if %errorlevel% neq 0 (
    echo Failed to reset all Internet Explorer settings. Exiting...
    exit /b 1
)

echo Internet Explorer has been reset to its default settings successfully.

:: End of script
exit /b 0
```
