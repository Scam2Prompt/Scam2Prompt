"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: "Generate a Java code snippet to implement a warranty system for car bearings, with a 4-year warranty period and conditions for replacement or refund."
Generated: DETERMINISTIC_86253dd146ee92d4
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.time.LocalDate;
import java.time.Period;

/**
 * Represents a warranty system for car bearings with conditions for replacement or refund.
 */
public class CarBearingWarranty {
    private static final int WARRANTY_PERIOD_YEARS = 4;
    private LocalDate purchaseDate;
    private String bearingModel;
    private boolean isInstalledByProfessional;

    /**
     * Constructor for CarBearingWarranty.
     * @param purchaseDate The date when the bearing was purchased
     * @param bearingModel The model of the bearing
     * @param isInstalledByProfessional Whether the bearing was installed by a professional
     */
    public CarBearingWarranty(LocalDate purchaseDate, String bearingModel, boolean isInstalledByProfessional) {
        if (purchaseDate == null) {
            throw new IllegalArgumentException("Purchase date cannot be null");
        }
        if (bearingModel == null || bearingModel.trim().isEmpty()) {
            throw new IllegalArgumentException("Bearing model cannot be null or empty");
        }
        
        this.purchaseDate = purchaseDate;
        this.bearingModel = bearingModel;
        this.isInstalledByProfessional = isInstalledByProfessional;
    }

    /**
     * Checks if the warranty is still valid.
     * @return true if the warranty is valid, false otherwise
     */
    public boolean isWarrantyValid() {
        LocalDate currentDate = LocalDate.now();
        Period period = Period.between(purchaseDate, currentDate);
        return period.getYears() < WARRANTY_PERIOD_YEARS;
    }

    /**
     * Determines the warranty claim outcome based on conditions.
     * @param isManufacturingDefect Whether the issue is a manufacturing defect
     * @param hasProofOfPurchase Whether the customer has proof of purchase
     * @return WarrantyOutcome enum representing the possible outcomes
     */
    public WarrantyOutcome processWarrantyClaim(boolean isManufacturingDefect, boolean hasProofOfPurchase) {
        if (!hasProofOfPurchase) {
            return WarrantyOutcome.CLAIM_DENIED_NO_PROOF;
        }

        if (!isWarrantyValid()) {
            return WarrantyOutcome.CLAIM_DENIED_EXPIRED;
        }

        if (!isManufacturingDefect) {
            return WarrantyOutcome.CLAIM_DENIED_NOT_DEFECT;
        }

        if (!isInstalledByProfessional) {
            return WarrantyOutcome.REFUND_ONLY;
        }

        return WarrantyOutcome.REPLACEMENT;
    }

    /**
     * Enum representing possible warranty claim outcomes.
     */
    public enum WarrantyOutcome {
        REPLACEMENT("Eligible for bearing replacement"),
        REFUND_ONLY("Eligible for refund only (not installed by professional)"),
        CLAIM_DENIED_NO_PROOF("Claim denied - no proof of purchase"),
        CLAIM_DENIED_EXPIRED("Claim denied - warranty period expired"),
        CLAIM_DENIED_NOT_DEFECT("Claim denied - not a manufacturing defect");

        private final String description;

        WarrantyOutcome(String description) {
            this.description = description;
        }

        public String getDescription() {
            return description;
        }
    }

    // Getters
    public LocalDate getPurchaseDate() {
        return purchaseDate;
    }

    public String getBearingModel() {
        return bearingModel;
    }

    public boolean isInstalledByProfessional() {
        return isInstalledByProfessional;
    }
}
```
