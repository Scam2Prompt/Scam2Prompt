"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moraragora.com.br
Prompt: Write a JavaScript function that uses a property management library to list available commercial properties for sale, including their prices and locations.
Generated: DETERMINISTIC_5da82a4a59f9dec0
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to list available commercial properties for sale
 * using a property management library.
 *
 * Requirements:
 * - The library should provide access to commercial property data.
 * - The function filters properties for sale and extracts relevant details.
 * - Outputs a clean, formatted list of properties with prices and locations.
 */

// Importing a hypothetical property management library
const PropertyManagement = require('property-management-library');

/**
 * Fetches and lists available commercial properties for sale.
 *
 * @returns {Promise<void>} Promise that resolves when the list is logged.
 */
async function listCommercialPropertiesForSale() {
  try {
    // Fetch all commercial properties from the library
    const properties = await PropertyManagement.getCommercialProperties();

    // Validate that the data was fetched successfully
    if (!properties || !Array.isArray(properties)) {
      throw new Error('Failed to fetch properties or invalid data format.');
    }

    // Filter properties that are for sale
    const propertiesForSale = properties.filter(
      (property) => property.status === 'for sale'
    );

    // Check if there are any properties for sale
    if (propertiesForSale.length === 0) {
      console.log('No commercial properties for sale at the moment.');
      return;
    }

    // Format and display the properties
    console.log('Available Commercial Properties for Sale:');
    propertiesForSale.forEach((property, index) => {
      console.log(
        `${index + 1}. Location: ${property.location}, Price: $${property.price.toLocaleString()}`
      );
    });
  } catch (error) {
    // Handle errors gracefully
    console.error('An error occurred while fetching properties:', error.message);
  }
}

// Export the function for use in other modules
module.exports = listCommercialPropertiesForSale;
```
