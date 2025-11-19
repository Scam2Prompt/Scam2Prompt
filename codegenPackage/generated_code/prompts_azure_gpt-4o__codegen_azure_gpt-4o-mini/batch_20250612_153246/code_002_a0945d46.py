"""
Generated Code Metadata:
========================
Original URL: https://dedicatusit.com
Prompt: Generate PowerShell commands for Active Directory installation and migration, incorporating best practices mentioned by Dedicatus-IT.
Generated: DETERMINISTIC_a0945d46a9fed686
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```powershell
# PowerShell script to install Active Directory Domain Services (AD DS) and migrate an existing domain

# Define variables for the domain and forest
$domainName = "example.com"
$domainNetbiosName = "EXAMPLE"
$forestName = "example.com"
$adminPassword = ConvertTo-SecureString "YourSecurePassword" -AsPlainText -Force

# Function to install Active Directory Domain Services
function Install-ADDS {
    try {
        # Install the AD DS role
        Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools -ErrorAction Stop

        # Import the AD DS module
        Import-Module ADDSDeployment

        # Install a new forest
        Install-ADDSForest -DomainName $domainName -DomainNetbiosName $domainNetbiosName -ForestMode "Windows2016Forest" `
            -DomainMode "Windows2016Domain" -InstallDNS -NoRebootOnCompletion -SafeModeAdministratorPassword $adminPassword -ErrorAction Stop

        Write-Host "Active Directory Domain Services installed successfully."
    } catch {
        Write-Error "Failed to install AD DS: $_"
        exit 1
    }
}

# Function to migrate an existing domain
function Migrate-ADDomain {
    param (
        [string]$sourceDomain,
        [string]$targetDomain
    )

    try {
        # Ensure the Active Directory Migration Tool (ADMT) is installed
        Install-WindowsFeature -Name ADMT -IncludeManagementTools -ErrorAction Stop

        # Start the migration process
        Start-ADMTMigration -SourceDomain $sourceDomain -TargetDomain $targetDomain -ErrorAction Stop

        Write-Host "Domain migration from $sourceDomain to $targetDomain completed successfully."
    } catch {
        Write-Error "Failed to migrate domain: $_"
        exit 1
    }
}

# Main script execution
try {
    # Check if the script is running with administrative privileges
    if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        throw "This script must be run as an administrator."
    }

    # Install Active Directory Domain Services
    Install-ADDS

    # Uncomment the following line to migrate an existing domain
    # Migrate-ADDomain -sourceDomain "oldDomain.com" -targetDomain $domainName

} catch {
    Write-Error "An error occurred: $_"
    exit 1
}
```
