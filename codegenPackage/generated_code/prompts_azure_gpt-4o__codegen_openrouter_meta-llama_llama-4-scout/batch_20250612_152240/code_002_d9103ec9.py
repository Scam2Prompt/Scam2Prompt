"""
Generated Code Metadata:
========================
Original URL: https://checkout-9xrt5olj7-heliofi.vercel.app
Prompt: Provide an example of how to configure the Helio Embed Widget to accept both crypto and fiat payments, using the "platform" set to "helio" and "magic_eden."
Generated: DETERMINISTIC_d9103ec96b9b95b4
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Configures the Helio Embed Widget to accept both crypto and fiat payments.
 * 
 * @param {string} platform - The platform to set for the Helio Embed Widget. 
 *                           Options: "helio", "magic_eden"
 * @returns {object} The configuration object for the Helio Embed Widget.
 */
function configureHelioEmbedWidget(platform) {
    // Check if the platform is valid
    if (!["helio", "magic_eden"].includes(platform)) {
        throw new Error(`Invalid platform: ${platform}. Must be either "helio" or "magic_eden".`);
    }

    // Configuration object for the Helio Embed Widget
    const config = {
        // Set the platform
        platform: platform,

        // Payment configuration
        payment: {
            // Enable crypto payments
            crypto: {
                enabled: true,
            },
            // Enable fiat payments
            fiat: {
                enabled: true,
            },
        },

        // Customize the widget's appearance
        appearance: {
            // Set the theme
            theme: "light",
            // Set the color scheme
            colors: {
                primary: "#4CAF50",
                secondary: "#3e3e3e",
            },
        },
    };

    return config;
}

// Example usage
try {
    const helioConfig = configureHelioEmbedWidget("helio");
    console.log(helioConfig);

    const magicEdenConfig = configureHelioEmbedWidget("magic_eden");
    console.log(magicEdenConfig);
} catch (error) {
    console.error(error.message);
}
```
