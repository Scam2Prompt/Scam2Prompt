"""
Generated Code Metadata:
========================
Original URL: https://ton-dex-contest-nine.vercel.app
Prompt: Provide an example of deploying a JavaScript-based app to Vercel, including configuration settings.
Generated: DETERMINISTIC_45a30fccf6cb91da
Batch ID: 20250612_153916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// vercel.json configuration file
{
  "version": 2,
  "env": {
    "NODE_ENV": "production"
  },
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "Access-Control-Allow-Origin",
          "value": "*"
        },
        {
          "key": "Access-Control-Allow-Headers",
          "value": "Origin, X-Requested-With, Content-Type, Accept"
        }
      ]
    }
  ],
  "redirects": [
    {
      "source": "/old-page",
      "destination": "/new-page",
      "permanent": true
    }
  ],
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/node"
    }
  ],
  "functions": {
    "api/_middleware.js": "experimental-edge",
    "api/hello.js": "experimental-edge"
  }
}
```

```javascript
// package.json
{
  "name": "vercel-app",
  "version": "1.0.0",
  "scripts": {
    "dev": "vercel dev",
    "build": "vercel build",
    "start": "vercel start"
  },
  "dependencies": {
    "express": "^4.17.1"
  }
}
```

```javascript
// server.js
const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Hello, World!');
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

```javascript
// api/hello.js
export default async function handler(req, res) {
  try {
    const { method } = req;
    switch (method) {
      case 'GET':
        res.status(200).json({ message: 'Hello from Vercel!' });
        break;
      default:
        res.setHeader('Allow', ['GET']);
        res.status(405).end(`Method ${method} Not Allowed`);
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
}
```

```javascript
// .gitignore
node_modules/
vercel.json
package-lock.json
```

```bash
# deploy script
#!/bin/bash

# Install dependencies
npm install

# Build the app
npm run build

# Deploy to Vercel
vercel deploy --prod
```
