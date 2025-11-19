"""
Generated Code Metadata:
========================
Original URL: https://webmakers.co.nz
Prompt: Write a PowerShell script to force online archive to start archiving emails in Microsoft 365, as described on the Webmakers website.
Generated: DETERMINISTIC_95eff9be81904b02
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
    Forces the online archive to start archiving emails in Microsoft 365.
.DESCRIPTION
    This script enables and starts the online archive process for a specified mailbox in Microsoft 365.
    It requires the Exchange Online PowerShell module to be installed and connected.
.NOTES
    File Name      : Force-OnlineArchive.ps1
    Prerequisite   : ExchangeOnlineManagement module
    Copyright      : (c) 2023 Webmakers. All rights reserved.
#>

#Requires -Module ExchangeOnlineManagement

function Force-OnlineArchive {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true, HelpMessage = "The email address of the mailbox to enable archive for.")]
        [ValidateNotNullOrEmpty()]
        [string]$UserPrincipalName,

        [Parameter(HelpMessage = "The name for the archive mailbox. Defaults to 'In-Place Archive'.")]
        [string]$ArchiveName = "In-Place Archive"
    )

    begin {
        # Check if connected to Exchange Online
        try {
            $session = Get-PSSession | Where-Object { $_.ConfigurationName -eq 'Microsoft.Exchange' -and $_.State -eq 'Opened' }
            if (-not $session) {
                throw "Not connected to Exchange Online. Please connect first using Connect-ExchangeOnline."
            }
        }
        catch {
            Write-Error "Error checking Exchange Online connection: $_"
            exit 1
        }
    }

    process {
        try {
            # Enable archive if not already enabled
            $mailbox = Get-Mailbox -Identity $UserPrincipalName -ErrorAction Stop
            if (-not $mailbox.ArchiveGuid) {
                Write-Verbose "Enabling archive mailbox for $UserPrincipalName..."
                Enable-Mailbox -Identity $UserPrincipalName -Archive -ArchiveName $ArchiveName -ErrorAction Stop
                Write-Output "Successfully enabled archive mailbox for $UserPrincipalName."
            }
            else {
                Write-Verbose "Archive mailbox already enabled for $UserPrincipalName."
            }

            # Start the archive process
            Write-Verbose "Starting archive process for $UserPrincipalName..."
            Start-ManagedFolderAssistant -Identity $UserPrincipalName -ErrorAction Stop
            Write-Output "Successfully started archive process for $UserPrincipalName."
        }
        catch {
            Write-Error "Error processing archive for $UserPrincipalName : $_"
            exit 1
        }
    }

    end {
        Write-Verbose "Archive process completed for $UserPrincipalName."
    }
}

# Example usage:
# Force-OnlineArchive -UserPrincipalName "user@domain.com" -Verbose
```
