"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marinekiosk.gr
Prompt: Suggest an API or library for implementing age verification on a website, ensuring users confirm they are over 18 before accessing cannabis product details like "CHARAS 100% CB9 AMNESIA."
Generated: DETERMINISTIC_587d87f5411c1477
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ageVerification.js

/**
 * Age Verification Module
 * This module provides a simple function to verify if a user is over 18.
 * In a real application, this could be connected to a server for enhanced security.
 */

class AgeVerification {
    constructor() {
        this.age = null;
    }

    /**
     * Prompt the user for their age.
     * @returns {Promise<boolean>} - Returns true if the user is over 18, false otherwise.
     */
    async promptAge() {
        return new Promise((resolve) => {
            const ageInput = prompt("Please enter your age:");

            // Validate if the input is a number
            if (!isNaN(ageInput) && ageInput !== null) {
                this.age = Number(ageInput);
                resolve(this.isOverEighteen());
            } else {
                alert("Invalid input. Please enter a valid age.");
                resolve(false);
            }
        });
    }

    /**
     * Check if the user is over 18.
     * @returns {boolean} - Returns true if age is greater than or equal to 18.
     */
    isOverEighteen() {
        return this.age >= 18;
    }
}

// Usage of the Age Verification Module
(async () => {
    const ageVerifier = new AgeVerification();
    const isValidAge = await ageVerifier.promptAge();

    if (isValidAge) {
        // User is verified; proceed to show cannabis product details
        displayProductDetails();
    } else {
        // User is not verified; show an error message or redirect
        alert("You must be at least 18 years old to access this content.");
    }
})();

/**
 * Function to display cannabis product details.
 */
function displayProductDetails() {
    const productDetails = {
        name: "CHARAS 100% CB9 AMNESIA",
        description: "A premium cannabis product with unique flavors.",
        pricing: "$50 per gram"
    };

    console.log("Product Name: " + productDetails.name);
    console.log("Description: " + productDetails.description);
    console.log("Pricing: " + productDetails.pricing);
}
```

### Note:
- Ensure that this JavaScript code is executed in a web environment where `prompt` and `alert` functions are available, such as a browser. 
- Consider server-side validation for production to enhance security.
