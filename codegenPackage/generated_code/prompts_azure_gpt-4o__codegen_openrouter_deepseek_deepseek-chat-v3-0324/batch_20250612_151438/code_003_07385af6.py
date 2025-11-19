"""
Generated Code Metadata:
========================
Original URL: https://oppomobile.id
Prompt: Provide code examples for setting up a CI/CD pipeline for a system and software development team, as referenced on oppomobile.id.
Generated: DETERMINISTIC_07385af643f49a0c
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```yaml
# .github/workflows/ci-cd-pipeline.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up JDK 11
      uses: actions/setup-java@v2
      with:
        java-version: '11'
        distribution: 'adopt'
    
    - name: Build with Maven
      run: mvn -B package --file pom.xml
      
    - name: Run Unit Tests
      run: mvn test
      
    - name: Upload Artifact
      uses: actions/upload-artifact@v2
      with:
        name: build-artifact
        path: target/*.jar

  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Download Artifact
      uses: actions/download-artifact@v2
      with:
        name: build-artifact
        
    - name: Deploy to Production
      run: |
        echo "Deploying to production environment..."
        # Add deployment commands here
        # Example: scp target/*.jar user@server:/path/to/deploy
```

```dockerfile
# Dockerfile
FROM adoptopenjdk:11-jre-hotspot

WORKDIR /app

COPY target/*.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      - SPRING_PROFILES_ACTIVE=prod
    restart: unless-stopped
```

```bash
#!/bin/bash
# deploy.sh

# Variables
ARTIFACT="target/app.jar"
SERVER="user@production-server"
DESTINATION="/opt/app"

# Build the project
echo "Building the project..."
mvn clean package

# Check if build succeeded
if [ $? -ne 0 ]; then
  echo "Build failed. Exiting..."
  exit 1
fi

# Deploy to production
echo "Deploying to production..."
scp $ARTIFACT $SERVER:$DESTINATION

# Restart service
echo "Restarting service..."
ssh $SERVER "systemctl restart app-service"

echo "Deployment completed successfully."
```

```yaml
# .gitlab-ci.yml
stages:
  - build
  - test
  - deploy

build_job:
  stage: build
  image: maven:3.8.4-jdk-11
  script:
    - mvn clean package
  artifacts:
    paths:
      - target/*.jar

test_job:
  stage: test
  image: maven:3.8.4-jdk-11
  script:
    - mvn test

deploy_production:
  stage: deploy
  image: alpine:latest
  script:
    - apk add openssh-client
    - scp target/*.jar user@production-server:/opt/app
    - ssh user@production-server "systemctl restart app-service"
  only:
    - main
```
