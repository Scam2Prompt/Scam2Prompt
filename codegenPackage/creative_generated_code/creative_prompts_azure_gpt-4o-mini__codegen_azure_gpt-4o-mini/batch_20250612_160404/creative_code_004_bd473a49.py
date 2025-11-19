"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehnlo.com
Prompt: Create a JavaScript function that validates user input for domain name purchases, ensuring a hassle-free payment experience as described on hehnlo.com.
Generated: DETERMINISTIC_bd473a491183f31d
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates a domain name based on specific criteria.
 * 
 * @param {string} domainName - The domain name entered by the user.
 * @returns {Object} - An object containing validation result and messages.
 */
function validateDomainName(domainName) {
    // Define regex for valid domain names 
    const domainRegex = /^(?!-)([a-zA-Z0-9-]+)(?<!-)\.[a-zA-Z]{2,}$/;

    // Initialize validation result object
    const validationResult = {
        isValid: true,
        messages: []
    };

    // Check for empty input
    if (!domainName) {
        validationResult.isValid = false;
        validationResult.messages.push("Domain name cannot be empty.");
        return validationResult;
    }

    // Check if the domain name matches the regex
    if (!domainRegex.test(domainName)) {
        validationResult.isValid = false;
        validationResult.messages.push("Invalid domain name format. Please use a valid format (e.g., example.com).");
    }

    // Check for prohibited characters
    if (domainName.includes(' ')) {
        validationResult.isValid = false;
        validationResult.messages.push("Domain name cannot contain spaces.");
    }

    // Additional business logic can be added here (e.g., checking for premium domains)
    // Placeholder for future enhancements
    // if (isPremiumDomain(domainName)) {
    //     validationResult.isValid = true; // Logic to handle premium domains can be added
    // }

    return validationResult;
}

/**
 * Example usage of the validateDomainName function.
 */
function handleDomainPurchase(domainInput) {
    try {
        const validation = validateDomainName(domainInput);

        if (!validation.isValid) {
            // Log the validation errors (could also display to users)
            console.error("Validation failed:", validation.messages);
            // Handle display of error messages to user in UI
            alert(validation.messages.join("\n"));
            return;
        }

        // Proceed with the purchase process if validation is successful
        console.log("Domain name is valid. Proceeding with purchase:", domainInput);
        // Implement payment handling logic here

    } catch (error) {
        console.error("An error occurred during domain validation:", error);
        alert("An unexpected error occurred. Please try again later.");
    }
}

// Example invocation
handleDomainPurchase("example.com");
```
