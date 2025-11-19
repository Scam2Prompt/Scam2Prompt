"""
Generated Code Metadata:
========================
Original URL: https://meta-drago.vercel.app
Prompt: Write code to integrate a JavaScript-based app with Vercel's deployment pipeline using GitHub Actions.
Generated: DETERMINISTIC_f59c4d5de4878abe
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**.github/workflows/vercel-deployment.yml**
```yml
name: Vercel Deployment

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Login to Vercel
        uses: amondnet/vercel-action@v20
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}

      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v20
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          deploy: true
```

**vercel.json**
```json
{
  "version": 2,
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/node"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "index.js"
    }
  ]
}
```

**package.json**
```json
{
  "name": "my-app",
  "version": "1.0.0",
  "scripts": {
    "build": "npm run build:js",
    "build:js": "babel src -d dist",
    "start": "node dist/index.js"
  },
  "dependencies": {
    "express": "^4.17.1"
  },
  "devDependencies": {
    "@babel/cli": "^7.12.10",
    "@babel/core": "^7.12.10",
    "@babel/preset-env": "^7.12.11"
  }
}
```

**src/index.js**
```javascript
import express from 'express';
import { NextApiRequest, NextApiResponse } from 'next';

/**
 * Create an Express app.
 * @type {express.Application}
 */
const app = express();

/**
 * A simple API endpoint.
 * @param {NextApiRequest} req - The request object.
 * @param {NextApiResponse} res - The response object.
 */
app.get('/api/hello', (req, res) => {
  res.status(200).json({ message: 'Hello, World!' });
});

/**
 * Start the server.
 * @param {number} port - The port to listen on.
 */
const port = process.env.PORT || 3000;
app.listen(port, () => {
  globalThis.console.log(`Server started on port ${port}`);
});

export default app;
```

**.babelrc**
```json
{
  "presets": ["@babel/preset-env"]
}
```
