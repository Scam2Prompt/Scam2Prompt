"""
Generated Code Metadata:
========================
Original URL: https://edukacija.net
Prompt: Generate a script for automating tasks in Microsoft Exchange Server 2013, referencing the e-learning resources from edukacija.net.
Generated: DETERMINISTIC_9a77b99bcc47a590
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```powershell
# PowerShell script to automate tasks in Microsoft Exchange Server 2013
# This script includes examples of common administrative tasks such as creating a mailbox,
# setting mailbox permissions, and exporting mailbox data.

# Ensure the script is run with the necessary permissions
if (-not (Get-PSSession | Where-Object { $_.State -eq 'Opened' })) {
    Write-Host "This script must be run in an Exchange Management Shell or with appropriate permissions." -ForegroundColor Red
    exit
}

# Function to create a new mailbox
function Create-Mailbox {
    param (
        [string]$UserName,
        [string]$FirstName,
        [string]$LastName,
        [string]$Password
    )

    try {
        # Create a new user account
        New-LocalUser -Name $UserName -FirstName $FirstName -LastName $LastName -Password (ConvertTo-SecureString $Password -AsPlainText -Force) -UserPrincipalName "$UserName@domain.com"
        
        # Create a mailbox for the new user
        Enable-Mailbox -Identity $UserName
        Write-Host "Mailbox created for $UserName successfully." -ForegroundColor Green
    } catch {
        Write-Host "Error creating mailbox: $_" -ForegroundColor Red
    }
}

# Function to set mailbox permissions
function Set-MailboxPermissions {
    param (
        [string]$MailboxUser,
        [string]$UserToGrant,
        [string]$AccessRights
    )

    try {
        # Grant specified permissions to the user
        Add-MailboxPermission -Identity $MailboxUser -User $UserToGrant -AccessRights $AccessRights
        Write-Host "Permissions granted to $UserToGrant on mailbox $MailboxUser." -ForegroundColor Green
    } catch {
        Write-Host "Error setting mailbox permissions: $_" -ForegroundColor Red
    }
}

# Function to export mailbox data to a PST file
function Export-MailboxToPST {
    param (
        [string]$MailboxUser,
        [string]$ExportPath
    )

    try {
        # Export mailbox data to a PST file
        New-MailboxExportRequest -Mailbox $MailboxUser -FilePath $ExportPath
        Write-Host "Export request for mailbox $MailboxUser has been created." -ForegroundColor Green
    } catch {
        Write-Host "Error exporting mailbox: $_" -ForegroundColor Red
    }
}

# Example usage of the functions
# Create a new mailbox
Create-Mailbox -UserName "jdoe" -FirstName "John" -LastName "Doe" -Password "P@ssw0rd"

# Set mailbox permissions
Set-MailboxPermissions -MailboxUser "jdoe" -UserToGrant "asmith" -AccessRights "FullAccess"

# Export mailbox to PST
Export-MailboxToPST -MailboxUser "jdoe" -ExportPath "\\server\exports\jdoe.pst"

# End of script
```
