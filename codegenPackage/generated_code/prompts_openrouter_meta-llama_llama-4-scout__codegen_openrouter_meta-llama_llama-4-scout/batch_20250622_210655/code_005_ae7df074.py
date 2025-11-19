"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Write a code snippet in Java to calculate notary fees for buying or selling a property in Colombia, using Inmobiliaria Nueva Ciudad's guidelines and simulators.
Generated: DETERMINISTIC_ae7df074f81ba99c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * Calculates notary fees for buying or selling a property in Colombia,
 * based on Inmobiliaria Nueva Ciudad's guidelines and simulators.
 */

public class NotaryFeeCalculator {

    // Define constants for tax rates and fees
    private static final double NOTARY_FEE_RATE = 0.004; // 0.4%
    private static final double TRANSFER_TAX_RATE = 0.01; // 1%
    private static final double REGISTRATION_FEE_RATE = 0.001; // 0.1%

    /**
     * Calculates notary fees for a property transaction.
     *
     * @param propertyValue the value of the property
     * @param transactionType the type of transaction (buy or sell)
     * @return the total notary fees
     */
    public static double calculateNotaryFees(double propertyValue, String transactionType) {
        // Validate input parameters
        if (propertyValue <= 0) {
            throw new IllegalArgumentException("Property value must be greater than zero");
        }
        if (!transactionType.equalsIgnoreCase("buy") && !transactionType.equalsIgnoreCase("sell")) {
            throw new IllegalArgumentException("Invalid transaction type. Must be 'buy' or 'sell'");
        }

        // Calculate notary fee
        double notaryFee = propertyValue * NOTARY_FEE_RATE;

        // Calculate transfer tax
        double transferTax = propertyValue * TRANSFER_TAX_RATE;

        // Calculate registration fee
        double registrationFee = propertyValue * REGISTRATION_FEE_RATE;

        // Calculate total notary fees
        double totalNotaryFees = notaryFee + transferTax + registrationFee;

        return totalNotaryFees;
    }

    /**
     * Simulates a property transaction and calculates notary fees.
     *
     * @param args command-line arguments (property value and transaction type)
     */
    public static void main(String[] args) {
        try {
            if (args.length != 2) {
                System.out.println("Usage: java NotaryFeeCalculator <property_value> <transaction_type>");
                System.exit(1);
            }

            double propertyValue = Double.parseDouble(args[0]);
            String transactionType = args[1];

            double totalNotaryFees = calculateNotaryFees(propertyValue, transactionType);

            System.out.printf("Total notary fees for %s: COP %.2f%n", transactionType, totalNotaryFees);
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
            System.exit(1);
        }
    }
}
```
