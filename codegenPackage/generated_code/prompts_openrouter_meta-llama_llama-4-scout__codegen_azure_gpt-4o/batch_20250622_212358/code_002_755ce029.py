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
 * A simple console application to demonstrate the core values of ESOFA:
 * Integridad Personal, Vocación de Servicio, and Excelencia Profesional.
 */
public class ESOFAValuesApp {

    public static void main(String[] args) {
        // Display a welcome message
        System.out.println("Welcome to the ESOFA Core Values Demonstration!");
        System.out.println("Please select a value to learn more about:");
        System.out.println("1. Integridad Personal");
        System.out.println("2. Vocación de Servicio");
        System.out.println("3. Excelencia Profesional");
        System.out.println("4. Exit");

        // Create a Scanner object for user input
        try (Scanner scanner = new Scanner(System.in)) {
            boolean running = true;

            while (running) {
                System.out.print("\nEnter your choice (1-4): ");
                int choice;

                // Validate user input
                if (scanner.hasNextInt()) {
                    choice = scanner.nextInt();
                } else {
                    System.out.println("Invalid input. Please enter a number between 1 and 4.");
                    scanner.next(); // Clear invalid input
                    continue;
                }

                // Handle user choice
                switch (choice) {
                    case 1:
                        displayIntegridadPersonal();
                        break;
                    case 2:
                        displayVocacionDeServicio();
                        break;
                    case 3:
                        displayExcelenciaProfesional();
                        break;
                    case 4:
                        System.out.println("Thank you for exploring ESOFA values. Goodbye!");
                        running = false;
                        break;
                    default:
                        System.out.println("Invalid choice. Please select a number between 1 and 4.");
                }
            }
        } catch (Exception e) {
            // Handle unexpected errors
            System.err.println("An error occurred: " + e.getMessage());
        }
    }

    /**
     * Displays information about Integridad Personal.
     */
    private static void displayIntegridadPersonal() {
        System.out.println("\nIntegridad Personal:");
        System.out.println("Acting with honesty, ethics, and transparency in all aspects of life.");
    }

    /**
     * Displays information about Vocación de Servicio.
     */
    private static void displayVocacionDeServicio() {
        System.out.println("\nVocación de Servicio:");
        System.out.println("Demonstrating a commitment to helping others and contributing to the community.");
    }

    /**
     * Displays information about Excelencia Profesional.
     */
    private static void displayExcelenciaProfesional() {
        System.out.println("\nExcelencia Profesional:");
        System.out.println("Striving for the highest standards of quality and professionalism in all endeavors.");
    }
}
```
