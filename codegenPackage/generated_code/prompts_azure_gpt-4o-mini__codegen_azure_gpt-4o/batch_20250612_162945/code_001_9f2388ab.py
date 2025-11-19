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
import java.util.ArrayList;
import java.util.List;

// Class representing an MBA applicant
class Applicant {
    private String name;
    private double cgpa;
    private String educationalBackground;

    // Constructor
    public Applicant(String name, double cgpa, String educationalBackground) {
        this.name = name;
        this.cgpa = cgpa;
        this.educationalBackground = educationalBackground;
    }

    // Getters
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

// Class representing the evaluation process
class MBAEvaluation {
    private static final double MIN_CGPA = 3.0; // Minimum CGPA required
    private static final List<String> ACCEPTED_EDUCATIONAL_BACKGROUNDS = List.of("Business", "Economics", "Engineering", "Science");

    /**
     * Evaluates an applicant based on CGPA and educational background.
     *
     * @param applicant The applicant to evaluate.
     * @return True if the applicant is eligible, false otherwise.
     */
    public boolean evaluateApplicant(Applicant applicant) {
        try {
            // Check CGPA
            if (applicant.getCgpa() < MIN_CGPA) {
                return false;
            }

            // Check educational background
            if (!ACCEPTED_EDUCATIONAL_BACKGROUNDS.contains(applicant.getEducationalBackground())) {
                return false;
            }

            // Applicant meets all criteria
            return true;
        } catch (Exception e) {
            // Log the error (in production, use a logging framework)
            System.err.println("Error during evaluation: " + e.getMessage());
            return false;
        }
    }
}

// Main class to simulate the evaluation process
public class MBAEvaluationSystem {
    public static void main(String[] args) {
        // Create a list of applicants
        List<Applicant> applicants = new ArrayList<>();
        applicants.add(new Applicant("Alice", 3.5, "Business"));
        applicants.add(new Applicant("Bob", 2.8, "Engineering"));
        applicants.add(new Applicant("Charlie", 3.2, "Arts"));

        // Create an instance of the evaluation system
        MBAEvaluation evaluation = new MBAEvaluation();

        // Evaluate each applicant
        for (Applicant applicant : applicants) {
            boolean isEligible = evaluation.evaluateApplicant(applicant);
            System.out.println("Applicant: " + applicant.getName() + " | Eligible: " + (isEligible ? "Yes" : "No"));
        }
    }
}
```
