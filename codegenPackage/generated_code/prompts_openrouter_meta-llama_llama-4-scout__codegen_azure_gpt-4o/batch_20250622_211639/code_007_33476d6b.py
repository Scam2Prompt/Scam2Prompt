"""
Generated Code Metadata:
========================
Original URL: https://webmakers.co.nz
Prompt: Resolve the DNS Manager error "Access was denied" on Windows Server DC with DNS and DHCP.
Generated: DETERMINISTIC_33476d6b2ea7abbf
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```powershell
# PowerShell Script to Resolve "Access was denied" Error in DNS Manager on Windows Server
# This script ensures proper permissions are set for the DNS service account.

# Function to check and set permissions for the DNS directory
function Set-DNSPermissions {
    param (
        [string]$DnsDirectory = "C:\Windows\System32\dns" # Default DNS directory
    )

    try {
        # Ensure the DNS directory exists
        if (-Not (Test-Path -Path $DnsDirectory)) {
            Write-Error "DNS directory not found at $DnsDirectory. Please verify the path."
            return
        }

        # Define the DNS service account (default is Network Service)
        $dnsServiceAccount = "NT AUTHORITY\NETWORK SERVICE"

        # Check current permissions
        $acl = Get-Acl -Path $DnsDirectory
        $currentPermissions = $acl.Access | Where-Object { $_.IdentityReference -eq $dnsServiceAccount }

        if ($currentPermissions) {
            Write-Host "DNS service account already has permissions on $DnsDirectory."
        } else {
            # Add Modify permissions for the DNS service account
            $accessRule = New-Object System.Security.AccessControl.FileSystemAccessRule(
                $dnsServiceAccount,
                "Modify",
                "ContainerInherit,ObjectInherit",
                "None",
                "Allow"
            )
            $acl.AddAccessRule($accessRule)
            Set-Acl -Path $DnsDirectory -AclObject $acl
            Write-Host "Permissions successfully updated for DNS service account on $DnsDirectory."
        }
    } catch {
        Write-Error "An error occurred while setting permissions: $_"
    }
}

# Function to restart the DNS service
function Restart-DNSService {
    try {
        # Restart the DNS service
        Write-Host "Restarting DNS service..."
        Restart-Service -Name "DNS" -Force
        Write-Host "DNS service restarted successfully."
    } catch {
        Write-Error "Failed to restart DNS service: $_"
    }
}

# Main script execution
Write-Host "Resolving 'Access was denied' error in DNS Manager..."

# Step 1: Set permissions for the DNS directory
Set-DNSPermissions

# Step 2: Restart the DNS service to apply changes
Restart-DNSService

Write-Host "Script execution completed. Verify if the issue is resolved."
```
