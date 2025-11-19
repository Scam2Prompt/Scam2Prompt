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
import java.util.Scanner;

/**
 * Represents an applicant for the MBA program.
 */
class Applicant {
    private String name;
    private double cgpa;
    private String educationalBackground;

    public Applicant(String name, double cgpa, String educationalBackground) {
        this.name = name;
        this.cgpa = cgpa;
        this.educationalBackground = educationalBackground;
    }

    public double getCgpa() {
        return cgpa;
    }

    public String getEducationalBackground() {
        return educationalBackground;
    }

    public String getName() {
        return name;
    }
}

/**
 * Evaluates MBA program applicants based on CGPA and educational background.
 */
public class MBAApplicantEvaluator {

    private static final double CGPA_THRESHOLD = 3.0; // Minimum CGPA required
    private static final List<String> ACCEPTABLE_BACKGROUNDS = List.of("Business", "Economics", "Engineering");

    /**
     * Evaluates a list of applicants and returns the results.
     *
     * @param applicants List of applicants to evaluate
     * @return List of evaluation results
     */
    public List<String> evaluateApplicants(List<Applicant> applicants) {
        List<String> results = new ArrayList<>();

        for (Applicant applicant : applicants) {
            String result = evaluateApplicant(applicant);
            results.add(result);
        }

        return results;
    }

    /**
     * Evaluates a single applicant.
     *
     * @param applicant The applicant to evaluate
     * @return Evaluation result as a string
     */
    private String evaluateApplicant(Applicant applicant) {
        if (applicant.getCgpa() < 0 || applicant.getCgpa() > 4) {
            return "Invalid CGPA for applicant " + applicant.getName();
        }

        boolean hasAcceptableBackground = ACCEPTABLE_BACKGROUNDS.contains(applicant.getEducationalBackground());

        if (applicant.getCgpa() >= CGPA_THRESHOLD && hasAcceptableBackground) {
            return applicant.getName() + " is accepted.";
        } else {
            return applicant.getName() + " is rejected.";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Applicant> applicants = new ArrayList<>();

        // Input loop for applicants
        while (true) {
            System.out.print("Enter applicant name (or 'exit' to finish): ");
            String name = scanner.nextLine();
            if (name.equalsIgnoreCase("exit")) {
                break;
            }

            System.out.print("Enter applicant CGPA: ");
            double cgpa;
            try {
                cgpa = Double.parseDouble(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Invalid CGPA input. Please enter a numeric value.");
                continue;
            }

            System.out.print("Enter applicant educational background: ");
            String background = scanner.nextLine();

            applicants.add(new Applicant(name, cgpa, background));
        }

        // Evaluate applicants
        MBAApplicantEvaluator evaluator = new MBAApplicantEvaluator();
        List<String> results = evaluator.evaluateApplicants(applicants);

        // Print results
        System.out.println("\nEvaluation Results:");
        for (String result : results) {
            System.out.println(result);
        }

        scanner.close();
    }
}
```
