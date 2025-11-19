"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge.org
Prompt: Write a code snippet that utilizes the deBridge Widget for bridging assets with guaranteed rates.
Generated: DETERMINISTIC_d66979f4eca28814
Batch ID: 20250612_155226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the deBridge SDK
import { deBridgeWidget } from '@debridge/sdk';

// Function to initialize and open the deBridge Widget for asset bridging
async function openDeBridgeWidget() {
    try {
        // Configuration for the deBridge Widget
        const widgetConfig = {
            fromChain: 'Ethereum', // Source chain
            toChain: 'Binance Smart Chain', // Target chain
            asset: 'USDT', // Asset to bridge
            amount: 100, // Amount to bridge
            guaranteedRate: true, // Enable guaranteed rates
            onSuccess: (response) => {
                console.log('Bridging successful:', response);
                // Handle success (e.g., notify user, update UI)
            },
            onError: (error) => {
                console.error('Error during bridging:', error);
                // Handle error (e.g., notify user, log error)
            },
            onClose: () => {
                console.log('Widget closed'); 
                // Handle widget close event (e.g., cleanup, reset state)
            },
        };

        // Open the deBridge Widget
        deBridgeWidget.open(widgetConfig);
    } catch (error) {
        console.error('Failed to open deBridge Widget:', error);
        // Handle any unexpected errors
    }
}

// Call the function to open the deBridge Widget
openDeBridgeWidget();
```

Make sure to adjust the `fromChain`, `toChain`, `asset`, and other parameters according to your bridging needs. Ensure you have the deBridge SDK installed in your project for the above code to run correctly.
