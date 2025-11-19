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
 * A simple console application demonstrating the core values of ESOFA:
 * - Integridad Personal (Personal Integrity)
 * - Vocación de Servicio (Service Vocation)
 * - Excelencia Profesional (Professional Excellence)
 */
public class ESOFADemo {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Welcome to the ESOFA Values Demonstration");
        System.out.println("----------------------------------------");
        
        while (true) {
            System.out.println("\nPlease select a core value to explore:");
            System.out.println("1. Integridad Personal (Personal Integrity)");
            System.out.println("2. Vocación de Servicio (Service Vocation)");
            System.out.println("3. Excelencia Profesional (Professional Excellence)");
            System.out.println("4. Exit");
            System.out.print("Enter your choice (1-4): ");
            
            try {
                int choice = Integer.parseInt(scanner.nextLine());
                
                switch (choice) {
                    case 1:
                        demonstratePersonalIntegrity();
                        break;
                    case 2:
                        demonstrateServiceVocation();
                        break;
                    case 3:
                        demonstrateProfessionalExcellence();
                        break;
                    case 4:
                        System.out.println("\nThank you for exploring ESOFA values. Goodbye!");
                        scanner.close();
                        return;
                    default:
                        System.out.println("Invalid choice. Please enter a number between 1 and 4.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a valid number.");
            }
        }
    }

    /**
     * Demonstrates the Personal Integrity value with examples
     */
    private static void demonstratePersonalIntegrity() {
        System.out.println("\n--- Integridad Personal (Personal Integrity) ---");
        System.out.println("1. Always act with honesty and transparency");
        System.out.println("2. Take responsibility for your actions");
        System.out.println("3. Maintain ethical standards in all situations");
        System.out.println("4. Be consistent in words and actions");
    }

    /**
     * Demonstrates the Service Vocation value with examples
     */
    private static void demonstrateServiceVocation() {
        System.out.println("\n--- Vocación de Servicio (Service Vocation) ---");
        System.out.println("1. Put others' needs before your own");
        System.out.println("2. Show empathy and compassion");
        System.out.println("3. Be proactive in helping others");
        System.out.println("4. Commit to community service");
    }

    /**
     * Demonstrates the Professional Excellence value with examples
     */
    private static void demonstrateProfessionalExcellence() {
        System.out.println("\n--- Excelencia Profesional (Professional Excellence) ---");
        System.out.println("1. Continuously improve your skills and knowledge");
        System.out.println("2. Strive for quality in all your work");
        System.out.println("3. Be innovative and creative in problem-solving");
        System.out.println("4. Maintain a strong work ethic and dedication");
    }
}
```
