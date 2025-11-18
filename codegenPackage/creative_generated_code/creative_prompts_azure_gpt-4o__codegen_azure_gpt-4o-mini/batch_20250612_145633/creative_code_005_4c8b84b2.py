"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mettamaks-log.azurewebsites.net
Prompt: Recommend libraries or APIs for deploying and managing web apps on Microsoft Azure App Service, specifically for Node.js and Java.
Generated: DETERMINISTIC_4c8b84b20c0415ca
Batch ID: 20250612_145633
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://management.azure.com/subscriptions/${AZURE_SUBSCRIPTION_ID}/resourceGroups/${AZURE_RESOURCE_GROUP}/providers/Microsoft.Web/sites/${AZURE_APP_NAME}/publish?api-version=2020-06-01`;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://login.microsoftonline.com/${AZURE_TENANT_ID}/oauth2/v2.0/token`;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://management.azure.com/.default": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Node.js: Code to deploy and manage a web app on Microsoft Azure App Service

const axios = require('axios');
const fs = require('fs');
const path = require('path');

// Azure configuration
const AZURE_SUBSCRIPTION_ID = 'your_subscription_id';
const AZURE_RESOURCE_GROUP = 'your_resource_group';
const AZURE_APP_NAME = 'your_app_name';
const AZURE_CLIENT_ID = 'your_client_id';
const AZURE_CLIENT_SECRET = 'your_client_secret';
const AZURE_TENANT_ID = 'your_tenant_id';

// Function to get Azure access token
async function getAzureToken() {
    const url = `https://login.microsoftonline.com/${AZURE_TENANT_ID}/oauth2/v2.0/token`;
    const params = new URLSearchParams();
    params.append('grant_type', 'client_credentials');
    params.append('client_id', AZURE_CLIENT_ID);
    params.append('client_secret', AZURE_CLIENT_SECRET);
    params.append('scope', 'https://management.azure.com/.default');

    try {
        const response = await axios.post(url, params);
        return response.data.access_token; // Return the access token
    } catch (error) {
        console.error('Error retrieving Azure token:', error.response.data);
        throw new Error('Failed to get Azure token.');
    }
}

// Function to deploy the web app
async function deployWebApp(archivePath) {
    const token = await getAzureToken();
    const url = `https://management.azure.com/subscriptions/${AZURE_SUBSCRIPTION_ID}/resourceGroups/${AZURE_RESOURCE_GROUP}/providers/Microsoft.Web/sites/${AZURE_APP_NAME}/publish?api-version=2020-06-01`;

    // Read the archive file
    const archive = fs.readFileSync(archivePath);
    
    try {
        const response = await axios.post(url, archive, {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/octet-stream',
            }
        });
        console.log('Deployment response:', response.data);
    } catch (error) {
        console.error('Deployment failed:', error.response.data);
        throw new Error('Deployment to Azure failed.');
    }
}

// Example usage
const archivePath = path.join(__dirname, 'your_app.zip'); // Path to your app's zip file
deployWebApp(archivePath)
    .then(() => console.log('Deployment completed successfully.'))
    .catch(err => console.error('Deployment error:', err.message));
```

```java
// Java: Code to deploy and manage a web app on Microsoft Azure App Service

import com.azure.identity.ClientSecretCredential;
import com.azure.identity.ClientSecretCredentialBuilder;
import com.azure.resourcemanager.AzureResourceManager;
import com.azure.resourcemanager.appservice.models.WebApp;

public class AzureWebAppManager {
    private static final String AZURE_SUBSCRIPTION_ID = "your_subscription_id";
    private static final String AZURE_CLIENT_ID = "your_client_id";
    private static final String AZURE_CLIENT_SECRET = "your_client_secret";
    private static final String AZURE_TENANT_ID = "your_tenant_id";
    private static final String RESOURCE_GROUP = "your_resource_group";
    private static final String APP_NAME = "your_app_name";

    // Azure Resource Manager instance
    private static AzureResourceManager azureResourceManager;

    static {
        // Initialize Azure Resource Manager with ClientSecretCredential
        ClientSecretCredential credential = new ClientSecretCredentialBuilder()
            .clientId(AZURE_CLIENT_ID)
            .clientSecret(AZURE_CLIENT_SECRET)
            .tenantId(AZURE_TENANT_ID)
            .build();

        azureResourceManager = AzureResourceManager.configure()
            .authenticate(credential, new com.azure.core.management.profile.AzureProfile())
            .withSubscription(AZURE_SUBSCRIPTION_ID);
    }
    
    // Deploy the web app
    public static void deployWebApp() {
        try {
            WebApp webApp = azureResourceManager.webApps().getByResourceGroup(RESOURCE_GROUP, APP_NAME);
            // Add code to deploy your web app files here
            System.out.println("Deployment successful for web app: " + webApp.name());
        } catch (Exception e) {
            System.err.println("Error during deployment: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        deployWebApp();
    }
}
```
