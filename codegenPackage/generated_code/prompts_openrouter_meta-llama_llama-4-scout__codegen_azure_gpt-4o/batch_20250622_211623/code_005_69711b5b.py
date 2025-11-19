"""
Generated Code Metadata:
========================
Original URL: https://l2lusty.site
Prompt: "Write a Java program to calculate enchant chances for items on L2Lusty, given their enchant rates and safety limits."
Generated: DETERMINISTIC_69711b5be27c1a43
Batch ID: 20250622_211623
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
 * A program to calculate enchant chances for items in L2Lusty.
 * Users provide enchant rates and safety limits, and the program calculates
 * the success probability for each enchant level.
 */
public class EnchantCalculator {

    public static void main(String[] args) {
        // Initialize Scanner for user input
        Scanner scanner = new Scanner(System.in);

        try {
            // Prompt user for enchant rate
            System.out.print("Enter the enchant rate (as a percentage, e.g., 70 for 70%): ");
            double enchantRate = scanner.nextDouble();

            // Validate enchant rate input
            if (enchantRate < 0 || enchantRate > 100) {
                System.out.println("Error: Enchant rate must be between 0 and 100.");
                return;
            }

            // Prompt user for safety limit
            System.out.print("Enter the safety limit (e.g., 3 for safe enchants up to +3): ");
            int safetyLimit = scanner.nextInt();

            // Validate safety limit input
            if (safetyLimit < 0) {
                System.out.println("Error: Safety limit must be a non-negative integer.");
                return;
            }

            // Prompt user for maximum enchant level
            System.out.print("Enter the maximum enchant level (e.g., 10 for +10): ");
            int maxEnchantLevel = scanner.nextInt();

            // Validate maximum enchant level input
            if (maxEnchantLevel <= 0) {
                System.out.println("Error: Maximum enchant level must be a positive integer.");
                return;
            }

            // Display enchant chances for each level
            System.out.println("\nEnchant Chances:");
            for (int level = 1; level <= maxEnchantLevel; level++) {
                if (level <= safetyLimit) {
                    System.out.printf("+%d: Guaranteed success (within safety limit)%n", level);
                } else {
                    double successChance = enchantRate / 100.0;
                    System.out.printf("+%d: %.2f%% chance of success%n", level, successChance * 100);
                }
            }
        } catch (Exception e) {
            // Handle invalid input
            System.out.println("Error: Invalid input. Please enter valid numbers.");
        } finally {
            // Close the scanner to prevent resource leaks
            scanner.close();
        }
    }
}
```
