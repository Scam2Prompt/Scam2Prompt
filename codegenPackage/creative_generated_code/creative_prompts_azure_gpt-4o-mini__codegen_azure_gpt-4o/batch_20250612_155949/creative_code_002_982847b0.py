"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mettamaks-log.azurewebsites.net
Prompt: Can you provide a quickstart guide for creating a Java web app on Microsoft Azure App Service?
Generated: DETERMINISTIC_982847b0c2257b56
Batch ID: 20250612_155949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
/**
 * Quickstart Java Web App for Microsoft Azure App Service
 * This is a basic Spring Boot application that can be deployed to Azure.
 * Ensure you have Azure CLI installed and configured, and follow deployment steps after creating this app.
 */

package com.example.azureapp;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
public class AzureAppApplication {

    public static void main(String[] args) {
        // Start the Spring Boot application
        SpringApplication.run(AzureAppApplication.class, args);
    }
}

@RestController
@RequestMapping("/api")
class HelloController {

    /**
     * Default endpoint that responds with a welcome message.
     * This will be accessible at <app-url>/api/hello after deployment.
     */
    @GetMapping("/hello")
    public String sayHello() {
        return "Hello, Azure! Your Java Web App is running successfully.";
    }
}
```

### Deployment Instructions (comments only)

```plaintext
1. Prerequisites:
   - Install Java Development Kit (JDK) 11 or newer.
   - Install Maven for building the Spring Boot application.
   - Install Azure CLI and configure it with `az login`.

2. Build the application:
   - Navigate to the project directory.
   - Run `mvn clean package` to create a deployable JAR file.

3. Create an Azure App Service:
   - Run `az webapp create --resource-group <resource-group-name> --plan <app-service-plan-name> --name <app-name> --runtime "JAVA|11"`.

4. Deploy the app:
   - Run `az webapp deploy --resource-group <resource-group-name> --name <app-name> --type jar --path target/<jar-file-name>.jar`.

5. Access the app:
   - Your app will be available at `https://<app-name>.azurewebsites.net/api/hello`.

6. Monitor and manage:
   - Use Azure Portal or `az webapp` CLI commands for monitoring and scaling.
```
