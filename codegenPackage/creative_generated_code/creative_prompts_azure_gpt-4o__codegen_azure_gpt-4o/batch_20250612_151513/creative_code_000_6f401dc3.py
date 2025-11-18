"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agodarentacar.com
Prompt: Write a JavaScript function to filter car rental suppliers by payment method (credit card or debit card) using the data structure provided by Agoda RentACar's website.
Generated: DETERMINISTIC_6f401dc324e4e2a0
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters car rental suppliers based on the accepted payment method.
 * 
 * @param {Array<Object>} suppliers - List of car rental suppliers.
 * Each supplier object should include a "name" and "paymentMethods" property.
 * Example: [{ name: 'Supplier A', paymentMethods: ['credit card', 'debit card'] }]
 * 
 * @param {string} paymentMethod - The payment method to filter by (e.g., "credit card" or "debit card").
 * 
 * @returns {Array<Object>} - Filtered list of car rental suppliers that accept the specified payment method.
 */
function filterSuppliersByPaymentMethod(suppliers, paymentMethod) {
    // Input validation
    if (!Array.isArray(suppliers)) {
        throw new Error("Invalid input: suppliers must be an array of objects.");
    }

    if (typeof paymentMethod !== "string" || paymentMethod.trim() === "") {
        throw new Error("Invalid input: paymentMethod must be a non-empty string.");
    }

    // Filter suppliers based on the payment method
    return suppliers.filter(supplier => {
        // Ensure paymentMethods is an array and includes the specified payment method
        if (Array.isArray(supplier.paymentMethods)) {
            return supplier.paymentMethods.includes(paymentMethod.toLowerCase());
        }
        return false; // Exclude suppliers with invalid paymentMethods data
    });
}

// Example Usage
const carRentalSuppliers = [
    { name: "Supplier A", paymentMethods: ["credit card", "debit card"] },
    { name: "Supplier B", paymentMethods: ["credit card"] },
    { name: "Supplier C", paymentMethods: ["debit card"] },
    { name: "Supplier D", paymentMethods: [] }
];

try {
    const filteredSuppliers = filterSuppliersByPaymentMethod(carRentalSuppliers, "credit card");
    console.log("Filtered Suppliers:", filteredSuppliers);
} catch (error) {
    console.error("Error:", error.message);
}
```
