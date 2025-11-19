"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: "Write a code snippet in Java to calculate the environmental impact of a construction project, considering factors mentioned in Unison Plus's safety and environmental regulations."
Generated: DETERMINISTIC_88ee1c2cb1f7f54e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * Calculates the environmental impact of a construction project based on Unison Plus's safety and environmental regulations.
 */

public class EnvironmentalImpactCalculator {

    // Define enum for pollution types
    public enum PollutionType {
        AIR,
        WATER,
        SOIL
    }

    /**
     * Calculates the environmental impact based on the project's details.
     *
     * @param projectName        the name of the construction project
     * @param projectLocation    the location of the construction project
     * @param emissions          the amount of emissions produced (in kg)
     * @param wasteGenerated     the amount of waste generated (in tons)
     * @param pollutionType      the type of pollution
     * @return a report detailing the environmental impact
     */
    public static String calculateEnvironmentalImpact(String projectName, String projectLocation, double emissions, double wasteGenerated, PollutionType pollutionType) {
        try {
            // Validate input parameters
            if (projectName == null || projectName.isEmpty()) {
                throw new IllegalArgumentException("Project name cannot be empty");
            }
            if (projectLocation == null || projectLocation.isEmpty()) {
                throw new IllegalArgumentException("Project location cannot be empty");
            }
            if (emissions < 0) {
                throw new IllegalArgumentException("Emissions cannot be negative");
            }
            if (wasteGenerated < 0) {
                throw new IllegalArgumentException("Waste generated cannot be negative");
            }

            // Calculate environmental impact score
            double impactScore = calculateImpactScore(emissions, wasteGenerated);

            // Generate report
            String report = generateReport(projectName, projectLocation, emissions, wasteGenerated, pollutionType, impactScore);

            return report;
        } catch (IllegalArgumentException e) {
            return "Error: " + e.getMessage();
        }
    }

    /**
     * Calculates the environmental impact score based on emissions and waste generated.
     *
     * @param emissions      the amount of emissions produced (in kg)
     * @param wasteGenerated the amount of waste generated (in tons)
     * @return the environmental impact score
     */
    private static double calculateImpactScore(double emissions, double wasteGenerated) {
        // Assign weights to emissions and waste generated
        double emissionWeight = 0.6;
        double wasteWeight = 0.4;

        // Calculate impact score
        double impactScore = (emissions * emissionWeight) + (wasteGenerated * wasteWeight);

        return impactScore;
    }

    /**
     * Generates a report detailing the environmental impact.
     *
     * @param projectName        the name of the construction project
     * @param projectLocation    the location of the construction project
     * @param emissions          the amount of emissions produced (in kg)
     * @param wasteGenerated     the amount of waste generated (in tons)
     * @param pollutionType      the type of pollution
     * @param impactScore        the environmental impact score
     * @return a report detailing the environmental impact
     */
    private static String generateReport(String projectName, String projectLocation, double emissions, double wasteGenerated, PollutionType pollutionType, double impactScore) {
        StringBuilder report = new StringBuilder();

        report.append("Environmental Impact Report for ").append(projectName).append(" at ").append(projectLocation).append("\n");
        report.append("--------------------------------------------------------\n");
        report.append("Emissions: ").append(emissions).append(" kg\n");
        report.append("Waste Generated: ").append(wasteGenerated).append(" tons\n");
        report.append("Pollution Type: ").append(pollutionType).append("\n");
        report.append("Environmental Impact Score: ").append(String.format("%.2f", impactScore)).append("\n");

        // Interpret impact score
        if (impactScore < 100) {
            report.append("Impact: Low\n");
        } else if (impactScore < 500) {
            report.append("Impact: Moderate\n");
        } else {
            report.append("Impact: High\n");
        }

        return report.toString();
    }

    public static void main(String[] args) {
        String projectName = "Construction Project Alpha";
        String projectLocation = "New York";
        double emissions = 5000; // in kg
        double wasteGenerated = 200; // in tons
        PollutionType pollutionType = PollutionType.AIR;

        String report = calculateEnvironmentalImpact(projectName, projectLocation, emissions, wasteGenerated, pollutionType);
        System.out.println(report);
    }
}
```
