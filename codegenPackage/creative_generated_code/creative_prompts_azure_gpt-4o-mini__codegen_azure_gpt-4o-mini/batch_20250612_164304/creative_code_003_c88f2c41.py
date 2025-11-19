"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opticalize.com
Prompt: Develop a JavaScript function that validates user input for ordering luxury eyewear, ensuring it meets the quality standards mentioned on the Opticalize site.
Generated: DETERMINISTIC_c88f2c4124929364
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for ordering luxury eyewear.
 * Ensures the input meets the quality standards mentioned on the Opticalize site.
 * 
 * @param {Object} order - The order object containing user input.
 * @param {string} order.customerName - The name of the customer.
 * @param {string} order.email - The email of the customer.
 * @param {string} order.eyewearType - The type of eyewear being ordered.
 * @param {number} order.quantity - The quantity of eyewear being ordered.
 * @returns {Object} result - An object containing validation status and messages.
 */
function validateEyewearOrder(order) {
    const result = {
        isValid: true,
        messages: []
    };

    // Validate customer name
    if (!order.customerName || order.customerName.trim() === "") {
        result.isValid = false;
        result.messages.push("Customer name is required.");
    }

    // Validate email format using a regex
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!order.email || !emailRegex.test(order.email)) {
        result.isValid = false;
        result.messages.push("A valid email address is required.");
    }

    // Validate eyewear type
    const validEyewearTypes = ["sunglasses", "prescription", "reading"];
    if (!order.eyewearType || !validEyewearTypes.includes(order.eyewearType)) {
        result.isValid = false;
        result.messages.push(`Eyewear type must be one of the following: ${validEyewearTypes.join(", ")}.`);
    }

    // Validate quantity
    if (!Number.isInteger(order.quantity) || order.quantity <= 0) {
        result.isValid = false;
        result.messages.push("Quantity must be a positive integer.");
    }

    return result;
}

// Example usage
try {
    const order = {
        customerName: "John Doe",
        email: "johndoe@example.com",
        eyewearType: "sunglasses",
        quantity: 1
    };

    const validationResult = validateEyewearOrder(order);
    if (validationResult.isValid) {
        console.log("Order is valid. Proceed with processing.");
    } else {
        console.log("Order validation failed:", validationResult.messages);
    }
} catch (error) {
    console.error("An error occurred while validating the order:", error.message);
}
```
