"""
Generated Code Metadata:
========================
Original URL: https://netsecurity.pages.dev
Prompt: "Generate a Java code snippet to parse TLS client extensions, such as 'tlsClientExtensionsSha1' and 'tlsClientExtensionsSha1Le', and determine their relevance in bot management."
Generated: DETERMINISTIC_709fec56d6026699
Batch ID: 20250622_211646
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
 * A utility class to parse and analyze TLS client extensions for bot management.
 */
public class TlsClientExtensionsParser {

    /**
     * Parses TLS client extensions and determines their relevance in bot management.
     *
     * @param extensions A map of extension names to their values (e.g., SHA-1 hashes).
     * @return A map indicating the relevance of each extension for bot management.
     * @throws IllegalArgumentException if the input map is null or empty.
     */
    public static Map<String, Boolean> analyzeExtensions(Map<String, String> extensions) {
        // Validate input
        if (extensions == null || extensions.isEmpty()) {
            throw new IllegalArgumentException("Extensions map cannot be null or empty.");
        }

        // Map to store the relevance of each extension
        Map<String, Boolean> relevanceMap = new HashMap<>();

        // Iterate through the extensions and determine relevance
        for (Map.Entry<String, String> entry : extensions.entrySet()) {
            String extensionName = entry.getKey();
            String extensionValue = entry.getValue();

            // Check for specific extensions and determine their relevance
            if ("tlsClientExtensionsSha1".equalsIgnoreCase(extensionName)) {
                // Example logic: SHA-1 is considered weak and may indicate bot-like behavior
                relevanceMap.put(extensionName, isWeakHash(extensionValue));
            } else if ("tlsClientExtensionsSha1Le".equalsIgnoreCase(extensionName)) {
                // Example logic: Check if the extension value matches a known bot pattern
                relevanceMap.put(extensionName, matchesBotPattern(extensionValue));
            } else {
                // For other extensions, mark as not relevant (default behavior)
                relevanceMap.put(extensionName, false);
            }
        }

        return relevanceMap;
    }

    /**
     * Determines if a given hash value is considered weak (e.g., SHA-1).
     *
     * @param hashValue The hash value to evaluate.
     * @return True if the hash is weak, false otherwise.
     */
    private static boolean isWeakHash(String hashValue) {
        // Example logic: Check if the hash value is non-null and matches a weak hash pattern
        return hashValue != null && hashValue.length() == 40; // SHA-1 hashes are 40 characters long
    }

    /**
     * Checks if a given extension value matches a known bot pattern.
     *
     * @param extensionValue The extension value to evaluate.
     * @return True if the value matches a bot pattern, false otherwise.
     */
    private static boolean matchesBotPattern(String extensionValue) {
        // Example logic: Check for specific patterns that indicate bot behavior
        return extensionValue != null && extensionValue.startsWith("bot_");
    }

    /**
     * Main method for testing the TLS client extensions parser.
     *
     * @param args Command-line arguments (not used).
     */
    public static void main(String[] args) {
        // Example input: TLS client extensions
        Map<String, String> extensions = new HashMap<>();
        extensions.put("tlsClientExtensionsSha1", "1234567890abcdef1234567890abcdef12345678");
        extensions.put("tlsClientExtensionsSha1Le", "bot_abcdef1234567890");
        extensions.put("otherExtension", "someValue");

        // Analyze the extensions
        try {
            Map<String, Boolean> relevance = analyzeExtensions(extensions);

            // Print the results
            relevance.forEach((key, value) -> {
                System.out.println("Extension: " + key + ", Relevant: " + value);
            });
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
