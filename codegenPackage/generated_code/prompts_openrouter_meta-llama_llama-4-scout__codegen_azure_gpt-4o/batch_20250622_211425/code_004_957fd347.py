"""
Generated Code Metadata:
========================
Original URL: https://fair-launch-a0xwde315-metaplex.vercel.app
Prompt: Write code to get started with a Next.js app, editing the `app/page.tsx` file.
Generated: DETERMINISTIC_957fd347fbeb328b
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```tsx
// File: app/page.tsx

// Import necessary modules from React and Next.js
import React from 'react';

// Define the HomePage component
const HomePage: React.FC = () => {
  return (
    <main style={styles.main}>
      {/* Page title */}
      <h1 style={styles.title}>Welcome to My Next.js App</h1>

      {/* Description */}
      <p style={styles.description}>
        This is a starter page for your Next.js application. Edit <code>app/page.tsx</code> to get started!
      </p>
    </main>
  );
};

// Inline styles for simplicity (can be replaced with CSS or styled-components)
const styles = {
  main: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    minHeight: '100vh',
    padding: '0 2rem',
    backgroundColor: '#f0f0f0',
  },
  title: {
    fontSize: '2.5rem',
    fontWeight: 'bold',
    margin: '1rem 0',
    color: '#333',
  },
  description: {
    fontSize: '1.25rem',
    textAlign: 'center',
    color: '#666',
  },
};

// Export the HomePage component as the default export
export default HomePage;
```
