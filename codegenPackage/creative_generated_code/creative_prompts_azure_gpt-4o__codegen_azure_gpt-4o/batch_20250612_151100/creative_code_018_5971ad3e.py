"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Provide code examples for implementing DevOps pipelines, referencing APTRON Gurgaon’s DevOps training.
Generated: DETERMINISTIC_5971ad3ef35276ac
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
# This is an example of a DevOps CI/CD pipeline implemented in a Jenkinsfile (Groovy DSL).
# The pipeline builds, tests, and deploys a sample application.
# References best practices taught in APTRON Gurgaon's DevOps training.

pipeline {
    agent any

    environment {
        // Define global environment variables
        APP_NAME = 'SampleApp'
        BUILD_DIR = 'build'
        DEPLOY_ENV = 'production'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Clone code from a Git repository
                echo "Checking out the code..."
                checkout scm
            }
        }

        stage('Build') {
            steps {
                // Run the build process
                echo "Building the application..."
                sh 'mvn clean package' // Assuming a Maven-based Java project
            }

            post {
                failure {
                    // Handle build failures
                    echo "Build failed. Check the logs for details."
                }
            }
        }

        stage('Unit Tests') {
            steps {
                // Run unit tests
                echo "Running unit tests..."
                sh 'mvn test'
            }

            post {
                always {
                    // Archive test results
                    junit 'target/surefire-reports/*.xml'
                }
                failure {
                    // Handle test failures
                    echo "Tests failed. Check test reports for details."
                }
            }
        }

        stage('Code Quality Analysis') {
            steps {
                // Analyze code quality (e.g., using SonarQube)
                echo "Running static code analysis..."
                sh 'sonar-scanner'
            }

            post {
                failure {
                    // Handle analysis failures
                    echo "Code analysis failed. Ensure code meets quality standards."
                }
            }
        }

        stage('Deploy to Production') {
            when {
                // Deploy only if the build and tests pass
                branch 'main'
            }
            steps {
                // Deploy to production environment
                echo "Deploying ${APP_NAME} to ${DEPLOY_ENV} environment..."
                sh './scripts/deploy.sh production'
            }

            post {
                success {
                    echo "Deployment successful!"
                }
                failure {
                    echo "Deployment failed! Please investigate the issue."
                }
            }
        }
    }

    post {
        always {
            // Cleanup workspace after the pipeline run
            echo "Cleaning up workspace..."
            cleanWs()
        }

        failure {
            // Notify about pipeline failure
            echo "Pipeline failed. Sending notifications..."
            mail to: 'devops-team@example.com',
                 subject: "Pipeline Failed: ${APP_NAME}",
                 body: "The pipeline failed. Please check Jenkins for details."
        }
    }
}
```

```yaml
# This is an example of a CI/CD pipeline implemented using GitHub Actions.
# It builds, tests, and deploys a sample application.

name: CI/CD Pipeline

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      # Checkout the code repository
      - name: Checkout Code
        uses: actions/checkout@v3

      # Set up Java (assuming a Java project)
      - name: Set Up JDK
        uses: actions/setup-java@v3
        with:
          java-version: '17'
          distribution: 'adopt'

      # Build the application
      - name: Build Application
        run: mvn clean package

      # Run unit tests
      - name: Run Unit Tests
        run: mvn test

      # Upload test results
      - name: Archive Test Results
        uses: actions/upload-artifact@v3
        with:
          name: test-results
          path: target/surefire-reports/*.xml

      # Code Quality Analysis (e.g., SonarQube)
      - name: Static Code Analysis
        run: sonar-scanner

  deploy:
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main' && success()

    steps:
      # Checkout the code repository
      - name: Checkout Code
        uses: actions/checkout@v3

      # Deploy to production environment
      - name: Deploy to Production
        run: ./scripts/deploy.sh production
```

```yaml
# Example of an Azure DevOps pipeline (azure-pipelines.yml).
# The pipeline builds, tests, and deploys a sample Node.js application.

trigger:
  branches:
    include:
      - main

pool:
  vmImage: 'ubuntu-latest'

variables:
  NODE_VERSION: '16'
  APP_NAME: 'SampleApp'
  DEPLOY_ENV: 'production'

stages:
- stage: Build
  displayName: "Build Stage"
  jobs:
  - job: BuildJob
    displayName: "Build Application"
    steps:
    - task: UseNode@2
      displayName: "Set up Node.js"
      inputs:
        version: $(NODE_VERSION)

    - script: |
        npm install
        npm run build
      displayName: "Install dependencies and build"

- stage: Test
  displayName: "Test Stage"
  dependsOn: Build
  jobs:
  - job: TestJob
    displayName: "Run Unit Tests"
    steps:
    - task: UseNode@2
      displayName: "Set up Node.js"
      inputs:
        version: $(NODE_VERSION)

    - script: |
        npm test
      displayName: "Run unit tests"

    - task: PublishTestResults@2
      displayName: "Publish Test Results"
      inputs:
        testResultsFormat: 'JUnit'
        testResultsFiles: '**/test-results.xml'

- stage: Deploy
  displayName: "Deploy Stage"
  dependsOn: Test
  condition: succeeded()

  jobs:
  - deployment: DeployJob
    displayName: "Deploy Application"
    environment: $(DEPLOY_ENV)
    strategy:
      runOnce:
        deploy:
          steps:
          - script: |
              echo "Deploying $(APP_NAME) to $(DEPLOY_ENV)..."
              ./scripts/deploy.sh production
            displayName: "Deploy to Production"
```
