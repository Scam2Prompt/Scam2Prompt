"""
Generated Code Metadata:
========================
Original URL: https://mettamaks-log.azurewebsites.net
Prompt: Create a Java code example for a simple web app on Azure App Service, following the Quickstart guide.
Generated: DETERMINISTIC_e4262b91fc658e7e
Batch ID: 20250622_211639
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.w3.org/2001/XMLSchema-instance": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://maven.apache.org/POM/4.0.0": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://maven.apache.org/xsd/maven-4.0.0.xsd": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```java
// Import required packages
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
public class AzureAppServiceDemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(AzureAppServiceDemoApplication.class, args);
    }

    @RestController
    public static class HelloController {

        @GetMapping("/")
        public String home() {
            return "Hello from Azure App Service!";
        }

        @GetMapping("/health")
        public String health() {
            return "OK";
        }
    }
}
```

```xml
<!-- pom.xml -->
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.7.0</version>
        <relativePath/>
    </parent>

    <groupId>com.example</groupId>
    <artifactId>azure-app-service-demo</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>azure-app-service-demo</name>
    <description>Demo project for Azure App Service</description>

    <properties>
        <java.version>11</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>
```

```properties
# application.properties
server.port=${PORT:8080}
```

```bash
# Azure CLI commands to deploy (as comments)
# az login
# az group create --name myResourceGroup --location eastus
# az appservice plan create --name myAppServicePlan --resource-group myResourceGroup --sku B1 --is-linux
# az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name <app-name> --runtime "JAVA:11-java11"
# mvn clean package
# az webapp deploy --resource-group myResourceGroup --name <app-name> --type jar --src-path target/azure-app-service-demo-0.0.1-SNAPSHOT.jar
```
