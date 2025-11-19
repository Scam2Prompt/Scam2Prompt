"""
Generated Code Metadata:
========================
Original URL: https://checkout-9xrt5olj7-heliofi.vercel.app
Prompt: Generate JavaScript code to display the Helio Checkout Embed Widget inline with custom settings, including "paymentType" set to "paystream" and "network" set to "test."
Generated: DETERMINISTIC_7db86fd9f8506e94
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the Helio Checkout Embed Widget script
const helioCheckout = window.helioCheckout;

// Define custom settings for the Helio Checkout Embed Widget
const customSettings = {
  // Set payment type to "paystream"
  paymentType: "paystream",
  // Set network to "test"
  network: "test",
  // Callback function for when the widget is loaded
  onLoad: function() {
    console.log("Helio Checkout Embed Widget loaded");
  },
  // Callback function for when a payment is successful
  onPaymentSuccess: function(data) {
    console.log("Payment successful:", data);
  },
  // Callback function for when a payment fails
  onPaymentFailed: function(error) {
    console.error("Payment failed:", error);
  }
};

// Function to initialize and display the Helio Checkout Embed Widget
function initHelioCheckout() {
  try {
    // Check if the helioCheckout function is available
    if (typeof helioCheckout !== "function") {
      throw new Error("Helio Checkout Embed Widget script not loaded");
    }

    // Initialize the Helio Checkout Embed Widget with custom settings
    helioCheckout(customSettings);
  } catch (error) {
    console.error("Error initializing Helio Checkout Embed Widget:", error);
  }
}

// Initialize and display the Helio Checkout Embed Widget when the page loads
document.addEventListener("DOMContentLoaded", function() {
  initHelioCheckout();
});
```
