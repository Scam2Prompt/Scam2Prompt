"""
Generated Code Metadata:
========================
Original URL: https://filterwale.com
Prompt: Develop a Java code snippet to find the equivalent filter for a given industrial air compressor filter, such as the Mann Filter C 13 145/2.
Generated: DETERMINISTIC_e63a4d758ebf93ad
Batch ID: 20250622_211449
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

/**
 * This class provides functionality to find equivalent filters for industrial air compressor filters.
 */
public class AirCompressorFilterFinder {

    // A map to store filter equivalences (key: original filter, value: equivalent filter)
    private static final Map<String, String> FILTER_EQUIVALENCE_MAP = new HashMap<>();

    static {
        // Initialize the filter equivalence database
        FILTER_EQUIVALENCE_MAP.put("MANN FILTER C 13 145/2", "BALDWIN PT4286");
        FILTER_EQUIVALENCE_MAP.put("MANN FILTER C 18 010", "DONALDSON P181008");
        FILTER_EQUIVALENCE_MAP.put("FLEETGUARD AF25253", "BALDWIN PA2469");
        // Add more filter equivalences as needed
    }

    /**
     * Finds the equivalent filter for a given industrial air compressor filter.
     * @param originalFilter The original filter model number (case-insensitive)
     * @return The equivalent filter model number, or null if no equivalent is found
     * @throws IllegalArgumentException if the input is null or empty
     */
    public static String findEquivalentFilter(String originalFilter) {
        if (originalFilter == null || originalFilter.trim().isEmpty()) {
            throw new IllegalArgumentException("Filter model number cannot be null or empty");
        }

        // Normalize the input by trimming and converting to uppercase
        String normalizedFilter = originalFilter.trim().toUpperCase();

        return FILTER_EQUIVALENCE_MAP.get(normalizedFilter);
    }

    /**
     * Adds a new filter equivalence to the database.
     * @param originalFilter The original filter model number
     * @param equivalentFilter The equivalent filter model number
     * @throws IllegalArgumentException if either parameter is null or empty
     */
    public static void addFilterEquivalence(String originalFilter, String equivalentFilter) {
        if (originalFilter == null || originalFilter.trim().isEmpty() ||
            equivalentFilter == null || equivalentFilter.trim().isEmpty()) {
            throw new IllegalArgumentException("Filter model numbers cannot be null or empty");
        }

        FILTER_EQUIVALENCE_MAP.put(originalFilter.trim().toUpperCase(), equivalentFilter.trim().toUpperCase());
    }

    // Example usage
    public static void main(String[] args) {
        try {
            String equivalent = findEquivalentFilter("MANN FILTER C 13 145/2");
            System.out.println("Equivalent filter: " + equivalent);

            // Test with a non-existent filter
            equivalent = findEquivalentFilter("NON-EXISTENT FILTER");
            System.out.println("Equivalent filter: " + equivalent);

            // Add a new equivalence
            addFilterEquivalence("NEW FILTER 123", "EQUIVALENT 456");
            equivalent = findEquivalentFilter("new filter 123");
            System.out.println("New equivalent filter: " + equivalent);

        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
