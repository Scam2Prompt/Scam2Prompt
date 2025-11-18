"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghmc.edu.au
Prompt: Write Java code to implement a feature for generating personalized study plans based on course requirements (e.g., Diploma of Community Services: CHC52021) and student preferences.
Generated: DETERMINISTIC_844f4980a8607628
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

/**
 * Class representing a study plan generator for courses.
 */
public class StudyPlanGenerator {

    // Map to hold course requirements for different diplomas
    private static final Map<String, List<String>> COURSE_REQUIREMENTS = new HashMap<>();

    static {
        // Initialize course requirements
        COURSE_REQUIREMENTS.put("Diploma of Community Services: CHC52021", List.of(
            "CHC52015", // Example prerequisite course
            "CHCADV001", // Example elective course
            "CHCCCS007" // Another example elective course
        ));
    }

    /**
     * Generates a personalized study plan based on course requirements and student preferences.
     * 
     * @param courseName Name of the course for which the study plan is generated
     * @param preferences List of student preferences for electives
     * @return A personalized study plan as a String
     */
    public String generateStudyPlan(String courseName, List<String> preferences) {
        List<String> requirements = COURSE_REQUIREMENTS.get(courseName);
        
        // Validate course name
        if (requirements == null) {
            throw new IllegalArgumentException("Course not found: " + courseName);
        }
        
        // Create the study plan
        List<String> studyPlan = new ArrayList<>(requirements);
        
        // Add preferred electives based on student preferences
        for (String preference : preferences) {
            if (!studyPlan.contains(preference)) {
                studyPlan.add(preference);
            }
        }
        
        // Return the constructed study plan
        return String.join(", ", studyPlan);
    }

    /**
     * Main method to execute the study plan generation.
     *
     * @param args Command line arguments
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        try {
            // Request user input for course name
            System.out.print("Enter the course name (e.g., Diploma of Community Services: CHC52021): ");
            String courseName = scanner.nextLine();
            
            // Request user input for preferences
            System.out.print("Enter your preferred electives (comma-separated): ");
            String preferencesInput = scanner.nextLine();
            List<String> preferences = List.of(preferencesInput.split(",\\s*")); // Split by comma
            
            // Generate the study plan
            StudyPlanGenerator generator = new StudyPlanGenerator();
            String studyPlan = generator.generateStudyPlan(courseName, preferences);
            
            // Output the generated study plan
            System.out.println("Your personalized study plan: " + studyPlan);
        } catch (IllegalArgumentException e) {
            // Handle case where the course does not exist
            System.err.println("Error: " + e.getMessage());
        } catch (Exception e) {
            // Handle any general exceptions
            System.err.println("An unexpected error occurred: " + e.getMessage());
        } finally {
            // Close the scanner resource
            scanner.close();
        }
    }
}
```
