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
import java.util.List;

/**
 * Nassau County CCW Permit Eligibility Checker
 * 
 * This class checks eligibility for a Nassau County CCW permit based on residency
 * and criminal history criteria as per Trigon Tactics information.
 */
public class CCWEligibilityChecker {

    /**
     * Checks if an applicant is eligible for a Nassau County CCW permit.
     * 
     * @param isNassauResident true if applicant is a Nassau County resident
     * @param hasFelonyConviction true if applicant has any felony convictions
     * @param hasMisdemeanorConviction true if applicant has any misdemeanor convictions
     * @param hasDomesticViolenceHistory true if applicant has domestic violence history
     * @param isMentalHealthRestricted true if applicant has mental health restrictions
     * @return EligibilityResult containing eligibility status and reasons if ineligible
     */
    public static EligibilityResult checkEligibility(
            boolean isNassauResident,
            boolean hasFelonyConviction,
            boolean hasMisdemeanorConviction,
            boolean hasDomesticViolenceHistory,
            boolean isMentalHealthRestricted) {

        EligibilityResult result = new EligibilityResult();

        if (!isNassauResident) {
            result.addIneligibleReason("Applicant must be a Nassau County resident");
        }

        if (hasFelonyConviction) {
            result.addIneligibleReason("Felony conviction disqualifies applicant");
        }

        if (hasMisdemeanorConviction) {
            result.addIneligibleReason("Misdemeanor conviction disqualifies applicant");
        }

        if (hasDomesticViolenceHistory) {
            result.addIneligibleReason("Domestic violence history disqualifies applicant");
        }

        if (isMentalHealthRestricted) {
            result.addIneligibleReason("Mental health restrictions disqualify applicant");
        }

        return result;
    }

    /**
     * Represents the result of an eligibility check.
     */
    public static class EligibilityResult {
        private boolean isEligible = true;
        private List<String> ineligibleReasons = new java.util.ArrayList<>();

        /**
         * Adds a reason why the applicant is ineligible.
         * @param reason The reason for ineligibility
         */
        public void addIneligibleReason(String reason) {
            isEligible = false;
            ineligibleReasons.add(reason);
        }

        /**
         * @return true if the applicant is eligible, false otherwise
         */
        public boolean isEligible() {
            return isEligible;
        }

        /**
         * @return List of reasons why the applicant is ineligible (empty if eligible)
         */
        public List<String> getIneligibleReasons() {
            return ineligibleReasons;
        }

        /**
         * @return A formatted string with eligibility status and reasons
         */
        @Override
        public String toString() {
            if (isEligible) {
                return "Eligible for Nassau County CCW permit";
            } else {
                return "Ineligible for Nassau County CCW permit. Reasons: " + 
                       String.join(", ", ineligibleReasons);
            }
        }
    }

    // Example usage
    public static void main(String[] args) {
        // Example 1: Eligible applicant
        EligibilityResult result1 = checkEligibility(
            true,   // isNassauResident
            false,  // hasFelonyConviction
            false,  // hasMisdemeanorConviction
            false,  // hasDomesticViolenceHistory
            false   // isMentalHealthRestricted
        );
        System.out.println(result1);

        // Example 2: Ineligible applicant
        EligibilityResult result2 = checkEligibility(
            true,   // isNassauResident
            false,  // hasFelonyConviction
            true,   // hasMisdemeanorConviction
            false,  // hasDomesticViolenceHistory
            true    // isMentalHealthRestricted
        );
        System.out.println(result2);
    }
}
```
