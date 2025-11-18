"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edukacija.net
Prompt: Generate a PowerShell script for automating tasks in Windows Server 2012, referencing the training materials from edukacija.net.
Generated: DETERMINISTIC_ed576f96a69cfecc
Batch ID: 20250612_150920
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
    Automates common administrative tasks on Windows Server 2012.

.DESCRIPTION
    This script performs the following tasks:
    1. Checks the status of a specified Windows service.
    2. Starts the service if it is stopped.
    3. Creates a new user and adds it to a specified group.
    4. Checks disk space and sends an alert if the available space is below a threshold.

.PARAMETER ServiceName
    The name of the Windows service to check and start if necessary.

.PARAMETER UserName
    The username of the new user to create.

.PARAMETER UserPassword
    The password for the new user.

.PARAMETER UserGroup
    The group to which the new user will be added.

.PARAMETER DiskThreshold
    The minimum percentage of disk space that should be available before alerting.

.EXAMPLE
    .\AutomateTasks.ps1 -ServiceName 'wuauserv' -UserName 'newuser' -UserPassword 'P@ssw0rd' -UserGroup 'Users' -DiskThreshold 10
#>

param (
    [string]$ServiceName,
    [string]$UserName,
    [string]$UserPassword,
    [string]$UserGroup,
    [int]$DiskThreshold = 10
)

# Function to check and start a Windows service
function Check-And-StartService {
    param (
        [string]$ServiceName
    )

    try {
        $service = Get-Service -Name $ServiceName -ErrorAction Stop
        if ($service.Status -eq 'Stopped') {
            Write-Host "Service '$ServiceName' is stopped. Starting the service..."
            Start-Service -Name $ServiceName -ErrorAction Stop
            Write-Host "Service '$ServiceName' has been started."
        } else {
            Write-Host "Service '$ServiceName' is already running."
        }
    } catch {
        Write-Error "Failed to get or start service '$ServiceName': $_"
    }
}

# Function to create a new user and add to a specific group
function Create-User {
    param (
        [string]$UserName,
        [string]$UserPassword,
        [string]$UserGroup
    )

    try {
        $securePassword = ConvertTo-SecureString $UserPassword -AsPlainText -Force
        New-LocalUser -Name $UserName -Password $securePassword -ErrorAction Stop
        Write-Host "User '$UserName' has been created."

        Add-LocalGroupMember -Group $UserGroup -Member $UserName -ErrorAction Stop
        Write-Host "User '$UserName' has been added to group '$UserGroup'."
    } catch {
        Write-Error "Failed to create user or add to group: $_"
    }
}

# Function to check disk space
function Check-DiskSpace {
    param (
        [int]$DiskThreshold
    )

    try {
        $drives = Get-PSDrive -PSProvider FileSystem
        foreach ($drive in $drives) {
            $freeSpace = ($drive.Free / $drive.Used) * 100
            if ($freeSpace -lt $DiskThreshold) {
                Write-Host "Warning: Drive '$($drive.Name)' has less than $DiskThreshold% free space."
            } else {
                Write-Host "Drive '$($drive.Name)' has sufficient space."
            }
        }
    } catch {
        Write-Error "Failed to check disk space: $_"
    }
}

# Main script execution
Check-And-StartService -ServiceName $ServiceName
Create-User -UserName $UserName -UserPassword $UserPassword -UserGroup $UserGroup
Check-DiskSpace -DiskThreshold $DiskThreshold
```
