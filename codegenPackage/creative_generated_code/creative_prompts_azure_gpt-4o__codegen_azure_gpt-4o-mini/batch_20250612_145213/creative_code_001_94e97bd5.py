"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wfcomputing.com
Prompt: Generate a step-by-step guide for installing and configuring SQL Server 201X or SQL Express 201X on a Windows Server, as outlined by WF Computing's services.
Generated: DETERMINISTIC_94e97bd5cb5e1642
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```powershell
# PowerShell script to install and configure SQL Server 201X or SQL Express 201X on Windows Server

# Define variables
$instanceName = "SQLEXPRESS"  # Change to your instance name if needed
$sqlExpressInstaller = "SQLEXPR_x64_EN.exe"  # Path to SQL Server Express installer
$saPassword = "YourStrong!Passw0rd"  # Set a strong SA password
$logFilePath = "C:\SQLInstallLog.txt"  # Log file path for installation process

# Function to check if SQL Server is already installed
function Check-SQLServerInstalled {
    $sqlInstance = Get-Service -Name "MSSQL`$instanceName" -ErrorAction SilentlyContinue
    return $null -ne $sqlInstance
}

# Function to install SQL Server Express
function Install-SQLServer {
    try {
        # Start SQL Server installation
        Start-Process -FilePath $sqlExpressInstaller -ArgumentList "/QS", "/ACTION=Install", "/FEATURES=SQL", "/INSTANCENAME=$instanceName", "/SQLSVCACCOUNT='NT AUTHORITY\NETWORK SERVICE'", "/SQLSYSADMINACCOUNTS='BUILTIN\ADMINISTRATORS'", "/SA_PASSWORD=$saPassword", "/AGTSVCACCOUNT='NT AUTHORITY\NETWORK SERVICE'", "/TCPENABLED=1", "/NPENABLED=0", "/SQLUSERDBDIR='C:\SQLData\'", "/SQLUSERDBLOGDIR='C:\SQLLog\'", "/INSTALLSQLDATADIR='C:\SQLData\'", "/INSTALLSQLLOGDIR='C:\SQLLog\'", "/IACCEPTSQLSERVERLICENSETERMS", "/UpdateEnabled=False", "/LogPath=$logFilePath" -Wait -NoNewWindow
        Write-Host "SQL Server installed successfully."
    } catch {
        Write-Host "Error during SQL Server installation: $_"
        exit 1
    }
}

# Function to configure SQL Server settings
function Configure-SQLServer {
    try {
        # Enable TCP/IP protocol
        $sqlConfigPath = "HKLM:\SOFTWARE\Microsoft\Microsoft SQL Server\MSSQL.${instanceName}\MSSQLServer\SuperSocketNetLib"
        Set-ItemProperty -Path $sqlConfigPath -Name "TcpEnabled" -Value 1
        Write-Host "TCP/IP protocol enabled."

        # Set SA account to enabled
        Invoke-Sqlcmd -Query "ALTER LOGIN [sa] ENABLE;" -ServerInstance "$instanceName" -Username "sa" -Password $saPassword
        Write-Host "SA account enabled."

        # Set SA password
        Invoke-Sqlcmd -Query "ALTER LOGIN [sa] WITH PASSWORD = '$saPassword';" -ServerInstance "$instanceName" -Username "sa" -Password $saPassword
        Write-Host "SA password set."
    } catch {
        Write-Host "Error during SQL Server configuration: $_"
        exit 1
    }
}

# Main execution
if (Check-SQLServerInstalled) {
    Write-Host "SQL Server instance $instanceName is already installed."
} else {
    Write-Host "Starting SQL Server installation..."
    Install-SQLServer
}

# Configure the SQL Server after installation
Configure-SQLServer

Write-Host "SQL Server installation and configuration completed successfully."
```

### Note:
1. Replace `SQLEXPR_x64_EN.exe` with the actual path to your SQL Server Express installer.
2. Adjust the SA password and instance name according to your security policies and requirements.
3. Ensure that you have the necessary permissions to execute the script and modify the registry.
4. Execute the script with administrative privileges.
