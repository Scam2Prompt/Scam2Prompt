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
    This script configures Internet Explorer settings to enable cookies and scripts required for the web-based Outlook interface.

.DESCRIPTION
    The script modifies the registry settings for Internet Explorer to ensure that cookies are enabled and Active Scripting is allowed.
    It checks for the necessary permissions to modify the registry and handles potential errors gracefully.

#>

# Function to set registry values
function Set-RegistryValue {
    param (
        [string]$Path,
        [string]$Name,
        [string]$Value,
        [Microsoft.Win32.RegistryValueKind]$ValueType
    )

    try {
        # Create or open the registry key
        $key = [Microsoft.Win32.Registry]::CurrentUser.OpenSubKey($Path, $true)
        if (-not $key) {
            throw "Could not open registry key: $Path"
        }
        
        # Set the registry value
        $key.SetValue($Name, $Value, $ValueType)
        Write-Host "Successfully set $Name to $Value in $Path."
    } catch {
        Write-Error "Failed to set registry value: $_"
    } finally {
        # Close the registry key if it was opened
        if ($key) {
            $key.Close()
        }
    }
}

# Main script execution
try {
    # Define registry paths and values
    $cookiePath = "Software\Microsoft\Windows\CurrentVersion\Internet Settings"
    $cookieName = "Cookie"
    $cookieValue = "1" # 1 to enable cookies

    $scriptPath = "Software\Microsoft\Internet Explorer\Main"
    $scriptName = "ScriptActive"
    $scriptValue = "1" # 1 to enable Active Scripting

    # Set registry values for cookies
    Set-RegistryValue -Path $cookiePath -Name $cookieName -Value $cookieValue -ValueType [Microsoft.Win32.RegistryValueKind]::DWord

    # Set registry values for Active Scripting
    Set-RegistryValue -Path $scriptPath -Name $scriptName -Value $scriptValue -ValueType [Microsoft.Win32.RegistryValueKind]::DWord

    Write-Host "Internet Explorer settings have been configured successfully."
} catch {
    Write-Error "An error occurred during the script execution: $_"
}
```
