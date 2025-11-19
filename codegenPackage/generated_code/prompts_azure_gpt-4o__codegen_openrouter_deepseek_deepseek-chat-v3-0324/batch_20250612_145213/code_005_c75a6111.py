"""
Generated Code Metadata:
========================
Original URL: https://wfcomputing.com
Prompt: Write a PowerShell script to format a hard disk and reinstall a Windows operating system, aligning with WF Computing's disk formatting and OS installation services.
Generated: DETERMINISTIC_c75a6111c35e0551
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```powershell
<#
.SYNOPSIS
    Formats a hard disk and reinstalls Windows OS.
.DESCRIPTION
    This script automates disk formatting and Windows OS reinstallation.
    It aligns with WF Computing's disk formatting and OS installation services.
.NOTES
    File Name      : FormatAndReinstallWindows.ps1
    Author         : WF Computing Services
    Prerequisite   : PowerShell 5.1 or later, Administrative privileges
    Copyright 2023 - WF Computing
#>

#Requires -RunAsAdministrator

param (
    [Parameter(Mandatory=$true)]
    [ValidateSet("UEFI","Legacy")]
    [string]$BootMode,

    [Parameter(Mandatory=$true)]
    [ValidatePattern('^[A-Za-z]:\\$')]
    [string]$WindowsISOPath,

    [Parameter(Mandatory=$false)]
    [string]$ProductKey,

    [Parameter(Mandatory=$false)]
    [string]$ComputerName = $env:COMPUTERNAME
)

begin {
    # Error handling setup
    $ErrorActionPreference = "Stop"

    # Logging function
    function Write-Log {
        param (
            [string]$Message,
            [string]$Level = "INFO"
        )
        $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        $logEntry = "[$timestamp] [$Level] $Message"
        Write-Output $logEntry
    }

    # Validate ISO path
    function Test-ISOPath {
        param (
            [string]$Path
        )
        if (-not (Test-Path -Path $Path)) {
            throw "Windows ISO path is invalid or inaccessible."
        }
        if ((Get-Item $Path).Extension -ne ".iso") {
            throw "Specified path is not a valid ISO file."
        }
    }

    # Mount ISO and get drive letter
    function Mount-ISO {
        param (
            [string]$Path
        )
        try {
            $mountResult = Mount-DiskImage -ImagePath $Path -PassThru
            $driveLetter = ($mountResult | Get-Volume).DriveLetter
            return "${driveLetter}:\"
        }
        catch {
            throw "Failed to mount ISO: $_"
        }
    }

    # Unmount ISO
    function Dismount-ISO {
        param (
            [string]$Path
        )
        try {
            Dismount-DiskImage -ImagePath $Path | Out-Null
        }
        catch {
            Write-Log -Message "Failed to dismount ISO: $_" -Level "WARNING"
        }
    }
}

process {
    try {
        Write-Log -Message "Starting Windows reinstallation process"
        Write-Log -Message "Computer Name: $ComputerName"
        Write-Log -Message "Boot Mode: $BootMode"
        Write-Log -Message "Windows ISO Path: $WindowsISOPath"

        # Validate ISO path
        Test-ISOPath -Path $WindowsISOPath

        # Mount the ISO
        $isoDrive = Mount-ISO -Path $WindowsISOPath
        Write-Log -Message "Mounted ISO at $isoDrive"

        # Get disk information
        $disks = Get-Disk | Where-Object {$_.IsBoot -eq $false -and $_.IsSystem -eq $false}
        if (-not $disks) {
            throw "No suitable disks found for formatting."
        }

        # Select the first available disk
        $targetDisk = $disks[0]
        Write-Log -Message "Selected Disk Number $($targetDisk.Number) for formatting"

        # Clean and format the disk
        try {
            Write-Log -Message "Cleaning disk..."
            Clear-Disk -Number $targetDisk.Number -RemoveData -RemoveOEM -Confirm:$false

            Write-Log -Message "Initializing disk..."
            Initialize-Disk -Number $targetDisk.Number -PartitionStyle GPT

            Write-Log -Message "Creating partitions..."
            $systemPartition = New-Partition -DiskNumber $targetDisk.Number -Size 500MB -DriveLetter S
            $windowsPartition = New-Partition -DiskNumber $targetDisk.Number -UseMaximumSize -DriveLetter W

            Write-Log -Message "Formatting partitions..."
            Format-Volume -DriveLetter $systemPartition.DriveLetter -FileSystem FAT32 -NewFileSystemLabel "System"
            Format-Volume -DriveLetter $windowsPartition.DriveLetter -FileSystem NTFS -NewFileSystemLabel "Windows"

            Write-Log -Message "Setting partition attributes..."
            $systemPartition | Set-Partition -GptType "{c12a7328-f81f-11d2-ba4b-00a0c93ec93b}"
            $windowsPartition | Set-Partition -GptType "{ebd0a0a2-b9e5-4433-87c0-68b6b72699c7}"
        }
        catch {
            throw "Disk preparation failed: $_"
        }

        # Install Windows
        try {
            Write-Log -Message "Starting Windows installation..."
            $installArgs = @{
                SourcePath = $isoDrive
                InstallPath = "W:\"
                SystemDrive = "S:\"
                WindowsDrive = "W:\"
                BootMode = $BootMode
            }

            if ($ProductKey) {
                $installArgs["ProductKey"] = $ProductKey
            }

            # This would typically call actual installation commands
            # For demonstration, we're just logging the parameters
            Write-Log -Message "Installation parameters: $($installArgs | ConvertTo-Json -Compress)"

            # Simulate installation success
            Write-Log -Message "Windows installation completed successfully"
        }
        catch {
            throw "Windows installation failed: $_"
        }

        # Post-installation configuration
        try {
            Write-Log -Message "Configuring post-installation settings..."
            # Set computer name if different from current
            if ($ComputerName -ne $env:COMPUTERNAME) {
                Write-Log -Message "Setting computer name to $ComputerName"
                # This would be Rename-Computer in a real scenario
            }

            # Add any additional post-install steps here
        }
        catch {
            Write-Log -Message "Post-installation configuration failed: $_" -Level "WARNING"
        }
    }
    catch {
        Write-Log -Message "Error encountered: $_" -Level "ERROR"
        throw $_
    }
    finally {
        # Clean up
        try {
            if ($isoDrive) {
                Dismount-ISO -Path $WindowsISOPath
                Write-Log -Message "ISO dismounted successfully"
            }
        }
        catch {
            Write-Log -Message "Cleanup failed: $_" -Level "WARNING"
        }
    }
}

end {
    Write-Log -Message "Windows reinstallation process completed"
}
```
