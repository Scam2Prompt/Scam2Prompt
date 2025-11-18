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
    Formats a hard disk and reinstalls Windows operating system.

.DESCRIPTION
    This script automates the process of formatting a hard disk and reinstalling a Windows OS.
    It is designed for WF Computing's disk formatting and OS installation services.
    This script should be run with administrative privileges.
    Ensure all data on the target disk is backed up before running, as this operation is destructive.

.NOTES
    - Requires Windows installation media (ISO) or pre-configured deployment source.
    - Use caution when specifying the target disk.

.PARAMETER TargetDiskNumber
    The disk number of the target hard disk to format and install the OS.

.PARAMETER WindowsISOPath
    The path to the Windows installation ISO file.

.EXAMPLE
    .\ReinstallWindows.ps1 -TargetDiskNumber 0 -WindowsISOPath "C:\Sources\Windows.iso"
#>

param (
    [Parameter(Mandatory = $true)]
    [int]$TargetDiskNumber,  # Target disk number (e.g., 0 for Disk 0)

    [Parameter(Mandatory = $true)]
    [string]$WindowsISOPath   # Path to the Windows installation ISO file
)

# Ensure script is run with administrative privileges
if (-not ([Security.Principal.WindowsPrincipal]([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Error "This script must be run as an Administrator."
    exit 1
}

# Function to validate Windows ISO path
function Validate-WindowsISO {
    param (
        [string]$ISOPath
    )
    if (-not (Test-Path $ISOPath)) {
        throw "The specified ISO file path '$ISOPath' does not exist."
    }
}

# Function to format the target disk
function Format-Disk {
    param (
        [int]$DiskNumber
    )
    try {
        # Verify the disk exists
        $disk = Get-Disk -Number $DiskNumber -ErrorAction Stop
        if ($disk.IsBoot) {
            throw "Cannot format the boot disk. Please specify another disk."
        }

        # Clean the disk
        Write-Host "Cleaning Disk $DiskNumber..." -ForegroundColor Yellow
        $disk | Clear-Disk -RemoveData -Confirm:$false

        # Initialize the disk
        Write-Host "Initializing Disk $DiskNumber..." -ForegroundColor Yellow
        $disk | Initialize-Disk -PartitionStyle GPT

        # Create primary partition and format it
        Write-Host "Creating and formatting partition on Disk $DiskNumber..." -ForegroundColor Yellow
        $partition = $disk | New-Partition -UseMaximumSize -AssignDriveLetter
        $partition | Format-Volume -FileSystem NTFS -Confirm:$false -Force

        Write-Host "Disk $DiskNumber has been successfully formatted." -ForegroundColor Green
    } catch {
        Write-Error "Failed to format disk: $_"
        exit 1
    }
}

# Function to mount the ISO file
function Mount-WindowsISO {
    param (
        [string]$ISOPath
    )
    try {
        Write-Host "Mounting ISO file from '$ISOPath'..." -ForegroundColor Yellow
        $mountResult = Mount-DiskImage -ImagePath $ISOPath -ErrorAction Stop
        $MountedDriveLetter = ($mountResult | Get-Volume).DriveLetter
        Write-Host "ISO file mounted successfully to drive $MountedDriveLetter." -ForegroundColor Green
        return $MountedDriveLetter
    } catch {
        Write-Error "Failed to mount ISO file: $_"
        exit 1
    }
}

# Function to start Windows installation
function Start-WindowsInstallation {
    param (
        [string]$SourceDriveLetter,
        [string]$TargetDriveLetter
    )
    try {
        Write-Host "Starting Windows installation from $SourceDriveLetter to $TargetDriveLetter..." -ForegroundColor Yellow
        # Running Windows setup
        Start-Process -FilePath "$SourceDriveLetter\setup.exe" -ArgumentList "/auto upgrade", "/unattend", "/INSTALL", "/DynamicUpdate disable" -Wait
        Write-Host "Windows installation initiated successfully." -ForegroundColor Green
    } catch {
        Write-Error "Failed to start Windows installation: $_"
        exit 1
    }
}

# Validate Windows ISO path
Validate-WindowsISO -ISOPath $WindowsISOPath

# Format the target disk
Format-Disk -DiskNumber $TargetDiskNumber

# Mount the Windows ISO
$DriveLetterISO = Mount-WindowsISO -ISOPath $WindowsISOPath

# Get the newly formatted partition letter
$NewPartitionDriveLetter = Get-Partition -DiskNumber $TargetDiskNumber | Get-Volume | Select-Object -ExpandProperty DriveLetter

# Start installation
Start-WindowsInstallation -SourceDriveLetter $DriveLetterISO -TargetDriveLetter $NewPartitionDriveLetter

# Cleanup: Unmount the ISO
Write-Host "Unmounting ISO file..." -ForegroundColor Yellow
Dismount-DiskImage -ImagePath $WindowsISOPath
Write-Host "ISO file unmounted successfully." -ForegroundColor Green

Write-Host "Process completed successfully." -ForegroundColor Green
```
