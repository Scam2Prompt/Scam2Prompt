"""
Generated Code Metadata:
========================
Original URL: https://metamamaski.azurewebsites.net
Prompt: Create a configuration file for publishing a Java web app to Microsoft Azure App Service using the Quickstart guide.
Generated: DETERMINISTIC_c73b40efc4cfd43b
Batch ID: 20250612_145633
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "http://maven.apache.org/xsd/maven-4.0.0.xsd": {
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
  "http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd": {
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
  }
}
"""

# Generated Code:
# ===============

**pom.xml (if using Maven)**
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.example</groupId>
  <artifactId>my-web-app</artifactId>
  <version>1.0</version>
  <packaging>war</packaging>

  <name>My Web App</name>

  <properties>
    <maven.compiler.source>1.8</maven.compiler.source>
    <maven.compiler.target>1.8</maven.compiler.target>
    <java.version>1.8</java.version>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
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
        <version>3.3.1</version>
        <configuration>
          <warSourceDirectory>src/main/webapp</warSourceDirectory>
        </configuration>
      </plugin>
      <plugin>
        <groupId>com.microsoft.azure</groupId>
        <artifactId>azure-maven-plugin</artifactId>
        <version>2.0.0</version>
        <executions>
          <execution>
            <id>azure-deploy</id>
            <phase>package</phase>
            <goals>
              <goal>deploy</goal>
            </goals>
          </execution>
        </executions>
        <configuration>
          <resourceGroup>my-resource-group</resourceGroup>
          <appName>my-web-app</appName>
          <appServicePlanName>my-app-service-plan</appServicePlanName>
          <subscriptionId>your-subscription-id</subscriptionId>
          <resourceGroupLocation>your-resource-group-location</resourceGroupLocation>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

**build.gradle (if using Gradle)**
```groovy
plugins {
  id 'java'
  id 'war'
  id 'com.microsoft.azure.azure-gradle-plugin' version '2.0.0'
}

group = 'com.example'
version = '1.0'
sourceCompatibility = '1.8'

repositories {
  mavenCentral()
}

dependencies {
  provided 'javax.servlet:javax.servlet-api:4.0.1'
}

azure {
  subscriptionId = 'your-subscription-id'
  resourceGroup = 'my-resource-group'
  appName = 'my-web-app'
  appServicePlanName = 'my-app-service-plan'
  resourceGroupLocation = 'your-resource-group-location'
}
```

**.azure-pipelines.yml (for Azure DevOps)**
```yml
trigger:
- main

pool:
  vmImage: 'ubuntu-latest'

variables:
  azureSubscription: 'your-azure-subscription'
  resourceGroupName: 'my-resource-group'
  appName: 'my-web-app'
  appServicePlanName: 'my-app-service-plan'

steps:
- task: Maven@3
  displayName: 'Build and package'
  inputs:
    mavenPomFile: 'pom.xml'
    goals: 'package'

- task: AzureWebApp@1
  displayName: 'Deploy to Azure App Service'
  inputs:
    ConnectionType: 'AzureRM'
    azureSubscription: '$(azureSubscription)'
    appType: 'webApp'
    resourceGroupName: '$(resourceGroupName)'
    appName: '$(appName)'
    appServicePlanName: '$(appServicePlanName)'
```

**appsettings.json (for .NET Core)**
```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "",
    "FUNCTIONS_WORKER_RUNTIME": "dotnet",
    "AzureAppServicePlan": "my-app-service-plan",
    "AzureResourceGroup": "my-resource-group",
    "AzureAppName": "my-web-app"
  }
}
```
