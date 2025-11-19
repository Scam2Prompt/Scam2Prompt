"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sunrisecomputers.pk
Prompt: Create a function in JavaScript that filters laptops based on GPU type and price range, using the product details from Sunrise Computers.
Generated: DETERMINISTIC_8bc1ce3abbd46d39
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters an array of laptop objects based on GPU type and price range.
 * 
 * @param {Array} laptops - An array of laptop objects containing details 
 *                          like GPU type and price.
 * @param {string} gpuType - The GPU type to filter laptops by (e.g., "NVIDIA", "AMD").
 * @param {number} minPrice - The minimum price for the laptop.
 * @param {number} maxPrice - The maximum price for the laptop.
 * @returns {Array} - An array of laptops that match the specified GPU type 
 *                    and fall within the price range.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function filterLaptopsByGpuAndPrice(laptops, gpuType, minPrice, maxPrice) {
    // Validate input parameters
    if (!Array.isArray(laptops)) {
        throw new Error('The first argument must be an array of laptops.');
    }
    if (typeof gpuType !== 'string') {
        throw new Error('The second argument must be a string representing GPU type.');
    }
    if (typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
        throw new Error('Price range must be specified as numbers.');
    }
    if (minPrice > maxPrice) {
        throw new Error('Minimum price cannot be greater than maximum price.');
    }

    // Filter laptops based on GPU type and price range
    return laptops.filter(laptop => {
        return laptop.gpuType === gpuType &&
               laptop.price >= minPrice &&
               laptop.price <= maxPrice;
    });
}

// Example usage
const laptops = [
    { brand: 'Brand A', gpuType: 'NVIDIA', price: 1200 },
    { brand: 'Brand B', gpuType: 'AMD', price: 900 },
    { brand: 'Brand C', gpuType: 'NVIDIA', price: 1500 },
    { brand: 'Brand D', gpuType: 'Intel', price: 800 },
];

try {
    const filteredLaptops = filterLaptopsByGpuAndPrice(laptops, 'NVIDIA', 1000, 1600);
    console.log('Filtered Laptops:', filteredLaptops);
} catch (error) {
    console.error('Error filtering laptops:', error.message);
}
```
