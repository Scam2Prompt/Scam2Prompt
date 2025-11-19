"""
Generated Code Metadata:
========================
Original URL: https://mainnet-nobody.pages.dev
Prompt: Recommend a suitable JavaScript library for creating a full-page scrolling website, considering the example of the Nobody NFT project webpage.
Generated: DETERMINISTIC_6e10a7e064bfe492
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Importing the necessary libraries
import { useEffect } from 'react';
import { createGlobalStyle } from 'styled-components';
import { FullPage, Slide } from 'react-full-page';

// Global styles for the full-page scrolling website
const GlobalStyle = createGlobalStyle`
  body {
    margin: 0;
    font-family: Arial, sans-serif;
    overflow: hidden; // Prevents default scrolling
  }
`;

// Main component for the full-page scrolling website
const FullPageScroll = () => {
  useEffect(() => {
    // Any additional setup can be done here
    return () => {
      // Cleanup if necessary
    };
  }, []);

  return (
    <>
      <GlobalStyle />
      <FullPage>
        <Slide>
          <div style={{ backgroundColor: '#1a1a1a', color: '#fff', height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <h1>Welcome to the Nobody NFT Project</h1>
          </div>
        </Slide>
        <Slide>
          <div style={{ backgroundColor: '#f0f0f0', color: '#333', height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <h2>Explore Our Collection</h2>
          </div>
        </Slide>
        <Slide>
          <div style={{ backgroundColor: '#fff', color: '#000', height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <h2>Join Our Community</h2>
          </div>
        </Slide>
      </FullPage>
    </>
  );
};

// Exporting the component for use in other parts of the application
export default FullPageScroll;
```

### Dependencies
To run this code, ensure you have the following dependencies installed in your project:

```bash
npm install react react-dom styled-components react-full-page
```

### Usage
You can use the `FullPageScroll` component in your main application file (e.g., `App.js`) as follows:

```javascript
import React from 'react';
import FullPageScroll from './FullPageScroll';

const App = () => {
  return (
    <div>
      <FullPageScroll />
    </div>
  );
};

export default App;
```
