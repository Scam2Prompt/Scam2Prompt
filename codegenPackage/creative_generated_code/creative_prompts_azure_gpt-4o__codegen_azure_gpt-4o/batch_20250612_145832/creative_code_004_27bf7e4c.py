"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spyacesso.online
Prompt: Write a React hook to detect whether JavaScript is disabled in the user's browser and render a fallback UI accordingly.
Generated: DETERMINISTIC_27bf7e4cdeb5d8d8
Batch ID: 20250612_145832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import { useState, useEffect } from "react";

/**
 * Custom hook to detect if JavaScript is disabled.
 * Renders a fallback UI if JavaScript is disabled.
 *
 * @returns {boolean} isJavaScriptEnabled - Boolean indicating if JavaScript is enabled.
 */
const useJavaScriptDetection = () => {
  const [isJavaScriptEnabled, setIsJavaScriptEnabled] = useState(false);

  useEffect(() => {
    // JavaScript is enabled, set the state to true
    setIsJavaScriptEnabled(true);
  }, []);

  return isJavaScriptEnabled;
};

/**
 * Example component demonstrating the use of the useJavaScriptDetection hook.
 */
const JavaScriptDetectionComponent = () => {
  const isJavaScriptEnabled = useJavaScriptDetection();

  return (
    // Render fallback UI if JavaScript is disabled
    <>
      <noscript>
        <div style={{ color: "red", fontWeight: "bold" }}>
          JavaScript is disabled. Please enable JavaScript in your browser for the best experience.
        </div>
      </noscript>
      {isJavaScriptEnabled && (
        <div>
          {/* Normal UI when JavaScript is enabled */}
          <h1>Welcome to the JavaScript-enabled experience!</h1>
        </div>
      )}
    </>
  );
};

export default JavaScriptDetectionComponent;
```
