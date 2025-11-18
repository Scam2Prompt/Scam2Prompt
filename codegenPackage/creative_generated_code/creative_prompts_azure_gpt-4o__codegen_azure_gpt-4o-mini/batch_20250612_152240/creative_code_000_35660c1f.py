"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://checkout-9xrt5olj7-heliofi.vercel.app
Prompt: Write code to integrate the Helio Checkout Embed Widget into a webpage using the "paylink id" and "primaryPaymentMethod" options described in the Helio documentation.
Generated: DETERMINISTIC_35660c1ff21dfa51
Batch ID: 20250612_152240
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.helio.com/checkout.js": {
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
    <title>Helio Checkout Integration</title>
    <script src="https://cdn.helio.com/checkout.js"></script>
    <style>
        /* Basic styling for the widget container */
        #helio-checkout-widget {
            width: 100%;
            max-width: 400px;
            margin: 20px auto;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 20px;
            text-align: center;
        }
    </style>
</head>
<body>

<div id="helio-checkout-widget"></div>

<script>
    // Function to initialize the Helio Checkout Embed Widget
    function initializeHelioCheckout(paylinkId, primaryPaymentMethod) {
        try {
            // Validate the inputs
            if (!paylinkId || !primaryPaymentMethod) {
                throw new Error("Both paylinkId and primaryPaymentMethod are required.");
            }

            // Create the Helio checkout widget
            HelioCheckout.create({
                paylinkId: paylinkId, // The paylink ID provided by Helio
                primaryPaymentMethod: primaryPaymentMethod, // The primary payment method
                container: '#helio-checkout-widget', // The container for the widget
                onSuccess: function(response) {
                    // Handle successful payment response
                    console.log('Payment successful:', response);
                    alert('Payment was successful! Thank you for your purchase.');
                },
                onError: function(error) {
                    // Handle error during payment
                    console.error('Payment error:', error);
                    alert('An error occurred during payment. Please try again.');
                }
            });
        } catch (error) {
            // Log the error and display a user-friendly message
            console.error('Initialization failed:', error);
            alert('Failed to initialize checkout. Please check console for details.');
        }
    }

    // Call the function with your paylink ID and preferred primary payment method
    const paylinkId = 'YOUR_PAYLINK_ID'; // Replace with your paylink ID
    const primaryPaymentMethod = 'credit_card'; // Replace with the desired primary payment method

    // Initialize the Helio Checkout Widget
    initializeHelioCheckout(paylinkId, primaryPaymentMethod);
</script>

</body>
</html>
```
