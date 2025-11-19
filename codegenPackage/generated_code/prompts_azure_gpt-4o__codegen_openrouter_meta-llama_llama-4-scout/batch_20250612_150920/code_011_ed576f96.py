"""
Generated Code Metadata:
========================
Original URL: https://edukacija.net
Prompt: Generate a PowerShell script for automating tasks in Windows Server 2012, referencing the training materials from edukacija.net.
Generated: DETERMINISTIC_ed576f96a69cfecc
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```powershell
# PowerShell Script for Automating Tasks in Windows Server 2012
# Based on training materials from edukacija.net

# Define a function to automate tasks
function Automate-Tasks {
    <#
    .SYNOPSIS
        Automates tasks in Windows Server 2012.

    .DESCRIPTION
        This function automates tasks such as:
        - Checking system updates
        - Checking disk space
        - Checking event logs

    .PARAMETER UpdateCheck
        Switch to check for system updates.

    .PARAMETER DiskSpaceCheck
        Switch to check disk space.

    .PARAMETER EventLogCheck
        Switch to check event logs.
    #>

    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $false)]
        [switch]$UpdateCheck,

        [Parameter(Mandatory = $false)]
        [switch]$DiskSpaceCheck,

        [Parameter(Mandatory = $false)]
        [switch]$EventLogCheck
    )

    # Check system updates
    if ($UpdateCheck) {
        Write-Host "Checking for system updates..."
        try {
            $updates = New-Object -ComObject "Microsoft.Update.AutoUpdate"
            $updates.CheckNow()
            $updates.Refresh()
            $updates.GetTotalHistoryCount()
            $updates.GetLastInstallationSuccessDate()
        }
        catch {
            Write-Error "Failed to check for system updates: $($Error[0].Message)"
        }
    }

    # Check disk space
    if ($DiskSpaceCheck) {
        Write-Host "Checking disk space..."
        try {
            $diskSpace = Get-WmiObject -Class Win32_LogicalDisk -Filter "Size > 0"
            foreach ($disk in $diskSpace) {
                $usedSpace = [math]::Round(($disk.Size - $disk.FreeSpace) / 1GB, 2)
                $totalSpace = [math]::Round($disk.Size / 1GB, 2)
                $freeSpace = [math]::Round($disk.FreeSpace / 1GB, 2)
                Write-Host "Drive $($disk.DeviceID) - Used: $usedSpace GB, Total: $totalSpace GB, Free: $freeSpace GB"
            }
        }
        catch {
            Write-Error "Failed to check disk space: $($Error[0].Message)"
        }
    }

    # Check event logs
    if ($EventLogCheck) {
        Write-Host "Checking event logs..."
        try {
            $eventLogs = Get-WmiObject -Class Win32_NTEventLogFile
            foreach ($log in $eventLogs) {
                Write-Host "Log: $($log.Name) - Size: $($log.Size) bytes"
            }
        }
        catch {
            Write-Error "Failed to check event logs: $($Error[0].Message)"
        }
    }
}

# Main function
function Main {
    # Automate tasks
    Automate-Tasks -UpdateCheck -DiskSpaceCheck -EventLogCheck
}

# Run the main function
Main
```
