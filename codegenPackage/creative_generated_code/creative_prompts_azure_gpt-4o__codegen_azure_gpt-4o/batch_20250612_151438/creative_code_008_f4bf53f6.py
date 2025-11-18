"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oppomobile.id
Prompt: Generate a Dockerfile to containerize a basic web application for a system and software development project, inspired by oppomobile.id.
Generated: DETERMINISTIC_f4bf53f6060171b6
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```dockerfile
# Use the official Node.js image as the base image
# Alpine is chosen for a smaller image size
FROM node:16-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json files to the container
# This allows us to install dependencies first and leverage Docker's caching
COPY package*.json ./

# Install dependencies
RUN npm install --production

# Copy the rest of the application code to the container
COPY . .

# Expose the port that the application listens on
EXPOSE 3000

# Define the command to start the application
CMD ["node", "app.js"]

# Notes:
# - This assumes the application entry point is app.js and listens on port 3000.
# - Ensure that your local application includes 'node_modules' in .dockerignore.
```
