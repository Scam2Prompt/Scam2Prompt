"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge.net
Prompt: Generate a script that integrates the deBridge widget to enable blazingly fast bridging between Ethereum and Solana in a web application.
Generated: DETERMINISTIC_71f916cb4aac874f
Batch ID: 20250612_151705
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://widget.debridge.finance/widget.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>deBridge Integration - Ethereum to Solana</title>
  <script src="https://widget.debridge.finance/widget.js"></script>
  <style>
    /* Simple styling for the widget container */
    #debridge-widget-container {
      margin: 20px auto;
      max-width: 800px;
      border: 1px solid #ccc;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      padding: 20px;
    }
  </style>
</head>
<body>
  <h1>Bridge Ethereum to Solana with deBridge</h1>
  <div id="debridge-widget-container"></div>

  <script>
    // Ensure the DOM is fully loaded before initializing the widget
    document.addEventListener('DOMContentLoaded', () => {
      try {
        // Initialize the deBridge widget
        deBridge.initWidget({
          container: '#debridge-widget-container', // ID of the container element
          fromChain: 'ethereum', // Source blockchain
          toChain: 'solana',    // Target blockchain
          width: '100%',        // Widget width
          height: '600px',      // Widget height
          // Customize additional options as needed
          theme: 'default',     // Optional: Use 'default' or 'dark' themes
          partnerId: '<YOUR_PARTNER_ID>', // Replace with your deBridge partner ID if applicable
        });

        console.log('deBridge widget initialized successfully.');
      } catch (error) {
        // Handle errors during widget initialization
        console.error('Error initializing deBridge widget:', error);
        const container = document.getElementById('debridge-widget-container');
        if (container) {
          container.innerHTML = '<p style="color: red;">Failed to load the widget. Please try again later.</p>';
        }
      }
    });
  </script>
</body>
</html>
```
