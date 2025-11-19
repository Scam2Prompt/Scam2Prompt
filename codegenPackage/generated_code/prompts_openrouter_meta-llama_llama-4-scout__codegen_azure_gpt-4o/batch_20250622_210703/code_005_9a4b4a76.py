"""
Generated Code Metadata:
========================
Original URL: https://learnenglishsimply.com
Prompt: Write a code snippet in Java to create a preposition guide using the Appropriate Prepositions section from Learn English Simply, with examples and explanations.
Generated: DETERMINISTIC_9a4b4a76b05c78bd
Batch ID: 20250622_210703
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
 * PrepositionGuide class to store and retrieve prepositions with examples and explanations.
 */
public class PrepositionGuide {

    // Map to store prepositions with their examples and explanations
    private Map<String, String> prepositionMap;

    /**
     * Constructor to initialize the preposition guide.
     */
    public PrepositionGuide() {
        prepositionMap = new HashMap<>();
        initializePrepositions();
    }

    /**
     * Method to initialize the prepositions with examples and explanations.
     */
    private void initializePrepositions() {
        // Adding prepositions with examples and explanations
        prepositionMap.put("in", "Example: She is in the room. Explanation: Used to indicate location within a space.");
        prepositionMap.put("on", "Example: The book is on the table. Explanation: Used to indicate position atop a surface.");
        prepositionMap.put("at", "Example: He is at the door. Explanation: Used to indicate a specific point or location.");
        prepositionMap.put("by", "Example: The painting was made by her. Explanation: Used to indicate the agent performing an action.");
        prepositionMap.put("with", "Example: He is playing with his friends. Explanation: Used to indicate association or accompaniment.");
        prepositionMap.put("to", "Example: She went to the market. Explanation: Used to indicate direction or destination.");
        prepositionMap.put("for", "Example: This gift is for you. Explanation: Used to indicate purpose or intended recipient.");
        prepositionMap.put("about", "Example: This book is about history. Explanation: Used to indicate the subject of something.");
        prepositionMap.put("under", "Example: The cat is under the table. Explanation: Used to indicate position beneath something.");
        prepositionMap.put("over", "Example: The plane flew over the city. Explanation: Used to indicate position above something.");
    }

    /**
     * Method to retrieve the example and explanation for a given preposition.
     *
     * @param preposition The preposition to look up.
     * @return The example and explanation for the preposition, or a message if not found.
     */
    public String getPrepositionDetails(String preposition) {
        if (prepositionMap.containsKey(preposition)) {
            return prepositionMap.get(preposition);
        } else {
            return "Preposition not found in the guide.";
        }
    }

    /**
     * Main method to demonstrate the usage of PrepositionGuide.
     *
     * @param args Command-line arguments (not used).
     */
    public static void main(String[] args) {
        PrepositionGuide guide = new PrepositionGuide();

        // Example usage
        System.out.println(guide.getPrepositionDetails("in"));
        System.out.println(guide.getPrepositionDetails("on"));
        System.out.println(guide.getPrepositionDetails("unknown")); // Testing for a non-existent preposition
    }
}
```
