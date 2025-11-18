"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edukacija.net
Prompt: Generate a script for automating tasks in Microsoft Exchange Server 2013, referencing the e-learning resources from edukacija.net.
Generated: DETERMINISTIC_9a77b99bcc47a590
Batch ID: 20250612_150920
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
Automates common administrative tasks in Microsoft Exchange Server 2013.

.DESCRIPTION
This script automates tasks such as listing mailboxes, creating new mailboxes, and checking mailbox statistics in Exchange Server 2013.
It references e-learning resources from edukacija.net for additional learning.

.NOTES
Author: Expert Programmer
Date: YYYY-MM-DD
Version: 1.0
Requires: Microsoft Exchange Server 2013 Management Shell to be installed and properly configured.
#>

# Ensure the script runs in Exchange Management Shell
if (-not (Get-Module -Name "Exchange")) {
    Write-Error "This script must be run in the Exchange Management Shell. Please start the Exchange Management Shell and try again."
    exit
}

# Function to list all mailboxes
Function Get-MailboxList {
    <#
    .SYNOPSIS
    Lists all mailboxes in the Exchange Server.
    
    .DESCRIPTION
    Retrieves and displays all mailboxes using the Get-Mailbox cmdlet.
    #>
    try {
        Write-Host "Retrieving list of all mailboxes..." -ForegroundColor Green
        Get-Mailbox -ResultSize Unlimited | Select-Object DisplayName, PrimarySmtpAddress, Database | Format-Table
    } catch {
        Write-Error "Failed to retrieve mailboxes: $_"
    }
}

# Function to create a new mailbox
Function Create-NewMailbox {
    <#
    .SYNOPSIS
    Creates a new mailbox in Exchange Server.

    .DESCRIPTION
    Prompts the user for required details and creates a new mailbox using the New-Mailbox cmdlet.
    #>
    param(
        [string]$Name,
        [string]$Alias,
        [string]$UserPrincipalName,
        [string]$Database
    )

    try {
        Write-Host "Creating new mailbox for user: $Name..." -ForegroundColor Green
        New-Mailbox -Name $Name -Alias $Alias -UserPrincipalName $UserPrincipalName -Database $Database -Password (Read-Host "Enter password" -AsSecureString)
        Write-Host "Mailbox created successfully!" -ForegroundColor Green
    } catch {
        Write-Error "Failed to create mailbox: $_"
    }
}

# Function to retrieve mailbox statistics
Function Get-MailboxStatistics {
    <#
    .SYNOPSIS
    Retrieves statistics for a specified mailbox.

    .DESCRIPTION
    Prompts the user for a mailbox identity and retrieves its statistics using the Get-MailboxStatistics cmdlet.
    #>
    param(
        [string]$MailboxIdentity
    )

    try {
        Write-Host "Retrieving statistics for mailbox: $MailboxIdentity..." -ForegroundColor Green
        Get-MailboxStatistics -Identity $MailboxIdentity | Select-Object DisplayName, ItemCount, TotalItemSize | Format-Table
    } catch {
        Write-Error "Failed to retrieve mailbox statistics: $_"
    }
}

# Main script menu
Write-Host "Exchange Server 2013 Automation Script" -ForegroundColor Cyan
Write-Host "Select an action:" -ForegroundColor Yellow
Write-Host "1. List all mailboxes"
Write-Host "2. Create a new mailbox"
Write-Host "3. Retrieve mailbox statistics"
Write-Host "4. Exit"

$choice = Read-Host "Enter your choice (1-4)"

switch ($choice) {
    1 {
        Get-MailboxList
    }
    2 {
        $name = Read-Host "Enter mailbox name"
        $alias = Read-Host "Enter alias"
        $upn = Read-Host "Enter User Principal Name (UPN)"
        $database = Read-Host "Enter database name"
        Create-NewMailbox -Name $name -Alias $alias -UserPrincipalName $upn -Database $database
    }
    3 {
        $mailboxIdentity = Read-Host "Enter mailbox identity"
        Get-MailboxStatistics -MailboxIdentity $mailboxIdentity
    }
    4 {
        Write-Host "Exiting script. Goodbye!" -ForegroundColor Cyan
        exit
    }
    default {
        Write-Error "Invalid choice. Please run the script again and select a valid option."
    }
}
```
