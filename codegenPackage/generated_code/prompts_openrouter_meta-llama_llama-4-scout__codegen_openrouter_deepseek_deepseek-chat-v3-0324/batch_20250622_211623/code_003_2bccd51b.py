"""
Generated Code Metadata:
========================
Original URL: https://labelmystuff.com
Prompt: Design a labeling system for a scouts group to identify their equipment and personal belongings, and provide a sample code snippet in Java to generate the labels.
Generated: DETERMINISTIC_2bccd51be09f413e
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

/**
 * A labeling system for a scouts group to identify their equipment and personal belongings.
 * This class generates labels with customizable information.
 */
public class ScoutsLabelingSystem {

    /**
     * Represents a label with customizable fields.
     */
    public static class Label {
        private final String scoutName;
        private final String itemName;
        private final String troopNumber;
        private final String contactInfo;

        /**
         * Constructs a new Label.
         *
         * @param scoutName   The name of the scout (cannot be null or empty).
         * @param itemName    The name of the item (cannot be null or empty).
         * @param troopNumber The troop number (can be null or empty).
         * @param contactInfo Contact information (can be null or empty).
         * @throws IllegalArgumentException if scoutName or itemName is null or empty.
         */
        public Label(String scoutName, String itemName, String troopNumber, String contactInfo) {
            if (scoutName == null || scoutName.trim().isEmpty()) {
                throw new IllegalArgumentException("Scout name cannot be null or empty");
            }
            if (itemName == null || itemName.trim().isEmpty()) {
                throw new IllegalArgumentException("Item name cannot be null or empty");
            }

            this.scoutName = scoutName.trim();
            this.itemName = itemName.trim();
            this.troopNumber = troopNumber != null ? troopNumber.trim() : "";
            this.contactInfo = contactInfo != null ? contactInfo.trim() : "";
        }

        /**
         * Generates a formatted label string.
         *
         * @return The formatted label.
         */
        public String generateLabel() {
            StringBuilder label = new StringBuilder();
            label.append("Scout: ").append(scoutName).append("\n");
            label.append("Item: ").append(itemName).append("\n");

            if (!troopNumber.isEmpty()) {
                label.append("Troop: ").append(troopNumber).append("\n");
            }

            if (!contactInfo.isEmpty()) {
                label.append("Contact: ").append(contactInfo).append("\n");
            }

            return label.toString();
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Label label = (Label) o;
            return scoutName.equals(label.scoutName) &&
                    itemName.equals(label.itemName) &&
                    Objects.equals(troopNumber, label.troopNumber) &&
                    Objects.equals(contactInfo, label.contactInfo);
        }

        @Override
        public int hashCode() {
            return Objects.hash(scoutName, itemName, troopNumber, contactInfo);
        }
    }

    /**
     * Generates a batch of labels from a map of scout names to item names.
     *
     * @param itemsMap      Map of scout names to item names (cannot be null).
     * @param troopNumber   The troop number (can be null or empty).
     * @param contactInfo   Contact information (can be null or empty).
     * @return A map of scout names to their generated labels.
     * @throws IllegalArgumentException if itemsMap is null or contains invalid entries.
     */
    public static Map<String, String> generateLabels(
            Map<String, String> itemsMap,
            String troopNumber,
            String contactInfo) {

        if (itemsMap == null) {
            throw new IllegalArgumentException("Items map cannot be null");
        }

        Map<String, String> labels = new HashMap<>();
        for (Map.Entry<String, String> entry : itemsMap.entrySet()) {
            Label label = new Label(entry.getKey(), entry.getValue(), troopNumber, contactInfo);
            labels.put(entry.getKey(), label.generateLabel());
        }

        return labels;
    }

    // Example usage
    public static void main(String[] args) {
        Map<String, String> items = new HashMap<>();
        items.put("John Doe", "Backpack");
        items.put("Jane Smith", "Sleeping Bag");

        String troopNumber = "Troop 123";
        String contactInfo = "jane.smith@example.com";

        try {
            Map<String, String> labels = generateLabels(items, troopNumber, contactInfo);
            labels.forEach((scout, label) -> {
                System.out.println("Label for " + scout + ":");
                System.out.println(label);
            });
        } catch (IllegalArgumentException e) {
            System.err.println("Error generating labels: " + e.getMessage());
        }
    }
}
```
