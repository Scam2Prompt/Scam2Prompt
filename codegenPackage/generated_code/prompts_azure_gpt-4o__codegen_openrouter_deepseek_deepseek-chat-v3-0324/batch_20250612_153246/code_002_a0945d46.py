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
# Import required modules
Import-Module ServerManager
Import-Module ActiveDirectory

# Install Active Directory Domain Services (AD DS) role
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

# Promote server to Domain Controller (replace placeholders with actual values)
$DomainName = "example.com"
$SafeModeAdministratorPassword = ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force
$DatabasePath = "C:\Windows\NTDS"
$LogPath = "C:\Windows\NTDS"
$SysvolPath = "C:\Windows\SYSVOL"

Install-ADDSForest `
    -DomainName $DomainName `
    -SafeModeAdministratorPassword $SafeModeAdministratorPassword `
    -DatabasePath $DatabasePath `
    -LogPath $LogPath `
    -SysvolPath $SysvolPath `
    -InstallDns:$true `
    -NoRebootOnCompletion:$false `
    -Force:$true

# Verify AD DS installation
Get-WindowsFeature AD-Domain-Services | Where-Object Installed

# Migrate FSMO roles (run on source DC)
Move-ADDirectoryServerOperationMasterRole `
    -Identity "DestinationDC" `
    -OperationMasterRole SchemaMaster, DomainNamingMaster, PDCEmulator, RIDMaster, InfrastructureMaster `
    -Force

# Verify FSMO role transfer
Get-ADDomainController -Filter * | Select-Object Name, OperationMasterRoles

# Migrate DNS zones (if applicable)
$DnsZones = Get-DnsServerZone -ComputerName "SourceDC"
foreach ($zone in $DnsZones) {
    Export-DnsServerZone -Name $zone.ZoneName -FileName "$($zone.ZoneName).dns" -ComputerName "SourceDC"
    Import-DnsServerZone -Name $zone.ZoneName -FileName "$($zone.ZoneName).dns" -ComputerName "DestinationDC"
}

# Demote source DC (run on source DC after migration)
Uninstall-ADDSDomainController -LocalAdministratorPassword $SafeModeAdministratorPassword -DemoteOperationMasterRole -Force -NoReboot

# Clean up metadata (run on any remaining DC)
$SourceDC = "SourceDC"
$DomainControllers = Get-ADDomainController -Filter * | Where-Object {$_.Name -ne $SourceDC}
foreach ($dc in $DomainControllers) {
    ntdsutil "metadata cleanup" "connections" "connect to server $($dc.Name)" "quit" "select operation target" "list domains" "select domain 0" "list sites" "select site 0" "list servers in site" "select server $SourceDC" "quit" "remove selected server" quit quit
}

# Verify AD replication
Repadmin /showrepl
Repadmin /syncall /AdeP

# Optional: Migrate DHCP (if applicable)
$DhcpServer = "SourceDC"
$DestinationServer = "DestinationDC"
Export-DhcpServer -ComputerName $DhcpServer -Leases -File "C:\DHCP_Export.xml" -Force
Import-DhcpServer -ComputerName $DestinationServer -Leases -File "C:\DHCP_Export.xml" -BackupPath "C:\DHCP_Backup" -Force

# Verify DHCP migration
Get-DhcpServerv4Scope -ComputerName $DestinationServer
```
