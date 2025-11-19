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
<#
.SYNOPSIS
    Fixes the "Source File Names Are Larger Than Is Supported By The File System" error when restoring files from shadow copies.
.DESCRIPTION
    This script modifies the registry to increase the maximum path length limit in Windows,
    allowing restoration of files with long paths from shadow copies.
.NOTES
    File Name      : Fix-ShadowCopyLongPath.ps1
    Prerequisite   : PowerShell 5.1 or later, Administrative privileges
    Copyright      : (c) 2024
#>

#Requires -Version 5.1
#Requires -RunAsAdministrator

try {
    # Define registry path and value name
    $registryPath = "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem"
    $valueName = "LongPathsEnabled"
    $valueData = 1

    # Check if the registry path exists
    if (-not (Test-Path $registryPath)) {
        throw "Registry path not found: $registryPath"
    }

    # Get current value if it exists
    $currentValue = Get-ItemProperty -Path $registryPath -Name $valueName -ErrorAction SilentlyContinue

    # Set or create the registry value
    if ($null -eq $currentValue) {
        New-ItemProperty -Path $registryPath -Name $valueName -Value $valueData -PropertyType DWORD -Force | Out-Null
        Write-Host "Created registry value $valueName with data $valueData"
    }
    elseif ($currentValue.$valueName -ne $valueData) {
        Set-ItemProperty -Path $registryPath -Name $valueName -Value $valueData
        Write-Host "Updated registry value $valueName to $valueData"
    }
    else {
        Write-Host "Registry value $valueName is already set to $valueData"
    }

    # Verify the change
    $verifiedValue = Get-ItemProperty -Path $registryPath -Name $valueName
    if ($verifiedValue.$valueName -eq $valueData) {
        Write-Host "Successfully configured long path support. A system restart may be required for changes to take effect."
    }
    else {
        throw "Failed to verify registry change. Expected $valueData but got $($verifiedValue.$valueName)"
    }
}
catch {
    Write-Error "An error occurred: $_"
    exit 1
}
```
