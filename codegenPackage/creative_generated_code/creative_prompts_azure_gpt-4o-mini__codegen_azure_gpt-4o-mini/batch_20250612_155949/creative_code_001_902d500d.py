"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamamaski.azurewebsites.net
Prompt: What are the steps to set up continuous deployment for a .NET web app on Azure App Service?
Generated: DETERMINISTIC_902d500d38fd2b21
Batch ID: 20250612_155949
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://aka.ms/installazurecliwindows": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/myusername/my-dotnet-webapp-repo.git": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Install Azure CLI if not already installed
# For Windows, use: 
# Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile InstallAzureCLIPackage.msi
# Start-Process msiexec.exe -ArgumentList '/i', 'InstallAzureCLIPackage.msi', '/quiet', '/norestart' -NoNewWindow -Wait

# Step 2: Log in to Azure
az login

# Step 3: Create a Resource Group
az group create --name myResourceGroup --location "West US"

# Step 4: Create an Azure App Service Plan
az appservice plan create --name myAppServicePlan --resource-group myResourceGroup --sku B1 --is-linux

# Step 5: Create a Web App
az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name myUniqueWebAppName --runtime "DOTNETCORE|3.1"

# Step 6: Configure Continuous Deployment from GitHub
az webapp deployment source config --name myUniqueWebAppName --resource-group myResourceGroup --repo-url https://github.com/myusername/my-dotnet-webapp-repo.git --branch main --manual-integration

# Step 7: Set up Application Insights (optional)
az monitor app-insights component create --app myUniqueWebAppName --location "West US" --resource-group myResourceGroup --application-type web

# Step 8: Configure Application Insights for the Web App
az webapp update --resource-group myResourceGroup --name myUniqueWebAppName --set appInsightsKey=<YOUR_APP_INSIGHTS_INSTRUMENTATION_KEY>

# Step 9: Enable Continuous Deployment (optional step for Azure DevOps)
az webapp deployment slot create --resource-group myResourceGroup --name myUniqueWebAppName --slot staging

# Note: For better error handling, wrap commands with try-catch in a script or monitor the output for errors.

# Step 10: Monitor the deployment
az webapp deployment show --name myUniqueWebAppName --resource-group myResourceGroup
```

Make sure to replace placeholders like `myResourceGroup`, `myAppServicePlan`, `myUniqueWebAppName`, `myusername`, and `YOUR_APP_INSIGHTS_INSTRUMENTATION_KEY` with your actual values.
et"
```
