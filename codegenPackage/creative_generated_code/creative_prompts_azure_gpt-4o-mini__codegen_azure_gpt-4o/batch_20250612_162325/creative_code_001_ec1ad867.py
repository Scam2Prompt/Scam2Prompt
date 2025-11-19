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

public class TaxCompliance {

    // Constants for tax rates specific to Chile
    private static final double VAT_RATE = 0.19; // Value-Added Tax (IVA)
    private static final double INCOME_TAX_RATE = 0.10; // Example for simplified rate

    // Error messages
    private static final String ERROR_NEGATIVE_AMOUNT = "Amount must be non-negative.";

    /**
     * Calculate VAT (IVA) for a given amount.
     *
     * @param amount The amount for which VAT is to be calculated.
     * @return The VAT amount.
     * @throws IllegalArgumentException if the amount is negative.
     */
    public static double calculateVAT(double amount) {
        if (amount < 0) {
            throw new IllegalArgumentException(ERROR_NEGATIVE_AMOUNT);
        }
        return roundToTwoDecimalPlaces(amount * VAT_RATE);
    }

    /**
     * Calculate income tax for a given income.
     *
     * @param income The income for which tax is to be calculated.
     * @return The income tax amount.
     * @throws IllegalArgumentException if the income is negative.
     */
    public static double calculateIncomeTax(double income) {
        if (income < 0) {
            throw new IllegalArgumentException(ERROR_NEGATIVE_AMOUNT);
        }
        return roundToTwoDecimalPlaces(income * INCOME_TAX_RATE);
    }

    /**
     * Generate a summary report of taxes.
     *
     * @param salesAmount The sales amount subject to VAT.
     * @param income The income subject to income tax.
     * @return A map containing the tax breakdown (VAT, Income Tax, Total Tax).
     */
    public static Map<String, Double> generateTaxReport(double salesAmount, double income) {
        Map<String, Double> taxReport = new HashMap<>();

        // Calculate individual taxes
        double vat = calculateVAT(salesAmount);
        double incomeTax = calculateIncomeTax(income);
        double totalTax = roundToTwoDecimalPlaces(vat + incomeTax);

        // Populate the report
        taxReport.put("VAT", vat);
        taxReport.put("Income Tax", incomeTax);
        taxReport.put("Total Tax", totalTax);

        return taxReport;
    }

    /**
     * Helper method to round a double value to two decimal places.
     *
     * @param value The value to be rounded.
     * @return The rounded value.
     */
    private static double roundToTwoDecimalPlaces(double value) {
        return Math.round(value * 100.0) / 100.0;
    }

    /**
     * Example usage of the tax compliance functions.
     * 
     * NOTE: For production, remove this main method and place unit tests in a separate test class.
     */
    public static void main(String[] args) {
        try {
            double salesAmount = 10000.0; // Example sales amount
            double income = 5000.0; // Example income

            // Generate tax report
            Map<String, Double> taxReport = generateTaxReport(salesAmount, income);

            // Print tax report
            System.out.println("Tax Report:");
            taxReport.forEach((key, value) -> System.out.println(key + ": " + value));
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
