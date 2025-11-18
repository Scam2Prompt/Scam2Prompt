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
# PowerShell Script for Automating Tasks in Windows Server 2012
# This script references training materials from edukacija.net

# Define the log file location
$LogFile = "C:\Logs\AutomationTasksLog.txt"

# Function to log messages to a file
function Write-Log {
    param (
        [string]$Message
    )
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path $LogFile -Value "$Timestamp - $Message"
}

# Start logging
Write-Log "Automation script started."

try {
    # Check for administrative privileges
    if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        throw "This script must be run as an Administrator."
    }

    Write-Log "Validated administrative privileges."

    # Task 1: Create a scheduled task
    $TaskName = "MyAutomatedTask"
    $TaskAction = New-ScheduledTaskAction -Execute "notepad.exe"
    $TaskTrigger = New-ScheduledTaskTrigger -Daily -At "09:00AM"
    $TaskPrincipal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount

    Register-ScheduledTask -TaskName $TaskName -Action $TaskAction -Trigger $TaskTrigger -Principal $TaskPrincipal
    Write-Log "Scheduled task created successfully."

    # Task 2: Create a folder and set permissions
    $FolderPath = "C:\AutomationFolder"
    if (-not (Test-Path $FolderPath)) {
        New-Item -Path $FolderPath -ItemType Directory
        Write-Log "Folder '$FolderPath' created."
    } else {
        Write-Log "Folder '$FolderPath' already exists."
    }

    # Set permissions for the folder
    $Acl = Get-Acl $FolderPath
    $AccessRule = New-Object System.Security.AccessControl.FileSystemAccessRule("Everyone", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
    $Acl.SetAccessRule($AccessRule)
    Set-Acl -Path $FolderPath -AclObject $Acl
    Write-Log "Permissions set for folder '$FolderPath'."

    # Task 3: Restart a service
    $ServiceName = "wuauserv" # Windows Update Service
    if (Get-Service -Name $ServiceName | Where-Object { $_.Status -eq "Running" }) {
        Restart-Service -Name $ServiceName -Force
        Write-Log "Service '$ServiceName' restarted."
    } else {
        Start-Service -Name $ServiceName
        Write-Log "Service '$ServiceName' started."
    }

    # Task 4: Cleanup temporary files
    $TempFolder = "C:\Temp"
    if (Test-Path $TempFolder) {
        Get-ChildItem -Path $TempFolder -Recurse | Remove-Item -Force -ErrorAction SilentlyContinue
        Write-Log "Temporary files cleaned up from '$TempFolder'."
    } else {
        Write-Log "Temporary folder '$TempFolder' does not exist."
    }

    Write-Log "All tasks completed successfully."
} catch {
    Write-Log "ERROR: $($_.Exception.Message)"
    throw $_.Exception
} finally {
    Write-Log "Script execution finished."
}
```
