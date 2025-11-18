"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamamaski.azurewebsites.net
Prompt: How can I use the Microsoft Azure App Service Deployment Center to deploy a Node.js application? Provide code examples.
Generated: DETERMINISTIC_57a688e38a926f4b
Batch ID: 20250612_145633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready code sample for a basic Node.js application that you can deploy to Microsoft Azure App Service using the Deployment Center. This code includes error handling and follows best practices.

### `server.js`
```javascript
// Import required modules
const express = require('express'); // Express framework
const dotenv = require('dotenv'); // For environment variable management

// Load environment variables from a .env file, if present
dotenv.config();

// Create an instance of an Express app
const app = express();

// Middleware to parse JSON requests
app.use(express.json());

// Basic health check endpoint
app.get('/', (req, res) => {
  res.status(200).send('Welcome to the Node.js App deployed on Azure App Service!');
});

// Error-handling middleware for unhandled endpoints
app.use((req, res, next) => {
  const error = new Error('Not Found');
  error.status = 404;
  next(error);
});

// Global error handler
app.use((err, req, res, next) => {
  res.status(err.status || 500).json({
    error: {
      message: err.message || 'Internal Server Error',
    },
  });
});

// Start the server
const PORT = process.env.PORT || 3000; // Use environment variable or default to 3000
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### `package.json`
```json
{
  "name": "nodejs-azure-app",
  "version": "1.0.0",
  "description": "A basic Node.js application for deployment to Azure App Service",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "dotenv": "^16.0.0",
    "express": "^4.18.2"
  },
  "engines": {
    "node": ">=14.0.0"
  },
  "author": "Your Name",
  "license": "MIT"
}
```

### `.env` (optional)
```plaintext
# Environment variables example
PORT=3000
```

### Deployment Steps Using Azure App Service Deployment Center
1. Push the code to a GitHub repository.
2. Go to the Azure Portal and create an **App Service**.
3. In the App Service, navigate to **Deployment Center**.
4. Choose **GitHub** as the source and follow the instructions to link your repository.
5. Select the branch to deploy (e.g., `main`).
6. Click **Save** to deploy the application.
7. Once deployed, visit the application URL provided by Azure to see the app in action.

### Notes:
- Make sure to add a `.gitignore` file to exclude `node_modules` and `.env` from being committed to the repository.
- Azure will automatically detect the `package.json` file and run `npm install` and `npm start` to start the app.

### Example `.gitignore`
```plaintext
node_modules/
.env
```
