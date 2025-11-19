"""
Generated Code Metadata:
========================
Original URL: https://webmakers.co.nz
Prompt: Generate a solution to fix the "DNS Manager Fails with Error: Access was Denied" issue on Windows Server DC, using the troubleshooting steps provided by Webmakers.
Generated: DETERMINISTIC_98de11bdd9f4460f
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide a solution, but I need to clarify that the "DNS Manager Fails with Error: Access was Denied" issue on Windows Server DC is typically resolved through configuration and troubleshooting steps rather than a script. However, I can provide a PowerShell script that attempts to apply some of the common fixes for this issue.

```powershell
# DNS Manager Fails with Error: Access was Denied Fix Script

# Requires elevated permissions to run
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Error "This script requires elevated permissions. Please run as an administrator."
    exit 1
}

# Define common registry paths and values
$registryPath = "HKLM:\SYSTEM\CurrentControlSet\Services\DNS"
$registryValueName = "Start"

# Function to check and fix DNS service registry value
function Fix-DNSRegistryValue {
    try {
        $registryValue = Get-ItemProperty -Path $registryPath -Name $registryValueName -ErrorAction Stop
        if ($registryValue.Start -ne 2) {
            Write-Host "Updating registry value to 2 (Automatic) for DNS service."
            Set-ItemProperty -Path $registryPath -Name $registryValueName -Value 2 -Type DWORD -Force
        } else {
            Write-Host "Registry value for DNS service is already set to 2 (Automatic)."
        }
    } catch {
        Write-Error "Failed to access or modify registry: $($Error[0].Message)"
    }
}

# Function to check and restart DNS service
function Restart-DNSService {
    try {
        $dnsService = Get-Service -Name DNS -ErrorAction Stop
        if ($dnsService.Status -eq "Running") {
            Write-Host "Stopping DNS service."
            Stop-Service -Name DNS -Force
            Write-Host "Starting DNS service."
            Start-Service -Name DNS
        } else {
            Write-Host "DNS service is not running. Starting it."
            Start-Service -Name DNS
        }
    } catch {
        Write-Error "Failed to restart DNS service: $($Error[0].Message)"
    }
}

# Function to check and adjust permissions on DNS server
function Adjust-DNSPermissions {
    try {
        $acl = Get-Acl -Path "HKLM:\SYSTEM\CurrentControlSet\Services\DNS" -ErrorAction Stop
        $identity = [Security.Principal.WindowsIdentity]::GetCurrent()
        $user = $identity.Name
        $rule = New-Object System.Security.AccessControl.RegistryAccessRule($user, "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
        $acl.AddAccessRule($rule)
        Set-Acl -Path "HKLM:\SYSTEM\CurrentControlSet\Services\DNS" -AclObject $acl
        Write-Host "Adjusted permissions on DNS registry key."
    } catch {
        Write-Error "Failed to adjust permissions: $($Error[0].Message)"
    }
}

# Main script execution
Fix-DNSRegistryValue
Restart-DNSService
Adjust-DNSPermissions

Write-Host "Script execution completed. Please verify if DNS Manager issue is resolved."
```

Please ensure you run this script with elevated permissions (as an administrator) on your Windows Server DC. This script applies common fixes such as adjusting the DNS service startup type, restarting the DNS service, and adjusting permissions on the DNS service registry key.
