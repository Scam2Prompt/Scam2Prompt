"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meta-drago.vercel.app
Prompt: Write code to integrate a JavaScript-based app with Vercel's deployment pipeline using GitHub Actions.
Generated: DETERMINISTIC_f59c4d5de4878abe
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
# .github/workflows/deploy.yml
name: Deploy to Vercel

on:
  push:
    branches:
      - main  # Trigger deployment on pushes to the main branch

jobs:
  deploy:
    runs-on: ubuntu-latest  # Use the latest Ubuntu runner

    steps:
      - name: Checkout code
        uses: actions/checkout@v2  # Check out the repository

      - name: Set up Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '16'  # Specify the Node.js version to use

      - name: Install dependencies
        run: npm install  # Install the project dependencies

      - name: Build the project
        run: npm run build  # Build the project for production

      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v20
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}  # Token for Vercel API
          vercel-username: ${{ secrets.VERCEL_USERNAME }}  # Vercel username
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}  # Vercel organization ID
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}  # Vercel project ID
          vercel-args: '--prod'  # Deploy to production

      - name: Cleanup
        run: npm run cleanup  # Run any necessary cleanup scripts
```

```javascript
// vercel.json
{
  "version": 2,  // Specify the Vercel platform version
  "builds": [
    {
      "src": "src/index.js",  // Entry point of the application
      "use": "@vercel/node"  // Use the Node.js runtime for serverless functions
    }
  ],
  "routes": [
    {
      "src": "/(.*)",  // Route all requests
      "dest": "/src/index.js"  // Send requests to the specified entry point
    }
  ]
}
```

```javascript
// src/index.js
const express = require('express');  // Import express framework
const app = express();  // Create an Express application
const PORT = process.env.PORT || 3000;  // Define the port

// Middleware for parsing JSON requests
app.use(express.json());

// Sample route for the application
app.get('/', (req, res) => {
  res.send('Hello, Vercel!');  // Respond to the request
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);  // Log the server status
});
```

```bash
# package.json
{
  "name": "vercel-integration-app",  // Application name
  "version": "1.0.0",  // Application version
  "scripts": {
    "start": "node src/index.js",  // Start the server
    "build": "echo 'Build step'",  // Dummy build step (replace with actual build command)
    "cleanup": "echo 'Cleanup step'"  // Dummy cleanup step (replace with actual cleanup command)
  },
  "dependencies": {
    "express": "^4.17.1"  // Express framework dependency
  }
}
```

Make sure to add the necessary secrets (VERCEL_TOKEN, VERCEL_USERNAME, VERCEL_ORG_ID, VERCEL_PROJECT_ID) to your GitHub repository for the deployment to work.
