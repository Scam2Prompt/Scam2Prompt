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
<#
.SYNOPSIS
    Fixes "DNS Manager Fails with Error: Access was Denied" issue on Windows Server DC.
.DESCRIPTION
    This script implements the troubleshooting steps recommended by Webmakers to resolve
    the DNS Manager access denied error on Windows Server Domain Controllers.
.NOTES
    File Name      : Fix-DnsManagerAccessDenied.ps1
    Prerequisites  : PowerShell 5.1 or later, Run as Administrator
    Copyright      : Webmakers
#>

#Requires -RunAsAdministrator

function Fix-DnsManagerAccessDenied {
    [CmdletBinding()]
    param()

    try {
        Write-Host "Starting DNS Manager Access Denied fix..." -ForegroundColor Cyan

        # Step 1: Verify DNS Service is running
        Write-Host "Checking DNS Service status..." -ForegroundColor Yellow
        $dnsService = Get-Service -Name DNS -ErrorAction Stop
        if ($dnsService.Status -ne "Running") {
            Write-Host "Starting DNS Service..." -ForegroundColor Yellow
            Start-Service -Name DNS -ErrorAction Stop
        }

        # Step 2: Verify DNS Server role is installed
        Write-Host "Checking DNS Server role installation..." -ForegroundColor Yellow
        $dnsRole = Get-WindowsFeature -Name DNS -ErrorAction Stop
        if (-not $dnsRole.Installed) {
            throw "DNS Server role is not installed. Please install it first."
        }

        # Step 3: Check and repair DNS permissions
        Write-Host "Verifying DNS permissions..." -ForegroundColor Yellow
        $dnsRoot = Get-Item "AD:\DC=DomainDnsZones,$((Get-ADDomain).DistinguishedName)" -ErrorAction Stop
        $acl = Get-Acl -Path "AD:\DC=DomainDnsZones,$((Get-ADDomain).DistinguishedName)" -ErrorAction Stop

        # Check if DnsAdmins has full control
        $dnsAdminsSid = (Get-ADGroup -Identity "DnsAdmins").SID
        $found = $false

        foreach ($access in $acl.Access) {
            if ($access.IdentityReference -eq $dnsAdminsSid -and $access.ActiveDirectoryRights -match "GenericAll") {
                $found = $true
                break
            }
        }

        if (-not $found) {
            Write-Host "Adding Full Control permissions for DnsAdmins group..." -ForegroundColor Yellow
            $rule = New-Object System.DirectoryServices.ActiveDirectoryAccessRule(
                $dnsAdminsSid,
                "GenericAll",
                "Allow"
            )
            $acl.AddAccessRule($rule)
            Set-Acl -Path "AD:\DC=DomainDnsZones,$((Get-ADDomain).DistinguishedName)" -AclObject $acl -ErrorAction Stop
        }

        # Step 4: Restart DNS Service
        Write-Host "Restarting DNS Service..." -ForegroundColor Yellow
        Restart-Service -Name DNS -Force -ErrorAction Stop

        # Step 5: Verify DNS Manager access
        Write-Host "Verifying DNS Manager access..." -ForegroundColor Yellow
        try {
            $dnsZones = Get-DnsServerZone -ErrorAction Stop
            Write-Host "DNS Manager access verified successfully." -ForegroundColor Green
            Write-Host "The issue should be resolved. Please try accessing DNS Manager again." -ForegroundColor Green
        }
        catch {
            throw "DNS Manager access verification failed. Error: $_"
        }
    }
    catch {
        Write-Host "Error occurred: $_" -ForegroundColor Red
        Write-Host "Failed to fix DNS Manager access issue." -ForegroundColor Red
        exit 1
    }
}

# Execute the function
Fix-DnsManagerAccessDenied
```
