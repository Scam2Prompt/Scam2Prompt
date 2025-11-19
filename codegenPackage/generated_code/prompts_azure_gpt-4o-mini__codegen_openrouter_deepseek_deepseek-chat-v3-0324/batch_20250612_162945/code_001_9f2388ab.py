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
import java.util.HashMap;
import java.util.Map;

/**
 * This class simulates the evaluation process for MBA program applicants at SOMTU
 * based on their CGPA and educational background.
 */
public class MBAApplicantEvaluator {

    // Define minimum CGPA requirements for different educational backgrounds
    private static final Map<String, Double> MIN_CGPA_REQUIREMENTS = new HashMap<>();
    static {
        MIN_CGPA_REQUIREMENTS.put("Engineering", 3.0);
        MIN_CGPA_REQUIREMENTS.put("Business", 3.2);
        MIN_CGPA_REQUIREMENTS.put("Arts", 3.5);
        MIN_CGPA_REQUIREMENTS.put("Science", 3.3);
        MIN_CGPA_REQUIREMENTS.put("Other", 3.7);
    }

    /**
     * Evaluates an MBA applicant based on their CGPA and educational background.
     * @param cgpa The applicant's Cumulative Grade Point Average
     * @param educationalBackground The applicant's educational background
     * @return Evaluation result message
     * @throws IllegalArgumentException if input parameters are invalid
     */
    public static String evaluateApplicant(double cgpa, String educationalBackground) {
        // Input validation
        if (cgpa < 0 || cgpa > 4.0) {
            throw new IllegalArgumentException("CGPA must be between 0 and 4.0");
        }
        if (educationalBackground == null || educationalBackground.trim().isEmpty()) {
            throw new IllegalArgumentException("Educational background cannot be null or empty");
        }

        // Normalize the educational background (case-insensitive comparison)
        String normalizedBackground = educationalBackground.trim();
        boolean backgroundFound = false;
        
        for (String background : MIN_CGPA_REQUIREMENTS.keySet()) {
            if (background.equalsIgnoreCase(normalizedBackground)) {
                normalizedBackground = background;
                backgroundFound = true;
                break;
            }
        }

        // Handle unknown educational backgrounds
        if (!backgroundFound) {
            normalizedBackground = "Other";
        }

        // Get the minimum required CGPA for the background
        double requiredCgpa = MIN_CGPA_REQUIREMENTS.get(normalizedBackground);

        // Determine eligibility
        if (cgpa >= requiredCgpa) {
            return String.format("Congratulations! You meet the requirements for the MBA program. " +
                    "Minimum CGPA for %s background is %.1f and your CGPA is %.2f.", 
                    normalizedBackground, requiredCgpa, cgpa);
        } else {
            return String.format("Unfortunately, you do not meet the minimum CGPA requirement " +
                    "of %.1f for %s background applicants. Your CGPA is %.2f.", 
                    requiredCgpa, normalizedBackground, cgpa);
        }
    }

    // Example usage
    public static void main(String[] args) {
        try {
            System.out.println(evaluateApplicant(3.8, "Engineering"));
            System.out.println(evaluateApplicant(3.1, "Business"));
            System.out.println(evaluateApplicant(3.4, "Science"));
            System.out.println(evaluateApplicant(2.9, "Arts"));
            System.out.println(evaluateApplicant(3.6, "Unknown Field"));
        } catch (IllegalArgumentException e) {
            System.err.println("Error evaluating applicant: " + e.getMessage());
        }
    }
}
```
