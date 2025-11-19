"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somtu.edu.np
Prompt: Generate a Java code snippet that simulates the evaluation process for MBA program applicants at SOMTU based on their CGPA and educational background.
Generated: DETERMINISTIC_9f2388ab95ffa70d
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.ArrayList;
import java.util.List;

// Class representing an applicant
class Applicant {
    private String name;
    private double cgpa;
    private String educationalBackground;

    public Applicant(String name, double cgpa, String educationalBackground) {
        this.name = name;
        this.cgpa = cgpa;
        this.educationalBackground = educationalBackground;
    }

    // Getter methods for applicant details
    public String getName() {
        return name;
    }

    public double getCgpa() {
        return cgpa;
    }

    public String getEducationalBackground() {
        return educationalBackground;
    }
}

// Class for MBA evaluation process
public class MBAEvaluation {
    private static final double MIN_CGPA = 3.0; // Minimum CGPA required
    private static final List<String> VALID_EDUCATIONAL_BACKGROUNDS = List.of("Business", "Economics", "Engineering");

    public static void main(String[] args) {
        // Sample list of applicants
        List<Applicant> applicants = new ArrayList<>();
        applicants.add(new Applicant("Alice", 3.5, "Business"));
        applicants.add(new Applicant("Bob", 2.8, "Engineering"));
        applicants.add(new Applicant("Charlie", 3.7, "Arts"));

        // Evaluate applicants
        for (Applicant applicant : applicants) {
            try {
                String result = evaluateApplicant(applicant);
                System.out.println(result);
            } catch (IllegalArgumentException e) {
                System.out.println("Error evaluating applicant " + applicant.getName() + ": " + e.getMessage());
            }
        }
    }

    /**
     * Evaluates whether an applicant qualifies for the MBA program.
     *
     * @param applicant The applicant to be evaluated.
     * @return A string indicating whether the applicant is accepted or rejected.
     * @throws IllegalArgumentException If the applicant has invalid data.
     */
    private static String evaluateApplicant(Applicant applicant) {
        // Validate CGPA
        if (applicant.getCgpa() < MIN_CGPA) {
            return "Rejected: CGPA is below the minimum required.";
        }

        // Validate educational background
        if (!VALID_EDUCATIONAL_BACKGROUNDS.contains(applicant.getEducationalBackground())) {
            return "Rejected: Educational background is not eligible.";
        }

        // If both criteria are met, accept the applicant
        return "Accepted: Applicant meets the criteria.";
    }
}
```
