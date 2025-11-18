"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metarestore.vercel.app
Prompt: Provide an example of editing `src/app/page.js` in a Next.js project to include navigation links to external resources like nextjs.org.
Generated: DETERMINISTIC_67426a98b3ee87af
Batch ID: 20250612_145633
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://reactjs.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://nextjs.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// src/app/page.js

import React from 'react';
import Link from 'next/link';

// Main functional component for the page
const HomePage = () => {
  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Welcome to My Next.js App</h1>
      <nav style={styles.nav}>
        <h2>Navigation</h2>
        <ul style={styles.list}>
          <li style={styles.listItem}>
            <Link href="https://nextjs.org" target="_blank" rel="noopener noreferrer">
              Next.js Official Site
            </Link>
          </li>
          <li style={styles.listItem}>
            <Link href="https://reactjs.org" target="_blank" rel="noopener noreferrer">
              React Official Site
            </Link>
          </li>
          {/* Add more links as needed */}
        </ul>
      </nav>
    </div>
  );
};

// Basic styles for the components
const styles = {
  container: {
    padding: '20px',
    textAlign: 'center',
  },
  title: {
    fontSize: '2em',
    margin: '20px 0',
  },
  nav: {
    margin: '20px 0',
  },
  list: {
    listStyleType: 'none',
    padding: 0,
  },
  listItem: {
    margin: '10px 0',
  },
};

export default HomePage;
```
