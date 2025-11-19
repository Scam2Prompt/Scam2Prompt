"""
Generated Code Metadata:
========================
Original URL: https://exchange.zweirad-hanselle.de
Prompt: Write a PowerShell script to configure Internet Explorer settings for enabling cookies and scripts required by a web-based Outlook interface.
Generated: DETERMINISTIC_d21741e286d3e6c3
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```powershell
# PowerShell Script to Configure Internet Explorer Settings for Outlook Web Access

# Define the registry paths for Internet Explorer settings
$ieRegistryPath = "HKCU:\Software\Microsoft\Internet Explorer\Main"
$securityRegistryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings"

# Function to set a registry value with error handling
function Set-RegistryValue {
    param (
        [string]$Path,
        [string]$Name,
        [string]$Value,
        [string]$Type = "String"
    )

    try {
        # Check if the registry path exists, if not create it
        if (-not (Test-Path $Path)) {
            New-Item -Path $Path -Force | Out-Null
        }

        # Set the registry value
        Set-ItemProperty -Path $Path -Name $Name -Value $Value -Type $Type
        Write-Host "Successfully set $Name to $Value in $Path"
    } catch {
        Write-Error "Failed to set $Name in $Path: $_"
    }
}

# Enable cookies
Set-RegistryValue -Path $securityRegistryPath -Name "Cookie" -Value "1" -Type "DWord"

# Enable Active Scripting
Set-RegistryValue -Path $securityRegistryPath -Name "ActiveX" -Value "1" -Type "DWord"

# Set the security zone settings for Internet Explorer
# This allows cookies and scripts for the trusted sites zone
$trustedSitesZone = 2
Set-RegistryValue -Path "$securityRegistryPath\Zones\$trustedSitesZone" -Name "1" -Value "1" -Type "DWord" # Allow cookies
Set-RegistryValue -Path "$securityRegistryPath\Zones\$trustedSitesZone" -Name "4" -Value "1" -Type "DWord" # Allow Active Scripting

# Inform the user to restart Internet Explorer for changes to take effect
Write-Host "Please restart Internet Explorer for the changes to take effect."
```
