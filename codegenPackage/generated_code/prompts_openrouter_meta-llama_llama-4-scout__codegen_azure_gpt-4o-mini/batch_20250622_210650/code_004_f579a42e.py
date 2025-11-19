"""
Generated Code Metadata:
========================
Original URL: https://sevalcikolata.com
Prompt: Write a Java code snippet to create a simple chatbot for Seval Çikolata's customer support, using a knowledge base of frequently asked questions and product information.
Generated: DETERMINISTIC_f579a42e6186f64e
Batch ID: 20250622_210650
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
 * Simple Chatbot for Seval Çikolata Customer Support
 * This chatbot provides answers to frequently asked questions
 * and product information based on a predefined knowledge base.
 */
public class SevalChocolataChatbot {

    // Knowledge base for frequently asked questions
    private static final Map<String, String> knowledgeBase = new HashMap<>();

    static {
        // Populate the knowledge base with FAQs and product information
        knowledgeBase.put("What is Seval Çikolata?", "Seval Çikolata is a premium chocolate brand offering a variety of delicious chocolates.");
        knowledgeBase.put("Where can I buy Seval Çikolata?", "You can purchase Seval Çikolata products from our official website or authorized retailers.");
        knowledgeBase.put("What are the ingredients in your chocolates?", "Our chocolates are made from high-quality cocoa, sugar, milk, and natural flavorings.");
        knowledgeBase.put("Do you offer vegan options?", "Yes, we offer a selection of vegan chocolates made without any animal products.");
        knowledgeBase.put("What is your return policy?", "We accept returns within 30 days of purchase if the product is unopened and in its original packaging.");
    }

    public static void main(String[] args) {
        // Create a scanner for user input
        Scanner scanner = new Scanner(System.in);
        System.out.println("Welcome to Seval Çikolata Customer Support Chatbot!");
        System.out.println("Type 'exit' to end the chat.");

        // Main loop for the chatbot
        while (true) {
            System.out.print("You: ");
            String userInput = scanner.nextLine().trim();

            // Exit condition
            if (userInput.equalsIgnoreCase("exit")) {
                System.out.println("Chatbot: Thank you for chatting with us. Have a great day!");
                break;
            }

            // Get the response from the knowledge base
            String response = getResponse(userInput);
            System.out.println("Chatbot: " + response);
        }

        // Close the scanner resource
        scanner.close();
    }

    /**
     * Retrieves a response from the knowledge base based on user input.
     *
     * @param userInput The input provided by the user.
     * @return The response from the knowledge base or a default message if not found.
     */
    private static String getResponse(String userInput) {
        // Normalize the user input to lower case for case-insensitive matching
        String normalizedInput = userInput.toLowerCase();

        // Check if the input matches any key in the knowledge base
        for (String key : knowledgeBase.keySet()) {
            if (normalizedInput.contains(key.toLowerCase())) {
                return knowledgeBase.get(key);
            }
        }

        // Default response if no match is found
        return "I'm sorry, I don't have the information you're looking for. Please contact our support team for further assistance.";
    }
}
```
