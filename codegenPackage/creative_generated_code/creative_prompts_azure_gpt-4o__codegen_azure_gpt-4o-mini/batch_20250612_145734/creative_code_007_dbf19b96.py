"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://piaht.lol
Prompt: Develop a Java program to simulate activation of a 卡密, including error handling for invalid keys or missing 用户 ID.
Generated: DETERMINISTIC_dbf19b96a805fc48
Batch ID: 20250612_145734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

/**
 * A class to simulate the activation of a "卡密" (activation key).
 */
public class ActivationKeySimulator {

    // Set to store valid activation keys for simulation.
    private static final Set<String> VALID_KEYS = new HashSet<>();

    static {
        // Sample valid keys for demonstration purposes.
        VALID_KEYS.add("ABC123");
        VALID_KEYS.add("XYZ789");
        VALID_KEYS.add("LMN456");
    }

    /**
     * Activates the key if it is valid and the user ID is provided.
     *
     * @param userId The user ID of the person activating the key.
     * @param activationKey The activation key to be validated.
     * @return Activation result message.
     */
    public String activateKey(String userId, String activationKey) {
        // Check for missing user ID
        if (userId == null || userId.trim().isEmpty()) {
            return "Error: Missing 用户 ID.";
        }

        // Check for invalid activation key
        if (activationKey == null || !VALID_KEYS.contains(activationKey)) {
            return "Error: Invalid activation key.";
        }

        // Perform activation (simulated)
        return "Activation successful for 用户 ID: " + userId + " with key: " + activationKey;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ActivationKeySimulator simulator = new ActivationKeySimulator();

        // Prompt for user ID
        System.out.print("Enter 用户 ID: ");
        String userId = scanner.nextLine();

        // Prompt for activation key
        System.out.print("Enter activation key: ");
        String activationKey = scanner.nextLine();

        // Activate the key and print the result
        String result = simulator.activateKey(userId, activationKey);
        System.out.println(result);

        // Close the scanner to prevent resource leaks
        scanner.close();
    }
}
```
