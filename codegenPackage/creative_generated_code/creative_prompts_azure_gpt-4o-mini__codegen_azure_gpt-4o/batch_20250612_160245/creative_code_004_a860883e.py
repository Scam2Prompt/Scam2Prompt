"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-pay3wfto1-dung-huynh-duc-kakas-projects.vercel.app
Prompt: What are the steps to edit the pages/index.tsx file for HMR updates in a Next.js project?
Generated: DETERMINISTIC_a860883e9b4e2b3f
Batch ID: 20250612_160245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```tsx
// pages/index.tsx

/**
 * This is the main page of the Next.js application.
 * It demonstrates Hot Module Replacement (HMR) for live updates during development.
 * Make sure the development server is running to see HMR in action.
 */

// Import necessary modules and React
import React, { useState } from 'react';

// Define a functional component for the index page
const Home: React.FC = () => {
  // State to manage dynamic content
  const [message, setMessage] = useState<string>('Welcome to Next.js with Hot Module Replacement!');

  // Function to update the message dynamically
  const updateMessage = () => {
    setMessage('HMR is working! Edit this file to see updates.');
  };

  return (
    <div style={styles.container}>
      <h1>{message}</h1>
      <button style={styles.button} onClick={updateMessage}>
        Click Me to Update Message
      </button>
    </div>
  );
};

// Inline styles for the components
const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    height: '100vh',
    textAlign: 'center',
  },
  button: {
    marginTop: '20px',
    padding: '10px 20px',
    fontSize: '16px',
    cursor: 'pointer',
    backgroundColor: '#0070f3',
    color: '#fff',
    border: 'none',
    borderRadius: '5px',
  },
};

// Export the component as default
export default Home;

// Note: HMR in Next.js works automatically during development. 
// Simply edit this file, save changes, and observe the live updates in the browser.
```
