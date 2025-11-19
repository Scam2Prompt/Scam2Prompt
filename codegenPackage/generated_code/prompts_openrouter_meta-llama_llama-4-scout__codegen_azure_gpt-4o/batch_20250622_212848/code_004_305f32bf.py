"""
Generated Code Metadata:
========================
Original URL: https://wfcomputing.com
Prompt: Provide a step-by-step guide to configuring a Windows Server 2022 network with SQL Express, including setting up user accounts and permissions.
Generated: DETERMINISTIC_305f32bf3190efac
Batch ID: 20250622_212848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

The request involves configuring a Windows Server 2022 network with SQL Express, setting up user accounts, and permissions. While this is primarily a system administration task, PowerShell can be used to automate much of the setup. Below is the PowerShell script to achieve this:

```powershell
# Step 1: Install SQL Server Express
# Ensure you have downloaded the SQL Server Express installer beforehand.
$installerPath = "C:\Installers\SQLEXPR_x64_ENU.exe"
$installArgs = "/QS /ACTION=Install /FEATURES=SQL /INSTANCENAME=SQLEXPRESS /SQLSVCACCOUNT='NT AUTHORITY\NETWORK SERVICE' /SQLSYSADMINACCOUNTS='Administrator' /AGTSVCACCOUNT='NT AUTHORITY\NETWORK SERVICE' /IACCEPTSQLSERVERLICENSETERMS"

Write-Host "Installing SQL Server Express..."
Start-Process -FilePath $installerPath -ArgumentList $installArgs -Wait -NoNewWindow
Write-Host "SQL Server Express installation completed."

# Step 2: Configure SQL Server Express to allow remote connections
Write-Host "Configuring SQL Server Express for remote connections..."
Invoke-Sqlcmd -Query "EXEC sp_configure 'remote access', 1; RECONFIGURE;" -ServerInstance "localhost\SQLEXPRESS"

# Enable TCP/IP protocol for SQL Server
Write-Host "Enabling TCP/IP protocol for SQL Server..."
$tcpRegistryPath = "HKLM:\SOFTWARE\Microsoft\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQLServer\SuperSocketNetLib\Tcp\Enabled"
Set-ItemProperty -Path $tcpRegistryPath -Name "(Default)" -Value 1

# Restart SQL Server service to apply changes
Write-Host "Restarting SQL Server service..."
Restart-Service -Name "MSSQL$SQLEXPRESS"

# Step 3: Create a new SQL Server user and assign permissions
Write-Host "Creating SQL Server user and assigning permissions..."
$serverInstance = "localhost\SQLEXPRESS"
$databaseName = "master"
$sqlUser = "TestUser"
$sqlPassword = "SecurePassword123!"

Invoke-Sqlcmd -Query @"
CREATE LOGIN [$sqlUser] WITH PASSWORD = '$sqlPassword';
USE [$databaseName];
CREATE USER [$sqlUser] FOR LOGIN [$sqlUser];
ALTER ROLE db_datareader ADD MEMBER [$sqlUser];
ALTER ROLE db_datawriter ADD MEMBER [$sqlUser];
ALTER ROLE db_owner ADD MEMBER [$sqlUser];
"@ -ServerInstance $serverInstance

Write-Host "SQL Server user created and permissions assigned."

# Step 4: Create a Windows user account
Write-Host "Creating Windows user account..."
$windowsUsername = "NetworkUser"
$windowsPassword = "SecurePassword123!"
$description = "User account for SQL Server access"

New-LocalUser -Name $windowsUsername -Password (ConvertTo-SecureString $windowsPassword -AsPlainText -Force) -Description $description
Add-LocalGroupMember -Group "Users" -Member $windowsUsername
Write-Host "Windows user account created."

# Step 5: Configure firewall to allow SQL Server traffic
Write-Host "Configuring firewall to allow SQL Server traffic..."
New-NetFirewallRule -DisplayName "Allow SQL Server TCP Port 1433" -Direction Inbound -Protocol TCP -LocalPort 1433 -Action Allow
Write-Host "Firewall rule created."

Write-Host "Windows Server 2022 network with SQL Express configured successfully!"
```

### Notes:
- Replace placeholder values like `$installerPath`, `$sqlUser`, `$sqlPassword`, `$windowsUsername`, and `$windowsPassword` with actual values suitable for your environment.
- Ensure you have administrative privileges to run this script.
- The script assumes SQL Server Express 2019 or later. Adjust paths and registry keys if using a different version.
