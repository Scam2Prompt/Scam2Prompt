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

```Dockerfile
# Use the official Node.js image as a base image
FROM node:14

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install application dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY . .

# Build the application (if needed, e.g., for React, Angular)
# RUN npm run build 

# Expose the port the app runs on
EXPOSE 3000

# Command to run the application
CMD ["npm", "start"]

# Note: Ensure that your application is set to listen on 0.0.0.0 to be accessible from outside the container
```

Make sure to create a `.dockerignore` file to avoid copying unnecessary files into the Docker image:
```
node_modules
npm-debug.log
.DS_Store
.git
```

Ensure your `package.json` has a `start` script defined to launch your web application.
