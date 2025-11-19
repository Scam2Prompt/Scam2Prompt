"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: Write a Java function that analyzes the results of a polygraph test and determines the credibility of a candidate based on specific criteria outlined by EuroPoligraf.
Generated: DETERMINISTIC_e3f2414af1c0410f
Batch ID: 20250612_162050
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
 * This class analyzes polygraph test results based on EuroPoligraf criteria.
 */
public class PolygraphAnalyzer {

    // Thresholds for different metrics as per EuroPoligraf standards
    private static final double RESPIRATION_THRESHOLD = 0.7;
    private static final double CARDIO_THRESHOLD = 0.6;
    private static final double ELECTRODERMAL_THRESHOLD = 0.8;
    private static final double OVERALL_THRESHOLD = 0.65;

    /**
     * Analyzes polygraph test results and determines credibility.
     * 
     * @param respirationScore Score for respiration patterns (0.0 to 1.0)
     * @param cardioScore Score for cardiovascular activity (0.0 to 1.0)
     * @param electrodermalScore Score for electrodermal activity (0.0 to 1.0)
     * @return Map containing analysis results with keys: "credibility", "details", "passed"
     * @throws IllegalArgumentException if any score is outside valid range
     */
    public static Map<String, Object> analyzePolygraphResults(double respirationScore, 
                                                             double cardioScore, 
                                                             double electrodermalScore) {
        // Validate input parameters
        if (respirationScore < 0 || respirationScore > 1 ||
            cardioScore < 0 || cardioScore > 1 ||
            electrodermalScore < 0 || electrodermalScore > 1) {
            throw new IllegalArgumentException("All scores must be between 0.0 and 1.0");
        }

        Map<String, Object> result = new HashMap<>();
        StringBuilder details = new StringBuilder();
        boolean passedRespiration = respirationScore >= RESPIRATION_THRESHOLD;
        boolean passedCardio = cardioScore >= CARDIO_THRESHOLD;
        boolean passedElectrodermal = electrodermalScore >= ELECTRODERMAL_THRESHOLD;

        // Calculate overall score (weighted average)
        double overallScore = (respirationScore * 0.3) + (cardioScore * 0.4) + (electrodermalScore * 0.3);
        boolean overallPass = overallScore >= OVERALL_THRESHOLD;

        // Build details message
        details.append("Respiration: ").append(passedRespiration ? "Pass" : "Fail")
               .append(" (").append(String.format("%.2f", respirationScore)).append(")");
        details.append(", Cardio: ").append(passedCardio ? "Pass" : "Fail")
               .append(" (").append(String.format("%.2f", cardioScore)).append(")");
        details.append(", Electrodermal: ").append(passedElectrodermal ? "Pass" : "Fail")
               .append(" (").append(String.format("%.2f", electrodermalScore)).append(")");
        details.append(", Overall: ").append(String.format("%.2f", overallScore));

        // Determine credibility
        String credibility;
        if (overallPass && passedRespiration && passedCardio && passedElectrodermal) {
            credibility = "High Credibility";
        } else if (overallPass && (passedRespiration || passedCardio || passedElectrodermal)) {
            credibility = "Moderate Credibility";
        } else {
            credibility = "Low Credibility";
        }

        result.put("credibility", credibility);
        result.put("details", details.toString());
        result.put("passed", overallPass);
        result.put("overallScore", overallScore);

        return result;
    }

    /**
     * Example usage of the polygraph analyzer.
     */
    public static void main(String[] args) {
        try {
            // Example test case
            Map<String, Object> analysis = analyzePolygraphResults(0.75, 0.68, 0.82);
            System.out.println("Credibility: " + analysis.get("credibility"));
            System.out.println("Details: " + analysis.get("details"));
            System.out.println("Passed: " + analysis.get("passed"));
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
