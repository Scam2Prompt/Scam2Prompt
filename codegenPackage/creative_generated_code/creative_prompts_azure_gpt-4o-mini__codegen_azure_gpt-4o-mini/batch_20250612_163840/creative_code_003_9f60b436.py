"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://camelot.netlify.app
Prompt: Develop a JavaScript function that generates a proof of funds letter template for real estate investors, incorporating details from Appak Capital's offerings.
Generated: DETERMINISTIC_9f60b4361068e36b
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Generates a proof of funds letter template for real estate investors.
 * @param {Object} investorDetails - The details of the investor.
 * @param {string} investorDetails.name - The name of the investor.
 * @param {string} investorDetails.address - The address of the investor.
 * @param {string} investorDetails.city - The city of the investor.
 * @param {string} investorDetails.state - The state of the investor.
 * @param {string} investorDetails.zip - The ZIP code of the investor.
 * @param {number} investorDetails.amount - The amount of funds available.
 * @param {string} investorDetails.investmentType - Type of investment (e.g. residential, commercial).
 * @param {string} investorDetails.contactNumber - The contact number of the investor.
 * @returns {string} The formatted proof of funds letter.
 * @throws Will throw an error if required details are missing or invalid.
 */
function generateProofOfFundsLetter(investorDetails) {
    // Validate input details
    if (!investorDetails || typeof investorDetails !== 'object') {
        throw new Error('Invalid investor details provided.');
    }

    const { name, address, city, state, zip, amount, investmentType, contactNumber } = investorDetails;

    if (!name || !address || !city || !state || !zip || !amount || !investmentType || !contactNumber) {
        throw new Error('All fields are required to generate the proof of funds letter.');
    }

    if (isNaN(amount) || amount <= 0) {
        throw new Error('The amount must be a positive number.');
    }

    // Create the letter
    const letter = `
        ------------------------------------------------------------
                            PROOF OF FUNDS LETTER
        ------------------------------------------------------------

        To Whom It May Concern,

        This letter serves as confirmation of funds available for investment.

        Investor Name: ${name}
        Address: ${address}, ${city}, ${state} ${zip}
        Available Funds: $${amount.toLocaleString()}
        Investment Type: ${investmentType}

        For any inquiries, please feel free to contact me at ${contactNumber}.

        Thank you for your consideration.

        Sincerely,
        Appak Capital
        ------------------------------------------------------------
    `;

    return letter;
}

// Example usage
try {
    const investorDetails = {
        name: 'John Doe',
        address: '123 Main St',
        city: 'Anytown',
        state: 'CA',
        zip: '90210',
        amount: 500000,
        investmentType: 'Residential',
        contactNumber: '555-123-4567'
    };

    const proofLetter = generateProofOfFundsLetter(investorDetails);
    console.log(proofLetter);
} catch (error) {
    console.error('Error generating proof of funds letter:', error.message);
}
```
