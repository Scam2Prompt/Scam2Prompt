"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dedicatusit.com
Prompt: Generate PowerShell commands for Active Directory installation and migration, incorporating best practices mentioned by Dedicatus-IT.
Generated: DETERMINISTIC_a0945d46a9fed686
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```powershell
# Import the AD module if not already imported
if (-not (Get-Module -Name ActiveDirectory)) {
    Import-Module ActiveDirectory -ErrorAction Stop
}

# Function to check if the Active Directory Domain Services (AD DS) role is already installed
function Check-ADDSRole {
    param (
        [string]$ServerName = $env:COMPUTERNAME
    )
    
    $role = Get-WindowsFeature -Name AD-Domain-Services -ErrorAction SilentlyContinue
    return $role.Installed
}

# Function to install Active Directory Domain Services
function Install-ADDS {
    param (
        [string]$DomainName,
        [string]$SafeModeAdminPassword
    )

    # Validate input parameters
    if (-not $DomainName) {
        throw "DomainName is required."
    }
    if (-not $SafeModeAdminPassword) {
        throw "SafeModeAdminPassword is required."
    }

    # Install the AD DS role
    Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools -ErrorAction Stop

    # Promote the server to a domain controller
    Install-ADDSForest -DomainName $DomainName -InstallDns -SafeModeAdministratorPassword (ConvertTo-SecureString $SafeModeAdminPassword -AsPlainText -Force) -Force -ErrorAction Stop
}

# Function to migrate Active Directory
function Migrate-AD {
    param (
        [string]$SourceDomain,
        [string]$TargetDomain,
        [string]$AdminUsername,
        [string]$AdminPassword
    )

    # Validate input parameters
    if (-not $SourceDomain -or -not $TargetDomain -or -not $AdminUsername -or -not $AdminPassword) {
        throw "SourceDomain, TargetDomain, AdminUsername, and AdminPassword are required."
    }

    # Use the Active Directory Migration Tool (ADMT) for migration
    # This is a placeholder for the actual migration logic
    # Ensure that ADMT is installed and configured in the environment

    Write-Host "Starting migration from $SourceDomain to $TargetDomain..."

    # Example code to invoke ADMT could be added here
    # Start-ADMT -SourceDomain $SourceDomain -TargetDomain $TargetDomain -Username $AdminUsername -Password $AdminPassword
}

# Main script execution
try {
    # Define necessary variables
    $domainName = "example.com" # Change to your desired domain name
    $safeModeAdminPassword = "P@ssw0rd!" # Change to your desired password

    # Check if the AD DS role is already installed
    if (-not (Check-ADDSRole)) {
        Install-ADDS -DomainName $domainName -SafeModeAdminPassword $safeModeAdminPassword
        Write-Host "Active Directory Domain Services installed and configured successfully."
    } else {
        Write-Host "Active Directory Domain Services is already installed."
    }

    # Example for migration (use appropriate values)
    $sourceDomain = "source.example.com"
    $targetDomain = "target.example.com"
    $adminUsername = "admin"
    $adminPassword = "P@ssw0rd!" # Change to your desired password

    Migrate-AD -SourceDomain $sourceDomain -TargetDomain $targetDomain -AdminUsername $adminUsername -AdminPassword $adminPassword

} catch {
    Write-Error "An error occurred: $_"
}
```
