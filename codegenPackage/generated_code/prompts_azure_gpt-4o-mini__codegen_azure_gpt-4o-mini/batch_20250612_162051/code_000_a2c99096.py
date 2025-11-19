"""
Generated Code Metadata:
========================
Original URL: https://mahnoorpc.net
Prompt: Generate a PowerShell script to automate tasks using Windows PowerShell 7.4.3 as described on Mahnoor PC.
Generated: DETERMINISTIC_a2c990961de58f4e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```powershell
# PowerShell Script to Automate Tasks on Mahnoor PC
# Version: 1.0
# Author: [Your Name]
# Date: [Current Date]
# This script automates the following tasks:
# 1. Check for Windows updates
# 2. Clean up temporary files
# 3. Backup specified directories

# Define variables
$backupSource = "C:\Users\Mahnoor\Documents"
$backupDestination = "D:\Backup\Documents"
$tempPath = "C:\Windows\Temp"
$updateSession = New-Object -ComObject Microsoft.Update.Session

# Function to check for Windows updates
function Check-WindowsUpdates {
    try {
        Write-Host "Checking for Windows updates..."
        $updateSearcher = $updateSession.CreateUpdateSearcher()
        $searchResult = $updateSearcher.Search("IsInstalled=0")
        
        if ($searchResult.Updates.Count -gt 0) {
            Write-Host "$($searchResult.Updates.Count) updates available."
            # Uncomment the following line to install updates automatically
            # $updateInstaller = $updateSession.CreateUpdateInstaller()
            # $updateInstaller.Updates = $searchResult.Updates
            # $updateInstaller.Install()
        } else {
            Write-Host "No updates available."
        }
    } catch {
        Write-Error "Failed to check for updates: $_"
    }
}

# Function to clean up temporary files
function Clean-TempFiles {
    try {
        Write-Host "Cleaning up temporary files..."
        Remove-Item "$tempPath\*" -Recurse -Force -ErrorAction Stop
        Write-Host "Temporary files cleaned up successfully."
    } catch {
        Write-Error "Failed to clean temporary files: $_"
    }
}

# Function to backup specified directories
function Backup-Directories {
    param (
        [string]$source,
        [string]$destination
    )

    try {
        Write-Host "Backing up files from $source to $destination..."
        if (-Not (Test-Path $source)) {
            throw "Source path does not exist: $source"
        }
        if (-Not (Test-Path $destination)) {
            New-Item -ItemType Directory -Path $destination -ErrorAction Stop
        }
        Copy-Item -Path "$source\*" -Destination $destination -Recurse -Force -ErrorAction Stop
        Write-Host "Backup completed successfully."
    } catch {
        Write-Error "Backup failed: $_"
    }
}

# Main script execution
try {
    Check-WindowsUpdates
    Clean-TempFiles
    Backup-Directories -source $backupSource -destination $backupDestination
} catch {
    Write-Error "An error occurred during script execution: $_"
}
```
