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
# DNS Manager Access Denied Fix Script for Windows Server DC with DNS and DHCP
# Requires administrative privileges to run

# Import required modules
Import-Module DnsServer
Import-Module DhcpServer

try {
    # Check if running as administrator
    $currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
    if (-not $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        throw "This script must be run as administrator"
    }

    # Verify DNS Server service is running
    $dnsService = Get-Service -Name DNS
    if ($dnsService.Status -ne "Running") {
        Start-Service -Name DNS -ErrorAction Stop
    }

    # Verify DHCP Server service is running
    $dhcpService = Get-Service -Name DHCPServer
    if ($dhcpService.Status -ne "Running") {
        Start-Service -Name DHCPServer -ErrorAction Stop
    }

    # Reset DNS Server permissions
    $dnsAcl = Get-Acl -Path "AD:\DC=DomainDnsZones,DC=domain,DC=com" -ErrorAction Stop
    $adminRule = New-Object System.DirectoryServices.ActiveDirectoryAccessRule(
        "NT AUTHORITY\Authenticated Users",
        "ReadProperty, WriteProperty",
        "Allow"
    )
    $dnsAcl.AddAccessRule($adminRule)
    Set-Acl -Path "AD:\DC=DomainDnsZones,DC=domain,DC=com" -AclObject $dnsAcl -ErrorAction Stop

    # Reset DHCP Server permissions
    $dhcpSecurity = Get-DhcpServerSecurityGroup -ErrorAction Stop
    if ($dhcpSecurity -eq $null) {
        Add-DhcpServerSecurityGroup -ErrorAction Stop
    }

    # Restart DNS and DHCP services to apply changes
    Restart-Service -Name DNS -Force -ErrorAction Stop
    Restart-Service -Name DHCPServer -Force -ErrorAction Stop

    # Verify DNS Server functionality
    $dnsTest = Get-DnsServerResourceRecord -ZoneName "domain.com" -ErrorAction Stop
    if (-not $dnsTest) {
        throw "DNS verification failed"
    }

    # Verify DHCP Server functionality
    $dhcpTest = Get-DhcpServerv4Scope -ErrorAction Stop
    if (-not $dhcpTest) {
        throw "DHCP verification failed"
    }

    Write-Output "DNS and DHCP access issues resolved successfully"
}
catch {
    Write-Error "Error encountered: $_"
    exit 1
}
```
