"""
Generated Code Metadata:
========================
Original URL: https://mettamaks-log.azurewebsites.net
Prompt: Create a Java code example for a simple web app on Azure App Service, following the Quickstart guide.
Generated: DETERMINISTIC_e4262b91fc658e7e
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
// Import necessary packages
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

// Main application class
@SpringBootApplication
public class AzureWebApp {

    public static void main(String[] args) {
        // Start the Spring Boot application
        SpringApplication.run(AzureWebApp.class, args);
    }
}

// REST controller to handle HTTP requests
@RestController
class HelloController {

    /**
     * Endpoint to return a greeting message.
     * Example: GET /hello?name=John
     *
     * @param name The name of the user (optional).
     * @return A greeting message.
     */
    @GetMapping("/hello")
    public String sayHello(@RequestParam(value = "name", defaultValue = "World") String name) {
        return String.format("Hello, %s!", name);
    }
}
```

### Notes:
1. To deploy this code to Azure App Service:
   - Package the application as a JAR file using Maven or Gradle.
   - Deploy the JAR file to Azure App Service using the Azure CLI or Azure Portal.
2. Ensure that the `application.properties` file is configured correctly for production use, including any necessary database or environment settings.
