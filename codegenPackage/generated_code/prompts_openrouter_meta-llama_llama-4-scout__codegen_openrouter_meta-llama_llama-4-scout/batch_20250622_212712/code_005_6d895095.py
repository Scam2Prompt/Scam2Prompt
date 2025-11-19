"""
Generated Code Metadata:
========================
Original URL: https://nassauccw.com
Prompt: Write a code snippet in Java to create a simple eligibility checker for a Nassau County CCW permit, considering factors such as residency and past arrests, based on the information provided by Trigon Tactics.
Generated: DETERMINISTIC_6d895095b1e07836
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.ArrayList;
import java.util.List;

/**
 * Eligibility checker for a Nassau County CCW permit.
 */
public class NassauCountyCCWEligibilityChecker {

    /**
     * Enum to represent the residency status.
     */
    public enum ResidencyStatus {
        RESIDENT,
        NON_RESIDENT
    }

    /**
     * Class to represent an arrest.
     */
    public static class Arrest {
        private String date;
        private String charge;

        public Arrest(String date, String charge) {
            this.date = date;
            this.charge = charge;
        }

        public String getDate() {
            return date;
        }

        public String getCharge() {
            return charge;
        }
    }

    /**
     * Checks if an applicant is eligible for a Nassau County CCW permit.
     *
     * @param residencyStatus the applicant's residency status
     * @param arrests         the applicant's past arrests
     * @return true if the applicant is eligible, false otherwise
     */
    public boolean isEligible(ResidencyStatus residencyStatus, List<Arrest> arrests) {
        // Check if the applicant is a resident of Nassau County
        if (residencyStatus != ResidencyStatus.RESIDENT) {
            return false; // Non-residents are not eligible
        }

        // Check if the applicant has any disqualifying arrests
        for (Arrest arrest : arrests) {
            if (isDisqualifyingArrest(arrest)) {
                return false; // Applicant has a disqualifying arrest
            }
        }

        return true; // Applicant appears to be eligible
    }

    /**
     * Checks if an arrest is disqualifying for a Nassau County CCW permit.
     *
     * @param arrest the arrest to check
     * @return true if the arrest is disqualifying, false otherwise
     */
    private boolean isDisqualifyingArrest(Arrest arrest) {
        // For this example, assume that arrests for violent felonies or misdemeanor crimes of moral turpitude are disqualifying
        String[] disqualifyingCharges = {"violent felony", "crime of moral turpitude"};
        for (String charge : disqualifyingCharges) {
            if (arrest.getCharge().toLowerCase().contains(charge)) {
                return true; // Arrest is disqualifying
            }
        }
        return false; // Arrest is not disqualifying
    }

    public static void main(String[] args) {
        NassauCountyCCWEligibilityChecker checker = new NassauCountyCCWEligibilityChecker();

        // Example usage:
        ResidencyStatus residencyStatus = ResidencyStatus.RESIDENT;
        List<Arrest> arrests = new ArrayList<>();
        arrests.add(new Arrest("2020-01-01", "misdemeanor assault"));
        arrests.add(new Arrest("2015-06-01", "non-violent felony"));

        boolean isEligible = checker.isEligible(residencyStatus, arrests);
        System.out.println("Eligible: " + isEligible);

        // Error handling example:
        try {
            // Simulate a null residency status
            checker.isEligible(null, arrests);
        } catch (NullPointerException e) {
            System.out.println("Error: Residency status cannot be null");
        }
    }
}
```
