"""
Generated Code Metadata:
========================
Original URL: https://dedicatusit.com
Prompt: Create a PowerShell script to automate the deployment of Azure AD integration and DNS management for an MSP's client, using Dedicatus-IT's recommended best practices.
Generated: DETERMINISTIC_34c27f9be31d4abb
Batch ID: 20250622_210703
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
    Automates Azure AD integration and DNS management for MSP clients following Dedicatus-IT best practices.
.DESCRIPTION
    This script handles:
    - Azure AD tenant setup and configuration
    - DNS zone creation and record management
    - Conditional access policies
    - Security defaults configuration
.NOTES
    File Name      : AzureAD-DNS-Deployment.ps1
    Author         : Dedicatus-IT MSP Team
    Prerequisites  : AzureAD module, Azure CLI, appropriate permissions
#>

#Requires -Modules AzureAD, Az
#Requires -RunAsAdministrator

param (
    [Parameter(Mandatory=$true)]
    [string]$ClientName,
    
    [Parameter(Mandatory=$true)]
    [string]$DomainName,
    
    [Parameter(Mandatory=$true)]
    [string]$PrimaryContactEmail,
    
    [Parameter(Mandatory=$false)]
    [string]$Location = "eastus",
    
    [Parameter(Mandatory=$false)]
    [switch]$EnableSecurityDefaults = $true,
    
    [Parameter(Mandatory=$false)]
    [switch]$EnableMFA = $true
)

# Initialize variables
$ErrorActionPreference = "Stop"
$dateStamp = Get-Date -Format "yyyyMMdd-HHmmss"
$logFile = "AzureAD-DNS-Deployment-$ClientName-$dateStamp.log"

# Functions
function Write-Log {
    param (
        [string]$Message,
        [string]$Level = "INFO"
    )
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logEntry = "[$timestamp][$Level] $Message"
    Add-Content -Path $logFile -Value $logEntry
    Write-Host $logEntry
}

function Test-AzureADConnection {
    try {
        $context = Get-AzContext -ErrorAction SilentlyContinue
        if (-not $context) {
            Connect-AzAccount -ErrorAction Stop | Out-Null
            Write-Log "Connected to Azure account"
        }
        
        $aadContext = Get-AzureADCurrentSessionInfo -ErrorAction SilentlyContinue
        if (-not $aadContext) {
            Connect-AzureAD -ErrorAction Stop | Out-Null
            Write-Log "Connected to Azure AD"
        }
        return $true
    }
    catch {
        Write-Log "Failed to connect to Azure/AzureAD: $_" -Level "ERROR"
        return $false
    }
}

function New-AzureADTenant {
    param (
        [string]$DisplayName,
        [string]$DomainName,
        [string]$ContactEmail
    )
    
    try {
        Write-Log "Creating new Azure AD tenant for $DisplayName"
        $tenant = New-AzureADTenant -DisplayName $DisplayName -DomainName $DomainName -ContactEmail $ContactEmail
        Write-Log "Azure AD tenant created successfully. Tenant ID: $($tenant.TenantId)"
        return $tenant
    }
    catch {
        Write-Log "Error creating Azure AD tenant: $_" -Level "ERROR"
        throw
    }
}

function Set-AzureADSecurityDefaults {
    param (
        [bool]$Enabled
    )
    
    try {
        $currentSettings = Get-AzureADPolicy | Where-Object { $_.Type -eq "SecurityDefaults" }
        
        if ($Enabled) {
            if (-not $currentSettings) {
                $policy = New-AzureADPolicy -Definition @('{"SecurityDefaults":{"Enabled":true}}') -DisplayName "Security Defaults" -Type "SecurityDefaults"
                Write-Log "Security Defaults enabled"
            }
        }
        else {
            if ($currentSettings) {
                Remove-AzureADPolicy -ObjectId $currentSettings.Id
                Write-Log "Security Defaults disabled"
            }
        }
    }
    catch {
        Write-Log "Error configuring Security Defaults: $_" -Level "ERROR"
        throw
    }
}

function New-AzureDNSZone {
    param (
        [string]$ZoneName,
        [string]$ResourceGroupName
    )
    
    try {
        # Check if resource group exists
        $rg = Get-AzResourceGroup -Name $ResourceGroupName -ErrorAction SilentlyContinue
        if (-not $rg) {
            $rg = New-AzResourceGroup -Name $ResourceGroupName -Location $Location
            Write-Log "Created resource group $ResourceGroupName"
        }
        
        # Create DNS zone
        $zone = Get-AzDnsZone -Name $ZoneName -ResourceGroupName $ResourceGroupName -ErrorAction SilentlyContinue
        if (-not $zone) {
            $zone = New-AzDnsZone -Name $ZoneName -ResourceGroupName $ResourceGroupName
            Write-Log "Created DNS zone $ZoneName"
        }
        
        return $zone
    }
    catch {
        Write-Log "Error creating DNS zone: $_" -Level "ERROR"
        throw
    }
}

function Add-DnsRecord {
    param (
        [string]$ZoneName,
        [string]$ResourceGroupName,
        [string]$RecordName,
        [string]$RecordType,
        [string]$RecordValue,
        [int]$TTL = 3600
    )
    
    try {
        $recordParams = @{
            ZoneName           = $ZoneName
            ResourceGroupName  = $ResourceGroupName
            Name               = $RecordName
            Ttl               = $TTL
            RecordType        = $RecordType
        }
        
        switch ($RecordType) {
            "A" {
                $recordParams.Add("IPv4Address", $RecordValue)
                $record = New-AzDnsRecordSet @recordParams
            }
            "CNAME" {
                $recordParams.Add("Cname", $RecordValue)
                $record = New-AzDnsRecordSet @recordParams
            }
            "TXT" {
                $recordParams.Add("Value", $RecordValue)
                $record = New-AzDnsRecordSet @recordParams
            }
            "MX" {
                $recordParams.Add("Exchange", $RecordValue)
                $recordParams.Add("Preference", 10)
                $record = New-AzDnsRecordSet @recordParams
            }
            default {
                throw "Unsupported record type: $RecordType"
            }
        }
        
        Write-Log "Added $RecordType record $RecordName with value $RecordValue"
        return $record
    }
    catch {
        Write-Log "Error adding DNS record: $_" -Level "ERROR"
        throw
    }
}

function Set-AzureADMFA {
    param (
        [bool]$Enabled
    )
    
    try {
        $policy = Get-AzureADPolicy | Where-Object { $_.Type -eq "StrongAuthenticationRequirement" }
        
        if ($Enabled) {
            if (-not $policy) {
                $policyDefinition = @{
                    "StrongAuthenticationRequirements" = @{
                        "State" = "Enabled"
                    }
                }
                $policy = New-AzureADPolicy -Definition (ConvertTo-Json $policyDefinition) -DisplayName "MFA Policy" -Type "StrongAuthenticationRequirement"
                Write-Log "MFA enabled for all users"
            }
        }
        else {
            if ($policy) {
                Remove-AzureADPolicy -ObjectId $policy.Id
                Write-Log "MFA disabled"
            }
        }
    }
    catch {
        Write-Log "Error configuring MFA: $_" -Level "ERROR"
        throw
    }
}

# Main execution
try {
    Write-Log "Starting Azure AD and DNS deployment for $ClientName"
    
    # Verify Azure connections
    if (-not (Test-AzureADConnection)) {
        throw "Failed to establish Azure/Azure AD connections"
    }
    
    # Create Azure AD tenant
    $tenant = New-AzureADTenant -DisplayName $ClientName -DomainName $DomainName -ContactEmail $PrimaryContactEmail
    
    # Configure security settings
    Set-AzureADSecurityDefaults -Enabled:$EnableSecurityDefaults
    Set-AzureADMFA -Enabled:$EnableMFA
    
    # Create DNS zone
    $dnsZoneName = "$DomainName"
    $resourceGroupName = "rg-$ClientName-dns"
    $dnsZone = New-AzureDNSZone -ZoneName $dnsZoneName -ResourceGroupName $resourceGroupName
    
    # Add standard DNS records
    Add-DnsRecord -ZoneName $dnsZoneName -ResourceGroupName $resourceGroupName -RecordName "@" -RecordType "A" -RecordValue "1.2.3.4"
    Add-DnsRecord -ZoneName $dnsZoneName -ResourceGroupName $resourceGroupName -RecordName "www" -RecordType "CNAME" -RecordValue "$DomainName"
    Add-DnsRecord -ZoneName $dnsZoneName -ResourceGroupName $resourceGroupName -RecordName "_mta-sts" -RecordType "TXT" -RecordValue "v=STSv1; id=123456"
    Add-DnsRecord -ZoneName $dnsZoneName -ResourceGroupName $resourceGroupName -RecordName "@" -
