"""
Generated Code Metadata:
========================
Original URL: https://esofa.edu.pe
Prompt: Generate a code snippet in Java to create a simple console application that demonstrates the core values of ESOFA (Integridad Personal, Vocación de Servicio, and Excelencia Profesional).
Generated: DETERMINISTIC_755ce029c3ba422d
Batch ID: 20250622_212358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.Scanner;

/**
 * A simple console application that demonstrates the core values of ESOFA:
 * Integridad Personal, Vocación de Servicio, and Excelencia Profesional.
 */
public class ESOFAValuesApp {

    // Main method to run the application
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        try {
            // Display the core values
            displayCoreValues();

            // Prompt user for their personal reflection on each value
            for (String value : new String[]{"Integridad Personal", "Vocación de Servicio", "Excelencia Profesional"}) {
                System.out.print("Please share your thoughts on " + value + ": ");
                String reflection = scanner.nextLine();
                System.out.println("Thank you for sharing your thoughts on " + value + ": " + reflection);
            }
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        } finally {
            // Close the scanner to prevent resource leaks
            scanner.close();
        }
    }

    /**
     * Displays the core values of ESOFA.
     */
    private static void displayCoreValues() {
        System.out.println("Core Values of ESOFA:");
        System.out.println("1. Integridad Personal: Upholding personal integrity in all actions.");
        System.out.println("2. Vocación de Servicio: A commitment to serving others with dedication.");
        System.out.println("3. Excelencia Profesional: Striving for excellence in professional endeavors.");
        System.out.println();
    }
}
```
