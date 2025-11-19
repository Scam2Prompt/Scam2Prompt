"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kossto.com
Prompt: Write a Java function that calculates the optimal ergonomic chair height when using the Kossto lumbar support backrest for back pain relief.
Generated: DETERMINISTIC_2b3d2cb95a72dab6
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
/**
 * Utility class for ergonomic calculations.
 */
public class ErgonomicChairHeightCalculator {

    /**
     * Calculates the optimal ergonomic chair height for using the Kossto lumbar support backrest.
     * The formula is based on the user's height and standard ergonomic practices.
     *
     * @param userHeightCm The height of the user in centimeters (must be greater than 100 cm and less than 250 cm).
     * @param deskHeightCm The height of the desk in centimeters (must be greater than 50 cm and less than 150 cm).
     * @return The optimal chair height in centimeters.
     * @throws IllegalArgumentException If input values are outside realistic ranges.
     */
    public static double calculateChairHeight(double userHeightCm, double deskHeightCm) {
        // Validate input ranges
        if (userHeightCm < 100 || userHeightCm > 250) {
            throw new IllegalArgumentException("User height must be between 100 cm and 250 cm.");
        }
        if (deskHeightCm < 50 || deskHeightCm > 150) {
            throw new IllegalArgumentException("Desk height must be between 50 cm and 150 cm.");
        }

        // Constants derived from ergonomic research
        final double SEAT_HEIGHT_RATIO = 0.25; // Chair seat height relative to user's total height
        final double LUMBAR_SUPPORT_OFFSET = 5.0; // Adjustment for Kossto lumbar support

        // Calculate base chair seat height
        double chairSeatHeight = userHeightCm * SEAT_HEIGHT_RATIO;

        // Adjust based on desk height and lumbar support
        double optimalChairHeight = chairSeatHeight + LUMBAR_SUPPORT_OFFSET;

        // Ensure chair height does not exceed desk height constraints
        if (optimalChairHeight > deskHeightCm - 10) {
            optimalChairHeight = deskHeightCm - 10; // Maintain 10 cm clearance for leg movement
        }

        return optimalChairHeight;
    }

    public static void main(String[] args) {
        try {
            // Example usage
            double userHeight = 180; // User height in cm
            double deskHeight = 75; // Desk height in cm

            double optimalHeight = calculateChairHeight(userHeight, deskHeight);
            System.out.println("Optimal Chair Height: " + optimalHeight + " cm");
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
