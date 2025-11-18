"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://checkout-9xrt5olj7-heliofi.vercel.app
Prompt: Provide an example of how to configure the Helio Embed Widget to accept both crypto and fiat payments, using the "platform" set to "helio" and "magic_eden."
Generated: DETERMINISTIC_d9103ec96b9b95b4
Batch ID: 20250612_152240
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://your-website.com/payment-callback": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.hel.io/embed-widget/init": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries (if using a Node.js environment, you may need to install packages like axios)
const axios = require('axios');

// Function to configure the Helio Embed Widget
async function configureHelioEmbedWidget() {
    try {
        // Configuration object for the Helio Embed Widget
        const widgetConfig = {
            platform: ["helio", "magic_eden"], // Accept payments on Helio and Magic Eden platforms
            paymentMethods: ["crypto", "fiat"], // Enable both cryptocurrency and fiat payments
            theme: "dark", // Optional: Set the widget theme to dark
            locale: "en", // Optional: Default language for the widget (English)
            callbackUrl: "https://your-website.com/payment-callback", // URL to handle payment status updates
            customData: {
                orderId: "12345", // Example of passing custom data (e.g., order ID)
                userId: "67890"   // Example of passing custom data (e.g., user ID)
            }
        };

        // Log the configuration for debugging purposes
        console.log("Widget Configuration:", widgetConfig);

        // Initialize the widget via API (example endpoint; replace with actual API if needed)
        const response = await axios.post("https://api.hel.io/embed-widget/init", widgetConfig);

        // Check for successful initialization
        if (response.status === 200) {
            console.log("Helio Embed Widget configured successfully.");
            console.log("Widget Embed URL:", response.data.embedUrl); // Log the embed URL
        } else {
            console.error("Failed to configure the widget. Status Code:", response.status);
        }
    } catch (error) {
        // Handle errors gracefully
        console.error("An error occurred while configuring the Helio Embed Widget:", error.message);

        // Optionally, log the full error object for deeper debugging
        console.error(error);
    }
}

// Invoke the function to configure the widget
configureHelioEmbedWidget();
```

### Notes:
- Replace `"https://api.hel.io/embed-widget/init"` with the actual Helio API endpoint.
- Update the `callbackUrl` and `customData` fields with your application's specific requirements.
- Ensure `axios` is installed and imported if you're running this in a Node.js environment (`npm install axios`).
