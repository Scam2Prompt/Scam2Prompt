"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Generate a Java code snippet that simulates the evaluation process for MBA program applicants at SOMTU based on their CGPA and educational background.
Generated: DETERMINISTIC_9f2388ab95ffa70d
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * Evaluates MBA program applicants at SOMTU based on their CGPA and educational background.
 */

public class MBAApplicantEvaluator {

    // Enum for educational background
    public enum EducationalBackground {
        BACHELORS,
        MASTERS,
        PHD,
        OTHER
    }

    /**
     * Evaluates an MBA applicant based on their CGPA and educational background.
     * 
     * @param cgpa            the applicant's CGPA
     * @param educationalBackground the applicant's educational background
     * @return a string indicating the evaluation result
     */
    public static String evaluateApplicant(double cgpa, EducationalBackground educationalBackground) {
        // Define CGPA thresholds for different educational backgrounds
        double cgpaThreshold = getCgpaThreshold(educationalBackground);

        // Check if the applicant's CGPA meets the threshold
        if (cgpa >= cgpaThreshold) {
            return "Applicant is eligible for the MBA program.";
        } else {
            return "Applicant is not eligible for the MBA program.";
        }
    }

    /**
     * Gets the CGPA threshold for a given educational background.
     * 
     * @param educationalBackground the educational background
     * @return the CGPA threshold
     */
    private static double getCgpaThreshold(EducationalBackground educationalBackground) {
        switch (educationalBackground) {
            case BACHELORS:
                return 3.0;
            case MASTERS:
                return 3.2;
            case PHD:
                return 3.5;
            default:
                return 3.0; // Default threshold for other backgrounds
        }
    }

    public static void main(String[] args) {
        try {
            // Example usage
            double cgpa = 3.5;
            EducationalBackground educationalBackground = EducationalBackground.BACHELORS;
            String evaluationResult = evaluateApplicant(cgpa, educationalBackground);
            System.out.println("Evaluation Result: " + evaluationResult);

            // Test cases
            testEvaluateApplicant(3.0, EducationalBackground.BACHELORS);
            testEvaluateApplicant(3.1, EducationalBackground.MASTERS);
            testEvaluateApplicant(3.4, EducationalBackground.PHD);
            testEvaluateApplicant(2.9, EducationalBackground.OTHER);
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }

    /**
     * Tests the evaluateApplicant method with different inputs.
     * 
     * @param cgpa            the applicant's CGPA
     * @param educationalBackground the applicant's educational background
     */
    private static void testEvaluateApplicant(double cgpa, EducationalBackground educationalBackground) {
        String evaluationResult = evaluateApplicant(cgpa, educationalBackground);
        System.out.println("CGPA: " + cgpa + ", Background: " + educationalBackground + ", Evaluation Result: " + evaluationResult);
    }
}
```
