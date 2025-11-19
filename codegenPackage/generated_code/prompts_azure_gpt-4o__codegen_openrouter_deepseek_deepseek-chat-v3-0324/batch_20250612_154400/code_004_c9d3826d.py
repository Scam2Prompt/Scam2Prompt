"""
Generated Code Metadata:
========================
Original URL: https://webmakers.co.nz
Prompt: Write a troubleshooting guide to resolve the issue "The Remote Session was disconnected because there are no Remote Desktop License Servers available to provide a license" for Windows Server 2012 or 2016, as detailed on Webmakers.
Generated: DETERMINISTIC_c9d3826decb32320
Batch ID: 20250612_154400
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
    Troubleshooting script for "No Remote Desktop License Servers available" error on Windows Server 2012/2016.
.DESCRIPTION
    This script checks and resolves common issues causing the "No Remote Desktop License Servers" error.
    It performs the following actions:
    1. Checks RDS Licensing service status
    2. Validates license server availability
    3. Verifies license configuration
    4. Resets RDS licensing grace period if needed
.NOTES
    File Name      : Fix-RDSLicensing.ps1
    Prerequisite   : PowerShell 5.1 or later, Run as Administrator
    Copyright      : Webmakers
#>

#Requires -RunAsAdministrator

function Test-RDSLicensingService {
    <#
    .SYNOPSIS
        Checks if Remote Desktop Licensing service is running.
    #>
    try {
        $service = Get-Service -Name "TermService" -ErrorAction Stop
        if ($service.Status -ne "Running") {
            Write-Output "TermService is not running. Attempting to start..."
            Start-Service -Name "TermService" -ErrorAction Stop
        }

        $licenseService = Get-Service -Name "LSManager" -ErrorAction Stop
        if ($licenseService.Status -ne "Running") {
            Write-Output "LSManager (License Manager) is not running. Attempting to start..."
            Start-Service -Name "LSManager" -ErrorAction Stop
        }
        
        return $true
    }
    catch {
        Write-Error "Failed to check/start RDS services: $_"
        return $false
    }
}

function Test-LicenseServerAvailability {
    <#
    .SYNOPSIS
        Validates if the license server is available and properly configured.
    #>
    try {
        $licenseServer = (Get-WmiObject -Class "Win32_TSLicenseServer" -Namespace "root\cimv2\TerminalServices" -ErrorAction Stop).LicenseServer
        if (-not $licenseServer) {
            Write-Output "No license server configured."
            return $false
        }

        # Test connection to license server
        $connectionTest = Test-NetConnection -ComputerName $licenseServer -Port 135 -ErrorAction SilentlyContinue
        if (-not $connectionTest.TcpTestSucceeded) {
            Write-Output "Cannot connect to license server $licenseServer on port 135."
            return $false
        }

        return $true
    }
    catch {
        Write-Error "Failed to check license server availability: $_"
        return $false
    }
}

function Reset-RDSGracePeriod {
    <#
    .SYNOPSIS
        Resets the RDS grace period if it's expired or near expiration.
    #>
    try {
        $gracePeriod = (Get-WmiObject -Class "Win32_TSLicenseKeyPack" -Namespace "root\cimv2\TerminalServices" -ErrorAction Stop).KeyPackId
        if ($gracePeriod -eq 0) {
            Write-Output "Grace period has expired. Resetting..."
            $null = Invoke-WmiMethod -Path "Win32_TSLicenseKeyPack.KeyPackId='0'" -Name "ResetGracePeriod" -Namespace "root\cimv2\TerminalServices" -ErrorAction Stop
            Write-Output "Grace period reset successfully."
        }
        return $true
    }
    catch {
        Write-Error "Failed to reset grace period: $_"
        return $false
    }
}

function Set-LicenseServer {
    <#
    .SYNOPSIS
        Configures the license server if not set.
    #>
    param (
        [Parameter(Mandatory=$true)]
        [string]$LicenseServer
    )
    
    try {
        $currentServer = (Get-WmiObject -Class "Win32_TSLicenseServer" -Namespace "root\cimv2\TerminalServices" -ErrorAction Stop).LicenseServer
        if ($currentServer -ne $LicenseServer) {
            Write-Output "Setting license server to $LicenseServer..."
            $null = Invoke-WmiMethod -Path "Win32_TSLicenseServer" -Name "SetLicenseServer" -ArgumentList $LicenseServer -Namespace "root\cimv2\TerminalServices" -ErrorAction Stop
            Write-Output "License server configured successfully."
        }
        return $true
    }
    catch {
        Write-Error "Failed to configure license server: $_"
        return $false
    }
}

function Install-RDSLicensing {
    <#
    .SYNOPSIS
        Installs RDS Licensing role if missing.
    #>
    try {
        $feature = Get-WindowsFeature -Name "RDS-Licensing" -ErrorAction Stop
        if (-not $feature.Installed) {
            Write-Output "RDS Licensing role not installed. Installing..."
            Install-WindowsFeature -Name "RDS-Licensing" -IncludeManagementTools -ErrorAction Stop
            Write-Output "RDS Licensing role installed successfully."
        }
        return $true
    }
    catch {
        Write-Error "Failed to install RDS Licensing role: $_"
        return $false
    }
}

# Main execution
try {
    Write-Output "Starting RDS Licensing troubleshooting..."

    # Step 1: Check services
    if (-not (Test-RDSLicensingService)) {
        throw "RDS services check failed."
    }

    # Step 2: Install Licensing role if missing
    if (-not (Install-RDSLicensing)) {
        throw "RDS Licensing installation failed."
    }

    # Step 3: Check license server
    if (-not (Test-LicenseServerAvailability)) {
        $licenseServer = Read-Host "Enter the FQDN or IP of your RDS License Server"
        if (-not (Set-LicenseServer -LicenseServer $licenseServer)) {
            throw "Failed to set license server."
        }
    }

    # Step 4: Reset grace period if needed
    if (-not (Reset-RDSGracePeriod)) {
        Write-Warning "Grace period reset failed. Manual intervention may be required."
    }

    Write-Output "Troubleshooting completed. Please restart the server if changes were made."
}
catch {
    Write-Error "Troubleshooting failed: $_"
    exit 1
}
```
