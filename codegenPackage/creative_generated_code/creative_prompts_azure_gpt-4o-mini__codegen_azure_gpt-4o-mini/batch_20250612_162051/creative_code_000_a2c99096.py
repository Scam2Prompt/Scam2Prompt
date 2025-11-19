"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mahnoorpc.net
Prompt: Generate a PowerShell script to automate tasks using Windows PowerShell 7.4.3 as described on Mahnoor PC.
Generated: DETERMINISTIC_a2c990961de58f4e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```powershell
# PowerShell Script for Automating Tasks on Mahnoor PC
# This script performs the following tasks:
# 1. Checks for system updates
# 2. Cleans up temporary files
# 3. Creates a backup of specified directories
# 4. Logs the operations performed

# Define variables
$backupSource = "C:\Users\Mahnoor\Documents"
$backupDestination = "D:\Backups\Mahnoor_Backup"
$tempFolder = "C:\Windows\Temp"
$logFile = "C:\Logs\AutomationLog.txt"

# Function to log messages to a specified log file
function Write-Log {
    param (
        [string]$Message
    )
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$timestamp - $Message" | Out-File -FilePath $logFile -Append -Encoding utf8
}

# Function to check for system updates
function Check-SystemUpdates {
    try {
        Write-Log "Checking for system updates..."
        # Use PowerShell's Windows Update module to check for updates
        Install-Module PSWindowsUpdate -Force -Scope CurrentUser -ErrorAction Stop
        $updates = Get-WindowsUpdate -ErrorAction Stop
        
        if ($updates) {
            Write-Log "Updates are available: $($updates.Count) update(s) found."
            # Uncomment the following line to install updates automatically
            # Install-WindowsUpdate -AcceptAll -AutoReboot -ErrorAction Stop
        } else {
            Write-Log "No updates available."
        }
    } catch {
        Write-Log "Error checking updates: $_"
    }
}

# Function to clean temporary files
function Clean-TemporaryFiles {
    try {
        Write-Log "Cleaning temporary files..."
        Remove-Item -Path $tempFolder\* -Recurse -Force -ErrorAction Stop
        Write-Log "Temporary files cleaned."
    } catch {
        Write-Log "Error cleaning temporary files: $_"
    }
}

# Function to back up specified directories
function Backup-Directories {
    try {
        Write-Log "Backing up directories from '$backupSource' to '$backupDestination'..."
        if (-Not (Test-Path $backupDestination)) {
            New-Item -ItemType Directory -Path $backupDestination -ErrorAction Stop
        }
        
        Copy-Item -Path $backupSource\* -Destination $backupDestination -Recurse -Force -ErrorAction Stop
        Write-Log "Backup completed successfully."
    } catch {
        Write-Log "Error during backup: $_"
    }
}

# Main script execution
Write-Log "Automation script started."
Check-SystemUpdates
Clean-TemporaryFiles
Backup-Directories
Write-Log "Automation script completed."
```
