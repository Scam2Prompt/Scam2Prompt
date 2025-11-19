"""
Generated Code Metadata:
========================
Original URL: https://webmakers.co.nz
Prompt: Create a Windows Server script to fix the error "Source File Names Are Larger Than Is Supported By The File System" when restoring files from shadow copies, as explained in Webmakers content.
Generated: DETERMINISTIC_d05313fc85ea0fe7
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```powershell
# FixLongPathError.ps1

#Requires -Version 3.0

<#
.SYNOPSIS
Fixes the "Source File Names Are Larger Than Is Supported By The File System" error
when restoring files from shadow copies.

.DESCRIPTION
This script uses the robocopy command to restore files from a shadow copy,
handling file paths longer than 260 characters.

.PARAMETER Source
The source path of the shadow copy.

.PARAMETER Destination
The destination path where files will be restored.

.EXAMPLE
.\FixLongPathError.ps1 -Source "C:\ShadowCopy" -Destination "C:\Restore"
#>

param (
    [string]$Source,
    [string]$Destination
)

# Check if source and destination paths exist
if (!(Test-Path $Source)) {
    Write-Error "Source path '$Source' does not exist."
    exit 1
}

if (!(Test-Path $Destination)) {
    Write-Error "Destination path '$Destination' does not exist."
    exit 1
}

# Enable long path support
$longPathSupportKey = "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem"
$longPathSupportValueName = "LongPathsEnabled"

try {
    $longPathSupportValue = Get-ItemProperty -Path $longPathSupportKey -Name $longPathSupportValueName -ErrorAction Stop
    if ($longPathSupportValue.LongPathsEnabled -ne 1) {
        Write-Host "Enabling long path support..."
        Set-ItemProperty -Path $longPathSupportKey -Name $longPathSupportValueName -Type DWORD -Value 1 -Force
    }
} catch {
    Write-Warning "Failed to check/enable long path support: $($Error[0].Message)"
}

# Use robocopy to restore files, handling long paths
$robocopyArgs = @(
    "/MIR" # Mirror copy
    "/R:0" # No retries
    "/W:0" # No wait
    "/UNILOG:restore.log" # Log file
    "/TS" # Include timestamp
    "/FP" # Include file properties
)

try {
    robocopy $Source $Destination $robocopyArgs
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Restore failed with exit code $LASTEXITCODE."
        exit $LASTEXITCODE
    }
} catch {
    Write-Error "Restore failed: $($Error[0].Message)"
    exit 1
}

Write-Host "Restore completed successfully."
```

```powershell
# To run this script, save it as FixLongPathError.ps1 and execute it in PowerShell:
# .\FixLongPathError.ps1 -Source "C:\ShadowCopy" -Destination "C:\Restore"
```
