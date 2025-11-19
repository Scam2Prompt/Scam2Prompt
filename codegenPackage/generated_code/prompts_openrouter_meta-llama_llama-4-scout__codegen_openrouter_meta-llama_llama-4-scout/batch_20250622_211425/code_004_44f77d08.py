"""
Generated Code Metadata:
========================
Original URL: https://ff7a4d70.swim-ui.pages.dev
Prompt: What are the key features of Swim framework that allow building web applications with plain HTML, and provide an example use case.
Generated: DETERMINISTIC_44f77d086d7eed4d
Batch ID: 20250622_211425
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "http://maven.apache.org/POM/4.0.0": {
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
  }
}
"""

# Generated Code:
# ===============

```java
import io.swimm.web.Main;
import io.swimm.web.WebApplication;
import io.swimm.web.WebRequest;
import io.swimm.web.WebResponse;

import java.util.logging.Logger;

/**
 * This class demonstrates a simple web application built using the Swim framework.
 * It showcases how to create a web application with plain HTML.
 */
public class SwimExample {

    private static final Logger LOGGER = Logger.getLogger(SwimExample.class.getName());

    public static void main(String[] args) {
        // Create a new web application
        WebApplication app = new WebApplication();

        // Define a route for the root URL
        app.get("/", (req, res) -> {
            // Handle GET requests to the root URL
            res.html("<html><body>Hello, World!</body></html>");
        });

        // Define a route for a specific URL
        app.get("/greeting", (req, res) -> {
            // Handle GET requests to the /greeting URL
            String name = req.query("name");
            if (name == null) {
                name = "World";
            }
            res.html("<html><body>Hello, " + name + "!</body></html>");
        });

        // Start the web application
        try {
            Main.start(app, 8080);
            LOGGER.info("Web application started on port 8080");
        } catch (Exception e) {
            LOGGER.severe("Error starting web application: " + e.getMessage());
        }
    }
}
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Swim Framework Example</title>
</head>
<body>
    <h1>Welcome to the Swim Framework Example</h1>
    <p>This is a simple web application built using the Swim framework.</p>
</body>
</html>
```

**pom.xml (if using Maven)**
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>swim-example</artifactId>
    <version>1.0</version>
    <packaging>jar</packaging>

    <name>Swim Framework Example</name>

    <dependencies>
        <dependency>
            <groupId>io.swimm</groupId>
            <artifactId>swimm-web</artifactId>
            <version>1.0.0</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.2.0</version>
                <configuration>
                    <archive>
                        <manifest>
                            <addClasspath>true</addClasspath>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```
