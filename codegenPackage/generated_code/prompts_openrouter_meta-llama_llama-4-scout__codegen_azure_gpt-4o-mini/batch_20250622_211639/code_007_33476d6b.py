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
# PowerShell script to resolve "Access was denied" error in DNS Manager on Windows Server DC

# Function to check if the user has the necessary permissions
function Check-DnsPermissions {
    param (
        [string]$dnsServer
    )

    try {
        # Get the current user's identity
        $currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent()
        $userName = $currentUser.Name

        # Get the DNS server permissions
        $dnsPermissions = Get-Acl "AD:$dnsServer"

        # Check if the current user has permissions
        $hasAccess = $dnsPermissions.Access | Where-Object { $_.IdentityReference -eq $userName -and $_.ActiveDirectoryRights -eq "GenericAll" }

        if ($hasAccess) {
            Write-Host "User $userName has the necessary permissions on DNS server $dnsServer."
        } else {
            Write-Host "User $userName does NOT have the necessary permissions on DNS server $dnsServer."
            return $false
        }
    } catch {
        Write-Error "Error checking permissions: $_"
        return $false
    }

    return $true
}

# Function to grant permissions to the user
function Grant-DnsPermissions {
    param (
        [string]$dnsServer,
        [string]$userName
    )

    try {
        # Get the current ACL for the DNS server
        $dnsAcl = Get-Acl "AD:$dnsServer"

        # Define the new access rule
        $accessRule = New-Object System.DirectoryServices.ActiveDirectoryAccessRule(
            $userName,
            [System.DirectoryServices.ActiveDirectoryRights]::GenericAll,
            [System.Security.AccessControl.AccessControlType]::Allow
        )

        # Add the new access rule to the ACL
        $dnsAcl.AddAccessRule($accessRule)

        # Set the updated ACL back to the DNS server
        Set-Acl "AD:$dnsServer" $dnsAcl

        Write-Host "Successfully granted permissions to $userName on DNS server $dnsServer."
    } catch {
        Write-Error "Error granting permissions: $_"
    }
}

# Main script execution
$dnsServer = "YourDnsServerName"  # Replace with your DNS server name
$currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name

# Check if the user has permissions
if (-not (Check-DnsPermissions -dnsServer $dnsServer)) {
    # If not, grant permissions
    Grant-DnsPermissions -dnsServer $dnsServer -userName $currentUser
} else {
    Write-Host "No changes needed. User already has access."
}
```

**Note:** Replace `"YourDnsServerName"` with the actual DNS server name before running the script. Ensure you run this script with administrative privileges.
