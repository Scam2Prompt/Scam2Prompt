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
/**
 * Energy Performance Certificate (ΠΕΑ) Calculator for Buildings
 * 
 * This Java application calculates the energy performance certificate (ΠΕA) for a building,
 * classifying it into one of the nine energy categories (from Α+ to Η).
 * 
 * @author [Your Name]
 * @version 1.0
 */

import java.util.InputMismatchException;
import java.util.Scanner;

public class EnergyPerformanceCertificateCalculator {

    // Define energy categories
    private enum EnergyCategory {
        A_PLUS("Α+"),
        A("A"),
        B_PLUS("Β+"),
        B("B"),
        C("C"),
        D("D"),
        E("E"),
        F("F"),
        G("G"),
        H("H");

        private final String category;

        EnergyCategory(String category) {
            this.category = category;
        }

        public String getCategory() {
            return category;
        }
    }

    /**
     * Calculates the energy performance certificate (ΠΕΑ) for a building.
     * 
     * @param energyConsumption The energy consumption of the building in kWh/m²/year.
     * @return The energy category of the building.
     */
    public static EnergyCategory calculateEnergyCategory(double energyConsumption) {
        // Define energy consumption limits for each category (in kWh/m²/year)
        // These limits are indicative and may vary based on the country's regulations
        if (energyConsumption <= 0) {
            throw new IllegalArgumentException("Energy consumption must be a positive value.");
        } else if (energyConsumption <= 50) {
            return EnergyCategory.A_PLUS;
        } else if (energyConsumption <= 70) {
            return EnergyCategory.A;
        } else if (energyConsumption <= 100) {
            return EnergyCategory.B_PLUS;
        } else if (energyConsumption <= 130) {
            return EnergyCategory.B;
        } else if (energyConsumption <= 160) {
            return EnergyCategory.C;
        } else if (energyConsumption <= 200) {
            return EnergyCategory.D;
        } else if (energyConsumption <= 250) {
            return EnergyCategory.E;
        } else if (energyConsumption <= 300) {
            return EnergyCategory.F;
        } else if (energyConsumption <= 400) {
            return EnergyCategory.G;
        } else {
            return EnergyCategory.H;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Enter the energy consumption of the building (in kWh/m²/year): ");
            double energyConsumption = scanner.nextDouble();

            EnergyCategory energyCategory = calculateEnergyCategory(energyConsumption);

            System.out.println("The energy performance certificate (ΠΕΑ) category for the building is: " + energyCategory.getCategory());
        } catch (InputMismatchException e) {
            System.err.println("Invalid input. Please enter a valid number.");
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
        } finally {
            scanner.close();
        }
    }
}
```
