"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://3becard.com
Prompt: What libraries can I use to implement a dark mode feature similar to the one on the عبي كارد website?
Generated: DETERMINISTIC_20b0c59faf3ae560
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import { createGlobalStyle } from 'styled-components';

// Create a GlobalStyle component to handle dark mode styles
const GlobalStyle = createGlobalStyle`
  body {
    background-color: ${(props) => (props.darkMode ? '#121212' : '#ffffff')};
    color: ${(props) => (props.darkMode ? '#ffffff' : '#000000')};
    transition: background-color 0.3s ease, color 0.3s ease;
  }
`;

// Main App component
const App = () => {
  // State to manage dark mode
  const [darkMode, setDarkMode] = useState(false);

  // Effect to read from local storage
  useEffect(() => {
    const savedMode = localStorage.getItem('darkMode') === 'true';
    setDarkMode(savedMode);
  }, []);

  // Function to toggle dark mode
  const toggleDarkMode = () => {
    setDarkMode((prevMode) => {
      const newMode = !prevMode;
      try {
        // Save the preference to local storage
        localStorage.setItem('darkMode', newMode);
      } catch (error) {
        console.error('Failed to save dark mode preference:', error);
      }
      return newMode;
    });
  };

  return (
    <>
      <GlobalStyle darkMode={darkMode} />
      <div>
        <h1>Welcome to the App!</h1>
        <button onClick={toggleDarkMode}>
          Switch to {darkMode ? 'Light' : 'Dark'} Mode
        </button>
      </div>
    </>
  );
};

// Export the App component as default
export default App;
```
