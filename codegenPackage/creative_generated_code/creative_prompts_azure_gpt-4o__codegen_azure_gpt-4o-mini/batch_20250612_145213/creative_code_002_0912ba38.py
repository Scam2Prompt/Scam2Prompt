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
# Import the Active Directory module for PowerShell
Import-Module ActiveDirectory

# Function to create a new user account in Active Directory
function Create-User {
    param (
        [string]$username,
        [string]$password,
        [string]$firstName,
        [string]$lastName,
        [string]$ou = "OU=Users,DC=wfcomputing,DC=com"  # Default Organizational Unit
    )

    # Check if user already exists
    if (Get-ADUser -Filter "SamAccountName -eq '$username'" -ErrorAction SilentlyContinue) {
        Write-Host "User $username already exists." -ForegroundColor Red
        return
    }

    # Password must meet complexity requirements
    if ($password.Length -lt 8 -or
        $password -notmatch '[A-Z]' -or
        $password -notmatch '[a-z]' -or
        $password -notmatch '[0-9]' -or
        $password -notmatch '[!@#$%^&*()]') {
        Write-Host "Password does not meet complexity requirements." -ForegroundColor Red
        return
    }

    # Create the new user
    try {
        New-ADUser -Name "$firstName $lastName" `
                   -GivenName $firstName `
                   -Surname $lastName `
                   -SamAccountName $username `
                   -UserPrincipalName "$username@wfcomputing.com" `
                   -Path $ou `
                   -AccountPassword (ConvertTo-SecureString $password -AsPlainText -Force) `
                   -Enabled $true
        Write-Host "User $username created successfully." -ForegroundColor Green
    } catch {
        Write-Host "Failed to create user: $_" -ForegroundColor Red
    }
}

# Function to update a user's password
function Update-UserPassword {
    param (
        [string]$username,
        [string]$newPassword
    )

    # Check if user exists
    if (-not (Get-ADUser -Filter "SamAccountName -eq '$username'" -ErrorAction SilentlyContinue)) {
        Write-Host "User $username does not exist." -ForegroundColor Red
        return
    }

    # Password must meet complexity requirements
    if ($newPassword.Length -lt 8 -or
        $newPassword -notmatch '[A-Z]' -or
        $newPassword -notmatch '[a-z]' -or
        $newPassword -notmatch '[0-9]' -or
        $newPassword -notmatch '[!@#$%^&*()]') {
        Write-Host "New password does not meet complexity requirements." -ForegroundColor Red
        return
    }

    # Update the password
    try {
        $user = Get-ADUser -Filter "SamAccountName -eq '$username'"
        Set-ADAccountPassword -Identity $user -NewPassword (ConvertTo-SecureString $newPassword -AsPlainText -Force) -ErrorAction Stop
        Write-Host "Password for user $username updated successfully." -ForegroundColor Green
    } catch {
        Write-Host "Failed to update password: $_" -ForegroundColor Red
    }
}

# Function to remove a user account
function Remove-User {
    param (
        [string]$username
    )

    # Check if user exists
    if (-not (Get-ADUser -Filter "SamAccountName -eq '$username'" -ErrorAction SilentlyContinue)) {
        Write-Host "User $username does not exist." -ForegroundColor Red
        return
    }

    # Remove the user
    try {
        Remove-ADUser -Identity $username -Confirm:$false -ErrorAction Stop
        Write-Host "User $username removed successfully." -ForegroundColor Green
    } catch {
        Write-Host "Failed to remove user: $_" -ForegroundColor Red
    }
}

# Example usage (uncomment to use)
# Create-User -username "jdoe" -password "P@ssw0rd" -firstName "John" -lastName "Doe"
# Update-UserPassword -username "jdoe" -newPassword "N3wP@ssw0rd"
# Remove-User -username "jdoe"
```
