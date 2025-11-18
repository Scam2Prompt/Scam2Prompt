"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange.zweirad-hanselle.de
Prompt: Write a PowerShell script to configure Internet Explorer settings for enabling cookies and scripts required by a web-based Outlook interface.
Generated: DETERMINISTIC_d21741e286d3e6c3
Batch ID: 20250612_145526
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
    Configures Internet Explorer settings to enable cookies and scripts required for a web-based Outlook interface.

.DESCRIPTION
    This script makes necessary changes to the registry to enable cookies and scripts in Internet Explorer.
    It is intended for environments where Outlook Web Access (OWA) or similar services are used via IE.

.NOTES
    Author: Expert Programmer
    Date: 2023-10-04
    Use with caution as this script modifies the Windows Registry.

#>

# Ensure the script is run as Administrator
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltinRole] "Administrator")) {
    Write-Error "This script must be run as Administrator."
    exit 1
}

# Define registry keys and values for enabling cookies and scripts
$registryKeys = @(
    @{
        Path  = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2"
        Name  = "1406"  # Enable cookies for trusted sites
        Value = 0       # 0 = Enable
    },
    @{
        Path  = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2"
        Name  = "1400"  # Enable Active Scripting
        Value = 0       # 0 = Enable
    }
)

# Loop through each registry key and set its value
foreach ($key in $registryKeys) {
    try {
        # Check if the registry path exists
        if (-not (Test-Path $key.Path)) {
            # Create the registry path if it does not exist
            New-Item -Path $key.Path -Force | Out-Null
        }

        # Set the registry value
        Set-ItemProperty -Path $key.Path -Name $key.Name -Value $key.Value

        # Log success message
        Write-Host "Successfully configured $($key.Name) in $($key.Path)" -ForegroundColor Green
    }
    catch {
        # Handle any errors during registry modification
        Write-Error "Failed to configure $($key.Name) in $($key.Path): $_"
    }
}

# Notify the user of completion
Write-Host "`nConfiguration of Internet Explorer settings is complete." -ForegroundColor Cyan
Write-Host "Please restart IE or your system for the changes to take effect." -ForegroundColor Yellow
```
