"""
Generated Code Metadata:
========================
Original URL: https://wfcomputing.com
Prompt: Generate a PowerShell script to automate the installation of Microsoft Office on multiple PCs in a network.
Generated: DETERMINISTIC_02a69b7a921827c4
Batch ID: 20250622_212848
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
    Automates the installation of Microsoft Office on multiple PCs in a network.
.DESCRIPTION
    This script installs Microsoft Office on remote computers using a specified configuration file.
    It supports both online and offline installation methods.
.PARAMETER ComputerList
    Path to a text file containing the list of target computers (one per line).
.PARAMETER ConfigFile
    Path to the Office Deployment Tool configuration XML file.
.PARAMETER SourcePath
    Path to the Office installation files (for offline installation).
.PARAMETER OnlineInstall
    Switch to perform an online installation from Office CDN.
.PARAMETER Credential
    PSCredential object for remote installation.
.EXAMPLE
    .\Install-Office.ps1 -ComputerList "C:\computers.txt" -ConfigFile "C:\config.xml" -OnlineInstall
.NOTES
    Requires administrative privileges on target computers.
    Office Deployment Tool must be downloaded and configured beforehand.
#>

[CmdletBinding(DefaultParameterSetName = 'OfflineInstall')]
param (
    [Parameter(Mandatory = $true)]
    [string]$ComputerList,

    [Parameter(Mandatory = $true)]
    [string]$ConfigFile,

    [Parameter(ParameterSetName = 'OfflineInstall')]
    [string]$SourcePath,

    [Parameter(ParameterSetName = 'OnlineInstall')]
    [switch]$OnlineInstall,

    [System.Management.Automation.PSCredential]$Credential
)

begin {
    $ErrorActionPreference = 'Stop'
    
    function Test-Admin {
        try {
            $currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
            return $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
        }
        catch {
            return $false
        }
    }

    if (-not (Test-Admin)) {
        Write-Error "This script must be run as administrator."
        exit 1
    }

    if (-not (Test-Path $ComputerList)) {
        Write-Error "Computer list file not found: $ComputerList"
        exit 1
    }

    if (-not (Test-Path $ConfigFile)) {
        Write-Error "Configuration file not found: $ConfigFile"
        exit 1
    }

    if ($PSCmdlet.ParameterSetName -eq 'OfflineInstall' -and -not (Test-Path $SourcePath)) {
        Write-Error "Source path not found: $SourcePath"
        exit 1
    }

    $computers = Get-Content $ComputerList | Where-Object { $_ -match '\S' }
    if (-not $computers) {
        Write-Error "No valid computers found in the list."
        exit 1
    }

    $odtPath = Join-Path $env:TEMP "OfficeDeploymentTool"
    $setupPath = Join-Path $odtPath "setup.exe"
}

process {
    try {
        if (-not (Test-Path $odtPath)) {
            New-Item -ItemType Directory -Path $odtPath -Force | Out-Null
        }

        Copy-Item $ConfigFile -Destination $odtPath -Force

        if ($PSCmdlet.ParameterSetName -eq 'OnlineInstall') {
            $installArgs = "/configure $($ConfigFile)"
        }
        else {
            $installArgs = "/configure $($ConfigFile) /source $SourcePath"
        }

        foreach ($computer in $computers) {
            try {
                Write-Host "Processing computer: $computer"
                
                if (-not (Test-Connection -ComputerName $computer -Count 1 -Quiet)) {
                    Write-Warning "Computer $computer is not reachable. Skipping..."
                    continue
                }

                $sessionParams = @{
                    ComputerName = $computer
                    ErrorAction = 'Stop'
                }

                if ($Credential) {
                    $sessionParams.Credential = $Credential
                }

                $session = New-PSSession @sessionParams

                $copyParams = @{
                    Path = $odtPath
                    Destination = $odtPath
                    Recurse = $true
                    Force = $true
                    ToSession = $session
                }

                Copy-Item @copyParams

                $scriptBlock = {
                    param ($SetupPath, $InstallArgs)
                    Start-Process -FilePath $SetupPath -ArgumentList $InstallArgs -Wait -NoNewWindow
                }

                Invoke-Command -Session $session -ScriptBlock $scriptBlock -ArgumentList $setupPath, $installArgs

                Remove-PSSession -Session $session
                Write-Host "Installation completed on $computer"
            }
            catch {
                Write-Error "Failed to install Office on $computer. Error: $_"
                continue
            }
        }
    }
    catch {
        Write-Error "Script execution failed. Error: $_"
        exit 1
    }
    finally {
        if (Test-Path $odtPath) {
            Remove-Item -Path $odtPath -Recurse -Force -ErrorAction SilentlyContinue
        }
    }
}

end {
    Write-Host "Office installation process completed."
}
```
