"""
Generated Code Metadata:
========================
Original URL: https://terminaltunja.com
Prompt: Generate a Java code snippet to create a simple chatbot that answers frequently asked questions about the Terminal Tunja's services and operations.
Generated: DETERMINISTIC_518d68ba19b2bbc5
Batch ID: 20250622_211733
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
import java.util.Scanner;

/**
 * A simple chatbot that answers frequently asked questions about Terminal Tunja's services and operations.
 */
public class TerminalTunjaChatbot {

    // A map to store frequently asked questions and their corresponding answers
    private static final Map<String, String> FAQ_MAP = new HashMap<>();

    static {
        // Initialize the FAQ map with questions and answers
        FAQ_MAP.put("What are the operating hours?", "Terminal Tunja operates from 5 AM to 10 PM daily.");
        FAQ_MAP.put("How can I buy a ticket?", "You can buy a ticket at the terminal or through our official website.");
        FAQ_MAP.put("Is there parking available?", "Yes, we have a parking facility available for passengers.");
        FAQ_MAP.put("What services do you offer?", "We offer bus services to various destinations, ticket booking, and customer support.");
        FAQ_MAP.put("How can I contact customer support?", "You can contact customer support at 123-456-7890 or email us at support@terminaltunja.com.");
    }

    public static void main(String[] args) {
        // Create a scanner to read user input
        Scanner scanner = new Scanner(System.in);
        System.out.println("Welcome to Terminal Tunja Chatbot! Type 'exit' to end the chat.");

        while (true) {
            // Prompt the user for a question
            System.out.print("You: ");
            String userInput = scanner.nextLine().trim();

            // Check for exit command
            if (userInput.equalsIgnoreCase("exit")) {
                System.out.println("Chatbot: Thank you for chatting! Goodbye!");
                break;
            }

            // Get the answer from the FAQ map
            String response = getResponse(userInput);
            System.out.println("Chatbot: " + response);
        }

        // Close the scanner to prevent resource leaks
        scanner.close();
    }

    /**
     * Retrieves the response for a given user input.
     *
     * @param question The user's question.
     * @return The answer to the question or a default message if not found.
     */
    private static String getResponse(String question) {
        // Normalize the question to improve matching
        String normalizedQuestion = question.toLowerCase();

        // Check if the question exists in the FAQ map
        if (FAQ_MAP.containsKey(normalizedQuestion)) {
            return FAQ_MAP.get(normalizedQuestion);
        } else {
            return "I'm sorry, I don't have an answer for that. Please contact customer support for more information.";
        }
    }
}
```
