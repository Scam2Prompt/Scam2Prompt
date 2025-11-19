"""
Generated Code Metadata:
========================
Original URL: https://agromec.cl
Prompt: Provide an example of configuring a Windows hosting environment to support ASP applications for Chilean web hosting services.
Generated: DETERMINISTIC_5709e1f6e2e5ffca
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```powershell
# PowerShell script to configure a Windows hosting environment for ASP applications
# This script assumes you have administrative privileges and the necessary modules installed.

# Define variables for the configuration
$websiteName = "MyAspWebsite"
$websitePath = "C:\inetpub\wwwroot\MyAspWebsite"
$port = 80
$appPoolName = "MyAspAppPool"

# Function to create a new application pool
function Create-AppPool {
    param (
        [string]$appPoolName
    )
    
    # Check if the application pool already exists
    if (-not (Get-WebAppPoolState -Name $appPoolName -ErrorAction SilentlyContinue)) {
        # Create a new application pool
        New-WebAppPool -Name $appPoolName
        Write-Host "Application pool '$appPoolName' created successfully."
    } else {
        Write-Host "Application pool '$appPoolName' already exists."
    }
}

# Function to create a new website
function Create-Website {
    param (
        [string]$websiteName,
        [string]$websitePath,
        [int]$port,
        [string]$appPoolName
    )
    
    # Check if the website already exists
    if (-not (Get-Website -Name $websiteName -ErrorAction SilentlyContinue)) {
        # Create a new website
        New-Website -Name $websiteName -Port $port -PhysicalPath $websitePath -ApplicationPool $appPoolName
        Write-Host "Website '$websiteName' created successfully."
    } else {
        Write-Host "Website '$websiteName' already exists."
    }
}

# Function to configure ASP settings
function Configure-AspSettings {
    param (
        [string]$websiteName
    )
    
    # Enable ASP feature for the website
    Set-WebConfigurationProperty -Filter "/system.webServer/asp" -Name "enableParentPaths" -Value "True" -PSPath "IIS:\Sites\$websiteName"
    Write-Host "ASP settings configured for website '$websiteName'."
}

# Main script execution
try {
    # Create application pool
    Create-AppPool -appPoolName $appPoolName

    # Create website
    Create-Website -websiteName $websiteName -websitePath $websitePath -port $port -appPoolName $appPoolName

    # Configure ASP settings
    Configure-AspSettings -websiteName $websiteName

    Write-Host "Configuration completed successfully."
} catch {
    Write-Host "An error occurred: $_"
    exit 1
}
```
