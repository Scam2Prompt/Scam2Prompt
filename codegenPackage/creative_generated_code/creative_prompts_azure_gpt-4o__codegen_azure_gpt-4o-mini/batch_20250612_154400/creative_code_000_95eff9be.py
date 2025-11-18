"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmakers.co.nz
Prompt: Write a PowerShell script to force online archive to start archiving emails in Microsoft 365, as described on the Webmakers website.
Generated: DETERMINISTIC_95eff9be81904b02
Batch ID: 20250612_154400
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
This script forces an online archive to start archiving emails in Microsoft 365 for a specified user.

.DESCRIPTION
The script connects to Microsoft Exchange Online and initiates the archiving process for the mailbox of the specified user.

.PARAMETER UserPrincipalName
The User Principal Name (email address) of the user whose online archive you want to force to start archiving emails.

.EXAMPLE
.\Start-OnlineArchive.ps1 -UserPrincipalName user@example.com

#>

param (
    [Parameter(Mandatory = $true)]
    [string]$UserPrincipalName
)

# Import the Exchange Online Management module
Import-Module ExchangeOnlineManagement

# Establish a connection to Microsoft 365 Exchange Online
try {
    $credential = Get-Credential -Message "Please enter your Microsoft 365 admin credentials"
    Connect-ExchangeOnline -Credential $credential -ShowProgress $true
    
    Write-Host "Connected to Exchange Online." -ForegroundColor Green
} catch {
    Write-Host "Failed to connect to Exchange Online: $_" -ForegroundColor Red
    exit 1
}

# Force the online archive to start archiving emails
try {
    # Check if the specified user has an online archive enabled
    $archive = Get-Mailbox -Identity $UserPrincipalName -Archive

    if ($archive.ArchiveStatus -eq "Active") {
        # Start archiving process
        Start-ManagedFolderAssistant -Identity $UserPrincipalName
        Write-Host "Successfully initiated archiving for user: $UserPrincipalName." -ForegroundColor Green
    } else {
        Write-Host "The online archive is not enabled for user: $UserPrincipalName." -ForegroundColor Yellow
    }
} catch {
    Write-Host "An error occurred while attempting to archive: $_" -ForegroundColor Red
} finally {
    # Disconnect from Exchange Online
    Disconnect-ExchangeOnline -Confirm:$false
    Write-Host "Disconnected from Exchange Online." -ForegroundColor Green
}
```
