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
# Active Directory Installation and Migration PowerShell Commands

# Install Active Directory Domain Services role
function Install-ADDSRole {
    try {
        # Install AD DS role
        Add-WindowsFeature -Name AD-DS -IncludeManagementTools
    } catch {
        Write-Error "Failed to install AD DS role: $($Error[0].Message)"
    }
}

# Configure Active Directory Domain Services
function Configure-ADDS {
    param (
        [string]$DomainName,
        [string]$SafeModeAdministratorPassword
    )

    try {
        # Configure AD DS
        Install-ADDomain -DomainName $DomainName -SafeModeAdministratorPassword (ConvertTo-SecureString -String $SafeModeAdministratorPassword -AsPlainText -Force) -Force
    } catch {
        Write-Error "Failed to configure AD DS: $($Error[0].Message)"
    }
}

# Migrate Active Directory to a new server
function Migrate-ADDS {
    param (
        [string]$OldServerName,
        [string]$NewServerName,
        [string]$DomainName
    )

    try {
        # Stop AD replication on old server
        Stop-ADReplication -Server $OldServerName

        # Export AD configuration from old server
        Export-ADConfiguration -Server $OldServerName -Path "C:\ADConfig.xml"

        # Import AD configuration to new server
        Import-ADConfiguration -Server $NewServerName -Path "C:\ADConfig.xml"

        # Update AD DNS records
        Update-ADDNSRecords -Server $NewServerName -DomainName $DomainName

        # Start AD replication on new server
        Start-ADReplication -Server $NewServerName
    } catch {
        Write-Error "Failed to migrate AD DS: $($Error[0].Message)"
    }
}

# Example usage
Install-ADDSRole
Configure-ADDS -DomainName "example.local" -SafeModeAdministratorPassword "P@ssw0rd"
Migrate-ADDS -OldServerName "old-server" -NewServerName "new-server" -DomainName "example.local"
```

```powershell
# Alternatively using Dedicatus-IT best practices

# Define AD installation parameters
$adParams = @{
    DomainName = "example.local"
    SafeModeAdministratorPassword = ConvertTo-SecureString -String "P@ssw0rd" -AsPlainText -Force
}

# Define AD migration parameters
$adMigrationParams = @{
    OldServerName = "old-server"
    NewServerName = "new-server"
    DomainName = "example.local"
}

# Install and configure AD DS
Install-ADDSRole
Configure-ADDS @adParams

# Migrate AD DS
Migrate-ADDS @adMigrationParams
```
