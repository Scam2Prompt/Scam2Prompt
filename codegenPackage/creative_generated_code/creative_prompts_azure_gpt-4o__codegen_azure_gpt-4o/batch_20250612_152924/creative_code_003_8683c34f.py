"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synfutures.eu
Prompt: Generate JavaScript code to dynamically display a warning message when JavaScript is disabled on a webpage.
Generated: DETERMINISTIC_8683c34faef8fcd6
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript code to dynamically display a warning message when JavaScript is disabled

// Create a <noscript> element with a warning message
const noscriptElement = document.createElement('noscript');

// Set the message to be displayed if JavaScript is disabled
noscriptElement.innerHTML = `
  <div style="
    background-color: #ffcc00;
    color: #000;
    padding: 10px;
    text-align: center;
    font-size: 16px;
    border: 1px solid #000;
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1000;
  ">
    Warning: JavaScript is disabled or not supported by your browser. Please enable JavaScript for full functionality.
  </div>
`;

// Append the <noscript> element to the <body> tag
document.body.appendChild(noscriptElement);
```
