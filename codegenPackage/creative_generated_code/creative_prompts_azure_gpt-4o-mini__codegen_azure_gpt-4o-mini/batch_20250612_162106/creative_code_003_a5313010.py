"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paypalreferralcode.com
Prompt: Generate code examples for using PayPal's referral program features in a JavaScript application.
Generated: DETERMINISTIC_a5313010bca23e97
Batch ID: 20250612_162106
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=buttons": {
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
/**
 * PayPal Referral Program Integration Example
 * This script demonstrates how to integrate PayPal's referral program features into a JavaScript application using the PayPal SDK.
 */

// Load the PayPal JavaScript SDK
const loadPayPalSDK = () => {
    return new Promise((resolve, reject) => {
        const script = document.createElement('script');
        script.src = 'https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=buttons';
        script.onload = () => resolve();
        script.onerror = () => reject(new Error('PayPal SDK failed to load'));
        document.body.appendChild(script);
    });
};

/**
 * Initializes PayPal Buttons
 * @param {string} referralLink - The referral link to use for the PayPal transaction
 */
const initPayPalButtons = (referralLink) => {
    // Check if PayPal Buttons is loaded
    if (typeof paypal === 'undefined') {
        console.error('PayPal SDK not loaded. Please load the SDK before initializing buttons.');
        return;
    }

    // Create PayPal button
    paypal.Buttons({
        createOrder: (data, actions) => {
            // Set up the transaction with a referral link
            return actions.order.create({
                purchase_units: [{
                    amount: {
                        value: '10.00', // Set the amount for the transaction
                    },
                    custom_id: referralLink // Include the referral link in the order
                }]
            });
        },
        onApprove: async (data, actions) => {
            try {
                // Capture the funds from the transaction
                const details = await actions.order.capture();
                console.log('Transaction completed successfully:', details);
                alert('Transaction completed successfully! Thank you for your support.');
            } catch (error) {
                console.error('Transaction capture failed:', error);
                alert('An error occurred while capturing the transaction. Please try again.');
            }
        },
        onError: (error) => {
            console.error('PayPal Button error:', error);
            alert('An error occurred with the PayPal Button. Please check the console for details.');
        }
    }).render('#paypal-button-container'); // Render the PayPal button in the specified container
};

// Main function to execute the script
const main = async () => {
    try {
        // Load the PayPal SDK
        await loadPayPalSDK();
        
        // Initialize PayPal buttons with a referral link
        initPayPalButtons('YOUR_REFERRAL_LINK'); // Replace with your actual referral link
    } catch (error) {
        console.error('Failed to initialize PayPal integration:', error);
        alert('An error occurred while loading PayPal. Please check the console for details.');
    }
};

// Execute main function when the window loads
window.onload = main;
```
