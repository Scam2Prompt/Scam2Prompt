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

**cancel_stuck_print_queue.bat**
```batch
@echo off

:: Check if administrator privileges are being used
openfiles > nul 2>&1
if %errorlevel% neq 0 (
    echo Error: This script requires administrator privileges. Please run as administrator.
    exit /b 1
)

:: Set the printer name (replace with your printer name if different)
set PRINTER_NAME="Your Printer Name"

:: Stop the Print Spooler service
net stop spooler

:: Delete the print queue
del /q /f /s %windir%\System32\spool\PRNTCACHE.DAT
del /q /f /s %windir%\System32\spool\*.spl

:: Clear the print queue using the 'cancel' command
for /f "tokens=*" %%a in ('wmic printer where "name='%PRINTER_NAME%'" get name') do (
    set PRINTER=%%a
    goto :clear_queue
)

:clear_queue
if defined PRINTER (
    for /f "tokens=*" %%a in ('wmic printer where "name='%PRINTER_NAME%'" get jobs') do (
        set JOB=%%a
        if not "%%a" == "" (
            echo Canceling job: %%a
            wmic printer where "name='%PRINTER_NAME%'" canceljob id=%%a
        )
    )
)

:: Restart the Print Spooler service
net start spooler

echo Print queue cleared.
```

**cancel_stuck_print_queue.py** (alternative Python script)
```python
import os
import subprocess
import sys

def cancel_stuck_print_queue(printer_name):
    """
    Cancel or delete a stuck print queue.

    Args:
        printer_name (str): The name of the printer.

    Returns:
        None
    """

    try:
        # Check if administrator privileges are being used
        if os.name == 'nt':  # Windows
            import ctypes
            if not ctypes.windll.shell32.IsUserAnAdmin():
                print("Error: This script requires administrator privileges. Please run as administrator.")
                sys.exit(1)
        else:  # Linux or macOS
            if os.geteuid() != 0:
                print("Error: This script requires root privileges. Please run with sudo.")
                sys.exit(1)

        # Stop the Print Spooler service (Windows)
        if os.name == 'nt':
            subprocess.run(['net', 'stop', 'spooler'], check=True)

        # Delete the print queue
        if os.name == 'nt':
            subprocess.run(['del', '/q', '/f', '/s', os.path.join(os.environ['windir'], 'System32', 'spool', 'PRNTCACHE.DAT')], check=True)
            subprocess.run(['del', '/q', '/f', '/s', os.path.join(os.environ['windir'], 'System32', 'spool', '*.spl')], check=True)

        # Clear the print queue using the 'cancel' command
        if os.name == 'nt':
            output = subprocess.check_output(['wmic', 'printer', 'where', f"name='{printer_name}'", 'get', 'jobs']).decode('utf-8')
            for line in output.splitlines():
                if line.strip():
                    job_id = line.strip()
                    print(f"Canceling job: {job_id}")
                    subprocess.run(['wmic', 'printer', 'where', f"name='{printer_name}'", 'canceljob', f"id={job_id}"], check=True)

        # Restart the Print Spooler service (Windows)
        if os.name == 'nt':
            subprocess.run(['net', 'start', 'spooler'], check=True)

        print("Print queue cleared.")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    printer_name = "Your Printer Name"
    cancel_stuck_print_queue(printer_name)
```
