"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.maxevent.pro
Prompt: Create a JavaScript function that allows users to select and customize their IPTV package from MaxEvent's offerings.
Generated: DETERMINISTIC_a3d4541058a35d72
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * IPTV Package Selector
 * @module IPTVPackageSelector
 */

/**
 * Represents an IPTV package.
 * @typedef {Object} IPTVPackage
 * @property {string} id - The unique identifier for the package.
 * @property {string} name - The name of the package.
 * @property {number} price - The price of the package.
 * @property {string[]} channels - List of channels included in the package.
 */

/**
 * Mock database of IPTV packages.
 * @type {IPTVPackage[]}
 */
const packages = [
    { id: 'basic', name: 'Basic Package', price: 29.99, channels: ['ABC', 'NBC', 'CBS'] },
    { id: 'premium', name: 'Premium Package', price: 49.99, channels: ['HBO', 'Showtime', 'Starz'] },
    { id: 'deluxe', name: 'Deluxe Package', price: 69.99, channels: ['ESPN', 'Fox Sports', 'NBC Sports'] }
];

/**
 * Selects and customizes an IPTV package based on user input.
 * @param {string} packageId - The ID of the selected package.
 * @param {Object} customization - Customization options for the package.
 * @param {number} customization.additionalChannels - Number of additional channels to add.
 * @throws Will throw an error if the packageId is not found or if customization is invalid.
 * @returns {IPTVPackage} - The customized IPTV package.
 */
function selectIPTVPackage(packageId, customization) {
    // Validate that the packageId is provided
    if (!packageId) {
        throw new Error('Package ID is required.');
    }

    // Find the selected package
    const selectedPackage = packages.find(pkg => pkg.id === packageId);
    if (!selectedPackage) {
        throw new Error(`Package with ID "${packageId}" not found.`);
    }

    // Validate customization input
    if (customization && typeof customization.additionalChannels === 'number') {
        // Create a new customized package based on the selected package
        const customizedPackage = {
            ...selectedPackage,
            additionalChannels: customization.additionalChannels,
            totalPrice: selectedPackage.price + (customization.additionalChannels * 5) // Example: $5 for each additional channel
        };
        return customizedPackage;
    } else {
        throw new Error('Customization must include a valid number of additional channels.');
    }
}

// Example usage:
try {
    const userSelection = selectIPTVPackage('premium', { additionalChannels: 2 });
    console.log('Customized IPTV Package:', userSelection);
} catch (error) {
    console.error('Error:', error.message);
}
```
