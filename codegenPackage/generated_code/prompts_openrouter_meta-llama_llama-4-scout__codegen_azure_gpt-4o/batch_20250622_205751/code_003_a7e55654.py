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
 * EnergyPerformanceCertificateCalculator
 * This application calculates the energy performance certificate (ΠΕΑ) for a building
 * and classifies it into one of the nine energy categories (from Α+ to Η).
 */
public class EnergyPerformanceCertificateCalculator {

    // Enum to represent energy categories
    public enum EnergyCategory {
        A_PLUS("Α+"),
        A("Α"),
        B_PLUS("Β+"),
        B("Β"),
        C("C"),
        D("D"),
        E("E"),
        Z("Ζ"),
        H("Η");

        private final String label;

        EnergyCategory(String label) {
            this.label = label;
        }

        @Override
        public String toString() {
            return label;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.println("Welcome to the Energy Performance Certificate Calculator!");
            System.out.print("Enter the building's energy consumption (kWh/m²/year): ");

            // Read energy consumption input
            double energyConsumption = scanner.nextDouble();

            // Validate input
            if (energyConsumption < 0) {
                System.out.println("Error: Energy consumption cannot be negative.");
                return;
            }

            // Determine energy category
            EnergyCategory category = classifyEnergyCategory(energyConsumption);

            // Display result
            System.out.println("The building's energy category is: " + category);
        } catch (Exception e) {
            System.out.println("Error: Invalid input. Please enter a valid numeric value.");
        } finally {
            scanner.close();
        }
    }

    /**
     * Classifies the building into an energy category based on its energy consumption.
     *
     * @param energyConsumption The energy consumption in kWh/m²/year.
     * @return The corresponding energy category.
     */
    private static EnergyCategory classifyEnergyCategory(double energyConsumption) {
        if (energyConsumption <= 30) {
            return EnergyCategory.A_PLUS;
        } else if (energyConsumption <= 60) {
            return EnergyCategory.A;
        } else if (energyConsumption <= 90) {
            return EnergyCategory.B_PLUS;
        } else if (energyConsumption <= 120) {
            return EnergyCategory.B;
        } else if (energyConsumption <= 150) {
            return EnergyCategory.C;
        } else if (energyConsumption <= 180) {
            return EnergyCategory.D;
        } else if (energyConsumption <= 210) {
            return EnergyCategory.E;
        } else if (energyConsumption <= 240) {
            return EnergyCategory.Z;
        } else {
            return EnergyCategory.H;
        }
    }
}
```
