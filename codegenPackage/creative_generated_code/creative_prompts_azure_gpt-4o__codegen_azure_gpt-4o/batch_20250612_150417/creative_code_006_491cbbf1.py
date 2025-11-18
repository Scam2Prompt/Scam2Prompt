"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-mixer.com
Prompt: Create a fee calculator tool in JavaScript that takes the amount of TONCOIN to be sent and calculates the exact amount to be received after fees, based on the TONCOIN Mixer fee structure.
Generated: DETERMINISTIC_491cbbf10111afdd
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Fee Calculator for TONCOIN Mixer
// This script calculates the exact amount of TONCOIN to be received after applying the mixer fees.

// Constants for fee settings
const MIXER_FIXED_FEE = 0.5; // Fixed fee in TONCOIN (e.g., 0.5 TONCOIN)
const MIXER_PERCENTAGE_FEE = 0.01; // Percentage fee (e.g., 1%)

// Function to validate input
function validateInput(amountToSend) {
    if (typeof amountToSend !== 'number' || isNaN(amountToSend)) {
        throw new Error("Invalid input: Amount to send must be a valid number.");
    }
    if (amountToSend <= 0) {
        throw new Error("Invalid input: Amount to send must be greater than zero.");
    }
}

// Function to calculate the received amount after fees
function calculateReceivedAmount(amountToSend) {
    try {
        // Validate the input first
        validateInput(amountToSend);

        // Calculate percentage fee
        const percentageFee = amountToSend * MIXER_PERCENTAGE_FEE;

        // Calculate total fees
        const totalFee = MIXER_FIXED_FEE + percentageFee;

        // Ensure total fee doesn't exceed the amount being sent
        if (totalFee >= amountToSend) {
            throw new Error("Error: Fees exceed or equal the amount to send. Transaction not possible.");
        }

        // Calculate the final amount to be received
        const amountReceived = amountToSend - totalFee;

        return amountReceived;
    } catch (error) {
        console.error("Error during calculation:", error.message);
        return null; // Return null in case of error
    }
}

// Example usage
const amountToSend = 10; // Amount of TONCOIN to be sent
const amountReceived = calculateReceivedAmount(amountToSend);

if (amountReceived !== null) {
    console.log(`Amount to Send: ${amountToSend} TONCOIN`);
    console.log(`Amount Received After Fees: ${amountReceived.toFixed(6)} TONCOIN`);
}
```
