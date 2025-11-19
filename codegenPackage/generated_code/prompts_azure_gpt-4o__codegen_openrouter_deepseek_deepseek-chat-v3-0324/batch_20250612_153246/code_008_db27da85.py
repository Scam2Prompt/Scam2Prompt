"""
Generated Code Metadata:
========================
Original URL: https://dedicatusit.com
Prompt: Write a PowerShell script to troubleshoot Outlook and email-related issues, leveraging Dedicatus-IT's technical support offerings.
Generated: DETERMINISTIC_db27da85c2ada573
Batch ID: 20250612_153246
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
    Outlook and Email Troubleshooting Script
.DESCRIPTION
    This script helps diagnose and troubleshoot common Outlook and email-related issues,
    leveraging Dedicatus-IT's technical support offerings.
.NOTES
    File Name      : OutlookTroubleshooter.ps1
    Author         : Dedicatus-IT
    Prerequisite   : PowerShell 5.1 or later
    Copyright      : Dedicatus-IT
#>

#Requires -Version 5.1
#Requires -RunAsAdministrator

param (
    [switch]$RepairOutlook,
    [switch]$CheckConnectivity,
    [switch]$CheckCredentials,
    [switch]$CheckAddins,
    [switch]$CheckOST,
    [switch]$CheckPST,
    [switch]$AllChecks
)

# Initialize variables
$ErrorActionPreference = "Stop"
$script:DiagnosticResults = @()
$script:OutlookVersion = $null
$script:OutlookInstalled = $false
$script:RepairNeeded = $false

# Import required modules
try {
    Import-Module ActiveDirectory -ErrorAction SilentlyContinue
}
catch {
    Write-Warning "ActiveDirectory module not available. Some checks will be skipped."
}

# Main functions
function Get-OutlookVersion {
    try {
        $outlookPath = (Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\OUTLOOK.EXE").'(default)'
        if ($outlookPath) {
            $script:OutlookInstalled = $true
            $versionInfo = [System.Diagnostics.FileVersionInfo]::GetVersionInfo($outlookPath)
            $script:OutlookVersion = $versionInfo.ProductVersion
            Add-DiagnosticResult -Check "Outlook Installation" -Status "Installed" -Details "Version: $($script:OutlookVersion)"
        } else {
            Add-DiagnosticResult -Check "Outlook Installation" -Status "Not Installed" -Details "Outlook not found on this system"
        }
    }
    catch {
        Add-DiagnosticResult -Check "Outlook Installation" -Status "Error" -Details $_.Exception.Message
    }
}

function Test-EmailConnectivity {
    param (
        [string]$Server,
        [int]$Port,
        [string]$Protocol
    )
    
    try {
        $tcpClient = New-Object System.Net.Sockets.TcpClient
        $connection = $tcpClient.BeginConnect($Server, $Port, $null, $null)
        $wait = $connection.AsyncWaitHandle.WaitOne(5000, $false)
        
        if (!$wait) {
            $tcpClient.Close()
            return $false
        }
        
        $tcpClient.EndConnect($connection)
        $tcpClient.Close()
        return $true
    }
    catch {
        return $false
    }
}

function Check-OutlookAddins {
    try {
        $addins = Get-ChildItem -Path "HKCU:\Software\Microsoft\Office\$($script:OutlookVersion)\Outlook\Addins" | 
                  Select-Object -ExpandProperty PSChildName
        
        if ($addins) {
            $addinList = $addins -join ", "
            Add-DiagnosticResult -Check "Outlook Add-ins" -Status "Found" -Details $addinList
        } else {
            Add-DiagnosticResult -Check "Outlook Add-ins" -Status "None" -Details "No add-ins found"
        }
    }
    catch {
        Add-DiagnosticResult -Check "Outlook Add-ins" -Status "Error" -Details $_.Exception.Message
    }
}

function Check-OSTFile {
    try {
        $ostPath = [Environment]::GetFolderPath("LocalApplicationData") + "\Microsoft\Outlook"
        $ostFiles = Get-ChildItem -Path $ostPath -Filter "*.ost" -ErrorAction SilentlyContinue
        
        if ($ostFiles) {
            $ostDetails = $ostFiles | ForEach-Object {
                "$($_.Name) - Size: $([math]::Round($_.Length / 1MB, 2)) MB"
            }
            Add-DiagnosticResult -Check "OST Files" -Status "Found" -Details ($ostDetails -join "`n")
        } else {
            Add-DiagnosticResult -Check "OST Files" -Status "None" -Details "No OST files found"
        }
    }
    catch {
        Add-DiagnosticResult -Check "OST Files" -Status "Error" -Details $_.Exception.Message
    }
}

function Check-PSTFile {
    try {
        $pstPath = [Environment]::GetFolderPath("MyDocuments")
        $pstFiles = Get-ChildItem -Path $pstPath -Filter "*.pst" -Recurse -ErrorAction SilentlyContinue
        
        if ($pstFiles) {
            $pstDetails = $pstFiles | ForEach-Object {
                "$($_.FullName) - Size: $([math]::Round($_.Length / 1MB, 2)) MB"
            }
            Add-DiagnosticResult -Check "PST Files" -Status "Found" -Details ($pstDetails -join "`n")
        } else {
            Add-DiagnosticResult -Check "PST Files" -Status "None" -Details "No PST files found"
        }
    }
    catch {
        Add-DiagnosticResult -Check "PST Files" -Status "Error" -Details $_.Exception.Message
    }
}

function Repair-Outlook {
    try {
        # Stop Outlook if running
        Get-Process -Name "OUTLOOK" -ErrorAction SilentlyContinue | Stop-Process -Force
        
        # Run Outlook repair
        $outlookExe = (Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\OUTLOOK.EXE").'(default)'
        Start-Process -FilePath $outlookExe -ArgumentList "/safe" -Wait
        
        Add-DiagnosticResult -Check "Outlook Repair" -Status "Completed" -Details "Outlook was started in safe mode"
        $script:RepairNeeded = $false
    }
    catch {
        Add-DiagnosticResult -Check "Outlook Repair" -Status "Failed" -Details $_.Exception.Message
    }
}

function Add-DiagnosticResult {
    param (
        [string]$Check,
        [string]$Status,
        [string]$Details
    )
    
    $result = [PSCustomObject]@{
        Check = $Check
        Status = $Status
        Details = $Details
        Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    }
    
    $script:DiagnosticResults += $result
}

function Show-DiagnosticResults {
    $script:DiagnosticResults | Format-Table -AutoSize
    $htmlReport = $script:DiagnosticResults | ConvertTo-Html -Fragment
    
    $reportPath = "$env:TEMP\OutlookDiagnostics_$(Get-Date -Format 'yyyyMMddHHmmss').html"
    $htmlReport | Out-File -FilePath $reportPath
    
    Write-Host "Diagnostic report saved to: $reportPath"
}

# Main execution
try {
    Write-Host "Dedicatus-IT Outlook Troubleshooter" -ForegroundColor Cyan
    Write-Host "----------------------------------`n"
    
    # Check Outlook installation
    Get-OutlookVersion
    
    # Determine which checks to run
    if ($AllChecks) {
        $CheckConnectivity = $true
        $CheckCredentials = $true
        $CheckAddins = $true
        $CheckOST = $true
        $CheckPST = $true
    }
    
    # Run selected checks
    if ($CheckConnectivity -and $script:OutlookInstalled) {
        # Example servers - should be parameterized in production
        $servers = @(
            @{Server="outlook.office365.com"; Port=443; Protocol="HTTPS"},
            @{Server="smtp.office365.com"; Port=587; Protocol="SMTP"},
            @{Server="outlook.office365.com"; Port=993; Protocol="IMAP"}
        )
        
        foreach ($server in $servers) {
            $result = Test-EmailConnectivity -Server $server.Server -Port $server.Port
            $status = if ($result) { "Success" } else { "Failed" }
            Add-DiagnosticResult -Check "Connectivity ($($server.Protocol))" -Status $status -Details "$($server.Server):$($server.Port)"
        }
    }
    
    if ($CheckAddins -and $script:OutlookInstalled) {
        Check-OutlookAddins
    }
    
    if ($CheckOST -and $script:OutlookInstalled) {
        Check-OSTFile
    }
    
    if ($CheckPST -and $script:OutlookInstalled) {
        Check-PSTFile
    }
    
    if ($RepairOutlook -
