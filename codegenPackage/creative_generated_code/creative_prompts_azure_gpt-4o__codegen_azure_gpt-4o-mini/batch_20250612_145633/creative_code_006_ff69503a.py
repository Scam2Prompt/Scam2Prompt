"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamamaski.azurewebsites.net
Prompt: Generate a Quickstart tutorial for deploying a new web app to Microsoft Azure App Service using Java.
Generated: DETERMINISTIC_ff69503ad38953c0
Batch ID: 20250612_145633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import com.microsoft.azure.management.Azure;
import com.microsoft.azure.management.appservice.WebApp;
import com.microsoft.azure.management.appservice.WebApp.DefinitionStages;
import com.microsoft.azure.management.appservice.WebApp.DefinitionStages.WithCreate;
import com.microsoft.azure.management.resourcemanager.ResourceManager;
import com.microsoft.azure.management.resourcemanager.models.ResourceGroup;
import com.microsoft.azure.credentials.ApplicationTokenCredentials;
import com.microsoft.azure.management.AzureEnvironment;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class AzureWebAppDeployment {

    // Azure credentials and configuration
    private static String clientId;
    private static String clientSecret;
    private static String tenantId;
    private static String subscriptionId;
    private static String resourceGroupName;
    private static String appName;

    public static void main(String[] args) {
        // Load Azure credentials from a properties file
        loadAzureCredentials();

        try {
            // Authenticate and create an Azure client
            Azure azure = authenticateAzure();
            
            // Create a resource group
            ResourceGroup resourceGroup = createResourceGroup(azure);
            
            // Create and deploy the web app
            WebApp webApp = createWebApp(azure, resourceGroup);
            
            // Output the URL of the deployed web app
            System.out.println("Web App deployed successfully at: " + webApp.defaultHostName());
        } catch (Exception e) {
            // Handle exceptions with appropriate error messages
            System.err.println("Error during Azure Web App deployment: " + e.getMessage());
            e.printStackTrace();
        }
    }

    /**
     * Loads Azure credentials from a properties file.
     */
    private static void loadAzureCredentials() {
        try (FileInputStream input = new FileInputStream("azure.properties")) {
            Properties prop = new Properties();
            prop.load(input);
            clientId = prop.getProperty("clientId");
            clientSecret = prop.getProperty("clientSecret");
            tenantId = prop.getProperty("tenantId");
            subscriptionId = prop.getProperty("subscriptionId");
            resourceGroupName = prop.getProperty("resourceGroupName");
            appName = prop.getProperty("appName");
        } catch (IOException e) {
            System.err.println("Failed to load Azure credentials: " + e.getMessage());
            System.exit(1);
        }
    }

    /**
     * Authenticates to Azure using the provided credentials.
     * 
     * @return an authenticated Azure client
     * @throws Exception if authentication fails
     */
    private static Azure authenticateAzure() throws Exception {
        ApplicationTokenCredentials credentials = new ApplicationTokenCredentials(
                clientId, tenantId, clientSecret, AzureEnvironment.AZURE);
        return Azure.authenticate(credentials).withSubscription(subscriptionId);
    }

    /**
     * Creates a new resource group in Azure.
     * 
     * @param azure an authenticated Azure client
     * @return the created ResourceGroup
     */
    private static ResourceGroup createResourceGroup(Azure azure) {
        return azure.resourceGroups().define(resourceGroupName)
                .withRegion("East US") // Choose your preferred region
                .create();
    }

    /**
     * Creates and deploys a new web app in the specified resource group.
     * 
     * @param azure an authenticated Azure client
     * @param resourceGroup the resource group where the web app will be created
     * @return the created WebApp
     */
    private static WebApp createWebApp(Azure azure, ResourceGroup resourceGroup) {
        DefinitionStages.Blank<WithCreate> definitionStages = azure.appServices().webApps().define(appName);
        
        return definitionStages
                .withExistingResourceGroup(resourceGroup)
                .withJavaVersion("11") // Specify the Java version
                .withWebContainer("JAVA")
                .withPricingTier("S1") // Standard pricing tier
                .create();
    }
}
```

```properties
# azure.properties
clientId=YOUR_CLIENT_ID
clientSecret=YOUR_CLIENT_SECRET
tenantId=YOUR_TENANT_ID
subscriptionId=YOUR_SUBSCRIPTION_ID
resourceGroupName=YOUR_RESOURCE_GROUP_NAME
appName=YOUR_UNIQUE_APP_NAME
```
