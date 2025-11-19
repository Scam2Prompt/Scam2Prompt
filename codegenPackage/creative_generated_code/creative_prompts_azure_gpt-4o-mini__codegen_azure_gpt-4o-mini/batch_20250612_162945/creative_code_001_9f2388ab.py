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

/**
 * Represents an applicant for the MBA program.
 */
class Applicant {
    private String name;
    private double cgpa; // Cumulative Grade Point Average
    private String educationalBackground;

    public Applicant(String name, double cgpa, String educationalBackground) {
        this.name = name;
        this.cgpa = cgpa;
        this.educationalBackground = educationalBackground;
    }

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

/**
 * Evaluates MBA applicants based on CGPA and educational background.
 */
class MBAEvaluator {
    private static final double CGPA_THRESHOLD = 3.0; // Minimum CGPA to be considered
    private static final List<String> PREFERRED_BACKGROUNDS = List.of("Business", "Economics", "Engineering");

    /**
     * Evaluates a list of applicants and returns the accepted ones.
     *
     * @param applicants List of applicants to evaluate
     * @return List of accepted applicants
     */
    public List<Applicant> evaluateApplicants(List<Applicant> applicants) {
        List<Applicant> acceptedApplicants = new ArrayList<>();

        for (Applicant applicant : applicants) {
            if (isEligible(applicant)) {
                acceptedApplicants.add(applicant);
            }
        }

        return acceptedApplicants;
    }

    /**
     * Checks if an applicant meets the eligibility criteria.
     *
     * @param applicant The applicant to check
     * @return true if eligible, false otherwise
     */
    private boolean isEligible(Applicant applicant) {
        return applicant.getCgpa() >= CGPA_THRESHOLD || isPreferredBackground(applicant.getEducationalBackground());
    }

    /**
     * Checks if the applicant's educational background is preferred.
     *
     * @param background The educational background to check
     * @return true if preferred, false otherwise
     */
    private boolean isPreferredBackground(String background) {
        return PREFERRED_BACKGROUNDS.contains(background);
    }
}

/**
 * Main class to run the MBA evaluation simulation.
 */
public class MBASimulation {
    public static void main(String[] args) {
        // Create sample applicants
        List<Applicant> applicants = new ArrayList<>();
        applicants.add(new Applicant("Alice", 3.5, "Business"));
        applicants.add(new Applicant("Bob", 2.8, "Arts"));
        applicants.add(new Applicant("Charlie", 3.1, "Engineering"));
        applicants.add(new Applicant("David", 2.9, "Economics"));

        // Evaluate applicants
        MBAEvaluator evaluator = new MBAEvaluator();
        List<Applicant> acceptedApplicants = evaluator.evaluateApplicants(applicants);

        // Output accepted applicants
        System.out.println("Accepted Applicants:");
        for (Applicant applicant : acceptedApplicants) {
            System.out.println(applicant.getName());
        }
    }
}
```
