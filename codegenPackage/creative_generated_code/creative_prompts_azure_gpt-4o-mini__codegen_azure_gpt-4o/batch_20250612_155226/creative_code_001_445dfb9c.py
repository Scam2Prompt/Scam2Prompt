"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge.net
Prompt: Write a code snippet that utilizes the deBridge Widget for seamless bridging of assets across major chains.
Generated: DETERMINISTIC_445dfb9ca36dae4b
Batch ID: 20250612_155226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Example implementation of the deBridge Widget for seamless asset bridging across major chains.
 * This code snippet assumes the use of JavaScript in a browser environment.
 * Ensure you have included the deBridge Widget library in your project before using this code.
 */

// Function to initialize and configure the deBridge Widget
function initializeDeBridgeWidget() {
  try {
    // Verify deBridgeWidget is available globally
    if (typeof deBridgeWidget === 'undefined') {
      console.error('Error: deBridgeWidget is not loaded. Ensure the library is included in your project.');
      return;
    }

    // Configuration object for the Widget
    const widgetConfig = {
      selector: '#deBridge-widget', // ID of the HTML element to embed the widget
      mode: 'light', // Display mode: 'light' or 'dark'
      apiKey: 'your-api-key-here', // Replace with your deBridge API key
      fromChain: 'Ethereum', // Source blockchain
      toChain: 'Binance Smart Chain', // Target blockchain
      asset: 'USDT', // Asset to be bridged
      amount: 100, // Default transfer amount
      // Optional callbacks for event handling
      onSuccess: (transaction) => {
        console.log('Transaction successful:', transaction);
      },
      onError: (error) => {
        console.error('Transaction error:', error);
      },
    };

    // Embed the Widget into the target selector
    deBridgeWidget.init(widgetConfig);

    console.log('deBridge Widget initialized successfully.');
  } catch (error) {
    console.error('Error initializing deBridge Widget:', error);
  }
}

// Call the initialization function when the DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  initializeDeBridgeWidget();
});
```

**HTML requirements**:
Make sure to include a container in your HTML for the widget:
```html
<div id="deBridge-widget" style="width: 100%; height: 500px;"></div>
```

**Additional Notes**:
Replace `your-api-key-here` in the configuration with your actual API key obtained from deBridge. Ensure the `deBridgeWidget` library script is properly included in your project (via CDN or npm package). Refer to the official deBridge documentation for more details.
