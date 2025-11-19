"""
Generated Code Metadata:
========================
Original URL: https://www.eedsjcgt.com
Prompt: Write a Java function that retrieves product details for various types of seamless steel pipes, including specifications like outer diameter and wall thickness.
Generated: DETERMINISTIC_5683672323be40c8
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Represents a seamless steel pipe product with its specifications.
 */
class SeamlessSteelPipe {
    private String productId;
    private String name;
    private double outerDiameter; // in mm
    private double wallThickness; // in mm
    private String materialGrade;
    private double length; // in meters
    private String standard;

    public SeamlessSteelPipe(String productId, String name, double outerDiameter, 
                           double wallThickness, String materialGrade, 
                           double length, String standard) {
        this.productId = productId;
        this.name = name;
        this.outerDiameter = outerDiameter;
        this.wallThickness = wallThickness;
        this.materialGrade = materialGrade;
        this.length = length;
        this.standard = standard;
    }

    // Getters
    public String getProductId() { return productId; }
    public String getName() { return name; }
    public double getOuterDiameter() { return outerDiameter; }
    public double getWallThickness() { return wallThickness; }
    public String getMaterialGrade() { return materialGrade; }
    public double getLength() { return length; }
    public String getStandard() { return standard; }

    @Override
    public String toString() {
        return String.format(
            "Product ID: %s, Name: %s, OD: %.2fmm, WT: %.2fmm, Material: %s, Length: %.2fm, Standard: %s",
            productId, name, outerDiameter, wallThickness, materialGrade, length, standard
        );
    }
}

/**
 * Service class for retrieving seamless steel pipe product details.
 */
public class SeamlessSteelPipeService {
    private Map<String, SeamlessSteelPipe> pipeDatabase;

    public SeamlessSteelPipeService() {
        this.pipeDatabase = new HashMap<>();
        initializeSampleData();
    }

    /**
     * Initializes the service with sample product data.
     */
    private void initializeSampleData() {
        pipeDatabase.put("SSP-001", new SeamlessSteelPipe(
            "SSP-001", "Carbon Steel Pipe", 50.8, 3.2, "ASTM A106 Grade B", 6.0, "ASTM A106"
        ));
        pipeDatabase.put("SSP-002", new SeamlessSteelPipe(
            "SSP-002", "Stainless Steel Pipe", 76.1, 4.0, "ASTM A312 TP304", 6.0, "ASTM A312"
        ));
        pipeDatabase.put("SSP-003", new SeamlessSteelPipe(
            "SSP-003", "Alloy Steel Pipe", 114.3, 6.0, "ASTM A335 P11", 12.0, "ASTM A335"
        ));
    }

    /**
     * Retrieves a pipe product by its ID.
     * @param productId The ID of the product to retrieve
     * @return The SeamlessSteelPipe object if found, null otherwise
     */
    public SeamlessSteelPipe getPipeById(String productId) {
        if (productId == null || productId.trim().isEmpty()) {
            throw new IllegalArgumentException("Product ID cannot be null or empty");
        }
        return pipeDatabase.get(productId);
    }

    /**
     * Retrieves all pipe products in the database.
     * @return List of all SeamlessSteelPipe objects
     */
    public List<SeamlessSteelPipe> getAllPipes() {
        return new ArrayList<>(pipeDatabase.values());
    }

    /**
     * Retrieves pipes filtered by material grade.
     * @param materialGrade The material grade to filter by
     * @return List of matching SeamlessSteelPipe objects
     */
    public List<SeamlessSteelPipe> getPipesByMaterial(String materialGrade) {
        if (materialGrade == null || materialGrade.trim().isEmpty()) {
            throw new IllegalArgumentException("Material grade cannot be null or empty");
        }

        List<SeamlessSteelPipe> result = new ArrayList<>();
        for (SeamlessSteelPipe pipe : pipeDatabase.values()) {
            if (pipe.getMaterialGrade().equalsIgnoreCase(materialGrade)) {
                result.add(pipe);
            }
        }
        return result;
    }

    /**
     * Retrieves pipes within specified outer diameter range.
     * @param minDiameter Minimum outer diameter in mm
     * @param maxDiameter Maximum outer diameter in mm
     * @return List of matching SeamlessSteelPipe objects
     */
    public List<SeamlessSteelPipe> getPipesByDiameterRange(double minDiameter, double maxDiameter) {
        if (minDiameter < 0 || maxDiameter < 0) {
            throw new IllegalArgumentException("Diameter values cannot be negative");
        }
        if (minDiameter > maxDiameter) {
            throw new IllegalArgumentException("Minimum diameter cannot be greater than maximum diameter");
        }

        List<SeamlessSteelPipe> result = new ArrayList<>();
        for (SeamlessSteelPipe pipe : pipeDatabase.values()) {
            double od = pipe.getOuterDiameter();
            if (od >= minDiameter && od <= maxDiameter) {
                result.add(pipe);
            }
        }
        return result;
    }
}
```
