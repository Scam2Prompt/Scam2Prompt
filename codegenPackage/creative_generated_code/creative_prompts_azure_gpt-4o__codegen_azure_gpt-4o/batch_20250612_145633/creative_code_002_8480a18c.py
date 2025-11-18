"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metarestore.vercel.app
Prompt: Provide an example of a Next.js project setup that includes instant updates when editing `src/app/page.js`.
Generated: DETERMINISTIC_8480a18c2f2c9a27
Batch ID: 20250612_145633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: package.json
{
  "name": "nextjs-instant-update-example",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",          // Starts the development server with HMR (Hot Module Replacement)
    "build": "next build",      // Builds the production-ready application
    "start": "next start"       // Starts the production server
  },
  "dependencies": {
    "next": "13.4.12",          // Replace with the latest version of Next.js
    "react": "18.2.0",          // Replace with the latest React version
    "react-dom": "18.2.0"       // Replace with the latest React-DOM version
  }
}
```

```javascript
// File: next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true, // Enables React's strict mode to catch potential issues
  swcMinify: true        // Enables faster builds using the SWC compiler
};

module.exports = nextConfig;
```

```javascript
// File: src/app/page.js
import React from 'react';

// The main page component
// This will instantly update when edited in development mode
export default function HomePage() {
  return (
    <main style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Welcome to the Next.js Instant Update Example!</h1>
      <p>
        Edit <code>src/app/page.js</code> and save to see instant updates in your browser.
      </p>
    </main>
  );
}
```

```javascript
// File: src/app/layout.js
import './globals.css'; // Import global styles (optional)

// Layout component for all pages
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <title>Next.js Instant Update Example</title>
      </head>
      <body>{children}</body>
    </html>
  );
}
```

```css
/* File: src/app/globals.css */
/* Global styles for the application */
body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  color: #333;
}
```

```bash
# Steps to initialize the project (run these commands in your terminal)

# 1. Initialize a new Next.js project
npx create-next-app@latest nextjs-instant-update-example --use-npm --src-dir --app

# 2. Navigate to the project directory
cd nextjs-instant-update-example

# 3. Replace the generated files with the ones provided above

# 4. Start the development server
npm run dev
```

```plaintext
# Note: No additional configuration is required for instant updates in development mode.
# Next.js includes Hot Module Replacement (HMR) by default, which provides instant updates when editing files.
```
