"""
Generated Code Metadata:
========================
Original URL: https://avasconcelos.adv.br
Prompt: "Develop a simple calculator in JavaScript to compare the tax benefits of different regimes tributários (tax regimes) in Brazil, such as Lucro Real, Lucro Presumido, and Simples Nacional."
Generated: DETERMINISTIC_f9e93182e1a8f415
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Tax Regime Calculator for Brazil
 * This script compares the tax benefits of different tax regimes: Lucro Real, Lucro Presumido, and Simples Nacional.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Function to calculate taxes for Lucro Real
function calculateLucroReal(revenue, expenses) {
    try {
        const IRPJ_RATE = 0.15; // Corporate Income Tax rate
        const CSLL_RATE = 0.09; // Social Contribution Tax rate
        const PIS_RATE = 0.0065; // PIS rate
        const COFINS_RATE = 0.03; // COFINS rate

        const taxableIncome = revenue - expenses;
        if (taxableIncome < 0) throw new Error("Taxable income cannot be negative.");

        const irpj = taxableIncome * IRPJ_RATE;
        const csll = taxableIncome * CSLL_RATE;
        const pis = revenue * PIS_RATE;
        const cofins = revenue * COFINS_RATE;

        return {
            regime: "Lucro Real",
            totalTax: irpj + csll + pis + cofins,
            breakdown: { irpj, csll, pis, cofins }
        };
    } catch (error) {
        console.error("Error calculating Lucro Real taxes:", error.message);
        return null;
    }
}

// Function to calculate taxes for Lucro Presumido
function calculateLucroPresumido(revenue) {
    try {
        const PRESUMED_PROFIT_RATE = 0.32; // Presumed profit rate for services
        const IRPJ_RATE = 0.15; // Corporate Income Tax rate
        const CSLL_RATE = 0.09; // Social Contribution Tax rate
        const PIS_RATE = 0.0065; // PIS rate
        const COFINS_RATE = 0.03; // COFINS rate

        const presumedProfit = revenue * PRESUMED_PROFIT_RATE;
        const irpj = presumedProfit * IRPJ_RATE;
        const csll = presumedProfit * CSLL_RATE;
        const pis = revenue * PIS_RATE;
        const cofins = revenue * COFINS_RATE;

        return {
            regime: "Lucro Presumido",
            totalTax: irpj + csll + pis + cofins,
            breakdown: { irpj, csll, pis, cofins }
        };
    } catch (error) {
        console.error("Error calculating Lucro Presumido taxes:", error.message);
        return null;
    }
}

// Function to calculate taxes for Simples Nacional
function calculateSimplesNacional(revenue) {
    try {
        const SIMPLES_RATE = 0.06; // General Simples Nacional rate (varies by activity and revenue bracket)

        const totalTax = revenue * SIMPLES_RATE;

        return {
            regime: "Simples Nacional",
            totalTax,
            breakdown: { simples: totalTax }
        };
    } catch (error) {
        console.error("Error calculating Simples Nacional taxes:", error.message);
        return null;
    }
}

// Main function to compare tax regimes
function compareTaxRegimes(revenue, expenses) {
    try {
        if (revenue <= 0) throw new Error("Revenue must be greater than zero.");
        if (expenses < 0) throw new Error("Expenses cannot be negative.");

        const lucroReal = calculateLucroReal(revenue, expenses);
        const lucroPresumido = calculateLucroPresumido(revenue);
        const simplesNacional = calculateSimplesNacional(revenue);

        return [lucroReal, lucroPresumido, simplesNacional].filter(result => result !== null);
    } catch (error) {
        console.error("Error comparing tax regimes:", error.message);
        return [];
    }
}

// Example usage
const revenue = 100000; // Example revenue in BRL
const expenses = 50000; // Example expenses in BRL

const results = compareTaxRegimes(revenue, expenses);
console.log("Tax Regime Comparison:");
results.forEach(result => {
    console.log(`Regime: ${result.regime}`);
    console.log(`Total Tax: R$ ${result.totalTax.toFixed(2)}`);
    console.log("Breakdown:", result.breakdown);
    console.log("----------------------------");
});
```
