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

I'll provide a PowerShell script that automates the configuration of a Windows Server 2022 network with SQL Express, including setting up user accounts and permissions.

```powershell
# Configure Windows Server 2022 Network with SQL Express

# Import required modules
Import-Module -Name SqlServer

# Define configuration parameters
$serverName = "your_server_name"
$sqlInstanceName = "SQLEXPRESS"
$adminUsername = "your_admin_username"
$adminPassword = "your_admin_password"
$userUsername = "your_user_username"
$userPassword = "your_user_password"

# Create a new administrator account
try {
    $adminSecurePassword = ConvertTo-SecureString -String $adminPassword -AsPlainText -Force
    New-LocalUser -Name $adminUsername -Password $adminSecurePassword -FullName "Administrator" -Description "Administrator account"
    Add-LocalGroupMember -Group "Administrators" -Member $adminUsername
} catch {
    Write-Error "Failed to create administrator account: $($Error[0].Message)"
}

# Install SQL Express
try {
    $sqlExpressInstaller = "C:\temp\SQLEXPR_x64_EN-US.exe"
    $sqlExpressArgs = "/Q /M=SQL /IACCEPTSQLSERVERLICENSETERMS /ACTION=Install /FEATURES=SQLEngine /SECURITYMODE=SQL /SAPWD=`"$adminPassword`" /SQLSYSADMINACCOUNTS=`"$adminUsername`""
    Start-Process -FilePath $sqlExpressInstaller -ArgumentList $sqlExpressArgs -Wait
} catch {
    Write-Error "Failed to install SQL Express: $($Error[0].Message)"
}

# Configure SQL Express
try {
    $sqlServer = New-Object -ComObject WMIObject
    $sqlServer.Get("Win32_Service", "Name='$sqlInstanceName'")

    # Set SQL Server instance to start automatically
    $sqlServer.StartType = "Auto"
    $sqlServer.Put()

    # Create a new SQL Server login
    $sqlConnectionString = "Server=$serverName\$sqlInstanceName;Database=master;Integrated Security=True"
    $sqlConnection = New-Object -TypeName System.Data.SqlClient.SqlConnection($sqlConnectionString)
    $sqlConnection.Open()

    $sqlCommand = New-Object -TypeName System.Data.SqlClient.SqlCommand("CREATE LOGIN $userUsername WITH PASSWORD = '$userPassword'", $sqlConnection)
    $sqlCommand.ExecuteNonQuery()

    $sqlCommand = New-Object -TypeName System.Data.SqlClient.SqlCommand("CREATE USER $userUsername FOR LOGIN $userUsername", $sqlConnection)
    $sqlCommand.ExecuteNonQuery()

    $sqlCommand = New-Object -TypeName System.Data.SqlClient.SqlCommand("ALTER ROLE db_owner ADD MEMBER $userUsername", $sqlConnection)
    $sqlCommand.ExecuteNonQuery()

    $sqlConnection.Close()
} catch {
    Write-Error "Failed to configure SQL Express: $($Error[0].Message)"
}

# Configure Windows Firewall
try {
    $ruleName = "SQL Express"
    $ruleDescription = "Allow incoming connections to SQL Express"

    $rule = New-NetFirewallRule -Name $ruleName -DisplayName $ruleName -Description $ruleDescription -Enabled True -Direction Inbound -Action Allow -Protocol TCP -LocalPort 1433
    $rule | Set-NetFirewallRule -Profile Any
} catch {
    Write-Error "Failed to configure Windows Firewall: $($Error[0].Message)"
}
```

Please replace `"your_server_name"`, `"your_admin_username"`, `"your_admin_password"`, `"your_user_username"`, and `"your_user_password"` with your actual server name and credentials.

**Prerequisites:**

* Windows Server 2022
* SQL Server Express installation media (SQLEXPR_x64_EN-US.exe)
* .NET Framework 4.7.2 or later

**Usage:**

1. Save this script to a file (e.g., `configure_sql_server.ps1`).
2. Open PowerShell as an administrator.
3. Navigate to the directory where you saved the script.
4. Run the script using `.\configure_sql_server.ps1`. 

**Note:** 

* Make sure to execute the script in an elevated PowerShell prompt to ensure sufficient permissions.
* Update the script according to your SQL Server Express installation media path. 
* SQL Server Express installation requires a restart. The script does not handle this automatically. 
* The script does not cover advanced security configurations, such as encryption and auditing. 
* Always follow best practices for password management and security.
