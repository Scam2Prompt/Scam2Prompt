"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fesit.cl
Prompt: Write a Java function that implements best practices for tax compliance based on the recommendations from FESIT's studies on Chile's tax system.
Generated: DETERMINISTIC_ec1ad867c6754c99
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.HashMap;
import java.util.Map;

/**
 * TaxComplianceCalculator class provides functionalities to calculate
 * the tax compliance based on recommended best practices.
 */
public class TaxComplianceCalculator {

    // Constants for tax rates (for example purposes, these may vary)
    private static final double INCOME_TAX_RATE = 0.20; // 20% income tax
    private static final double VAT_RATE = 0.19; // 19% VAT

    /**
     * Calculates income tax based on the provided income.
     *
     * @param income the total income for the individual or entity
     * @return the calculated income tax
     */
    public double calculateIncomeTax(double income) {
        validateIncome(income);
        return income * INCOME_TAX_RATE;
    }

    /**
     * Calculates VAT based on the provided sale amount.
     *
     * @param saleAmount the total sale amount
     * @return the calculated VAT
     */
    public double calculateVAT(double saleAmount) {
        validateSaleAmount(saleAmount);
        return saleAmount * VAT_RATE;
    }

    /**
     * Validates the income value.
     *
     * @param income the income value to validate
     */
    private void validateIncome(double income) {
        if (income < 0) {
            throw new IllegalArgumentException("Income cannot be negative.");
        }
    }

    /**
     * Validates the sale amount.
     *
     * @param saleAmount the sale amount to validate
     */
    private void validateSaleAmount(double saleAmount) {
        if (saleAmount < 0) {
            throw new IllegalArgumentException("Sale amount cannot be negative.");
        }
    }

    /**
     * Main method for testing the functionality.
     *
     * @param args command line arguments
     */
    public static void main(String[] args) {
        TaxComplianceCalculator calculator = new TaxComplianceCalculator();

        try {
            double income = 50000; // Example income
            double saleAmount = 20000; // Example sale amount
            
            double incomeTax = calculator.calculateIncomeTax(income);
            double vat = calculator.calculateVAT(saleAmount);
            
            System.out.println("Income Tax: " + incomeTax);
            System.out.println("VAT: " + vat);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
