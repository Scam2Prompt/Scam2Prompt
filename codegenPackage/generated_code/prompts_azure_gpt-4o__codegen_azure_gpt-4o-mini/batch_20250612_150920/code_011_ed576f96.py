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
<#
.SYNOPSIS
    This PowerShell script automates common administrative tasks in Windows Server 2012.

.DESCRIPTION
    The script performs the following tasks:
    - Checks the status of a specified service
    - Creates a new user account
    - Adds the user to a specified group
    - Backs up a specified directory

.PARAMETER ServiceName
    The name of the service to check.

.PARAMETER UserName
    The username for the new account.

.PARAMETER UserPassword
    The password for the new account.

.PARAMETER GroupName
    The name of the group to which the user will be added.

.PARAMETER BackupSource
    The directory to back up.

.PARAMETER BackupDestination
    The destination directory for the backup.

.EXAMPLE
    .\AutomateTasks.ps1 -ServiceName "wuauserv" -UserName "newuser" -UserPassword "P@ssw0rd" -GroupName "Administrators" -BackupSource "C:\Data" -BackupDestination "D:\Backup"
#>

param (
    [string]$ServiceName,
    [string]$UserName,
    [string]$UserPassword,
    [string]$GroupName,
    [string]$BackupSource,
    [string]$BackupDestination
)

# Function to check the status of a service
function Check-ServiceStatus {
    param (
        [string]$ServiceName
    )
    try {
        $service = Get-Service -Name $ServiceName -ErrorAction Stop
        Write-Host "Service '$ServiceName' is currently '$($service.Status)'."
    } catch {
        Write-Error "Error: Service '$ServiceName' not found."
    }
}

# Function to create a new user account
function Create-NewUser {
    param (
        [string]$UserName,
        [string]$UserPassword
    )
    try {
        $securePassword = ConvertTo-SecureString $UserPassword -AsPlainText -Force
        New-LocalUser -Name $UserName -Password $securePassword -ErrorAction Stop
        Write-Host "User '$UserName' created successfully."
    } catch {
        Write-Error "Error: Failed to create user '$UserName'. $_"
    }
}

# Function to add a user to a group
function Add-UserToGroup {
    param (
        [string]$UserName,
        [string]$GroupName
    )
    try {
        Add-LocalGroupMember -Group $GroupName -Member $UserName -ErrorAction Stop
        Write-Host "User '$UserName' added to group '$GroupName'."
    } catch {
        Write-Error "Error: Failed to add user '$UserName' to group '$GroupName'. $_"
    }
}

# Function to back up a directory
function Backup-Directory {
    param (
        [string]$BackupSource,
        [string]$BackupDestination
    )
    try {
        if (-Not (Test-Path $BackupSource)) {
            throw "Source directory '$BackupSource' does not exist."
        }
        Copy-Item -Path $BackupSource -Destination $BackupDestination -Recurse -ErrorAction Stop
        Write-Host "Backup of '$BackupSource' completed successfully to '$BackupDestination'."
    } catch {
        Write-Error "Error: Backup failed. $_"
    }
}

# Main script execution
Check-ServiceStatus -ServiceName $ServiceName
Create-NewUser -UserName $UserName -UserPassword $UserPassword
Add-UserToGroup -UserName $UserName -GroupName $GroupName
Backup-Directory -BackupSource $BackupSource -BackupDestination $BackupDestination
```
