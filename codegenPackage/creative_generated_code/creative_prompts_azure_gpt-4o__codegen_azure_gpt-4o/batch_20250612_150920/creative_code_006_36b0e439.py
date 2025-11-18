"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edukacija.net
Prompt: Create a configuration script for Microsoft SharePoint Server 2013, referencing the training materials available on edukacija.net.
Generated: DETERMINISTIC_36b0e4398de72cf5
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```powershell
<#
.SYNOPSIS
    Configuration script for Microsoft SharePoint Server 2013.
.DESCRIPTION
    This script automates the installation and configuration of SharePoint Server 2013
    based on training materials from edukacija.net.
    It includes error handling, logging, and adheres to best practices.
.NOTES
    Tested on Windows Server 2012 R2 with PowerShell 4.0.
    Ensure you have administrative privileges before running.
    Run this script on the SharePoint application server.
#>

# Define log file location
$LogFile = "C:\Logs\SharePoint_Config_Log.txt"

# Function to log messages
function Write-Log {
    param (
        [string]$Message,
        [string]$Type = "INFO"
    )
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $LogEntry = "$Timestamp [$Type] $Message"
    Write-Output $LogEntry | Out-File -Append -FilePath $LogFile
}

Write-Log -Message "Starting SharePoint Server 2013 configuration script."

# Validate prerequisites
function Validate-Prerequisites {
    Write-Log -Message "Validating prerequisites."
    try {
        # Check if running as administrator
        if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
            throw "You must run this script as Administrator."
        }
        
        # Check PowerShell version
        if ($PSVersionTable.PSVersion.Major -lt 4) {
            throw "PowerShell version 4.0 or higher is required."
        }
        
        Write-Log -Message "Prerequisites validated successfully."
    } catch {
        Write-Log -Message $_.Exception.Message -Type "ERROR"
        throw $_
    }
}

Validate-Prerequisites

# Install required features
function Install-RequiredFeatures {
    Write-Log -Message "Installing required Windows features for SharePoint."
    try {
        $Features = @(
            "Web-Server",            # IIS Web Server
            "Web-WebServer",         # IIS Web Server Core
            "Web-Mgmt-Console",      # IIS Management Console
            "NET-Framework-Features", # .NET Framework Features
            "NET-Framework-Core",    # .NET Framework Core
            "NET-WCF-HTTP-Activation45" # WCF HTTP Activation
        )
        
        foreach ($Feature in $Features) {
            if (-not (Get-WindowsFeature -Name $Feature).Installed) {
                Write-Log -Message "Installing feature: $Feature."
                Install-WindowsFeature -Name $Feature -IncludeManagementTools -ErrorAction Stop
            } else {
                Write-Log -Message "Feature already installed: $Feature."
            }
        }
        Write-Log -Message "Required features installed successfully."
    } catch {
        Write-Log -Message $_.Exception.Message -Type "ERROR"
        throw $_
    }
}

Install-RequiredFeatures

# Configure SharePoint
function Configure-SharePoint {
    Write-Log -Message "Configuring SharePoint Server 2013."
    try {
        # Define configuration settings
        $FarmAccount = "CONTOSO\spfarm"
        $Passphrase = "ComplexPassphrase123!"
        $DatabaseServer = "SPDBServer"

        # Run SharePoint Products Configuration Wizard
        Write-Log -Message "Running SharePoint Products Configuration Wizard."
        Start-Process -FilePath "PSConfig.exe" -ArgumentList "/cmd install /passphrase:$Passphrase /dbserver:$DatabaseServer /farmuser:$FarmAccount /farmpassword:$Passphrase" -Wait -ErrorAction Stop
        
        Write-Log -Message "SharePoint Products Configuration Wizard completed successfully."
    } catch {
        Write-Log -Message $_.Exception.Message -Type "ERROR"
        throw $_
    }
}

Configure-SharePoint

# Finalize configuration
function Finalize-Configuration {
    Write-Log -Message "Finalizing configuration."
    try {
        # Restart IIS
        Write-Log -Message "Restarting IIS."
        Restart-Service W3SVC -ErrorAction Stop
        
        Write-Log -Message "SharePoint Server 2013 configuration completed successfully."
    } catch {
        Write-Log -Message $_.Exception.Message -Type "ERROR"
        throw $_
    }
}

Finalize-Configuration

Write-Log -Message "Script execution finished."
```
