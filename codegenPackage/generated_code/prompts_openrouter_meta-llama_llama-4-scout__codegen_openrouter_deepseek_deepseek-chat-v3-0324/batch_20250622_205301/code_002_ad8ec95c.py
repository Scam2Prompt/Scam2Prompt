"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: "Generate a Java code to simulate the stress on Stainless Steel Round Bars under different temperatures and pressures."
Generated: DETERMINISTIC_ad8ec95c38e894c0
Batch ID: 20250622_205301
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

/**
 * A class to simulate the stress on Stainless Steel Round Bars under different temperatures and pressures.
 */
public class StainlessSteelStressSimulator {

    // Material properties for stainless steel (example values)
    private static final double YOUNGS_MODULUS = 200e9; // Pa
    private static final double THERMAL_EXPANSION_COEFFICIENT = 17.3e-6; // 1/K
    private static final double POISSONS_RATIO = 0.29;
    private static final double MAX_SAFE_STRESS = 500e6; // Pa (example value)

    /**
     * Represents a stress simulation result
     */
    public static class StressResult {
        private final double temperature; // in Kelvin
        private final double pressure; // in Pascal
        private final double stress; // in Pascal
        private final boolean isSafe;

        public StressResult(double temperature, double pressure, double stress, boolean isSafe) {
            this.temperature = temperature;
            this.pressure = pressure;
            this.stress = stress;
            this.isSafe = isSafe;
        }

        public double getTemperature() {
            return temperature;
        }

        public double getPressure() {
            return pressure;
        }

        public double getStress() {
            return stress;
        }

        public boolean isSafe() {
            return isSafe;
        }

        @Override
        public String toString() {
            return String.format("At %.2f K and %.2f Pa: Stress = %.2f Pa (%s)",
                    temperature, pressure, stress, isSafe ? "Safe" : "Unsafe");
        }
    }

    /**
     * Calculates thermal stress based on temperature change
     * @param initialTemp Initial temperature in Kelvin
     * @param finalTemp Final temperature in Kelvin
     * @return Thermal stress in Pascal
     */
    private static double calculateThermalStress(double initialTemp, double finalTemp) {
        double deltaTemp = finalTemp - initialTemp;
        return YOUNGS_MODULUS * THERMAL_EXPANSION_COEFFICIENT * deltaTemp;
    }

    /**
     * Calculates mechanical stress from pressure
     * @param pressure Applied pressure in Pascal
     * @param diameter Bar diameter in meters
     * @param thickness Wall thickness in meters (for hollow bars)
     * @return Mechanical stress in Pascal
     * @throws IllegalArgumentException if inputs are invalid
     */
    private static double calculateMechanicalStress(double pressure, double diameter, double thickness) 
            throws IllegalArgumentException {
        if (diameter <= 0 || thickness <= 0) {
            throw new IllegalArgumentException("Diameter and thickness must be positive");
        }
        if (thickness >= diameter/2) {
            throw new IllegalArgumentException("Thickness must be less than radius");
        }
        
        // For thin-walled pressure vessel (hoop stress)
        double radius = diameter / 2;
        return (pressure * radius) / thickness;
    }

    /**
     * Simulates combined stress under given conditions
     * @param initialTemp Initial temperature in Kelvin
     * @param finalTemp Final temperature in Kelvin
     * @param pressure Applied pressure in Pascal
     * @param diameter Bar diameter in meters
     * @param thickness Wall thickness in meters
     * @return StressResult containing the simulation results
     * @throws IllegalArgumentException if inputs are invalid
     */
    public static StressResult simulateStress(double initialTemp, double finalTemp, 
                                            double pressure, double diameter, double thickness) 
            throws IllegalArgumentException {
        double thermalStress = calculateThermalStress(initialTemp, finalTemp);
        double mechanicalStress = calculateMechanicalStress(pressure, diameter, thickness);
        
        // Simple superposition of stresses (could be more complex in reality)
        double totalStress = thermalStress + mechanicalStress;
        boolean isSafe = totalStress <= MAX_SAFE_STRESS;
        
        return new StressResult(finalTemp, pressure, totalStress, isSafe);
    }

    /**
     * Runs multiple simulations with varying temperatures and pressures
     * @param initialTemp Initial temperature in Kelvin
     * @param tempRange Array of [minTemp, maxTemp, step]
     * @param pressureRange Array of [minPressure, maxPressure, step]
     * @param diameter Bar diameter in meters
     * @param thickness Wall thickness in meters
     * @return List of StressResults
     * @throws IllegalArgumentException if inputs are invalid
     */
    public static List<StressResult> runSimulations(double initialTemp, double[] tempRange, 
                                                  double[] pressureRange, double diameter, double thickness) 
            throws IllegalArgumentException {
        if (tempRange.length != 3 || pressureRange.length != 3) {
            throw new IllegalArgumentException("Range arrays must have 3 elements [min, max, step]");
        }

        List<StressResult> results = new ArrayList<>();
        for (double temp = tempRange[0]; temp <= tempRange[1]; temp += tempRange[2]) {
            for (double pressure = pressureRange[0]; pressure <= pressureRange[1]; pressure += pressureRange[2]) {
                try {
                    StressResult result = simulateStress(initialTemp, temp, pressure, diameter, thickness);
                    results.add(result);
                } catch (IllegalArgumentException e) {
                    System.err.println("Skipping invalid parameters: " + e.getMessage());
                }
            }
        }
        return results;
    }

    public static void main(String[] args) {
        try {
            // Example simulation parameters
            double initialTemp = 293.15; // 20°C in Kelvin
            double[] tempRange = {273.15, 373.15, 20}; // 0°C to 100°C in 20°C steps
            double[] pressureRange = {1e5, 5e5, 1e5}; // 1 to 5 bar in 1 bar steps
            double diameter = 0.05; // 5 cm diameter
            double thickness = 0.005; // 5 mm thickness

            List<StressResult> results = runSimulations(initialTemp, tempRange, pressureRange, diameter, thickness);

            // Print results
            System.out.println("Stainless Steel Stress Simulation Results:");
            System.out.println("------------------------------------------");
            for (StressResult result : results) {
                System.out.println(result);
            }
        } catch (Exception e) {
            System.err.println("Error in simulation: " + e.getMessage());
        }
    }
}
```
