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
 * This class is responsible for parsing TLS client extensions
 * and determining their relevance in bot management.
 */
public class TlsClientExtensionsParser {

    // Constants for TLS client extensions
    private static final String TLS_CLIENT_EXTENSIONS_SHA1 = "tlsClientExtensionsSha1";
    private static final String TLS_CLIENT_EXTENSIONS_SHA1_LE = "tlsClientExtensionsSha1Le";

    /**
     * Parses the provided TLS client extensions and evaluates their relevance.
     *
     * @param extensions A map containing TLS client extensions.
     * @return A map indicating the relevance of each extension for bot management.
     * @throws IllegalArgumentException if the extensions map is null.
     */
    public Map<String, Boolean> parseExtensions(Map<String, String> extensions) {
        if (extensions == null) {
            throw new IllegalArgumentException("Extensions map cannot be null.");
        }

        Map<String, Boolean> relevanceMap = new HashMap<>();

        // Check for SHA1 extension
        if (extensions.containsKey(TLS_CLIENT_EXTENSIONS_SHA1)) {
            relevanceMap.put(TLS_CLIENT_EXTENSIONS_SHA1, isRelevantForBotManagement(extensions.get(TLS_CLIENT_EXTENSIONS_SHA1)));
        }

        // Check for SHA1 LE extension
        if (extensions.containsKey(TLS_CLIENT_EXTENSIONS_SHA1_LE)) {
            relevanceMap.put(TLS_CLIENT_EXTENSIONS_SHA1_LE, isRelevantForBotManagement(extensions.get(TLS_CLIENT_EXTENSIONS_SHA1_LE)));
        }

        return relevanceMap;
    }

    /**
     * Determines if a given extension value is relevant for bot management.
     *
     * @param extensionValue The value of the extension to evaluate.
     * @return true if the extension is relevant for bot management, false otherwise.
     */
    private boolean isRelevantForBotManagement(String extensionValue) {
        // Placeholder logic for determining relevance
        // In a real scenario, this would involve more complex checks
        return extensionValue != null && !extensionValue.isEmpty();
    }

    public static void main(String[] args) {
        // Example usage
        TlsClientExtensionsParser parser = new TlsClientExtensionsParser();
        Map<String, String> extensions = new HashMap<>();
        extensions.put(TLS_CLIENT_EXTENSIONS_SHA1, "exampleValue1");
        extensions.put(TLS_CLIENT_EXTENSIONS_SHA1_LE, "exampleValue2");

        try {
            Map<String, Boolean> relevance = parser.parseExtensions(extensions);
            relevance.forEach((key, value) -> System.out.println(key + " is relevant: " + value));
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
