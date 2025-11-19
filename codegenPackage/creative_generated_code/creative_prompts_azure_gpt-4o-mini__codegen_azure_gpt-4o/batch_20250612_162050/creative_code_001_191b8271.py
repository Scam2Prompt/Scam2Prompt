"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://silverseals.co
Prompt: Generate a Java code snippet that demonstrates how to create a seal ring using the specifications provided by Silver Seals.
Generated: DETERMINISTIC_191b82712a47e6af
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.Objects;

/**
 * Represents a SealRing with specifications provided by Silver Seals.
 */
public class SealRing {

    private final double innerDiameter; // Inner diameter of the seal ring in millimeters
    private final double outerDiameter; // Outer diameter of the seal ring in millimeters
    private final double thickness;     // Thickness of the seal ring in millimeters
    private final String material;      // Material type of the seal ring
    private final String coating;       // Coating applied to the seal ring, if any

    /**
     * Constructs a SealRing instance with specified parameters.
     *
     * @param innerDiameter The inner diameter of the seal ring in millimeters
     * @param outerDiameter The outer diameter of the seal ring in millimeters
     * @param thickness The thickness of the seal ring in millimeters
     * @param material The material type of the seal ring
     * @param coating The coating applied to the seal ring (optional)
     * @throws IllegalArgumentException if any parameter is invalid
     */
    public SealRing(double innerDiameter, double outerDiameter, double thickness, String material, String coating) {
        if (innerDiameter <= 0 || outerDiameter <= 0 || thickness <= 0) {
            throw new IllegalArgumentException("Dimensions must be positive values.");
        }
        if (innerDiameter >= outerDiameter) {
            throw new IllegalArgumentException("Inner diameter must be smaller than outer diameter.");
        }
        if (material == null || material.trim().isEmpty()) {
            throw new IllegalArgumentException("Material must not be null or empty.");
        }

        this.innerDiameter = innerDiameter;
        this.outerDiameter = outerDiameter;
        this.thickness = thickness;
        this.material = material;
        this.coating = (coating != null && !coating.trim().isEmpty()) ? coating : "None";
    }

    /**
     * @return the inner diameter of the seal ring
     */
    public double getInnerDiameter() {
        return innerDiameter;
    }

    /**
     * @return the outer diameter of the seal ring
     */
    public double getOuterDiameter() {
        return outerDiameter;
    }

    /**
     * @return the thickness of the seal ring
     */
    public double getThickness() {
        return thickness;
    }

    /**
     * @return the material type of the seal ring
     */
    public String getMaterial() {
        return material;
    }

    /**
     * @return the coating applied to the seal ring
     */
    public String getCoating() {
        return coating;
    }

    @Override
    public String toString() {
        return "SealRing{" +
                "innerDiameter=" + innerDiameter +
                ", outerDiameter=" + outerDiameter +
                ", thickness=" + thickness +
                ", material='" + material + '\'' +
                ", coating='" + coating + '\'' +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        SealRing sealRing = (SealRing) o;
        return Double.compare(sealRing.innerDiameter, innerDiameter) == 0 &&
                Double.compare(sealRing.outerDiameter, outerDiameter) == 0 &&
                Double.compare(sealRing.thickness, thickness) == 0 &&
                Objects.equals(material, sealRing.material) &&
                Objects.equals(coating, sealRing.coating);
    }

    @Override
    public int hashCode() {
        return Objects.hash(innerDiameter, outerDiameter, thickness, material, coating);
    }

    /**
     * Main method to demonstrate the creation of a SealRing instance.
     */
    public static void main(String[] args) {
        try {
            SealRing sealRing = new SealRing(50.0, 100.0, 5.0, "Stainless Steel", "Nickel Coating");
            System.out.println(sealRing);
        } catch (IllegalArgumentException e) {
            System.err.println("Error creating SealRing: " + e.getMessage());
        }
    }
}
```
