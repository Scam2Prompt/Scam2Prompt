"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: "Create a simple web application using Java and Spring framework, as covered in the Java training course at APTRON Gurgaon."
Generated: DETERMINISTIC_6316185169487b7f
Batch ID: 20250622_204551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
// Main application class
package com.aptron.gurgaon.webapp;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
public class WebApplication {

    public static void main(String[] args) {
        SpringApplication.run(WebApplication.class, args);
    }
}

// Simple REST controller
@RestController
class GreetingController {

    /**
     * Returns a greeting message
     * @param name Optional name parameter
     * @return Greeting message
     */
    @GetMapping("/greet")
    public String greet(@RequestParam(value = "name", defaultValue = "World") String name) {
        return String.format("Hello %s from APTRON Gurgaon!", name);
    }

    /**
     * Health check endpoint
     * @return Application status
     */
    @GetMapping("/health")
    public String healthCheck() {
        return "Application is running!";
    }
}

// Configuration class
package com.aptron.gurgaon.webapp.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig {

    @Bean
    public WebMvcConfigurer corsConfigurer() {
        return new WebMvcConfigurer() {
            @Override
            public void addCorsMappings(CorsRegistry registry) {
                registry.addMapping("/**")
                        .allowedOrigins("*")
                        .allowedMethods("GET", "POST", "PUT", "DELETE", "OPTIONS");
            }
        };
    }
}

// Exception handler
package com.aptron.gurgaon.webapp.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public String handleAllExceptions(Exception ex) {
        return "An error occurred: " + ex.getMessage();
    }
}

// Application properties
# src/main/resources/application.properties
server.port=8080
spring.application.name=aptron-webapp
```
