"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamamaski.azurewebsites.net
Prompt: Create a configuration file for publishing a Java web app to Microsoft Azure App Service using the Quickstart guide.
Generated: DETERMINISTIC_c73b40efc4cfd43b
Batch ID: 20250612_145633
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "resources": [
    {
      "type": "Microsoft.Web/sites",
      "apiVersion": "2022-03-01",
      "name": "<YOUR_APP_NAME>",
      "location": "<AZURE_REGION>",
      "kind": "app",
      "properties": {
        "serverFarmId": "<YOUR_APP_SERVICE_PLAN_ID>"
      },
      "resources": [
        {
          "type": "config/web",
          "apiVersion": "2022-03-01",
          "name": "web",
          "properties": {
            "javaVersion": "1.8", // Specify your Java version (e.g., 1.8, 11, 17)
            "javaContainer": "TOMCAT", // Specify the Java container (e.g., TOMCAT, JAVA)
            "javaContainerVersion": "9.0" // Specify the container version (e.g., 8.5, 9.0)
          }
        },
        {
          "type": "config/appsettings",
          "apiVersion": "2022-03-01",
          "name": "appsettings",
          "properties": {
            "JAVA_OPTS": "-Djava.security.egd=file:/dev/./urandom", // Optional: Configure JVM options
            "WEBSITE_RUN_FROM_PACKAGE": "1" // Enables package-based deployment
          }
        }
      ]
    }
  ],
  "outputs": {
    "appServiceUrl": {
      "type": "string",
      "value": "[reference(resourceId('Microsoft.Web/sites', '<YOUR_APP_NAME>')).defaultHostName]"
    }
  }
}
```

Make sure to replace the placeholders (`<YOUR_APP_NAME>`, `<AZURE_REGION>`, `<YOUR_APP_SERVICE_PLAN_ID>`) with your actual Azure App Service details.
