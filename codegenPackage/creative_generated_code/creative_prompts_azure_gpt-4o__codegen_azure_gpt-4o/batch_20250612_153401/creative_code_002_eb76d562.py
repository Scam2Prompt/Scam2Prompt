"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meta-drago.vercel.app
Prompt: Generate code for a React-based application that dynamically enables JavaScript functionality when hosted on Vercel.
Generated: DETERMINISTIC_eb76d56232c944af
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// React-based Application: Dynamically enables JavaScript functionality when hosted on Vercel

import React, { useEffect, useState } from "react";

// Utility function to check if the app is running on Vercel
const isHostedOnVercel = () => {
  // Check if environment variables include VERCEL
  return process.env.REACT_APP_HOST === "vercel";
};

const App = () => {
  const [isVercel, setIsVercel] = useState(false);

  useEffect(() => {
    // Dynamically detect hosting environment
    const hostedOnVercel = isHostedOnVercel();
    setIsVercel(hostedOnVercel);
  }, []);

  return (
    <div>
      <h1>React Application</h1>
      {isVercel ? (
        // Render this content only when hosted on Vercel
        <div>
          <p>The application is running on Vercel, JavaScript functionality is enabled.</p>
        </div>
      ) : (
        // Fallback content for other environments
        <div>
          <p>This application is not hosted on Vercel. Basic functionality is available.</p>
        </div>
      )}
    </div>
  );
};

export default App;

// .env file: Ensure environment variables are properly set
// REACT_APP_HOST=vercel

// Notes:
// 1. Add a .env file with the REACT_APP_HOST variable set to "vercel" for apps hosted on Vercel.
// 2. Environment variables are loaded via the dotenv package (already supported in Create React App).
// 3. Ensure proper deployment setup on Vercel to include the REACT_APP_HOST variable.
```
