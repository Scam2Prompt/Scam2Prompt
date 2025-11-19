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
 * Filters laptops based on GPU type and price range.
 * 
 * @param {Array<Object>} laptops - Array of laptop objects with product details.
 * @param {string} gpuType - The GPU type to filter laptops by (e.g., "NVIDIA", "AMD").
 * @param {number} minPrice - The minimum price of the laptop.
 * @param {number} maxPrice - The maximum price of the laptop.
 * @returns {Array<Object>} - Filtered array of laptops matching criteria.
 */
function filterLaptopsByGPUAndPrice(laptops, gpuType, minPrice, maxPrice) {
    // Input validation
    if (!Array.isArray(laptops)) {
        throw new TypeError("The laptops parameter must be an array.");
    }
    if (typeof gpuType !== "string") {
        throw new TypeError("The gpuType parameter must be a string.");
    }
    if (typeof minPrice !== "number" || typeof maxPrice !== "number") {
        throw new TypeError("The price parameters must be numbers.");
    }

    // Filter laptops based on criteria
    return laptops.filter(laptop => {
        // Ensure GPU and price exist on laptop object, and validate criteria
        return (
            laptop.gpu && laptop.gpu.includes(gpuType) && // GPU type matches
            laptop.price && laptop.price >= minPrice && // Price >= minPrice
            laptop.price <= maxPrice // Price <= maxPrice
        );
    });
}

// Example usage:

// List of laptop objects (sample data from Sunrise Computers)
const laptops = [
    { brand: "Dell", model: "XPS 15", gpu: "NVIDIA GTX 1650", price: 1500 },
    { brand: "HP", model: "Spectre x360", gpu: "Intel Integrated", price: 1200 },
    { brand: "Lenovo", model: "Legion 5", gpu: "AMD Radeon RX 6600M", price: 1400 },
    { brand: "Apple", model: "MacBook Pro", gpu: "Apple M1 GPU", price: 2000 },
    { brand: "Asus", model: "ROG Zephyrus G14", gpu: "NVIDIA RTX 3060", price: 1700 }
];

// Filtering laptops with NVIDIA GPUs within a price range of $1000 to $1600
const filteredLaptops = filterLaptopsByGPUAndPrice(laptops, "NVIDIA", 1000, 1600);

console.log(filteredLaptops);
// Output: [{ brand: "Dell", model: "XPS 15", gpu: "NVIDIA GTX 1650", price: 1500 }]
```
