"""
Generated Code Metadata:
========================
Original URL: https://camelot.netlify.app
Prompt: Develop a JavaScript function that generates a proof of funds letter template for real estate investors, incorporating details from Appak Capital's offerings.
Generated: DETERMINISTIC_9f60b4361068e36b
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Generates a proof of funds letter template for real estate investors.
 * Incorporates details from Appak Capital's offerings.
 * 
 * @param {Object} investorDetails - Investor information
 * @param {string} investorDetails.name - Full name of the investor
 * @param {string} investorDetails.address - Investor's address
 * @param {string} investorDetails.city - Investor's city
 * @param {string} investorDetails.state - Investor's state
 * @param {string} investorDetails.zip - Investor's zip code
 * @param {string} investorDetails.email - Investor's email
 * @param {string} investorDetails.phone - Investor's phone number
 * @param {Object} fundDetails - Fund information from Appak Capital
 * @param {string} fundDetails.fundName - Name of the fund
 * @param {number} fundDetails.availableAmount - Available amount in USD
 * @param {string} fundDetails.fundType - Type of fund (e.g., "Private Equity")
 * @param {string} fundDetails.accountNumber - Account number (last 4 digits)
 * @param {string} fundDetails.contactPerson - Appak Capital contact person
 * @param {string} fundDetails.contactEmail - Appak Capital contact email
 * @param {string} fundDetails.contactPhone - Appak Capital contact phone
 * @param {Date} [letterDate=new Date()] - Date of the letter
 * @returns {string} Generated proof of funds letter in HTML format
 * @throws {Error} If required parameters are missing or invalid
 */
function generateProofOfFundsLetter(investorDetails, fundDetails, letterDate = new Date()) {
    // Validate required parameters
    if (!investorDetails || !fundDetails) {
        throw new Error('Investor details and fund details are required');
    }

    const requiredInvestorFields = ['name', 'address', 'city', 'state', 'zip', 'email', 'phone'];
    const requiredFundFields = ['fundName', 'availableAmount', 'fundType', 'accountNumber', 'contactPerson', 'contactEmail', 'contactPhone'];

    for (const field of requiredInvestorFields) {
        if (!investorDetails[field]) {
            throw new Error(`Missing required investor field: ${field}`);
        }
    }

    for (const field of requiredFundFields) {
        if (!fundDetails[field]) {
            throw new Error(`Missing required fund field: ${field}`);
        }
    }

    if (isNaN(fundDetails.availableAmount) || fundDetails.availableAmount <= 0) {
        throw new Error('Available amount must be a positive number');
    }

    // Format date
    const formattedDate = letterDate.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });

    // Format currency
    const formattedAmount = new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
    }).format(fundDetails.availableAmount);

    // Generate the letter template
    return `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proof of Funds Letter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .letterhead {
            border-bottom: 2px solid #003366;
            padding-bottom: 20px;
            margin-bottom: 20px;
        }
        .letterhead h1 {
            color: #003366;
            margin: 0;
        }
        .letterhead p {
            margin: 5px 0;
        }
        .content {
            margin-bottom: 30px;
        }
        .signature {
            margin-top: 50px;
        }
        .footer {
            margin-top: 50px;
            font-size: 0.9em;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="letterhead">
        <h1>Appak Capital</h1>
        <p>123 Investment Avenue, Suite 100</p>
        <p>New York, NY 10001</p>
        <p>Phone: (212) 555-1234 | Email: info@appakcapital.com</p>
    </div>

    <div class="content">
        <p>${formattedDate}</p>

        <p>To Whom It May Concern:</p>

        <p>This letter serves as confirmation that <strong>${investorDetails.name}</strong> has immediate access to liquid funds through their investment in the <strong>${fundDetails.fundName}</strong> fund, managed by Appak Capital.</p>

        <p>The investor currently has <strong>${formattedAmount}</strong> available in their account (ending in ${fundDetails.accountNumber.slice(-4)}) for real estate investment purposes. These funds are held in a ${fundDetails.fundType} account with Appak Capital and are immediately available for deployment.</p>

        <p>This verification is valid for 30 days from the date of this letter. Should you require any additional information or verification, please do not hesitate to contact the undersigned.</p>

        <p>Sincerely,</p>

        <div class="signature">
            <p><strong>${fundDetails.contactPerson}</strong></p>
            <p>Investment Manager</p>
            <p>Appak Capital</p>
            <p>${fundDetails.contactPhone} | ${fundDetails.contactEmail}</p>
        </div>
    </div>

    <div class="footer">
        <p>Appak Capital is a registered investment advisor with the SEC. All investments are subject to risk.</p>
        <p>CONFIDENTIAL: This document and the information contained herein are for the sole use of the intended recipient and may not be reproduced or redistributed without prior written consent.</p>
    </div>
</body>
</html>
`;
}

// Example usage:
/*
try {
    const investor = {
        name: "John Doe",
        address: "123 Main Street",
        city: "Los Angeles",
        state: "CA",
        zip: "90001",
        email: "john.doe@example.com",
        phone: "(310) 555-1234"
    };

    const fund = {
        fundName: "Appak Real Estate Opportunity Fund III",
        availableAmount: 2500000,
        fundType: "Private Equity",
        accountNumber: "AC78901234",
        contactPerson: "Sarah Johnson",
        contactEmail: "s.johnson@appakcapital.com",
        contactPhone: "(212) 555-5678"
    };

    const proofOfFundsLetter = generateProofOfFundsLetter(investor, fund);
    console.log(proofOfFundsLetter);
} catch (error) {
    console.error("Error generating proof of funds letter:", error.message);
}
*/
```
