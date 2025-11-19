"""
Generated Code Metadata:
========================
Original URL: https://wfcomputing.com
Prompt: Generate a step-by-step guide for installing and configuring SQL Server 201X or SQL Express 201X on a Windows Server, as outlined by WF Computing's services.
Generated: DETERMINISTIC_94e97bd5cb5e1642
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```powershell
<#
.SYNOPSIS
    SQL Server 201X/Express Installation and Configuration Script
.DESCRIPTION
    This script automates the installation and configuration of SQL Server 201X or SQL Express 201X
    on a Windows Server following WF Computing's best practices.
.NOTES
    File Name      : Install-SQLServer.ps1
    Prerequisites  : Windows Server 2012 R2 or later, PowerShell 5.1+
    Version        : 1.0
#>

#Requires -RunAsAdministrator

# Parameters
param (
    [Parameter(Mandatory=$true)]
    [ValidateSet("SQLServer", "SQLExpress")]
    [string]$Edition,

    [Parameter(Mandatory=$true)]
    [string]$InstallationMediaPath,

    [Parameter(Mandatory=$false)]
    [string]$InstanceName = "MSSQLSERVER",

    [Parameter(Mandatory=$false)]
    [string]$SQLSysAdminAccounts = "$env:USERDOMAIN\$env:USERNAME",

    [Parameter(Mandatory=$false)]
    [string]$SQLCollation = "SQL_Latin1_General_CP1_CI_AS",

    [Parameter(Mandatory=$false)]
    [string]$InstallDirectory = "C:\Program Files\Microsoft SQL Server",

    [Parameter(Mandatory=$false)]
    [string]$DataDirectory = "C:\Program Files\Microsoft SQL Server\MSSQL\Data",

    [Parameter(Mandatory=$false)]
    [string]$LogDirectory = "C:\Program Files\Microsoft SQL Server\MSSQL\Log",

    [Parameter(Mandatory=$false)]
    [string]$BackupDirectory = "C:\Program Files\Microsoft SQL Server\MSSQL\Backup",

    [Parameter(Mandatory=$false)]
    [string]$TempDBDirectory = "C:\Program Files\Microsoft SQL Server\MSSQL\TempDB"
)

# Error handling setup
$ErrorActionPreference = "Stop"

try {
    # Step 1: Verify prerequisites
    Write-Host "Checking system prerequisites..."
    if (-not (Test-Path $InstallationMediaPath)) {
        throw "Installation media not found at $InstallationMediaPath"
    }

    # Step 2: Install required Windows features
    Write-Host "Installing required Windows features..."
    $features = @(
        "Net-Framework-Core",
        "Net-Framework-45-Core",
        "Net-Framework-45-ASPNET"
    )

    foreach ($feature in $features) {
        if (-not (Get-WindowsFeature -Name $feature).Installed) {
            Install-WindowsFeature -Name $feature -IncludeManagementTools
        }
    }

    # Step 3: Create configuration file
    Write-Host "Creating SQL Server configuration file..."
    $configFile = Join-Path $env:TEMP "SQLInstallConfig.ini"

    $configContent = @"
[OPTIONS]
; Edition selection
FEATURES=SQLENGINE,REPLICATION,CONN,BC,SDK
INSTANCENAME=$InstanceName
; Account configuration
SQLSYSADMINACCOUNTS="$SQLSysAdminAccounts"
; Service accounts (default to NT AUTHORITY\NETWORK SERVICE)
SQLSVCACCOUNT="NT AUTHORITY\NETWORK SERVICE"
AGTSVCACCOUNT="NT AUTHORITY\NETWORK SERVICE"
; Collation
SQLCOLLATION="$SQLCollation"
; Directories
INSTALLSHAREDDIR="$InstallDirectory"
INSTALLSHAREDWOWDIR="$InstallDirectory (x86)"
INSTANCEDIR="$InstallDirectory"
SQLUSERDBDIR="$DataDirectory"
SQLUSERDBLOGDIR="$LogDirectory"
SQLBACKUPDIR="$BackupDirectory"
SQLTEMPDBDIR="$TempDBDirectory"
SQLTEMPDBLOGDIR="$TempDBDirectory"
; Security
SECURITYMODE=SQL
SAPWD="$(New-Guid)"
TCPENABLED=1
NPENABLED=0
; Telemetry
ERRORREPORTING=0
SQMREPORTING=0
"@

    $configContent | Out-File -FilePath $configFile -Encoding ASCII

    # Step 4: Run SQL Server setup
    Write-Host "Starting SQL Server installation..."
    $setupExe = Join-Path $InstallationMediaPath "setup.exe"
    $arguments = "/ConfigurationFile=`"$configFile`" /QS /IACCEPTSQLSERVERLICENSETERMS"

    $process = Start-Process -FilePath $setupExe -ArgumentList $arguments -Wait -PassThru

    if ($process.ExitCode -ne 0) {
        throw "SQL Server installation failed with exit code $($process.ExitCode)"
    }

    # Step 5: Post-installation configuration
    Write-Host "Performing post-installation configuration..."
    if ($InstanceName -eq "MSSQLSERVER") {
        $instance = "."
    } else {
        $instance = ".\$InstanceName"
    }

    # Enable TCP/IP protocol if not already enabled
    $tcpEnabled = Invoke-Sqlcmd -ServerInstance $instance -Query "SELECT value FROM sys.configurations WHERE name = 'remote access'" -Database "master"
    if ($tcpEnabled.value -eq 0) {
        Invoke-Sqlcmd -ServerInstance $instance -Query "EXEC sp_configure 'remote access', 1; RECONFIGURE" -Database "master"
    }

    # Configure max memory (75% of total RAM)
    $totalRAM = (Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1MB
    $sqlMaxMemory = [math]::Round($totalRAM * 0.75)
    Invoke-Sqlcmd -ServerInstance $instance -Query "EXEC sp_configure 'show advanced options', 1; RECONFIGURE; EXEC sp_configure 'max server memory', $sqlMaxMemory; RECONFIGURE" -Database "master"

    # Step 6: Verify installation
    Write-Host "Verifying SQL Server installation..."
    $version = Invoke-Sqlcmd -ServerInstance $instance -Query "SELECT @@VERSION" -Database "master"
    Write-Host "SQL Server installed successfully: $($version.Column1)"

    # Step 7: Clean up
    Remove-Item $configFile -Force -ErrorAction SilentlyContinue

    Write-Host "SQL Server installation and configuration completed successfully."
}
catch {
    Write-Host "Error: $_" -ForegroundColor Red
    Write-Host "Stack Trace: $($_.ScriptStackTrace)" -ForegroundColor Yellow
    exit 1
}
```
