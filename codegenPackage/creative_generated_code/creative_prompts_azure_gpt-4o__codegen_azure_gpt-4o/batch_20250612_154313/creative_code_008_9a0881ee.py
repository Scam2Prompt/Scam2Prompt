"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airtm-app.com
Prompt: Develop a tool using JavaScript that helps users negotiate medical bills or split expenses, following the practical budgeting tips shared by Cashflow Routine.
Generated: DETERMINISTIC_9a0881ee054e46ab
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Medical Bill Negotiator and Expense Splitter Tool
 * Developed using JavaScript
 * 
 * This tool assists users in negotiating medical bills or splitting expenses
 * based on practical budgeting tips.
 */

// Main application object
const ExpenseTool = {
    /**
     * Function to negotiate medical bills
     * @param {number} originalAmount - The original medical bill amount
     * @param {number} discountPercentage - Negotiated discount percentage
     * @returns {number} - Negotiated amount
     */
    negotiateMedicalBill: function (originalAmount, discountPercentage) {
        if (typeof originalAmount !== "number" || originalAmount <= 0) {
            throw new Error("Invalid original amount. Must be a positive number.");
        }
        if (typeof discountPercentage !== "number" || discountPercentage < 0 || discountPercentage > 100) {
            throw new Error("Invalid discount percentage. Must be between 0 and 100.");
        }
        const discount = (originalAmount * discountPercentage) / 100;
        return originalAmount - discount; // Return the negotiated amount
    },

    /**
     * Function to split expenses among multiple participants
     * @param {number} totalAmount - The total expense amount
     * @param {number} numParticipants - Number of participants to split the expense
     * @returns {number} - Amount each participant needs to pay
     */
    splitExpense: function (totalAmount, numParticipants) {
        if (typeof totalAmount !== "number" || totalAmount <= 0) {
            throw new Error("Invalid total amount. Must be a positive number.");
        }
        if (typeof numParticipants !== "number" || numParticipants <= 0 || !Number.isInteger(numParticipants)) {
            throw new Error("Invalid number of participants. Must be a positive integer.");
        }
        return totalAmount / numParticipants; // Return the split amount
    }
};

// Example Usage

try {
    // Negotiating medical bills
    const originalBill = 1000; // Example original amount in USD
    const discount = 20; // Example negotiated discount percentage
    const negotiatedAmount = ExpenseTool.negotiateMedicalBill(originalBill, discount);
    console.log(`Negotiated medical bill amount: $${negotiatedAmount.toFixed(2)}`);

    // Splitting expenses
    const totalExpense = 500; // Example total expense in USD
    const participants = 5; // Example number of participants
    const amountPerPerson = ExpenseTool.splitExpense(totalExpense, participants);
    console.log(`Amount each participant needs to pay: $${amountPerPerson.toFixed(2)}`);
} catch (error) {
    console.error("Error:", error.message);
}

/**
 * Production-ready code
 * - Includes input validation and error handling
 * - Follows JavaScript best practices
 * - Can be extended or integrated into a larger budgeting application
 */
```
