"""
Generated Code Metadata:
========================
Original URL: https://l2lusty.site
Prompt: Provide code to simulate the enchantment process on the L2Lusty server, incorporating the enchant rates (50% for +3 to +16) and B.Enchant rates (60% for +3 to +16).
Generated: DETERMINISTIC_445f2b3df4990c6d
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.Random;

/**
 * Simulates the enchantment process on the L2Lusty server.
 */
public class EnchantmentSimulator {

    // Enchant rates for +3 to +16
    private static final double ENCHANT_RATE = 0.5;

    // B.Enchant rates for +3 to +16
    private static final double B_ENCHANT_RATE = 0.6;

    // Maximum enchant level
    private static final int MAX_ENCHANT_LEVEL = 16;

    // Minimum enchant level
    private static final int MIN_ENCHANT_LEVEL = 3;

    private Random random;

    public EnchantmentSimulator() {
        this.random = new Random();
    }

    /**
     * Simulates the enchantment process.
     *
     * @param currentLevel the current enchant level
     * @param useBEnchant  whether to use B.Enchant
     * @return the new enchant level
     */
    public int simulateEnchantment(int currentLevel, boolean useBEnchant) {
        if (currentLevel < MIN_ENCHANT_LEVEL) {
            throw new IllegalArgumentException("Current level must be " + MIN_ENCHANT_LEVEL + " or higher");
        }

        if (currentLevel >= MAX_ENCHANT_LEVEL) {
            throw new IllegalArgumentException("Current level cannot exceed " + MAX_ENCHANT_LEVEL);
        }

        double enchantRate = useBEnchant ? B_ENCHANT_RATE : ENCHANT_RATE;

        // Generate a random number between 0 and 1
        double roll = random.nextDouble();

        // Check if enchantment is successful
        if (roll < enchantRate) {
            // Enchantment successful, increase level
            return currentLevel + 1;
        } else {
            // Enchantment failed, level remains the same
            return currentLevel;
        }
    }

    public static void main(String[] args) {
        EnchantmentSimulator simulator = new EnchantmentSimulator();

        int currentLevel = 10;
        boolean useBEnchant = true;

        for (int i = 0; i < 10; i++) {
            int newLevel = simulator.simulateEnchantment(currentLevel, useBEnchant);
            System.out.println("Enchantment attempt " + (i + 1) + ": Level " + currentLevel + " -> " + newLevel);
            currentLevel = newLevel;

            if (currentLevel >= MAX_ENCHANT_LEVEL) {
                System.out.println("Maximum enchant level reached!");
                break;
            }
        }
    }
}
```
