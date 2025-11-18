"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitsoft360.de
Prompt: Write code to implement a JavaScript-based notification system for users when JavaScript is disabled on their browser.
Generated: DETERMINISTIC_36f3ec56502306aa
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Notification system for users when JavaScript is disabled in their browser
// This code adds a "noscript" element to notify users that JavaScript is required

// Create a <noscript> element dynamically
const noScriptMessage = document.createElement("noscript");

// Add meaningful text to notify users
noScriptMessage.innerHTML = `
  <div style="background-color: #f8d7da; color: #721c24; padding: 10px; border: 1px solid #f5c6cb; border-radius: 5px;">
    <strong>Notice:</strong> JavaScript is disabled in your browser. Please enable JavaScript for a smooth experience.
  </div>
`;

// Append the <noscript> message to the body
document.body.appendChild(noScriptMessage);

// Error handling: Ensure the function runs safely
try {
  if (typeof document === "undefined") {
    throw new Error("Document object is not available.");
  }
} catch (error) {
  console.error("Error initializing notification system:", error.message);
}
```
