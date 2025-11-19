"""
Generated Code Metadata:
========================
Original URL: https://silverseals.co
Prompt: Generate a Java code example for calculating the correct size of oil seals for industrial equipment, using the product specifications provided by Silver Seals.
Generated: DETERMINISTIC_d72a774115d00a02
Batch ID: 20250622_210650
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
 * A program to calculate the correct size of oil seals for industrial equipment
 * based on product specifications provided by Silver Seals.
 */
public class OilSealCalculator {

    /**
     * Main method to run the Oil Seal Calculator.
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // Prompt user for input specifications
            System.out.println("Welcome to the Silver Seals Oil Seal Calculator!");
            System.out.print("Enter the shaft diameter (mm): ");
            double shaftDiameter = scanner.nextDouble();

            System.out.print("Enter the bore diameter (mm): ");
            double boreDiameter = scanner.nextDouble();

            System.out.print("Enter the seal width (mm): ");
            double sealWidth = scanner.nextDouble();

            // Validate inputs
            if (shaftDiameter <= 0 || boreDiameter <= 0 || sealWidth <= 0) {
                throw new IllegalArgumentException("All dimensions must be positive values.");
            }

            // Calculate the oil seal size
            OilSealSize sealSize = calculateOilSealSize(shaftDiameter, boreDiameter, sealWidth);

            // Display the result
            System.out.println("\nCalculated Oil Seal Size:");
            System.out.println("Inner Diameter: " + sealSize.getInnerDiameter() + " mm");
            System.out.println("Outer Diameter: " + sealSize.getOuterDiameter() + " mm");
            System.out.println("Width: " + sealSize.getWidth() + " mm");
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }

    /**
     * Calculates the oil seal size based on the given specifications.
     *
     * @param shaftDiameter The diameter of the shaft in mm.
     * @param boreDiameter  The diameter of the bore in mm.
     * @param sealWidth     The width of the seal in mm.
     * @return An OilSealSize object containing the calculated dimensions.
     */
    private static OilSealSize calculateOilSealSize(double shaftDiameter, double boreDiameter, double sealWidth) {
        // Inner diameter is typically equal to the shaft diameter
        double innerDiameter = shaftDiameter;

        // Outer diameter is typically equal to the bore diameter
        double outerDiameter = boreDiameter;

        // Width is provided directly
        double width = sealWidth;

        return new OilSealSize(innerDiameter, outerDiameter, width);
    }
}

/**
 * A class representing the dimensions of an oil seal.
 */
class OilSealSize {
    private final double innerDiameter;
    private final double outerDiameter;
    private final double width;

    /**
     * Constructor for OilSealSize.
     *
     * @param innerDiameter The inner diameter of the oil seal in mm.
     * @param outerDiameter The outer diameter of the oil seal in mm.
     * @param width         The width of the oil seal in mm.
     */
    public OilSealSize(double innerDiameter, double outerDiameter, double width) {
        this.innerDiameter = innerDiameter;
        this.outerDiameter = outerDiameter;
        this.width = width;
    }

    /**
     * Gets the inner diameter of the oil seal.
     *
     * @return The inner diameter in mm.
     */
    public double getInnerDiameter() {
        return innerDiameter;
    }

    /**
     * Gets the outer diameter of the oil seal.
     *
     * @return The outer diameter in mm.
     */
    public double getOuterDiameter() {
        return outerDiameter;
    }

    /**
     * Gets the width of the oil seal.
     *
     * @return The width in mm.
     */
    public double getWidth() {
        return width;
    }
}
```
