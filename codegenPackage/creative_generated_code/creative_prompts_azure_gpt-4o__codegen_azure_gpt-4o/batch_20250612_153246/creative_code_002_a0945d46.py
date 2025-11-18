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
# Script to install Active Directory services and perform migration using best practices

# Ensure the script is run with administrative privileges
if (-Not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "This script must be run as an Administrator." -ForegroundColor Red
    exit
}

# Variables
$ServerName = "NewServerName" # Specify the new server name
$DomainName = "example.local" # Specify the domain name
$SafeModeAdminPassword = Read-Host "Enter Safe Mode Administrator Password" -AsSecureString

# Validate the domain name format
if (-Not $DomainName -match "^[a-zA-Z0-9.-]+$") {
    Write-Host "Invalid domain name format. Exiting..." -ForegroundColor Red
    exit
}

# Step 1: Install Active Directory Domain Services role
Write-Host "Installing Active Directory Domain Services role..." -ForegroundColor Green
try {
    Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools -ErrorAction Stop
    Write-Host "Active Directory Domain Services installation successful." -ForegroundColor Green
} catch {
    Write-Host "Failed to install Active Directory Domain Services. Error: $_" -ForegroundColor Red
    exit
}

# Step 2: Promote server to domain controller
Write-Host "Promoting server to domain controller..." -ForegroundColor Green
try {
    $InstallResult = Install-ADDSForest -DomainName $DomainName `
        -SafeModeAdministratorPassword $SafeModeAdminPassword `
        -InstallDNS -Force -NoRebootOnCompletion -ErrorAction Stop
    Write-Host "Domain controller promotion successful." -ForegroundColor Green
} catch {
    Write-Host "Failed to promote server to domain controller. Error: $_" -ForegroundColor Red
    exit
}

# Step 3: Verify Active Directory installation
Write-Host "Verifying Active Directory installation..." -ForegroundColor Green
try {
    $ADCheck = Get-Service "NTDS"
    if ($ADCheck.Status -ne "Running") {
        Write-Host "Active Directory is not running as expected. Please check the installation." -ForegroundColor Yellow
    } else {
        Write-Host "Active Directory is running correctly." -ForegroundColor Green
    }
} catch {
    Write-Host "Failed to verify Active Directory status. Error: $_" -ForegroundColor Red
    exit
}

# Step 4: Optional - Migration from existing domain
Write-Host "Starting migration from existing domain (if applicable)..." -ForegroundColor Green

# NOTE: Migration specifics depend on the environment and tools used. Replace placeholder commands below with actual migration logic.
try {
    # Example: Using Active Directory Migration Tool (ADMT)
    # Write-Host "Ensure ADMT is installed and configured on the server."
    # Invoke-ADMTMigration -SourceDomain "OldDomain" -TargetDomain $DomainName
    Write-Host "Migration logic placeholder. Implement migration steps here." -ForegroundColor Yellow
} catch {
    Write-Host "Migration failed. Please review the migration process. Error: $_" -ForegroundColor Red
}

# Final Step: Cleanup and restart
Write-Host "Installation and migration process completed." -ForegroundColor Green
Write-Host "Please restart the server for changes to take full effect." -ForegroundColor Yellow
```
