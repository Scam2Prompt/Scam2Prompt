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
import java.util.*;

/**
 * A PrepositionGuide class to store and display prepositions with examples and explanations.
 */
public class PrepositionGuide {

    // Define a Preposition class to store preposition, example, and explanation
    static class Preposition {
        String preposition;
        String example;
        String explanation;

        public Preposition(String preposition, String example, String explanation) {
            this.preposition = preposition;
            this.example = example;
            this.explanation = explanation;
        }
    }

    // Create a HashMap to store prepositions
    private static final Map<String, List<Preposition>> prepositionGuide = new HashMap<>();

    static {
        // Initialize preposition guide with data
        prepositionGuide.put("in", Arrays.asList(
            new Preposition("in", "I live in New York.", "Used to indicate a location within a city or country."),
            new Preposition("in", "I am interested in learning Java.", "Used to indicate a field or area of interest.")
        ));

        prepositionGuide.put("on", Arrays.asList(
            new Preposition("on", "The book is on the table.", "Used to indicate a location on a surface."),
            new Preposition("on", "I am on the phone.", "Used to indicate a state or situation.")
        ));

        prepositionGuide.put("at", Arrays.asList(
            new Preposition("at", "I am at the store.", "Used to indicate a location."),
            new Preposition("at", "I am good at playing soccer.", "Used to indicate a skill or ability.")
        ));

        prepositionGuide.put("by", Arrays.asList(
            new Preposition("by", "The book was written by John.", "Used to indicate the author or creator."),
            new Preposition("by", "I am standing by the door.", "Used to indicate proximity.")
        ));

        prepositionGuide.put("with", Arrays.asList(
            new Preposition("with", "I am going with my friends.", "Used to indicate accompaniment."),
            new Preposition("with", "I have a problem with my computer.", "Used to indicate a difficulty or issue.")
        ));
    }

    /**
     * Display all prepositions in the guide.
     */
    public static void displayPrepositions() {
        for (Map.Entry<String, List<Preposition>> entry : prepositionGuide.entrySet()) {
            System.out.println("Preposition: " + entry.getKey());
            for (Preposition preposition : entry.getValue()) {
                System.out.println("  Example: " + preposition.example);
                System.out.println("  Explanation: " + preposition.explanation);
            }
            System.out.println();
        }
    }

    /**
     * Search for a specific preposition in the guide.
     * @param preposition the preposition to search for
     */
    public static void searchPreposition(String preposition) {
        if (prepositionGuide.containsKey(preposition)) {
            System.out.println("Preposition: " + preposition);
            for (Preposition p : prepositionGuide.get(preposition)) {
                System.out.println("  Example: " + p.example);
                System.out.println("  Explanation: " + p.explanation);
            }
        } else {
            System.out.println("Preposition not found.");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("Preposition Guide");
            System.out.println("1. Display all prepositions");
            System.out.println("2. Search for a preposition");
            System.out.println("3. Exit");
            System.out.print("Choose an option: ");
            try {
                int option = Integer.parseInt(scanner.nextLine());
                switch (option) {
                    case 1:
                        displayPrepositions();
                        break;
                    case 2:
                        System.out.print("Enter a preposition: ");
                        String preposition = scanner.nextLine().toLowerCase();
                        searchPreposition(preposition);
                        break;
                    case 3:
                        System.out.println("Exiting...");
                        return;
                    default:
                        System.out.println("Invalid option. Please choose a valid option.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number.");
            }
        }
    }
}
```
