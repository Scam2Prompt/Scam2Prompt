"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://checkout-9xrt5olj7-heliofi.vercel.app
Prompt: Provide an example of how to configure the Helio Embed Widget to accept both crypto and fiat payments, using the "platform" set to "helio" and "magic_eden."
Generated: DETERMINISTIC_d9103ec96b9b95b4
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { HelioEmbed } from 'helio-embed-sdk'; // Assuming this is the correct import path

// Configuration for Helio Embed Widget
const helioConfig = {
    platform: 'helio', // Set the platform to 'helio'
    magic_eden: true, // Enable Magic Eden integration
    paymentMethods: [
        { type: 'crypto', currency: 'SOL' }, // Adding crypto payment option (e.g., SOL)
        { type: 'fiat', currency: 'USD' } // Adding fiat payment option (e.g., USD)
    ],
    widgetSettings: {
        theme: 'light', // Set the widget theme
        language: 'en', // Set the language for the widget
        // Additional settings can be added here
    },
    onSuccess: (response) => {
        // Handle successful payment
        console.log('Payment Successful:', response);
        // Additional logic for post-payment processing can be added here
    },
    onError: (error) => {
        // Handle errors during payment
        console.error('Payment Error:', error);
        // Display user-friendly error message
        alert('There was an error processing your payment. Please try again.');
    }
};

// Initialize the Helio Embed Widget
try {
    const helioWidget = new HelioEmbed(helioConfig);
    helioWidget.render('#helio-embed-container'); // Render the widget in the specified container
} catch (error) {
    // Handle any initialization errors
    console.error('Failed to initialize Helio Embed Widget:', error);
    alert('Could not load payment widget. Please refresh the page and try again.');
}
```
