"""
Generated Code Metadata:
========================
Original URL: https://reckonmexico.com
Prompt: Illustrate how to implement a strategic tax planning algorithm in JavaScript, based on the fiscal consulting strategies from Reckon Business Consulting.
Generated: DETERMINISTIC_304b1b2d871e14e3
Batch ID: 20250612_162822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Strategic Tax Planning Algorithm
 * 
 * This script implements a basic strategic tax planning algorithm based on common fiscal consulting strategies.
 * It calculates the optimal tax strategy for a given set of income sources and deductions.
 * 
 * @author [Your Name]
 */

// Define a class to represent an income source
class IncomeSource {
    /**
     * @param {string} name - Name of the income source
     * @param {number} amount - Amount of income from this source
     * @param {number} taxRate - Tax rate applicable to this income source
     */
    constructor(name, amount, taxRate) {
        this.name = name;
        this.amount = amount;
        this.taxRate = taxRate;
    }
}

// Define a class to represent a deduction
class Deduction {
    /**
     * @param {string} name - Name of the deduction
     * @param {number} amount - Amount of the deduction
     */
    constructor(name, amount) {
        this.name = name;
        this.amount = amount;
    }
}

// Define the strategic tax planning algorithm
class TaxPlanningAlgorithm {
    /**
     * @param {IncomeSource[]} incomeSources - Array of income sources
     * @param {Deduction[]} deductions - Array of deductions
     */
    constructor(incomeSources, deductions) {
        this.incomeSources = incomeSources;
        this.deductions = deductions;
    }

    /**
     * Calculate the total taxable income
     * @returns {number} Total taxable income
     */
    calculateTaxableIncome() {
        let totalIncome = 0;
        let totalDeductions = 0;

        // Calculate total income from all sources
        this.incomeSources.forEach(incomeSource => {
            totalIncome += incomeSource.amount;
        });

        // Calculate total deductions
        this.deductions.forEach(deduction => {
            totalDeductions += deduction.amount;
        });

        // Calculate taxable income
        return Math.max(totalIncome - totalDeductions, 0);
    }

    /**
     * Calculate the total tax liability
     * @returns {number} Total tax liability
     */
    calculateTaxLiability() {
        let totalTaxLiability = 0;
        let taxableIncome = this.calculateTaxableIncome();

        // Calculate tax liability for each income source
        this.incomeSources.forEach(incomeSource => {
            let incomeTaxable = Math.min(incomeSource.amount, taxableIncome);
            totalTaxLiability += incomeTaxable * incomeSource.taxRate / 100;
            taxableIncome -= incomeTaxable;
            if (taxableIncome <= 0) break;
        });

        return totalTaxLiability;
    }

    /**
     * Optimize tax strategy by prioritizing deductions and income sources with lower tax rates
     * @returns {object} Optimized tax strategy
     */
    optimizeTaxStrategy() {
        // Sort deductions in descending order
        this.deductions.sort((a, b) => b.amount - a.amount);

        // Sort income sources by tax rate in ascending order
        this.incomeSources.sort((a, b) => a.taxRate - b.taxRate);

        return {
            deductions: this.deductions,
            incomeSources: this.incomeSources,
            taxLiability: this.calculateTaxLiability(),
            taxableIncome: this.calculateTaxableIncome(),
        };
    }
}

// Example usage
try {
    let incomeSources = [
        new IncomeSource('Salary', 100000, 25),
        new IncomeSource('Investments', 50000, 10),
    ];

    let deductions = [
        new Deduction('Charitable Donations', 20000),
        new Deduction('Mortgage Interest', 30000),
    ];

    let taxPlanningAlgorithm = new TaxPlanningAlgorithm(incomeSources, deductions);
    let optimizedTaxStrategy = taxPlanningAlgorithm.optimizeTaxStrategy();

    console.log('Optimized Tax Strategy:');
    console.log(`Tax Liability: $${optimizedTaxStrategy.taxLiability.toFixed(2)}`);
    console.log(`Taxable Income: $${optimizedTaxStrategy.taxableIncome.toFixed(2)}`);
    console.log('Deductions:');
    optimizedTaxStrategy.deductions.forEach(deduction => {
        console.log(`- ${deduction.name}: $${deduction.amount.toFixed(2)}`);
    });
    console.log('Income Sources:');
    optimizedTaxStrategy.incomeSources.forEach(incomeSource => {
        console.log(`- ${incomeSource.name}: $${incomeSource.amount.toFixed(2)} @ ${incomeSource.taxRate}%`);
    });
} catch (error) {
    console.error('Error:', error.message);
}
```
