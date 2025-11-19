"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamamaski.azurewebsites.net
Prompt: What are the steps to set up continuous deployment for a .NET web app on Azure App Service?
Generated: DETERMINISTIC_902d500d38fd2b21
Batch ID: 20250612_155949
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/YourGitHubAccount/YourRepository.git": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```ps1
# Continuous Deployment Setup for .NET Web App on Azure App Service using PowerShell
# Ensure you have the Azure PowerShell module installed and are logged into your Azure account.

# Step 1: Define variables for resource names and paths
$resourceGroupName = "YourResourceGroupName" # Replace with your resource group name
$appServiceName = "YourAppServiceName"       # Replace with your App Service name
$deploymentSourceUrl = "https://github.com/YourGitHubAccount/YourRepository.git" # Replace with your repository URL
$branchName = "main"                         # Replace with the branch you want to deploy from

# Step 2: Authenticate to Azure
# Ensure you are logged in using the `Connect-AzAccount` command before running this script.

# Step 3: Enable continuous deployment
try {
    Write-Host "Enabling continuous deployment for App Service '$appServiceName' in resource group '$resourceGroupName'..."
    
    # Set deployment source to GitHub
    $deploymentResult = Set-AzWebApp -ResourceGroupName $resourceGroupName `
                                     -Name $appServiceName `
                                     -SourceControlDeployment `
                                     -RepoUrl $deploymentSourceUrl `
                                     -Branch $branchName

    if ($deploymentResult -ne $null) {
        Write-Host "Continuous deployment successfully set up!"
    } else {
        Write-Host "Failed to enable continuous deployment."
    }
} catch {
    # Catch and display error messages
    Write-Error "An error occurred while setting up continuous deployment: $_"
}

# Step 4: Confirm deployment status
try {
    Write-Host "Retrieving deployment status..."
    $deploymentStatus = Get-AzWebAppDeploymentLog -ResourceGroupName $resourceGroupName -Name $appServiceName

    if ($deploymentStatus -ne $null) {
        Write-Host "Deployment logs retrieved successfully:"
        Write-Host $deploymentStatus
    } else {
        Write-Host "No deployment logs found."
    }
} catch {
    # Catch and display error messages
    Write-Error "An error occurred while retrieving deployment status: $_"
}

# Step 5: Verify App Service is running
try {
    Write-Host "Checking App Service status..."
    $appServiceStatus = Get-AzWebApp -ResourceGroupName $resourceGroupName -Name $appServiceName

    if ($appServiceStatus.State -eq "Running") {
        Write-Host "App Service '$appServiceName' is running and ready to serve requests."
    } else {
        Write-Host "App Service '$appServiceName' is not running. Current state: $($appServiceStatus.State)"
    }
} catch {
    # Catch and display error messages
    Write-Error "An error occurred while verifying App Service status: $_"
}

# End of script
Write-Host "Continuous deployment setup completed."
```
