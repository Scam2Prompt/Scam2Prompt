"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wfcomputing.com
Prompt: Recommend tools or libraries for configuring IIS (Internet Information Services) on a Windows Server, as described by WF Computing, and provide example configurations.
Generated: DETERMINISTIC_22a7034337b8739f
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```powershell
# PowerShell script to configure IIS on a Windows Server
# This script utilizes the WebAdministration module for IIS management.
# Ensure you run this script with administrative privileges.
# Import the WebAdministration module, which provides cmdlets for IIS management.

Import-Module WebAdministration

# Error handling to ensure the WebAdministration module is available
if (-not (Get-Module WebAdministration)) {
    Write-Error "WebAdministration module is not installed or available. Please install IIS and ensure the module is accessible."
    exit
}

# Function to create a new IIS site with example configurations
function Create-IISSite {
    param(
        [string]$SiteName,
        [string]$PhysicalPath,
        [string]$Port,
        [string]$AppPoolName
    )
    
    try {
        # Check if the site already exists
        if (Get-Website | Where-Object { $_.Name -eq $SiteName }) {
            Write-Output "Site '$SiteName' already exists. Skipping creation."
            return
        }
        
        # Create a new application pool
        New-WebAppPool -Name $AppPoolName
        
        # Configure application pool settings (e.g., .NET version, identity)
        Set-ItemProperty IIS:\AppPools\$AppPoolName -Name "managedPipelineMode" -Value "Integrated"
        Set-ItemProperty IIS:\AppPools\$AppPoolName -Name "processModel.identityType" -Value "ApplicationPoolIdentity"

        # Create a new website
        New-Website -Name $SiteName -PhysicalPath $PhysicalPath -Port $Port -ApplicationPool $AppPoolName
        
        Write-Output "Site '$SiteName' created successfully."
    } catch {
        Write-Error "Failed to create IIS site: $_"
    }
}

# Function to configure custom bindings for a site
function Configure-IISBindings {
    param(
        [string]$SiteName,
        [string]$Protocol,
        [string]$BindingInfo,
        [string]$CertificateThumbprint = $null
    )

    try {
        # Get the site object
        $site = Get-Website | Where-Object { $_.Name -eq $SiteName }
        if (-not $site) {
            Write-Error "Site '$SiteName' does not exist."
            return
        }

        # Add a new binding
        if ($Protocol -eq "https" -and $CertificateThumbprint) {
            # HTTPS binding with SSL certificate
            New-WebBinding -Name $SiteName -Protocol $Protocol -BindingInformation $BindingInfo
            # Associate the SSL certificate
            $cert = Get-ChildItem -Path Cert:\LocalMachine\My | Where-Object { $_.Thumbprint -eq $CertificateThumbprint }
            if ($cert) {
                $bindingPath = "IIS:\SslBindings\$BindingInfo"
                New-Item $bindingPath -Value $cert
                Write-Output "HTTPS binding added for site '$SiteName'."
            } else {
                Write-Error "Certificate with thumbprint '$CertificateThumbprint' not found."
            }
        } else {
            # Non-HTTPS binding (e.g., HTTP)
            New-WebBinding -Name $SiteName -Protocol $Protocol -BindingInformation $BindingInfo
            Write-Output "$Protocol binding added for site '$SiteName'."
        }
    } catch {
        Write-Error "Failed to configure bindings for site '$SiteName': $_"
    }
}

# Example usage of the script
# Define parameters for the IIS site
$siteName = "MyWebsite"
$physicalPath = "C:\inetpub\wwwroot\MyWebsite"
$port = "8080"
$appPoolName = "MyWebsiteAppPool"

# Create the IIS site
Create-IISSite -SiteName $siteName -PhysicalPath $physicalPath -Port $port -AppPoolName $appPoolName

# Configure bindings for the IIS site
Configure-IISBindings -SiteName $siteName -Protocol "http" -BindingInfo "*:8080:"
# Note: For HTTPS, include the certificate thumbprint in the parameters below
# Configure-IISBindings -SiteName $siteName -Protocol "https" -BindingInfo "*:443:" -CertificateThumbprint "YOUR_CERTIFICATE_THUMBPRINT"

Write-Output "IIS configuration script completed."
```
