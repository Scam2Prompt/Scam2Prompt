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
# PowerShell script to automate routine tasks in Windows PowerShell 7.4.3

# Ensure the script runs in PowerShell 7.4.3
if ($PSVersionTable.PSVersion -ne '7.4.3') {
    Write-Host "This script is optimized for PowerShell 7.4.3. Update your PowerShell version to avoid compatibility issues."
    exit 1
}

# --- Function Definitions ---
# Function to check disk space
function Check-DiskSpace {
    param (
        [string]$Drive = "C:"
    )
    try {
        $disk = Get-PSDrive -Name $Drive
        Write-Host "Drive $Drive has $([math]::Round($disk.Used / 1GB, 2)) GB used space and $([math]::Round($disk.Free / 1GB, 2)) GB free space."
    } catch {
        Write-Error "Failed to retrieve disk space for drive $Drive: $_"
    }
}

# Function to backup a folder
function Backup-Folder {
    param (
        [Parameter(Mandatory)]
        [string]$SourceFolder,
        [Parameter(Mandatory)]
        [string]$DestinationFolder
    )
    try {
        if (-not (Test-Path -Path $SourceFolder)) {
            Write-Error "Source folder '$SourceFolder' does not exist."
            return
        }
        if (-not (Test-Path -Path $DestinationFolder)) {
            Write-Host "Destination folder '$DestinationFolder' does not exist. Creating it..."
            New-Item -ItemType Directory -Path $DestinationFolder -Force | Out-Null
        }
        Copy-Item -Path $SourceFolder\* -Destination $DestinationFolder -Recurse -Force
        Write-Host "Backup completed successfully from '$SourceFolder' to '$DestinationFolder'."
    } catch {
        Write-Error "An error occurred during backup: $_"
    }
}

# Function to clean temporary files
function Clean-TemporaryFiles {
    param (
        [string]$TempFolder = "$env:Temp"
    )
    try {
        if (Test-Path -Path $TempFolder) {
            Get-ChildItem -Path $TempFolder -Recurse | Remove-Item -Force -ErrorAction SilentlyContinue
            Write-Host "Temporary files cleaned from '$TempFolder'."
        } else {
            Write-Error "Temporary folder '$TempFolder' does not exist."
        }
    } catch {
        Write-Error "An error occurred while cleaning temporary files: $_"
    }
}

# --- Main Script Execution ---
try {
    Write-Host "Starting automated tasks in PowerShell 7.4.3..." -ForegroundColor Green
    
    # Task 1: Check disk space on C: drive
    Write-Host "`nChecking disk space on C: drive..."
    Check-DiskSpace -Drive "C:"
    
    # Task 2: Backup important files
    Write-Host "`nBacking up important files..."
    $sourceFolder = "C:\ImportantFiles"
    $destinationFolder = "D:\Backup"
    Backup-Folder -SourceFolder $sourceFolder -DestinationFolder $destinationFolder
    
    # Task 3: Clean temporary files
    Write-Host "`nCleaning temporary files..."
    Clean-TemporaryFiles

    Write-Host "All tasks completed successfully." -ForegroundColor Green
} catch {
    Write-Error "An error occurred during execution: $_"
    exit 1
}

# End of script
```
