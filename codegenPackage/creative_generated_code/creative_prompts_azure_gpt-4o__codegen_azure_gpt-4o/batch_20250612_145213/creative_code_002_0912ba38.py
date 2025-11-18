"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wfcomputing.com
Prompt: Provide code examples for setting up and managing user accounts and passwords in a Windows network environment, based on WF Computing's expertise in network administration.
Generated: DETERMINISTIC_0912ba381d5b9167
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```powershell
# PowerShell script to set up and manage user accounts and passwords in a Windows network environment.
# This script must be executed with administrative privileges.

# Function to create a new Active Directory user account
Function Create-ADUser {
    param (
        [Parameter(Mandatory=$true)]
        [string]$Username,           # Username for the new account
        
        [Parameter(Mandatory=$true)]
        [string]$FirstName,          # First name of the user
        
        [Parameter(Mandatory=$true)]
        [string]$LastName,           # Last name of the user
        
        [Parameter(Mandatory=$true)]
        [string]$Password,           # Password for the user account
        
        [string]$OU = "OU=Users,DC=example,DC=com" # Organizational Unit where the account will be created
    )

    try {
        # Check if the user already exists
        $userExists = Get-ADUser -Filter {SamAccountName -eq $Username} -ErrorAction SilentlyContinue
        if ($userExists) {
            Write-Host "User '$Username' already exists in Active Directory." -ForegroundColor Yellow
            return
        }

        # Create the new user in Active Directory
        New-ADUser -SamAccountName $Username `
                   -UserPrincipalName "$Username@example.com" `
                   -Name "$FirstName $LastName" `
                   -GivenName $FirstName `
                   -Surname $LastName `
                   -AccountPassword (ConvertTo-SecureString $Password -AsPlainText -Force) `
                   -Enabled $true `
                   -Path $OU `
                   -PasswordNeverExpires $false `
                   -ChangePasswordAtLogon $true

        Write-Host "User '$Username' created successfully." -ForegroundColor Green
    } catch {
        Write-Host "Error creating user '$Username': $_" -ForegroundColor Red
    }
}

# Function to update a user's password
Function Update-ADUserPassword {
    param (
        [Parameter(Mandatory=$true)]
        [string]$Username,           # Username for the account
        
        [Parameter(Mandatory=$true)]
        [string]$NewPassword         # New password for the user
    )

    try {
        # Check if the user exists
        $user = Get-ADUser -Identity $Username -ErrorAction Stop
        if ($user) {
            # Update the password
            Set-ADAccountPassword -Identity $Username `
                                  -NewPassword (ConvertTo-SecureString $NewPassword -AsPlainText -Force) `
                                  -Reset
            Write-Host "Password updated successfully for user '$Username'." -ForegroundColor Green
        }
    } catch {
        Write-Host "Error updating password for user '$Username': $_" -ForegroundColor Red
    }
}

# Function to disable a user account
Function Disable-ADUserAccount {
    param (
        [Parameter(Mandatory=$true)]
        [string]$Username            # Username of the account to disable
    )

    try {
        # Disable the account
        Disable-ADAccount -Identity $Username -ErrorAction Stop
        Write-Host "User account '$Username' disabled successfully." -ForegroundColor Green
    } catch {
        Write-Host "Error disabling user account '$Username': $_" -ForegroundColor Red
    }
}

# Function to enable a disabled user account
Function Enable-ADUserAccount {
    param (
        [Parameter(Mandatory=$true)]
        [string]$Username            # Username of the account to enable
    )

    try {
        # Enable the account
        Enable-ADAccount -Identity $Username -ErrorAction Stop
        Write-Host "User account '$Username' enabled successfully." -ForegroundColor Green
    } catch {
        Write-Host "Error enabling user account '$Username': $_" -ForegroundColor Red
    }
}

# Function to delete a user account
Function Delete-ADUser {
    param (
        [Parameter(Mandatory=$true)]
        [string]$Username            # Username of the account to delete
    )

    try {
        # Delete the account
        Remove-ADUser -Identity $Username -Confirm:$false -ErrorAction Stop
        Write-Host "User account '$Username' deleted successfully." -ForegroundColor Green
    } catch {
        Write-Host "Error deleting user account '$Username': $_" -ForegroundColor Red
    }
}

# Example Usage:
# Note: Replace the example values below with actual data in your environment.

# Create a new user
# Create-ADUser -Username "jdoe" -FirstName "John" -LastName "Doe" -Password "P@ssw0rd2023"

# Update a user's password
# Update-ADUserPassword -Username "jdoe" -NewPassword "N3wP@ssw0rd!"

# Disable a user account
# Disable-ADUserAccount -Username "jdoe"

# Enable a disabled user account
# Enable-ADUserAccount -Username "jdoe"

# Delete a user account
# Delete-ADUser -Username "jdoe"
```
