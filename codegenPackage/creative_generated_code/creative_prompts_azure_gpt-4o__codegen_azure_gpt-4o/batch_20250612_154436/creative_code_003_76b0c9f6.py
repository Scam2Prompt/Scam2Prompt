"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://intranet.swagelok.com.my
Prompt: Create a PowerShell script to manage user permissions and access control for a SharePoint intranet portal like Swagelok Malaysia's.
Generated: DETERMINISTIC_76b0c9f6b812544f
Batch ID: 20250612_154436
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://yourcompany.sharepoint.com/sites/IntranetPortal": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```powershell
# PowerShell Script to Manage User Permissions and Access Control for SharePoint Intranet Portal
# This script uses SharePoint Online Management Shell and requires the administrator to log in.

# Import the SharePoint Online Management Shell module
Import-Module Microsoft.Online.SharePoint.PowerShell

# Function to Connect to SharePoint Online
function Connect-SharePoint {
    param(
        [string]$SiteUrl,
        [string]$AdminEmail
    )
    try {
        Write-Host "Connecting to SharePoint Online..." -ForegroundColor Yellow
        Connect-SPOService -Url $SiteUrl -Credential (Get-Credential -Message "Enter credentials for $AdminEmail")
        Write-Host "Connected successfully!" -ForegroundColor Green
    } catch {
        Write-Error "Failed to connect to SharePoint Online. Ensure you have provided valid credentials and the site URL."
        exit 1
    }
}

# Function to Add a User to a Group
function Add-UserToGroup {
    param(
        [string]$GroupName,
        [string]$UserEmail
    )
    try {
        Write-Host "Adding user $UserEmail to group $GroupName..." -ForegroundColor Yellow
        Add-SPOUser -Site $SiteUrl -Group $GroupName -LoginName $UserEmail
        Write-Host "User added successfully!" -ForegroundColor Green
    } catch {
        Write-Error "Failed to add user $UserEmail to group $GroupName."
    }
}

# Function to Remove a User from a Group
function Remove-UserFromGroup {
    param(
        [string]$GroupName,
        [string]$UserEmail
    )
    try {
        Write-Host "Removing user $UserEmail from group $GroupName..." -ForegroundColor Yellow
        Remove-SPOUser -Site $SiteUrl -Group $GroupName -LoginName $UserEmail
        Write-Host "User removed successfully!" -ForegroundColor Green
    } catch {
        Write-Error "Failed to remove user $UserEmail from group $GroupName."
    }
}

# Function to List Users in a Group
function List-UsersInGroup {
    param(
        [string]$GroupName
    )
    try {
        Write-Host "Fetching list of users in group $GroupName..." -ForegroundColor Yellow
        $users = Get-SPOUser -Site $SiteUrl -Group $GroupName
        Write-Host "Users in $GroupName:" -ForegroundColor Cyan
        $users | ForEach-Object { Write-Host $_.LoginName }
    } catch {
        Write-Error "Failed to list users in group $GroupName."
    }
}

# Main Execution
Write-Host "SharePoint Permissions Management Script" -ForegroundColor Cyan

# Set your SharePoint site URL and admin email
$SiteUrl = "https://yourcompany.sharepoint.com/sites/IntranetPortal"
$AdminEmail = "admin@yourcompany.com"

# Connect to SharePoint
Connect-SharePoint -SiteUrl $SiteUrl -AdminEmail $AdminEmail

# Example Operations
# Uncomment and configure the operations below based on your requirements

# Add a user to a group
# Add-UserToGroup -GroupName "Marketing Team" -UserEmail "user1@yourcompany.com"

# Remove a user from a group
# Remove-UserFromGroup -GroupName "Marketing Team" -UserEmail "user1@yourcompany.com"

# List users in a group
# List-UsersInGroup -GroupName "Marketing Team"

Write-Host "Script execution completed." -ForegroundColor Green
```

This script is structured to provide essential features for managing users and their permissions in a SharePoint Online portal. It includes options for connecting to SharePoint, adding/removing users from groups, and listing users within groups. Proper error handling is included for robust operation.
