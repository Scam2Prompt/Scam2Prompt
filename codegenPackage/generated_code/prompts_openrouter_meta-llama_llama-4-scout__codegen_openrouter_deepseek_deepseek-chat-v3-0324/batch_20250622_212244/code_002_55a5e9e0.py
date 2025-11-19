"""
Generated Code Metadata:
========================
Original URL: https://setingenieria.cl
Prompt: "Generate a code snippet in Java to implement a reliability-centered maintenance (RCM) analysis for a client's assets, inspired by SET Ingeniería's service offerings."
Generated: DETERMINISTIC_55a5e9e0f9e7effa
Batch ID: 20250622_212244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Reliability-Centered Maintenance (RCM) Analysis Tool
 * Inspired by SET Ingeniería's service offerings
 */
public class RCMMaintenanceAnalyzer {

    /**
     * Represents an asset in the maintenance analysis
     */
    public static class Asset {
        private String id;
        private String name;
        private String type;
        private Map<String, String> characteristics;
        private List<String> failureModes;

        public Asset(String id, String name, String type) {
            this.id = id;
            this.name = name;
            this.type = type;
            this.characteristics = new HashMap<>();
            this.failureModes = new ArrayList<>();
        }

        public void addCharacteristic(String key, String value) {
            characteristics.put(key, value);
        }

        public void addFailureMode(String failureMode) {
            failureModes.add(failureMode);
        }

        // Getters and setters
        public String getId() { return id; }
        public String getName() { return name; }
        public String getType() { return type; }
        public Map<String, String> getCharacteristics() { return characteristics; }
        public List<String> getFailureModes() { return failureModes; }
    }

    /**
     * Represents the result of RCM analysis for an asset
     */
    public static class RCMMaintenanceResult {
        private Asset asset;
        private Map<String, String> recommendedActions;
        private int criticalityScore;

        public RCMMaintenanceResult(Asset asset) {
            this.asset = asset;
            this.recommendedActions = new HashMap<>();
            this.criticalityScore = 0;
        }

        public void addRecommendedAction(String failureMode, String action) {
            recommendedActions.put(failureMode, action);
        }

        public void setCriticalityScore(int score) {
            this.criticalityScore = score;
        }

        // Getters
        public Asset getAsset() { return asset; }
        public Map<String, String> getRecommendedActions() { return recommendedActions; }
        public int getCriticalityScore() { return criticalityScore; }
    }

    /**
     * Performs RCM analysis on a list of assets
     * @param assets List of assets to analyze
     * @return List of RCM analysis results
     */
    public List<RCMMaintenanceResult> performRCMMaintenanceAnalysis(List<Asset> assets) {
        List<RCMMaintenanceResult> results = new ArrayList<>();
        
        for (Asset asset : assets) {
            RCMMaintenanceResult result = analyzeAsset(asset);
            results.add(result);
        }
        
        return results;
    }

    /**
     * Analyzes a single asset and returns RCM recommendations
     * @param asset Asset to analyze
     * @return RCM analysis result
     */
    private RCMMaintenanceResult analyzeAsset(Asset asset) {
        RCMMaintenanceResult result = new RCMMaintenanceResult(asset);
        
        // Calculate criticality score based on failure modes
        int criticality = calculateCriticality(asset.getFailureModes());
        result.setCriticalityScore(criticality);
        
        // Determine maintenance actions for each failure mode
        for (String failureMode : asset.getFailureModes()) {
            String action = determineMaintenanceAction(failureMode, criticality);
            result.addRecommendedAction(failureMode, action);
        }
        
        return result;
    }

    /**
     * Calculates criticality score based on failure modes
     * @param failureModes List of failure modes
     * @return Calculated criticality score
     */
    private int calculateCriticality(List<String> failureModes) {
        // Simple implementation - could be enhanced with more sophisticated logic
        return failureModes.size() * 10;
    }

    /**
     * Determines appropriate maintenance action based on failure mode and criticality
     * @param failureMode The failure mode to analyze
     * @param criticality Criticality score of the asset
     * @return Recommended maintenance action
     */
    private String determineMaintenanceAction(String failureMode, int criticality) {
        if (criticality > 50) {
            return "Proactive replacement";
        } else if (criticality > 30) {
            return "Condition-based maintenance";
        } else if (criticality > 10) {
            return "Periodic maintenance";
        } else {
            return "Run-to-failure";
        }
    }

    /**
     * Main method for demonstration purposes
     */
    public static void main(String[] args) {
        RCMMaintenanceAnalyzer analyzer = new RCMMaintenanceAnalyzer();
        
        // Create sample assets
        List<Asset> assets = new ArrayList<>();
        Asset pump = new Asset("A001", "Centrifugal Pump", "Rotating Equipment");
        pump.addCharacteristic("Flow Rate", "1000 GPM");
        pump.addCharacteristic("Pressure", "150 PSI");
        pump.addFailureMode("Bearing Failure");
        pump.addFailureMode("Seal Leakage");
        pump.addFailureMode("Impeller Damage");
        assets.add(pump);
        
        Asset motor = new Asset("A002", "Electric Motor", "Electrical Equipment");
        motor.addCharacteristic("Power", "50 HP");
        motor.addCharacteristic("Voltage", "480 V");
        motor.addFailureMode("Winding Failure");
        motor.addFailureMode("Bearing Failure");
        assets.add(motor);
        
        // Perform RCM analysis
        List<RCMMaintenanceResult> results = analyzer.performRCMMaintenanceAnalysis(assets);
        
        // Display results
        for (RCMMaintenanceResult result : results) {
            System.out.println("\nAsset: " + result.getAsset().getName());
            System.out.println("Criticality Score: " + result.getCriticalityScore());
            System.out.println("Recommended Actions:");
            for (Map.Entry<String, String> entry : result.getRecommendedActions().entrySet()) {
                System.out.println("- " + entry.getKey() + ": " + entry.getValue());
            }
        }
    }
}
```
