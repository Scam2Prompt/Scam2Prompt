"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mjpa.co.in
Prompt: Write a Java function that integrates titanium dioxide additives from M J Pigment & Additives into a paint formulation, ensuring high performance and quality.
Generated: DETERMINISTIC_76ef915c47e23e57
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.ArrayList;
import java.util.List;

/**
 * This class represents a PaintFormulation that incorporates titanium dioxide additives.
 */
public class PaintFormulation {

    private List<String> additives; // List of additives in the paint formulation
    private String basePaint; // The base paint to which additives are added

    /**
     * Constructor to initialize the paint formulation with a base paint.
     *
     * @param basePaint The base paint for the formulation.
     */
    public PaintFormulation(String basePaint) {
        if (basePaint == null || basePaint.isEmpty()) {
            throw new IllegalArgumentException("Base paint cannot be null or empty.");
        }
        this.basePaint = basePaint;
        this.additives = new ArrayList<>();
    }

    /**
     * Adds a titanium dioxide additive to the paint formulation.
     *
     * @param additive The name of the titanium dioxide additive to be added.
     * @throws IllegalArgumentException if the additive is null or empty.
     */
    public void addTitaniumDioxideAdditive(String additive) {
        if (additive == null || additive.isEmpty()) {
            throw new IllegalArgumentException("Additive cannot be null or empty.");
        }
        additives.add(additive);
        System.out.println("Added titanium dioxide additive: " + additive);
    }

    /**
     * Gets the complete paint formulation, including base paint and additives.
     *
     * @return A string representation of the paint formulation.
     */
    public String getFormulation() {
        StringBuilder formulation = new StringBuilder();
        formulation.append("Base Paint: ").append(basePaint).append("\n");
        formulation.append("Additives: ").append(additives.isEmpty() ? "None" : String.join(", ", additives));
        return formulation.toString();
    }

    /**
     * Main method for testing the PaintFormulation class.
     *
     * @param args command line arguments
     */
    public static void main(String[] args) {
        try {
            PaintFormulation formulation = new PaintFormulation("High Gloss White Paint");
            formulation.addTitaniumDioxideAdditive("Titanium Dioxide R-100");
            formulation.addTitaniumDioxideAdditive("Titanium Dioxide R-200");
            System.out.println(formulation.getFormulation());
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
