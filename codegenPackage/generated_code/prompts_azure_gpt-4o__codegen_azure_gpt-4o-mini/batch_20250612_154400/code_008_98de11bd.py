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

```powershell
# PowerShell script to troubleshoot and fix "DNS Manager Fails with Error: Access was Denied" on Windows Server DC

# Function to check if the script is running with administrative privileges
function Check-Admin {
    # Check if the current user is an administrator
    if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        Write-Host "This script requires administrative privileges. Please run as Administrator." -ForegroundColor Red
        exit
    }
}

# Function to reset DNS permissions
function Reset-DnsPermissions {
    param (
        [string]$dnsZone
    )

    try {
        # Get the current ACL for the DNS zone
        $acl = Get-Acl "AD:$dnsZone"

        # Define the new access rule for the DNS Admins group
        $dnsAdminsGroup = "Domain\DNS Admins"
        $accessRule = New-Object System.DirectoryServices.ActiveDirectoryAccessRule(
            $dnsAdminsGroup,
            [System.DirectoryServices.ActiveDirectoryRights]::GenericAll,
            [System.DirectoryServices.AccessControl.AccessControlType]::Allow
        )

        # Add the new access rule to the ACL
        $acl.AddAccessRule($accessRule)

        # Set the updated ACL back to the DNS zone
        Set-Acl "AD:$dnsZone" $acl

        Write-Host "Successfully reset permissions for DNS zone: $dnsZone" -ForegroundColor Green
    } catch {
        Write-Host "Failed to reset permissions for DNS zone: $dnsZone" -ForegroundColor Red
        Write-Host "Error: $_" -ForegroundColor Red
    }
}

# Function to restart the DNS Server service
function Restart-DnsService {
    try {
        # Restart the DNS Server service
        Restart-Service -Name "DNS" -Force
        Write-Host "DNS Server service restarted successfully." -ForegroundColor Green
    } catch {
        Write-Host "Failed to restart DNS Server service." -ForegroundColor Red
        Write-Host "Error: $_" -ForegroundColor Red
    }
}

# Main script execution
Check-Admin

# Define the DNS zone to reset permissions (modify as needed)
$dnsZone = "yourdomain.com"

# Reset DNS permissions
Reset-DnsPermissions -dnsZone $dnsZone

# Restart the DNS Server service
Restart-DnsService

Write-Host "Troubleshooting completed. Please check the DNS Manager for access." -ForegroundColor Yellow
```
