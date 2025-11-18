"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://checkout-9xrt5olj7-heliofi.vercel.app
Prompt: Provide an example of how to test the Helio Checkout Embed Widget on the "main" network while using custom "additional JSON" settings.
Generated: DETERMINISTIC_f71d86c7f0a21d16
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Example code to test the Helio Checkout Embed Widget on the "main" network
 * with custom "additional JSON" settings.
 */

// Ensure the DOM is fully loaded before executing the script
document.addEventListener('DOMContentLoaded', () => {
  try {
    // Helio Checkout widget configuration
    const helioCheckoutConfig = {
      network: 'main', // Specify the "main" network
      widgetId: 'your-widget-id-here', // Replace with your actual Helio widget ID
      targetElementId: 'helio-checkout-container', // The ID of the HTML element where the widget will be embedded
      additionalJson: {
        customSetting1: 'value1', // Example of a custom setting
        customSetting2: 'value2', // Add more custom settings as needed
      },
    };

    // Function to initialize and load the Helio Checkout Widget
    const loadHelioCheckoutWidget = (config) => {
      // Validate required parameters
      if (!config.network || !config.widgetId || !config.targetElementId) {
        throw new Error('Missing required configuration parameters');
      }

      // Ensure the target container exists in the DOM
      const targetElement = document.getElementById(config.targetElementId);
      if (!targetElement) {
        throw new Error(`The target container with ID "${config.targetElementId}" does not exist`);
      }

      // Load the Helio Checkout Embed Widget
      try {
        const helioCheckoutEmbed = new HelioCheckoutEmbedWidget({
          network: config.network,
          widgetId: config.widgetId,
          additionalJson: config.additionalJson,
        });

        // Render the widget into the target container
        helioCheckoutEmbed.render(targetElement);
        console.log('Helio Checkout Widget loaded successfully.');
      } catch (err) {
        console.error('Failed to initialize the Helio Checkout Widget:', err);
        throw err; // Re-throw the error for further handling
      }
    };

    // Load the widget with the defined configuration
    loadHelioCheckoutWidget(helioCheckoutConfig);
  } catch (error) {
    console.error('An error occurred while testing the Helio Checkout Widget:', error);
  }
});
```
