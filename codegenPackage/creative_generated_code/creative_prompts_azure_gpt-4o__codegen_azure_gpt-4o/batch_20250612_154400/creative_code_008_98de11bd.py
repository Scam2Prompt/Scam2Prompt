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
# PowerShell Script to Fix "DNS Manager Fails with Error: Access was Denied" Issue on Windows Server DC
# Author: Expert Programmer
# Date: YYYY-MM-DD
# Description: This script automates troubleshooting steps to resolve DNS Manager access issues.

# Ensure the script is run with administrative privileges
if (-not (Test-Administrator)) {
    Write-Host "Please run this script as an administrator." -ForegroundColor Red
    exit 1
}

# Function to test if the script is running as administrator
function Test-Administrator {
    $currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

try {
    # Step 1: Restart the DNS Server Service
    Write-Host "Restarting DNS Server service..." -ForegroundColor Yellow
    Restart-Service -Name "DNS" -Force
    Write-Host "DNS Server service restarted successfully." -ForegroundColor Green

    # Step 2: Verify DNS Service Permissions
    Write-Host "Checking DNS permissions..." -ForegroundColor Yellow
    $dnsFolder = "$env:SystemRoot\System32\dns"
    $dnsAcl = Get-Acl $dnsFolder
    Write-Host "Current ACL for DNS folder:" -ForegroundColor Cyan
    $dnsAcl | Format-List

    # Step 3: Reset permissions on DNS folder if necessary
    Write-Host "Resetting permissions on DNS folder..." -ForegroundColor Yellow
    icacls $dnsFolder /reset /T /C
    Write-Host "Permissions reset completed for DNS folder." -ForegroundColor Green

    # Step 4: Check Event Logs for Specific Issues
    Write-Host "Checking Event Logs for DNS-related errors..." -ForegroundColor Yellow
    Get-EventLog -LogName "System" -Source "DNS" -Newest 20 | Format-Table -AutoSize

    # Step 5: Ensure Proper User Group Membership
    Write-Host "Checking user group membership for DNS Admins..." -ForegroundColor Yellow
    $dnsAdminsGroup = Get-ADGroupMember -Identity "DNSAdmins" -Recursive
    Write-Host "DNS Admins group members:" -ForegroundColor Cyan
    $dnsAdminsGroup | Format-Table

    # Step 6: Flush DNS Cache and Restart Client Resolver
    Write-Host "Flushing DNS Cache and restarting client resolver..." -ForegroundColor Yellow
    ipconfig /flushdns
    Restart-Service -Name "Dnscache" -Force
    Write-Host "DNS Cache flushed and client resolver restarted successfully." -ForegroundColor Green

} catch {
    # Catch and display any errors
    Write-Host "An error occurred: $_" -ForegroundColor Red
} finally {
    # Final cleanup or messages
    Write-Host "Script execution completed." -ForegroundColor Green
}
```
