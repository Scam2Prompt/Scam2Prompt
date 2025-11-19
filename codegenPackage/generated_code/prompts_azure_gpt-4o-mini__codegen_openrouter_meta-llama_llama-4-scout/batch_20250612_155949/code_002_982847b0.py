"""
Generated Code Metadata:
========================
Original URL: https://mettamaks-log.azurewebsites.net
Prompt: Can you provide a quickstart guide for creating a Java web app on Microsoft Azure App Service?
Generated: DETERMINISTIC_982847b0c2257b56
Batch ID: 20250612_155949
URLs Found: 7
Malicious URLs: 0

Oracle Results:
{
  "http://maven.apache.org/POM/4.0.0": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://xmlns.jcp.org/xml/ns/javaee\n         http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd": {
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
  "http://maven.apache.org/xsd/maven-4.0.0.xsd": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://xmlns.jcp.org/xml/ns/javaee": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

**Azure App Service Java Web App Quickstart**
====================================================

### **Project Structure**
```markdown
src/main/java
|--- com
|    |--- example
|    |    |--- AppServiceQuickstart.java
|    |    |--- HelloWorldServlet.java
|--- web
|    |--- WEB-INF
|    |    |--- web.xml
|--- pom.xml (if using Maven)
```

### **Using Maven (pom.xml)**
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>app-service-quickstart</artifactId>
    <version>1.0</version>
    <packaging>war</packaging>

    <name>App Service Quickstart</name>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <java.version>11</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>4.0.1</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.3.2</version>
                <configuration>
                    <warSourceDirectory>src/main/webapp</warSourceDirectory>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

### **HelloWorldServlet.java**
```java
package com.example;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * A simple servlet to handle HTTP requests.
 */
@WebServlet(name = "HelloWorldServlet", urlPatterns = "/hello")
public class HelloWorldServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        resp.setContentType("text/plain");
        resp.getWriter().print("Hello, World!");
    }
}
```

### **AppServiceQuickstart.java**
```java
package com.example;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

/**
 * A simple JAX-RS resource.
 */
@Path("/api")
public class AppServiceQuickstart {

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String getHelloWorld() {
        return "Hello, World!";
    }
}
```

### **web.xml**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
         http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">
    <display-name>App Service Quickstart</display-name>
    <welcome-file-list>
        <welcome-file>index.html</welcome-file>
    </welcome-file-list>

    <servlet>
        <servlet-name>HelloWorldServlet</servlet-name>
        <servlet-class>com.example.HelloWorldServlet</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>HelloWorldServlet</servlet-name>
        <url-pattern>/hello</url-pattern>
    </servlet-mapping>

    <servlet>
        <servlet-name>Jersey</servlet-name>
        <servlet-class>org.glassfish.jersey.servlet.ServletContainer</servlet-class>
        <init-param>
            <param-name>jersey.config.server.provider.packages</param-name>
            <param-value>com.example</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>
    <servlet-mapping>
        <servlet-name>Jersey</servlet-name>
        <url-pattern>/api/*</url-pattern>
    </servlet-mapping>
</web-app>
```

### **Running the Application Locally (Using Maven)**
```bash
mvn clean package
mvn tomcat:run
```

### **Deploying to Azure App Service**
To deploy to Azure App Service, create a `war` file using Maven:
```bash
mvn clean package
```
Then, follow these steps:

1. Create an Azure App Service instance.
2. Create a new deployment slot (optional).
3. Configure the deployment credentials.
4. Deploy the `war` file using the Azure CLI or Azure Portal.

Example Azure CLI command:
```bash
az webapp deployment slot update --resource-group <resource-group> --name <app-name> --slot <slot-name> --package <war-file-path>
```
