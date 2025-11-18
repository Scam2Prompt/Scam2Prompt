"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://events-pepe.net
Prompt: Provide an example of a Kubernetes YAML configuration file for deploying a Node.js application, based on the DevOps tutorials from https://events-pepe.net.
Generated: DETERMINISTIC_6b02f7a7f343f6da
Batch ID: 20250612_150644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
# This is a Kubernetes YAML configuration file for deploying a Node.js application.
# The setup includes a Deployment and a Service to expose the application.

apiVersion: apps/v1
kind: Deployment
metadata:
  name: nodejs-app-deployment  # Name of the deployment
  labels:
    app: nodejs-app  # Label to identify the application
spec:
  replicas: 3  # Number of pod replicas for scaling
  selector:
    matchLabels:
      app: nodejs-app  # Matching label for pod selection
  template:
    metadata:
      labels:
        app: nodejs-app  # Label to associate with pods
    spec:
      containers:
        - name: nodejs-app-container  # Name of the container
          image: node:16-alpine  # Node.js base image (lightweight Alpine version)
          ports:
            - containerPort: 3000  # Port the app listens on inside the container
          env:
            - name: NODE_ENV  # Environment variable
              value: production  # Set environment to production
            - name: APP_PORT  # Environment variable for app port
              value: "3000"
          readinessProbe:  # Health check to ensure the app is ready
            httpGet:
              path: /
              port: 3000
            initialDelaySeconds: 5
            periodSeconds: 10
          livenessProbe:  # Health check to ensure the app is alive
            httpGet:
              path: /
              port: 3000
            initialDelaySeconds: 5
            periodSeconds: 10
          resources:  # Resource limits and requests for the container
            limits:
              memory: "256Mi"
              cpu: "500m"
            requests:
              memory: "128Mi"
              cpu: "250m"

---
apiVersion: v1
kind: Service
metadata:
  name: nodejs-app-service  # Name of the service
  labels:
    app: nodejs-app  # Label to associate with the service
spec:
  selector:
    app: nodejs-app  # Match pods with this label
  ports:
    - protocol: TCP
      port: 80  # Port on the service
      targetPort: 3000  # Port on the container
  type: ClusterIP  # Service type (internal access only)
```
