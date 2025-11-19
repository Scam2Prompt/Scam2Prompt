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
 * A preposition guide that provides examples and explanations for common English prepositions.
 */
public class PrepositionGuide {

    // Map to store prepositions with their examples and explanations
    private static final Map<String, PrepositionEntry> prepositionMap = new HashMap<>();

    /**
     * Entry class to store preposition details
     */
    private static class PrepositionEntry {
        String preposition;
        String example;
        String explanation;

        public PrepositionEntry(String preposition, String example, String explanation) {
            this.preposition = preposition;
            this.example = example;
            this.explanation = explanation;
        }
    }

    // Initialize the preposition guide with data
    static {
        prepositionMap.put("about", new PrepositionEntry("about", 
            "She was talking about her vacation.", 
            "Used to indicate the subject of discussion"));
        
        prepositionMap.put("above", new PrepositionEntry("above", 
            "The picture hangs above the fireplace.", 
            "Indicates a higher position or level"));
        
        prepositionMap.put("across", new PrepositionEntry("across", 
            "We walked across the bridge.", 
            "Indicates movement from one side to another"));
        
        prepositionMap.put("after", new PrepositionEntry("after", 
            "We'll meet after lunch.", 
            "Indicates time following an event"));
        
        prepositionMap.put("against", new PrepositionEntry("against", 
            "He leaned against the wall.", 
            "Indicates physical contact with a surface"));
        
        prepositionMap.put("among", new PrepositionEntry("among", 
            "She was standing among her friends.", 
            "Indicates being surrounded by or part of a group"));
        
        prepositionMap.put("at", new PrepositionEntry("at", 
            "We'll meet at the restaurant.", 
            "Indicates a specific location or time"));
        
        prepositionMap.put("before", new PrepositionEntry("before", 
            "Please arrive before 8 PM.", 
            "Indicates time preceding an event"));
        
        prepositionMap.put("behind", new PrepositionEntry("behind", 
            "The car was parked behind the building.", 
            "Indicates position at the back of something"));
        
        prepositionMap.put("between", new PrepositionEntry("between", 
            "The book is between the two bookends.", 
            "Indicates position in the middle of two things"));
    }

    /**
     * Gets the preposition entry for the given preposition
     * @param preposition The preposition to look up
     * @return PrepositionEntry containing details or null if not found
     */
    public static PrepositionEntry getPreposition(String preposition) {
        if (preposition == null || preposition.trim().isEmpty()) {
            throw new IllegalArgumentException("Preposition cannot be null or empty");
        }
        return prepositionMap.get(preposition.toLowerCase());
    }

    /**
     * Prints all available prepositions in the guide
     */
    public static void listAllPrepositions() {
        System.out.println("Available prepositions:");
        for (String prep : prepositionMap.keySet()) {
            System.out.println("- " + prep);
        }
    }

    /**
     * Prints details for a specific preposition
     * @param preposition The preposition to display
     */
    public static void displayPreposition(String preposition) {
        PrepositionEntry entry = getPreposition(preposition);
        if (entry == null) {
            System.out.println("Preposition '" + preposition + "' not found in the guide.");
            return;
        }

        System.out.println("Preposition: " + entry.preposition);
        System.out.println("Example: " + entry.example);
        System.out.println("Explanation: " + entry.explanation);
    }

    public static void main(String[] args) {
        // Example usage
        listAllPrepositions();
        System.out.println();
        displayPreposition("between");
        System.out.println();
        displayPreposition("nonexistent");
    }
}
```
