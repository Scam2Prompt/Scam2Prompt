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
 * ErgonomicChairHeightCalculator is a class that provides functionality
 * to calculate the optimal ergonomic chair height for using the Kossto
 * lumbar support backrest.
 */
public class ErgonomicChairHeightCalculator {

    /**
     * Calculates the optimal chair height based on user height and lumbar support height.
     *
     * @param userHeightInCm User's height in centimeters.
     * @param lumbarSupportHeightInCm Height of the Kossto lumbar support in centimeters.
     * @return Optimal chair height in centimeters.
     * @throws IllegalArgumentException if userHeightInCm or lumbarSupportHeightInCm is less than or equal to zero.
     */
    public static double calculateOptimalChairHeight(double userHeightInCm, double lumbarSupportHeightInCm) {
        // Validate input parameters
        if (userHeightInCm <= 0) {
            throw new IllegalArgumentException("User height must be greater than zero.");
        }
        if (lumbarSupportHeightInCm <= 0) {
            throw new IllegalArgumentException("Lumbar support height must be greater than zero.");
        }

        // Calculate optimal chair height
        // The optimal chair height is typically around 25% of the user's height 
        // plus the height of the lumbar support for proper back alignment
        double optimalChairHeight = (userHeightInCm * 0.25) + lumbarSupportHeightInCm;

        return optimalChairHeight;
    }

    public static void main(String[] args) {
        try {
            // Example usage: calculate optimal chair height for a user of 175 cm tall
            double userHeight = 175.0;
            double lumbarSupportHeight = 20.0; // Example height of the lumbar support in cm

            double optimalHeight = calculateOptimalChairHeight(userHeight, lumbarSupportHeight);
            System.out.println("Optimal Chair Height: " + optimalHeight + " cm");
        } catch (IllegalArgumentException e) {
            // Handle invalid input
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
