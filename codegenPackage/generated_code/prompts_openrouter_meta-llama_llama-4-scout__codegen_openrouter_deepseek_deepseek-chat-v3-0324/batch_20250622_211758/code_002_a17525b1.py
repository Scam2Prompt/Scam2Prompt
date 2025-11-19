"""
Generated Code Metadata:
========================
Original URL: https://trattar.blogspot.com
Prompt: "Generate a Java code snippet to compare the mechanical properties of eucalyptus and pine wood, considering their density and resistance, as discussed on the Trattar Madeiras website."
Generated: DETERMINISTIC_a17525b1d31f77c6
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.Objects;

/**
 * This class represents the mechanical properties of a wood type.
 * It includes properties such as density and resistance.
 */
class WoodProperties {
    private final String woodType;
    private final double density; // in kg/m³
    private final double resistance; // in MPa

    /**
     * Constructor for WoodProperties.
     *
     * @param woodType   The type of wood (e.g., "Eucalyptus", "Pine")
     * @param density    The density of the wood in kg/m³
     * @param resistance The resistance of the wood in MPa
     * @throws IllegalArgumentException if woodType is null or empty, or if density/resistance is negative
     */
    public WoodProperties(String woodType, double density, double resistance) {
        if (woodType == null || woodType.trim().isEmpty()) {
            throw new IllegalArgumentException("Wood type cannot be null or empty");
        }
        if (density < 0 || resistance < 0) {
            throw new IllegalArgumentException("Density and resistance must be non-negative");
        }

        this.woodType = woodType;
        this.density = density;
        this.resistance = resistance;
    }

    public String getWoodType() {
        return woodType;
    }

    public double getDensity() {
        return density;
    }

    public double getResistance() {
        return resistance;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        WoodProperties that = (WoodProperties) o;
        return Double.compare(that.density, density) == 0 &&
                Double.compare(that.resistance, resistance) == 0 &&
                woodType.equals(that.woodType);
    }

    @Override
    public int hashCode() {
        return Objects.hash(woodType, density, resistance);
    }

    @Override
    public String toString() {
        return String.format("WoodProperties{woodType='%s', density=%.2f kg/m³, resistance=%.2f MPa}",
                woodType, density, resistance);
    }
}

/**
 * This class compares the mechanical properties of two wood types.
 */
public class WoodPropertiesComparator {

    /**
     * Compares two WoodProperties objects and prints the comparison results.
     *
     * @param wood1 The first wood properties to compare
     * @param wood2 The second wood properties to compare
     * @throws IllegalArgumentException if either wood1 or wood2 is null
     */
    public static void compareWoods(WoodProperties wood1, WoodProperties wood2) {
        if (wood1 == null || wood2 == null) {
            throw new IllegalArgumentException("Wood properties cannot be null");
        }

        System.out.println("Comparing wood properties:");
        System.out.println("1. " + wood1);
        System.out.println("2. " + wood2);

        System.out.println("\nComparison Results:");
        compareProperty("Density", wood1.getDensity(), wood2.getDensity());
        compareProperty("Resistance", wood1.getResistance(), wood2.getResistance());
    }

    private static void compareProperty(String propertyName, double value1, double value2) {
        System.out.printf("%s: %.2f vs %.2f", propertyName, value1, value2);
        if (value1 > value2) {
            System.out.printf(" - %s is higher by %.2f%n", propertyName, value1 - value2);
        } else if (value2 > value1) {
            System.out.printf(" - %s is higher by %.2f%n", propertyName, value2 - value1);
        } else {
            System.out.println(" - Both are equal");
        }
    }

    public static void main(String[] args) {
        try {
            // Example data based on typical values (actual values should be sourced from Trattar Madeiras)
            WoodProperties eucalyptus = new WoodProperties("Eucalyptus", 650.0, 85.0);
            WoodProperties pine = new WoodProperties("Pine", 500.0, 60.0);

            compareWoods(eucalyptus, pine);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
