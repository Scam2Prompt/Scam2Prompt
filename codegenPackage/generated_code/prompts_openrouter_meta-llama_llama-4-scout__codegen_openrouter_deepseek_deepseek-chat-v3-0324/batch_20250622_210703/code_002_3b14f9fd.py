"""
Generated Code Metadata:
========================
Original URL: https://www.marodconsultores.com.pe
Prompt: "Generate a code snippet in Java or C++ to simulate the behavior of an electrical distribution system, taking into account factors such as power flow, voltage drops, and line losses, as studied by Marod Consultores in their electrical engineering consulting services."
Generated: DETERMINISTIC_3b14f9fd200fe42b
Batch ID: 20250622_210703
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
 * Simulates an electrical distribution system with power flow calculations,
 * voltage drops, and line losses.
 */
public class ElectricalDistributionSystem {

    // Represents a node in the electrical distribution system
    public static class Node {
        private String id;
        private double voltage; // in kV
        private double powerDemand; // in MW
        private List<Line> connectedLines;

        public Node(String id, double voltage, double powerDemand) {
            this.id = id;
            this.voltage = voltage;
            this.powerDemand = powerDemand;
            this.connectedLines = new ArrayList<>();
        }

        public void addLine(Line line) {
            connectedLines.add(line);
        }

        // Getters
        public String getId() { return id; }
        public double getVoltage() { return voltage; }
        public double getPowerDemand() { return powerDemand; }
        public List<Line> getConnectedLines() { return connectedLines; }
    }

    // Represents a transmission line between nodes
    public static class Line {
        private String id;
        private Node fromNode;
        private Node toNode;
        private double resistance; // in ohms
        private double reactance; // in ohms
        private double length; // in km
        private double currentCapacity; // in A

        public Line(String id, Node fromNode, Node toNode, 
                   double resistance, double reactance, 
                   double length, double currentCapacity) {
            this.id = id;
            this.fromNode = fromNode;
            this.toNode = toNode;
            this.resistance = resistance;
            this.reactance = reactance;
            this.length = length;
            this.currentCapacity = currentCapacity;
        }

        // Calculate voltage drop across this line
        public double calculateVoltageDrop(double current) {
            return current * (resistance * Math.cos(reactance) + reactance * Math.sin(reactance)) * length;
        }

        // Calculate power loss in this line
        public double calculatePowerLoss(double current) {
            return Math.pow(current, 2) * resistance * length;
        }

        // Getters
        public String getId() { return id; }
        public Node getFromNode() { return fromNode; }
        public Node getToNode() { return toNode; }
        public double getResistance() { return resistance; }
        public double getReactance() { return reactance; }
        public double getLength() { return length; }
        public double getCurrentCapacity() { return currentCapacity; }
    }

    private Map<String, Node> nodes;
    private Map<String, Line> lines;

    public ElectricalDistributionSystem() {
        this.nodes = new HashMap<>();
        this.lines = new HashMap<>();
    }

    public void addNode(Node node) {
        nodes.put(node.getId(), node);
    }

    public void addLine(Line line) {
        lines.put(line.getId(), line);
        line.getFromNode().addLine(line);
        line.getToNode().addLine(line);
    }

    /**
     * Simulates power flow through the system
     * @return Map of node IDs to their calculated voltages after power flow
     * @throws IllegalStateException if system is not properly configured
     */
    public Map<String, Double> simulatePowerFlow() throws IllegalStateException {
        if (nodes.isEmpty() || lines.isEmpty()) {
            throw new IllegalStateException("System must contain nodes and lines");
        }

        Map<String, Double> nodeVoltages = new HashMap<>();
        Map<String, Double> lineCurrents = new HashMap<>();

        // Initialize with nominal voltages
        nodes.forEach((id, node) -> nodeVoltages.put(id, node.getVoltage()));

        // Simplified power flow calculation (DC approximation)
        for (Line line : lines.values()) {
            double powerFlow = calculatePowerFlow(line);
            double current = powerFlow / (line.getFromNode().getVoltage() * Math.sqrt(3));
            lineCurrents.put(line.getId(), current);

            // Update voltage at receiving end
            double voltageDrop = line.calculateVoltageDrop(current);
            double receivingVoltage = nodeVoltages.get(line.getFromNode().getId()) - voltageDrop;
            nodeVoltages.put(line.getToNode().getId(), 
                Math.min(nodeVoltages.get(line.getToNode().getId()), receivingVoltage));
        }

        return nodeVoltages;
    }

    private double calculatePowerFlow(Line line) {
        // Simplified power flow calculation
        // In a real implementation, this would use more complex algorithms
        // like Newton-Raphson or Gauss-Seidel methods
        return line.getToNode().getPowerDemand() / line.getConnectedLines().size();
    }

    /**
     * Calculates total power losses in the system
     * @return Total power loss in MW
     */
    public double calculateTotalLosses() {
        double totalLoss = 0;
        for (Line line : lines.values()) {
            double current = line.getToNode().getPowerDemand() / 
                           (line.getFromNode().getVoltage() * Math.sqrt(3));
            totalLoss += line.calculatePowerLoss(current);
        }
        return totalLoss;
    }

    /**
     * Checks if any lines are overloaded
     * @return Map of line IDs to their overload percentage (0 = not overloaded)
     */
    public Map<String, Double> checkLineOverloads() {
        Map<String, Double> overloads = new HashMap<>();
        for (Line line : lines.values()) {
            double current = line.getToNode().getPowerDemand() / 
                           (line.getFromNode().getVoltage() * Math.sqrt(3));
            double overloadPercent = (current / line.getCurrentCapacity()) * 100 - 100;
            if (overloadPercent > 0) {
                overloads.put(line.getId(), overloadPercent);
            } else {
                overloads.put(line.getId(), 0.0);
            }
        }
        return overloads;
    }
}
```
