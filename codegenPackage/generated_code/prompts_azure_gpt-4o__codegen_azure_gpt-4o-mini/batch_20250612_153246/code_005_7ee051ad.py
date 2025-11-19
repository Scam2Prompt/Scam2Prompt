"""
Generated Code Metadata:
========================
Original URL: https://outsource.s1soft.com
Prompt: Write a JavaScript function for accurate financial reporting, inspired by the accounting services offered by Special One Outsourcing.
Generated: DETERMINISTIC_7ee051addfd7e4f9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Financial Reporting Module
 * This module provides functions for accurate financial reporting.
 * It includes methods to calculate total revenue, total expenses, and net profit.
 * 
 * @module FinancialReporting
 */

/**
 * Class representing a financial report.
 */
class FinancialReport {
    /**
     * Create a financial report.
     * @param {Array} revenues - An array of revenue amounts.
     * @param {Array} expenses - An array of expense amounts.
     */
    constructor(revenues = [], expenses = []) {
        this.revenues = revenues;
        this.expenses = expenses;
    }

    /**
     * Calculate total revenue.
     * @returns {number} The total revenue.
     * @throws {Error} If revenues are not an array or contain non-numeric values.
     */
    calculateTotalRevenue() {
        this.validateArray(this.revenues);
        return this.revenues.reduce((total, amount) => total + this.validateNumber(amount), 0);
    }

    /**
     * Calculate total expenses.
     * @returns {number} The total expenses.
     * @throws {Error} If expenses are not an array or contain non-numeric values.
     */
    calculateTotalExpenses() {
        this.validateArray(this.expenses);
        return this.expenses.reduce((total, amount) => total + this.validateNumber(amount), 0);
    }

    /**
     * Calculate net profit.
     * @returns {number} The net profit (total revenue - total expenses).
     */
    calculateNetProfit() {
        const totalRevenue = this.calculateTotalRevenue();
        const totalExpenses = this.calculateTotalExpenses();
        return totalRevenue - totalExpenses;
    }

    /**
     * Validate if the input is an array and contains only numbers.
     * @param {Array} arr - The array to validate.
     * @throws {Error} If the input is not an array or contains non-numeric values.
     */
    validateArray(arr) {
        if (!Array.isArray(arr)) {
            throw new Error('Input must be an array.');
        }
        arr.forEach(amount => {
            this.validateNumber(amount);
        });
    }

    /**
     * Validate if the input is a number.
     * @param {any} value - The value to validate.
     * @returns {number} The validated number.
     * @throws {Error} If the value is not a number.
     */
    validateNumber(value) {
        if (typeof value !== 'number' || isNaN(value)) {
            throw new Error('All values must be numeric.');
        }
        return value;
    }
}

// Example usage:
try {
    const report = new FinancialReport([1000, 2000, 1500], [500, 700]);
    console.log('Total Revenue:', report.calculateTotalRevenue()); // Output: Total Revenue: 4500
    console.log('Total Expenses:', report.calculateTotalExpenses()); // Output: Total Expenses: 1200
    console.log('Net Profit:', report.calculateNetProfit()); // Output: Net Profit: 3300
} catch (error) {
    console.error('Error calculating financial report:', error.message);
}
```
