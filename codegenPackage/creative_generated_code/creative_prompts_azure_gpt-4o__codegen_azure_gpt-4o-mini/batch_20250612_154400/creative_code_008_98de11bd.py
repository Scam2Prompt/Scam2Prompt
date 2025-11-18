"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmakers.co.nz
Prompt: Generate a solution to fix the "DNS Manager Fails with Error: Access was Denied" issue on Windows Server DC, using the troubleshooting steps provided by Webmakers.
Generated: DETERMINISTIC_98de11bdd9f4460f
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```powershell
# PowerShell script to troubleshoot and fix "DNS Manager Fails with Error: Access was Denied" on Windows Server DC

# Function to check and restart the DNS Server service
function Restart-DnsService {
    Try {
        # Check the status of the DNS service
        $dnsService = Get-Service -Name "DNS" -ErrorAction Stop
        
        if ($dnsService.Status -ne 'Running') {
            # Attempt to start the DNS service
            Write-Host "DNS service is not running. Attempting to start it..."
            Start-Service -Name "DNS" -ErrorAction Stop
            Write-Host "DNS service started successfully."
        } else {
            Write-Host "DNS service is already running."
        }
    } Catch {
        Write-Host "Error: Unable to manage DNS service. $_"
    }
}

# Function to check user permissions on DNS
function Check-DnsPermissions {
    Try {
        # Define DNS zone to check permissions
        $zone = "yourdomain.local"
        
        # Get current permissions for the DNS zone
        $acl = Get-Acl "AD:$zone"
        
        # Check if the current user has the appropriate permissions
        $currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent()
        $userHasPermission = $acl.Access | Where-Object {
            $_.IdentityReference -eq $currentUser.Name -and $_.ActiveDirectoryRights -eq "WriteProperty"
        }

        if (-not $userHasPermission) {
            Write-Host "Current user does not have sufficient permissions on the DNS zone."
            # You may include code here to add permissions if necessary
        } else {
            Write-Host "Current user has sufficient permissions on the DNS zone."
        }
    } Catch {
        Write-Host "Error: Unable to check DNS permissions. $_"
    }
}

# Function to review DNS configuration for issues
function Review-DnsConfiguration {
    Try {
        # Check DNS configuration for common issues
        $dnsConfig = Get-DnsServerZone -ErrorAction Stop
        
        # Display zones and their status
        foreach ($zone in $dnsConfig) {
            Write-Host "Zone: $($zone.ZoneName) - Status: $($zone.ZoneType)"
        }
    } Catch {
        Write-Host "Error: Unable to retrieve DNS configuration. $_"
    }
}

# Main execution block
Try {
    Write-Host "Starting DNS troubleshooting script..."

    # Restart DNS Service
    Restart-DnsService

    # Check DNS Permissions
    Check-DnsPermissions

    # Review DNS Configuration
    Review-DnsConfiguration

    Write-Host "DNS troubleshooting completed."
} Catch {
    Write-Host "An unexpected error occurred. $_"
}
```
