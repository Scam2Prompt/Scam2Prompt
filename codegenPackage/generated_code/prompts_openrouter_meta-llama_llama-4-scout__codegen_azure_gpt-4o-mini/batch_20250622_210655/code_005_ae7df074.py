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
import java.util.Scanner;

/**
 * This class calculates notary fees for buying or selling a property in Colombia
 * based on Inmobiliaria Nueva Ciudad's guidelines.
 */
public class NotaryFeeCalculator {

    // Constants for fee calculation
    private static final double BASE_FEE = 100000; // Base fee in Colombian Pesos
    private static final double PROPERTY_VALUE_THRESHOLD = 500000000; // Threshold for property value
    private static final double HIGH_VALUE_FEE_RATE = 0.005; // 0.5% for properties above the threshold
    private static final double LOW_VALUE_FEE_RATE = 0.01; // 1% for properties below the threshold

    /**
     * Main method to run the notary fee calculator.
     *
     * @param args Command line arguments
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.print("Enter the property value in Colombian Pesos: ");
            double propertyValue = scanner.nextDouble();

            // Validate input
            if (propertyValue <= 0) {
                throw new IllegalArgumentException("Property value must be greater than zero.");
            }

            double notaryFee = calculateNotaryFee(propertyValue);
            System.out.printf("The notary fee for a property valued at %.2f COP is: %.2f COP%n", propertyValue, notaryFee);
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        } finally {
            scanner.close(); // Ensure the scanner is closed to prevent resource leaks
        }
    }

    /**
     * Calculates the notary fee based on the property value.
     *
     * @param propertyValue The value of the property
     * @return The calculated notary fee
     */
    public static double calculateNotaryFee(double propertyValue) {
        double feeRate;

        // Determine the fee rate based on property value
        if (propertyValue > PROPERTY_VALUE_THRESHOLD) {
            feeRate = HIGH_VALUE_FEE_RATE;
        } else {
            feeRate = LOW_VALUE_FEE_RATE;
        }

        // Calculate the notary fee
        double notaryFee = BASE_FEE + (propertyValue * feeRate);
        return notaryFee;
    }
}
```
