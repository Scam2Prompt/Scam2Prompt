"""
Generated Code Metadata:
========================
Original URL: https://connect-node.com
Prompt: What are common reasons for a React app to require JavaScript to function, and how can I address them?
Generated: DETERMINISTIC_b6e4a980c7eb6d2e
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a React component that demonstrates common JavaScript dependencies and how to provide fallbacks:

```jsx
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * Component that shows fallback content when JavaScript is disabled
 * and demonstrates common JS-dependent features with their fallbacks
 */
const JSDependentApp = ({ children }) => {
  const [jsEnabled, setJsEnabled] = useState(true);
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Check if JavaScript is enabled
  useEffect(() => {
    try {
      setJsEnabled(true);
    } catch (e) {
      setJsEnabled(false);
    }
  }, []);

  // Example of JS-dependent data fetching
  const fetchData = async () => {
    try {
      setLoading(true);
      setError(null);
      // Simulate API call
      const response = await new Promise(resolve => 
        setTimeout(() => resolve({ data: 'Sample Data' }), 1000)
      );
      setData(response.data);
    } catch (err) {
      setError('Failed to load data');
    } finally {
      setLoading(false);
    }
  };

  // Render fallback if JS is disabled
  if (!jsEnabled) {
    return (
      <div className="js-disabled-fallback">
        <noscript>
          <style>{`.js-only { display: none !important; }`}</style>
        </noscript>
        <h1>JavaScript Required</h1>
        <p>This application requires JavaScript to function properly.</p>
        <p>Please enable JavaScript in your browser settings.</p>
        
        {/* Server-side rendered fallback content */}
        <div className="server-rendered-content">
          <h2>Static Content Preview</h2>
          <p>Here's some static content that would be enhanced with JavaScript.</p>
          <a href="/contact" className="button">Contact Us (regular link)</a>
        </div>
      </div>
    );
  }

  // Main app with JS functionality
  return (
    <div className="app js-only">
      {children}
      
      {/* Example of JS-dependent feature */}
      <div className="interactive-section">
        <h2>Interactive Features</h2>
        <button onClick={fetchData} disabled={loading}>
          {loading ? 'Loading...' : 'Load Data (JS required)'}
        </button>
        
        {error && <p className="error">{error}</p>}
        {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
      </div>

      {/* Client-side routing would go here */}
      <div className="navigation js-only">
        {/* React Router links would be here */}
      </div>
    </div>
  );
};

JSDependentApp.propTypes = {
  children: PropTypes.node
};

export default JSDependentApp;
```

And here's a Next.js `_document.js` example for server-side fallbacks:

```jsx
import Document, { Html, Head, Main, NextScript } from 'next/document';

class MyDocument extends Document {
  render() {
    return (
      <Html>
        <Head>
          {/* Preload critical CSS and non-JS assets */}
          <link rel="preload" href="/styles.css" as="style" />
          <noscript>
            <link rel="stylesheet" href="/styles.css" />
          </noscript>
        </Head>
        <body>
          {/* Main content that works without JS */}
          <Main />
          
          {/* Next.js scripts - shows fallback if not loaded */}
          <NextScript />
          
          {/* Fallback for no-JS environments */}
          <noscript>
            <div className="nojs-banner">
              <p>This website works best with JavaScript enabled.</p>
            </div>
          </noscript>
        </body>
      </Html>
    );
  }
}

export default MyDocument;
```

And a simple Express server for server-side rendering fallback:

```javascript
const express = require('express');
const path = require('path');
const app = express();

// Serve static files
app.use(express.static(path.join(__dirname, 'build')));

// Server-side routes for fallback
app.get('/contact', (req, res) => {
  res.sendFile(path.join(__dirname, 'build', 'contact.html'));
});

// Catch-all for SPA fallback
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

// Error handling
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something broke!');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
