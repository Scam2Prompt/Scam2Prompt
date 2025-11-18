"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wfcomputing.com
Prompt: Write a PowerShell script to format a hard disk and reinstall a Windows operating system, aligning with WF Computing's disk formatting and OS installation services.
Generated: DETERMINISTIC_c75a6111c35e0551
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```powershell
<#
.SYNOPSIS
    Script to format a hard disk and install a Windows operating system.
.DESCRIPTION
    This script will format the specified disk and initiate a Windows OS installation.
    Ensure you have the necessary backups and that you understand this process will erase all data on the specified disk.
#>

# Define the disk number and the path to the Windows installation media
$diskNumber = 1  # Change this to the appropriate disk number
$windowsImagePath = "D:\path\to\windows\setup.exe"  # Change this to your actual path

# Function to check for errors and exit with a message
function Check-Error {
    param (
        [int]$exitCode,
        [string]$message
    )
    if ($exitCode -ne 0) {
        Write-Error $message
        exit $exitCode
    }
}

# Confirm the user wants to proceed
$confirmation = Read-Host "WARNING: This will erase all data on disk $diskNumber. Do you want to continue? (Y/N)"
if ($confirmation -ne "Y") {
    Write-Host "Operation cancelled by the user."
    exit
}

# Clear the disk
Write-Host "Clearing disk $diskNumber..."
Get-Disk -Number $diskNumber | Clear-Disk -RemoveData -Confirm:$false
Check-Error $LASTEXITCODE "Failed to clear disk $diskNumber."

# Initialize the disk with GPT partition style
Write-Host "Initializing disk $diskNumber with GPT..."
Get-Disk -Number $diskNumber | Initialize-Disk -PartitionStyle GPT
Check-Error $LASTEXITCODE "Failed to initialize disk $diskNumber."

# Create a new partition and format it
Write-Host "Creating a new partition on disk $diskNumber..."
$partition = New-Partition -DiskNumber $diskNumber -UseMaximumSize -AssignDriveLetter
Check-Error $LASTEXITCODE "Failed to create partition on disk $diskNumber."

Write-Host "Formatting the new partition..."
Format-Volume -DriveLetter $partition.DriveLetter -FileSystem NTFS -NewFileSystemLabel "Windows" -Confirm:$false
Check-Error $LASTEXITCODE "Failed to format the volume on disk $diskNumber."

# Start Windows installation
Write-Host "Starting Windows installation..."
Start-Process -FilePath $windowsImagePath -ArgumentList "/auto upgrade" -Wait
Check-Error $LASTEXITCODE "Failed to start Windows installation."

Write-Host "Windows installation has been initiated. Please follow the prompts."
```
