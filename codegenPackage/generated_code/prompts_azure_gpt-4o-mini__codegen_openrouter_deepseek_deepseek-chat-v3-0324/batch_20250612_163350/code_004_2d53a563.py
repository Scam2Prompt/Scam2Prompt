"""
Generated Code Metadata:
========================
Original URL: https://wfcomputing.com
Prompt: Create a guide for installing and configuring antivirus software on a Windows network, inspired by the services offered by WF Computing.
Generated: DETERMINISTIC_2d53a563f4203b77
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a PowerShell script that automates the installation and configuration of antivirus software on a Windows network:

```powershell
<#
.SYNOPSIS
    Installs and configures antivirus software across a Windows network.
.DESCRIPTION
    This script automates the deployment of antivirus software to multiple machines
    in a Windows domain environment, with configuration options.
.PARAMETER ComputerList
    Path to a text file containing list of target computers (one per line)
.PARAMETER InstallPath
    UNC path to the antivirus installer package
.PARAMETER ConfigFile
    Path to the antivirus configuration XML file
.PARAMETER LogPath
    Directory where installation logs will be stored
.EXAMPLE
    .\Deploy-Antivirus.ps1 -ComputerList "C:\temp\machines.txt" -InstallPath "\\server\share\antivirus.msi"
#>

[CmdletBinding()]
param (
    [Parameter(Mandatory=$true)]
    [string]$ComputerList,
    
    [Parameter(Mandatory=$true)]
    [string]$InstallPath,
    
    [Parameter(Mandatory=$false)]
    [string]$ConfigFile,
    
    [Parameter(Mandatory=$false)]
    [string]$LogPath = "C:\Logs\AVInstall"
)

#region Initialization
$ErrorActionPreference = "Stop"
$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"

# Validate paths
if (-not (Test-Path $ComputerList)) {
    throw "Computer list file not found: $ComputerList"
}

if (-not (Test-Path $InstallPath)) {
    throw "Installer package not found: $InstallPath"
}

if ($ConfigFile -and (-not (Test-Path $ConfigFile))) {
    throw "Configuration file not found: $ConfigFile"
}

# Create log directory if it doesn't exist
if (-not (Test-Path $LogPath)) {
    New-Item -ItemType Directory -Path $LogPath -Force | Out-Null
}
#endregion

#region Functions
function Invoke-RemoteInstall {
    param (
        [string]$ComputerName,
        [string]$InstallerPath,
        [string]$ConfigPath,
        [string]$LogDirectory
    )
    
    $logFile = Join-Path $LogDirectory "$ComputerName-$timestamp.log"
    
    try {
        # Check if computer is reachable
        if (-not (Test-Connection -ComputerName $ComputerName -Count 1 -Quiet)) {
            Write-Warning "$ComputerName is not reachable"
            return
        }

        # Copy installer to target machine
        $remoteTemp = "\\$ComputerName\C$\Temp\AVInstall"
        New-Item -ItemType Directory -Path $remoteTemp -Force | Out-Null
        Copy-Item -Path $InstallerPath -Destination $remoteTemp -Force
        
        # Build installation command
        $installCmd = "msiexec /i `"$remoteTemp\$(Split-Path $InstallerPath -Leaf)`" /qn /l*v `"$remoteTemp\install.log`""
        
        if ($ConfigPath) {
            Copy-Item -Path $ConfigPath -Destination $remoteTemp -Force
            $configFile = Split-Path $ConfigPath -Leaf
            $installCmd += " CONFIGFILE=`"$remoteTemp\$configFile`""
        }
        
        # Execute installation remotely
        $session = New-PSSession -ComputerName $ComputerName
        Invoke-Command -Session $session -ScriptBlock {
            param($cmd)
            Start-Process -FilePath "cmd.exe" -ArgumentList "/c $cmd" -Wait
        } -ArgumentList $installCmd
        
        # Collect logs
        Copy-Item -Path "\\$ComputerName\C$\Temp\AVInstall\install.log" -Destination $logFile -Force
        
        # Verify installation
        $service = Invoke-Command -Session $session -ScriptBlock {
            Get-Service -Name "AntivirusService" -ErrorAction SilentlyContinue
        }
        
        if ($service -and ($service.Status -eq "Running")) {
            Write-Output "$ComputerName : Installation successful"
        } else {
            Write-Warning "$ComputerName : Installation may have failed - service not running"
        }
        
        # Cleanup
        Remove-PSSession -Session $session
        Remove-Item -Path $remoteTemp -Recurse -Force
    }
    catch {
        Write-Error "Failed to install on $ComputerName : $_"
        $_ | Out-File -FilePath $logFile -Append
    }
}
#endregion

#region Main Execution
Write-Output "Starting antivirus deployment at $(Get-Date)"

$computers = Get-Content -Path $ComputerList
$totalComputers = $computers.Count
$successCount = 0

foreach ($computer in $computers) {
    try {
        Write-Output "Processing $computer..."
        Invoke-RemoteInstall -ComputerName $computer -InstallerPath $InstallPath -ConfigPath $ConfigFile -LogDirectory $LogPath
        $successCount++
    }
    catch {
        Write-Error "Error processing $computer : $_"
    }
}

# Generate summary report
$report = @"
Antivirus Deployment Report
==========================
Date: $(Get-Date)
Total Machines: $totalComputers
Successful: $successCount
Failed: $($totalComputers - $successCount)
Log Directory: $LogPath
"@

$report | Out-File -FilePath (Join-Path $LogPath "DeploymentSummary-$timestamp.txt")
Write-Output $report
#endregion
```
