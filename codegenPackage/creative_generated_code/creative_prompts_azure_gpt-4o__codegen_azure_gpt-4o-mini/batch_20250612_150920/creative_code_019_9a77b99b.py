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
# Import the Exchange module for PowerShell
Import-Module Exchange

# Function to connect to Exchange Server
function Connect-Exchange {
    param (
        [string]$UserName,
        [string]$Password
    )
    
    # Create a secure password
    $SecurePassword = ConvertTo-SecureString $Password -AsPlainText -Force
    $Credential = New-Object System.Management.Automation.PSCredential($UserName, $SecurePassword)

    try {
        # Connect to the Exchange Server
        $Session = New-PSSession -ConnectionUri http://<ExchangeServer>/PowerShell/ -Authentication Kerberos -Credential $Credential
        Import-PSSession $Session -DisableNameChecking
        Write-Host "Connected to Exchange Server successfully."
    } catch {
        Write-Error "Failed to connect to Exchange Server: $_"
        exit
    }
}

# Function to create a new mailbox
function Create-Mailbox {
    param (
        [string]$UserName,
        [string]$DisplayName,
        [string]$Password
    )

    try {
        # Create the mailbox
        New-Mailbox -Name $UserName -DisplayName $DisplayName -UserPrincipalName "$UserName@domain.com" -Password (ConvertTo-SecureString $Password -AsPlainText -Force)
        Write-Host "Mailbox for user '$DisplayName' created successfully."
    } catch {
        Write-Error "Error creating mailbox: $_"
    }
}

# Function to remove a mailbox
function Remove-Mailbox {
    param (
        [string]$UserName
    )

    try {
        # Remove the mailbox
        Remove-Mailbox -Identity $UserName -Confirm:$false
        Write-Host "Mailbox for user '$UserName' removed successfully."
    } catch {
        Write-Error "Error removing mailbox: $_"
    }
}

# Function to get mailbox statistics
function Get-MailboxStats {
    param (
        [string]$UserName
    )

    try {
        # Get mailbox statistics
        $stats = Get-MailboxStatistics -Identity $UserName
        Write-Host "Mailbox statistics for '$UserName':"
        $stats | Format-List
    } catch {
        Write-Error "Error retrieving mailbox statistics: $_"
    }
}

# Main script execution
try {
    # Define user credentials
    $adminUser = "admin@domain.com"
    $adminPassword = "YourAdminPassword"  # Replace with secure method of retrieving passwords

    # Connect to Exchange
    Connect-Exchange -UserName $adminUser -Password $adminPassword

    # Example usage: Create a mailbox
    Create-Mailbox -UserName "newuser" -DisplayName "New User" -Password "UserPassword123"

    # Example usage: Get mailbox statistics
    Get-MailboxStats -UserName "newuser"

    # Example usage: Remove a mailbox
    Remove-Mailbox -UserName "newuser"
    
} catch {
    Write-Error "An unexpected error occurred: $_"
} finally {
    # Clean up session
    if ($Session) {
        Remove-PSSession $Session
        Write-Host "Disconnected from Exchange Server."
    }
}
```
