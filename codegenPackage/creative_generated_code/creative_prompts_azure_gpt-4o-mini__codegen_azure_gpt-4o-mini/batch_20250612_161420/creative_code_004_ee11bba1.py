"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v1-sturdy.pages.dev
Prompt: Explain how to enable Dark Mode in a web application that utilizes the Sturdy lending protocol.
Generated: DETERMINISTIC_ee11bba142549e6e
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Dark Mode Toggle for Web Application using Sturdy Lending Protocol

// Import necessary libraries
import React, { useEffect, useState } from 'react';
import { SturdyProvider } from 'sturdy-lending-protocol'; // Assuming this is the library for Sturdy
import './App.css'; // Include your CSS for styling

const App = () => {
  // State to manage dark mode
  const [darkMode, setDarkMode] = useState(false);

  // Effect to apply dark mode class to body
  useEffect(() => {
    const body = document.body;
    if (darkMode) {
      body.classList.add('dark-mode');
    } else {
      body.classList.remove('dark-mode');
    }
    
    // Cleanup function
    return () => {
      body.classList.remove('dark-mode');
    };
  }, [darkMode]);

  // Toggle dark mode
  const toggleDarkMode = () => {
    setDarkMode(prevMode => !prevMode);
  };

  return (
    <SturdyProvider>
      <div className="app">
        <header className="app-header">
          <h1>Sturdy Lending Protocol</h1>
          <button onClick={toggleDarkMode} className="toggle-button">
            Switch to {darkMode ? 'Light' : 'Dark'} Mode
          </button>
        </header>
        <main>
          {/* Your main application content will go here */}
        </main>
      </div>
    </SturdyProvider>
  );
};

export default App;

/* CSS (App.css) */
body {
  transition: background-color 0.3s ease, color 0.3s ease;
}

.dark-mode {
  background-color: #121212; /* Dark background */
  color: #ffffff; /* Light text color */
}

.toggle-button {
  padding: 10px 20px;
  margin-top: 20px;
  cursor: pointer;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: white;
  transition: background-color 0.3s;
}

.toggle-button:hover {
  background-color: #0056b3;
}
```
