"""
Generated Code Metadata:
========================
Original URL: https://600n-wl-mint.vercel.app
Prompt: "Generate a basic React or Next.js page that requires JavaScript to display its content, similar to the 600N Mint website."
Generated: DETERMINISTIC_8c9bf614602acae8
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// pages/index.js
import { useEffect, useState } from "react";

export default function Home() {
  // State to manage whether JavaScript is enabled
  const [isJSLoaded, setIsJSLoaded] = useState(false);

  useEffect(() => {
    // Set the state to true once the component is mounted (JavaScript is running)
    setIsJSLoaded(true);
  }, []);

  return (
    <div>
      {/* Basic styling */}
      <style jsx>{`
        .container {
          display: flex;
          justify-content: center;
          align-items: center;
          height: 100vh;
          font-family: Arial, sans-serif;
          text-align: center;
        }
        .message {
          font-size: 1.5rem;
          color: #333;
        }
      `}</style>

      <div className="container">
        {/* Conditionally render content based on JavaScript being enabled */}
        {isJSLoaded ? (
          <div className="message">
            <h1>Welcome to the 600N Mint Website</h1>
            <p>JavaScript is enabled, and the content is displayed!</p>
          </div>
        ) : (
          <noscript>
            <div className="message">
              <h1>JavaScript is required to view this page.</h1>
              <p>Please enable JavaScript in your browser settings.</p>
            </div>
          </noscript>
        )}
      </div>
    </div>
  );
}
```

This code is a basic Next.js page that checks if JavaScript is enabled and displays content accordingly. It uses React's `useEffect` hook to detect when JavaScript is running and conditionally renders the content.
