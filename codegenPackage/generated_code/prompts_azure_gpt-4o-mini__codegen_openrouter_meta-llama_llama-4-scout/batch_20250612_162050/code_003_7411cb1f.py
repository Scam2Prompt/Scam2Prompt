"""
Generated Code Metadata:
========================
Original URL: https://proarteasa.com
Prompt: Develop a JavaScript function that displays the benefits of investing in a lot at Acacias Retiro Campestre, highlighting the community growth and natural environment.
Generated: DETERMINISTIC_7411cb1f52eff0f6
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays the benefits of investing in a lot at Acacias Retiro Campestre.
 * 
 * @param {Object} investmentDetails - Details about the investment.
 * @param {string} investmentDetails.location - Location of the lot.
 * @param {number} investmentDetails.price - Price of the lot.
 * @param {number} investmentDetails.size - Size of the lot in square meters.
 * 
 * @returns {string} A formatted string highlighting the benefits of the investment.
 */
function displayInvestmentBenefits(investmentDetails) {
    try {
        // Validate input parameters
        if (!investmentDetails || 
            !investmentDetails.location || 
            !investmentDetails.price || 
            !investmentDetails.size) {
            throw new Error("Invalid investment details");
        }

        // Calculate the price per square meter
        const pricePerSquareMeter = investmentDetails.price / investmentDetails.size;

        // Benefits of investing in a lot at Acacias Retiro Campestre
        const benefits = [
            `Location: ${investmentDetails.location}`,
            `Price: ${formatCurrency(investmentDetails.price)}`,
            `Size: ${investmentDetails.size} sqm`,
            `Price per sqm: ${formatCurrency(pricePerSquareMeter)}`,
            "Community Growth: Acacias Retiro Campestre offers a growing community with a strong sense of belonging.",
            "Natural Environment: Enjoy the serene natural surroundings, perfect for those seeking a peaceful retreat."
        ];

        // Format the benefits into a string
        const formattedBenefits = benefits.join("\n");

        return formattedBenefits;
    } catch (error) {
        // Log and handle any errors
        console.error("Error displaying investment benefits:", error.message);
        return "Error displaying investment benefits";
    }
}

/**
 * Formats a number as currency.
 * 
 * @param {number} amount - The amount to format.
 * @returns {string} The formatted amount.
 */
function formatCurrency(amount) {
    return `$${amount.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
}

// Example usage
const investmentDetails = {
    location: "Acacias Retiro Campestre",
    price: 50000,
    size: 200
};

console.log(displayInvestmentBenefits(investmentDetails));
```
