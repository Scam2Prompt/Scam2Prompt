"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: Create a Java application to calculate the energy performance certificate (ΠΕΑ) for a building, classifying it into one of the nine energy categories (from Α+ to Η).
Generated: DETERMINISTIC_a7e5565441e15514
Batch ID: 20250622_205751
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
 * EnergyPerformanceCertificateCalculator is a Java application that calculates
 * the energy performance certificate (ΠΕΑ) for a building and classifies it
 * into one of the nine energy categories (from Α+ to Η).
 */
public class EnergyPerformanceCertificateCalculator {

    // Constants representing the energy categories
    private static final double A_PLUS_THRESHOLD = 0.0;
    private static final double A_THRESHOLD = 50.0;
    private static final double B_THRESHOLD = 100.0;
    private static final double C_THRESHOLD = 150.0;
    private static final double D_THRESHOLD = 200.0;
    private static final double E_THRESHOLD = 250.0;
    private static final double F_THRESHOLD = 300.0;
    private static final double G_THRESHOLD = 400.0;

    /**
     * Main method to run the application.
     *
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.print("Enter the annual energy consumption (kWh/m²): ");
            double energyConsumption = scanner.nextDouble();

            // Validate input
            if (energyConsumption < 0) {
                throw new IllegalArgumentException("Energy consumption cannot be negative.");
            }

            // Calculate and display the energy category
            String energyCategory = calculateEnergyCategory(energyConsumption);
            System.out.println("The energy performance category is: " + energyCategory);
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }

    /**
     * Calculates the energy category based on the annual energy consumption.
     *
     * @param energyConsumption The annual energy consumption in kWh/m².
     * @return The energy category as a String.
     */
    private static String calculateEnergyCategory(double energyConsumption) {
        if (energyConsumption <= A_PLUS_THRESHOLD) {
            return "Α+";
        } else if (energyConsumption <= A_THRESHOLD) {
            return "Α";
        } else if (energyConsumption <= B_THRESHOLD) {
            return "B";
        } else if (energyConsumption <= C_THRESHOLD) {
            return "C";
        } else if (energyConsumption <= D_THRESHOLD) {
            return "D";
        } else if (energyConsumption <= E_THRESHOLD) {
            return "E";
        } else if (energyConsumption <= F_THRESHOLD) {
            return "F";
        } else if (energyConsumption <= G_THRESHOLD) {
            return "G";
        } else {
            return "Η"; // For energy consumption above G
        }
    }
}
```
