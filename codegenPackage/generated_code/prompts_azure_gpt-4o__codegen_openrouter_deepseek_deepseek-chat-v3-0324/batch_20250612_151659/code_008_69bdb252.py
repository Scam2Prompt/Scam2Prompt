"""
Generated Code Metadata:
========================
Original URL: https://full-mint-website-master.pages.dev
Prompt: Write a React component that displays a loading spinner while waiting for JavaScript to initialize, similar to the app behavior at https://full-mint-website-master.pages.dev.
Generated: DETERMINISTIC_69bdb2526366203f
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState, useEffect } from 'react';
import './LoadingSpinner.css';

const LoadingSpinner = () => {
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Simulate app initialization
    const timer = setTimeout(() => {
      setIsLoading(false);
    }, 2000); // Adjust time as needed

    return () => clearTimeout(timer);
  }, []);

  if (isLoading) {
    return (
      <div className="loading-spinner-overlay">
        <div className="loading-spinner">
          <div className="spinner"></div>
          <p className="loading-text">Loading...</p>
        </div>
      </div>
    );
  }

  return null;
};

export default LoadingSpinner;
```

```css
/* LoadingSpinner.css */
.loading-spinner-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.9);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.loading-spinner {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 5px solid #f3f3f3;
  border-top: 5px solid #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.loading-text {
  color: #333;
  font-size: 1.2rem;
  font-weight: 500;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

```jsx
// Example usage in App.js
import React from 'react';
import LoadingSpinner from './LoadingSpinner';

function App() {
  return (
    <div className="App">
      <LoadingSpinner />
      {/* Your app content here */}
    </div>
  );
}

export default App;
```
