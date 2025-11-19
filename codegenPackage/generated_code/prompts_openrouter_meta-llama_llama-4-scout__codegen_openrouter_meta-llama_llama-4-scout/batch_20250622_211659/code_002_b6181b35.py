"""
Generated Code Metadata:
========================
Original URL: https://popcorn.claims
Prompt: "Write a code snippet in Java to create a simple claims calculator that adheres to a specific set of privacy and data protection policies."
Generated: DETERMINISTIC_b6181b356d942997
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * A simple claims calculator that adheres to a specific set of privacy and data protection policies.
 * 
 * @author [Your Name]
 * @version 1.0
 */

// Define a custom exception for invalid claim data
class InvalidClaimDataException extends Exception {
    public InvalidClaimDataException(String message) {
        super(message);
    }
}

public class ClaimsCalculator {

    // Define a Claim class to hold claim data
    static class Claim {
        private String claimantName;
        private double claimAmount;
        private String claimType;

        public Claim(String claimantName, double claimAmount, String claimType) {
            this.claimantName = claimantName;
            this.claimAmount = claimAmount;
            this.claimType = claimType;
        }

        // Getters and setters
        public String getClaimantName() { return claimantName; }
        public double getClaimAmount() { return claimAmount; }
        public String getClaimType() { return claimType; }
    }

    /**
     * Calculates the claim amount based on the claim type and amount.
     * 
     * @param claim The claim data
     * @return The calculated claim amount
     * @throws InvalidClaimDataException If the claim data is invalid
     */
    public static double calculateClaim(Claim claim) throws InvalidClaimDataException {
        // Validate claim data
        if (claim.getClaimantName() == null || claim.getClaimantName().isEmpty()) {
            throw new InvalidClaimDataException("Claimant name is required");
        }
        if (claim.getClaimAmount() <= 0) {
            throw new InvalidClaimDataException("Claim amount must be greater than zero");
        }
        if (claim.getClaimType() == null || claim.getClaimType().isEmpty()) {
            throw new InvalidClaimDataException("Claim type is required");
        }

        // Define claim type multipliers
        java.util.HashMap<String, Double> claimTypeMultipliers = new java.util.HashMap<>();
        claimTypeMultipliers.put("theft", 1.0);
        claimTypeMultipliers.put("damage", 0.5);
        claimTypeMultipliers.put("loss", 0.75);

        // Calculate claim amount
        double calculatedClaimAmount = claim.getClaimAmount();
        if (claimTypeMultipliers.containsKey(claim.getClaimType().toLowerCase())) {
            calculatedClaimAmount *= claimTypeMultipliers.get(claim.getClaimType().toLowerCase());
        } else {
            throw new InvalidClaimDataException("Unsupported claim type");
        }

        return calculatedClaimAmount;
    }

    public static void main(String[] args) {
        try {
            // Create a new claim
            Claim claim = new Claim("John Doe", 1000.0, "theft");

            // Calculate the claim amount
            double calculatedClaimAmount = calculateClaim(claim);

            // Print the result
            System.out.println("Calculated claim amount: " + calculatedClaimAmount);
        } catch (InvalidClaimDataException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
