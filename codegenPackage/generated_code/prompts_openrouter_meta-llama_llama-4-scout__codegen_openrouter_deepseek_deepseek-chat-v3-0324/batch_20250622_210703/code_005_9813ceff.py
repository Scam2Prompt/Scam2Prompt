"""
Generated Code Metadata:
========================
Original URL: https://azalearesidence.com
Prompt: Write a code snippet in Java to calculate mortgage payments for properties in Jakarta, taking into account the location and features of Azalea Residence.
Generated: DETERMINISTIC_9813ceffbcce9dba
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.HashMap;
import java.util.Map;

/**
 * Calculates mortgage payments for properties in Jakarta, with special considerations
 * for Azalea Residence features.
 */
public class MortgageCalculator {

    // Location-based adjustment factors for Jakarta areas
    private static final Map<String, Double> LOCATION_FACTORS = new HashMap<>();
    static {
        LOCATION_FACTORS.put("Central Jakarta", 1.15);
        LOCATION_FACTORS.put("South Jakarta", 1.10);
        LOCATION_FACTORS.put("West Jakarta", 1.05);
        LOCATION_FACTORS.put("East Jakarta", 1.03);
        LOCATION_FACTORS.put("North Jakarta", 1.00);
    }

    // Azalea Residence premium features multiplier
    private static final double AZALEA_PREMIUM = 1.08;

    /**
     * Calculates monthly mortgage payment using standard formula with location adjustments.
     * 
     * @param principal Loan amount in IDR
     * @param annualRate Annual interest rate (e.g., 0.08 for 8%)
     * @param years Loan term in years
     * @param location Property location in Jakarta
     * @param isAzaleaResidence Whether property is in Azalea Residence
     * @return Monthly payment amount in IDR
     * @throws IllegalArgumentException if input parameters are invalid
     */
    public static BigDecimal calculateMonthlyPayment(
            BigDecimal principal,
            double annualRate,
            int years,
            String location,
            boolean isAzaleaResidence) {

        // Validate input parameters
        if (principal.compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("Principal must be positive");
        }
        if (annualRate <= 0 || annualRate > 1) {
            throw new IllegalArgumentException("Annual rate must be between 0 and 1");
        }
        if (years <= 0) {
            throw new IllegalArgumentException("Loan term must be positive");
        }
        if (!LOCATION_FACTORS.containsKey(location)) {
            throw new IllegalArgumentException("Invalid Jakarta location");
        }

        // Calculate base monthly payment
        double monthlyRate = annualRate / 12;
        int numberOfPayments = years * 12;
        
        double factor = (monthlyRate * Math.pow(1 + monthlyRate, numberOfPayments)) / 
                        (Math.pow(1 + monthlyRate, numberOfPayments) - 1);
        
        BigDecimal monthlyPayment = principal.multiply(BigDecimal.valueOf(factor));

        // Apply location adjustment
        double locationFactor = LOCATION_FACTORS.get(location);
        monthlyPayment = monthlyPayment.multiply(BigDecimal.valueOf(locationFactor));

        // Apply Azalea Residence premium if applicable
        if (isAzaleaResidence) {
            monthlyPayment = monthlyPayment.multiply(BigDecimal.valueOf(AZALEA_PREMIUM));
        }

        // Round to nearest rupiah (no decimal places)
        return monthlyPayment.setScale(0, RoundingMode.HALF_UP);
    }

    public static void main(String[] args) {
        try {
            BigDecimal principal = new BigDecimal("1000000000"); // 1 billion IDR
            double rate = 0.08; // 8% annual rate
            int term = 15; // 15 years
            
            BigDecimal payment = calculateMonthlyPayment(
                principal, rate, term, "South Jakarta", true);
            
            System.out.println("Monthly mortgage payment: IDR " + payment);
        } catch (IllegalArgumentException e) {
            System.err.println("Error calculating mortgage: " + e.getMessage());
        }
    }
}
```
