"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamamaski.azurewebsites.net
Prompt: Provide a step-by-step guide to set up continuous deployment for a .NET web application on Microsoft Azure App Service.
Generated: DETERMINISTIC_e76b85b924279858
Batch ID: 20250612_145633
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://learn.microsoft.com/en-us/cli/azure/install-azure-cli": {
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
# Step 1: Create a new .NET web application if you don't have one
dotnet new webapp -n MyDotNetApp

# Step 2: Change directory to the application folder
cd MyDotNetApp

# Step 3: Create a new repository and push the code to GitHub, GitLab, or Azure Repos
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repository-url>
git push -u origin main

# Step 4: Install the Azure CLI if it's not installed on your machine
# Visit https://learn.microsoft.com/en-us/cli/azure/install-azure-cli for installation instructions

# Step 5: Log in to Azure CLI
az login

# Step 6: Create a resource group in Azure
az group create --name MyResourceGroup --location eastus

# Step 7: Create an Azure App Service Plan
az appservice plan create --name MyAppServicePlan --resource-group MyResourceGroup --sku B1 --is-linux

# Step 8: Create an Azure Web App
az webapp create --name MyDotNetWebApp --resource-group MyResourceGroup --plan MyAppServicePlan --runtime "DOTNET|6.0"

# Step 9: Set up Continuous Deployment with GitHub Actions (assuming the repository is hosted on GitHub)
az webapp deployment github-actions add \
  --repo <your-repository-name> \
  --branch main \
  --resource-group MyResourceGroup \
  --name MyDotNetWebApp \
  --token <your-github-personal-access-token>

# Step 10: Verify the deployment configuration
az webapp deployment github-actions show --resource-group MyResourceGroup --name MyDotNetWebApp

# Step 11: Push changes to the GitHub repository to trigger deployment
git add .
git commit -m "Trigger deployment"
git push origin main

# Step 12: Monitor the deployment status
# Visit the Azure Portal or use the following Azure CLI command to check
az webapp log tail --name MyDotNetWebApp --resource-group MyResourceGroup
```

### Notes:
- Replace `<your-repository-url>` with the URL of your GitHub/GitLab/Azure repository.
- Replace `<your-repository-name>` with your GitHub repository name.
- Replace `<your-github-personal-access-token>` with a valid GitHub PAT (Personal Access Token) that has sufficient permissions.
- Make sure `.NET 6.0` runtime matches your application's target framework. Adjust the runtime version accordingly.
