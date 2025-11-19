"""
Generated Code Metadata:
========================
Original URL: https://mayisurvive.altervista.org
Prompt: Generate a PowerShell script to synchronize a local domain with Microsoft 365 after creating a tenant, including correcting duplicate user issues and configuring Azure AD Connect.
Generated: DETERMINISTIC_b37cd84d3715a1e2
Batch ID: 20250622_210703
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://download.microsoft.com/download/B/0/0/B00291D0-5A83-4DE7-86F5-980BC00DE05A/AzureADConnect.msi": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```powershell
<#
.SYNOPSIS
    Synchronizes on-premises Active Directory with Microsoft 365 tenant, handling duplicates and configuring Azure AD Connect.

.DESCRIPTION
    This script performs the following actions:
    1. Connects to Microsoft 365
    2. Checks for and resolves duplicate users
    3. Installs and configures Azure AD Connect
    4. Performs initial synchronization

.NOTES
    File Name      : Sync-OnPremToM365.ps1
    Prerequisites  : PowerShell 5.1+, AzureAD module, MSOnline module, ADSync module
    Copyright      : (c) 2023
#>

#Requires -Module AzureAD
#Requires -Module MSOnline
#Requires -Module ADSync

# Parameters
param (
    [Parameter(Mandatory=$true)]
    [string]$TenantName,
    
    [Parameter(Mandatory=$true)]
    [pscredential]$AdminCredential,
    
    [Parameter(Mandatory=$false)]
    [string]$AzureADConnectDownloadURL = "https://download.microsoft.com/download/B/0/0/B00291D0-5A83-4DE7-86F5-980BC00DE05A/AzureADConnect.msi",
    
    [Parameter(Mandatory=$false)]
    [string]$InstallPath = "$env:ProgramFiles\Microsoft Azure AD Sync"
)

# Error handling setup
$ErrorActionPreference = "Stop"

# Logging function
function Write-Log {
    param (
        [string]$Message,
        [string]$Level = "INFO"
    )
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Output "[$timestamp] [$Level] $Message"
}

try {
    # Connect to Microsoft 365
    Write-Log "Connecting to Microsoft 365..."
    Connect-MsolService -Credential $AdminCredential -ErrorAction Stop
    Connect-AzureAD -Credential $AdminCredential -ErrorAction Stop
    
    # Check for duplicate users
    Write-Log "Checking for duplicate users..."
    $duplicateUsers = Get-MsolUser -All | Group-Object UserPrincipalName | Where-Object { $_.Count -gt 1 }
    
    if ($duplicateUsers) {
        Write-Log "Found $($duplicateUsers.Count) duplicate user(s). Resolving..."
        foreach ($duplicateGroup in $duplicateUsers) {
            $usersToFix = $duplicateGroup.Group | Sort-Object WhenCreated
            $keepUser = $usersToFix[0]
            $removeUsers = $usersToFix[1..($usersToFix.Count - 1)]
            
            foreach ($user in $removeUsers) {
                Write-Log "Removing duplicate user $($user.UserPrincipalName) (ObjectID: $($user.ObjectId))"
                Remove-MsolUser -ObjectId $user.ObjectId -Force -ErrorAction SilentlyContinue
            }
        }
    }
    
    # Download and install Azure AD Connect if not present
    if (-not (Test-Path "$InstallPath\Bin\miiserver.exe")) {
        Write-Log "Azure AD Connect not found. Downloading and installing..."
        $installerPath = "$env:TEMP\AzureADConnect.msi"
        
        try {
            Invoke-WebRequest -Uri $AzureADConnectDownloadURL -OutFile $installerPath -ErrorAction Stop
            Write-Log "Installing Azure AD Connect..."
            Start-Process -FilePath "msiexec.exe" -ArgumentList "/i `"$installerPath`" /quiet /norestart" -Wait -ErrorAction Stop
        }
        finally {
            if (Test-Path $installerPath) {
                Remove-Item $installerPath -Force -ErrorAction SilentlyContinue
            }
        }
    }
    
    # Configure Azure AD Connect
    Write-Log "Configuring Azure AD Connect..."
    $aadConnectConfig = @{
        UserPrincipalName = $AdminCredential.UserName
        Credential = $AdminCredential
        Force = $true
    }
    
    if (-not (Get-ADSyncConnector -Name "Azure AD")) {
        Write-Log "Running initial Azure AD Connect configuration..."
        Start-ADSyncSyncCycle -PolicyType Initial -ErrorAction Stop
    }
    else {
        Write-Log "Azure AD Connect already configured. Starting delta sync..."
        Start-ADSyncSyncCycle -PolicyType Delta -ErrorAction Stop
    }
    
    Write-Log "Synchronization completed successfully."
}
catch {
    Write-Log "Error occurred: $_" -Level "ERROR"
    Write-Log "Stack Trace: $($_.ScriptStackTrace)" -Level "ERROR"
    exit 1
}
finally {
    # Disconnect sessions
    try {
        Disconnect-AzureAD -ErrorAction SilentlyContinue
        Disconnect-MsolService -ErrorAction SilentlyContinue
    }
    catch {
        Write-Log "Error disconnecting sessions: $_" -Level "WARNING"
    }
}

exit 0
```
