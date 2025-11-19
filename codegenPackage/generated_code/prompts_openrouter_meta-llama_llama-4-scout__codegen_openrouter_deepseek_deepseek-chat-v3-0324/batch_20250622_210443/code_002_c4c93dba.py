"""
Generated Code Metadata:
========================
Original URL: https://espinelycia.com
Prompt: "Write a code snippet in Java to create a simple hydraulic network model that can be used for simulation and analysis in construction projects, incorporating factors like pressure drop and flow rate."
Generated: DETERMINISTIC_c4c93dba5430c25f
Batch ID: 20250622_210443
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
 * A simple hydraulic network model for construction project simulations.
 * Models pressure drop and flow rate in a network of pipes.
 */
public class HydraulicNetworkModel {

    /**
     * Represents a pipe in the hydraulic network.
     */
    public static class Pipe {
        private final String id;
        private final double length;
        private final double diameter;
        private final double roughness;
        private double flowRate;
        private double pressureDrop;

        public Pipe(String id, double length, double diameter, double roughness) {
            this.id = id;
            this.length = length;
            this.diameter = diameter;
            this.roughness = roughness;
        }

        public void calculatePressureDrop(double flowRate) {
            // Simplified Darcy-Weisbach equation for pressure drop calculation
            double velocity = flowRate / (Math.PI * Math.pow(diameter / 2, 2));
            double reynoldsNumber = (velocity * diameter) / 1e-6; // Assuming water viscosity
            double frictionFactor;

            if (reynoldsNumber < 2000) {
                frictionFactor = 64 / reynoldsNumber; // Laminar flow
            } else {
                // Colebrook-White approximation for turbulent flow
                double relativeRoughness = roughness / diameter;
                frictionFactor = 0.25 / Math.pow(Math.log10((relativeRoughness / 3.7) + (5.74 / Math.pow(reynoldsNumber, 0.9))), 2);
            }

            this.pressureDrop = (frictionFactor * length * Math.pow(velocity, 2)) / (diameter * 2 * 9.81);
            this.flowRate = flowRate;
        }

        public String getId() {
            return id;
        }

        public double getFlowRate() {
            return flowRate;
        }

        public double getPressureDrop() {
            return pressureDrop;
        }
    }

    /**
     * Represents a node in the hydraulic network where pipes connect.
     */
    public static class Node {
        private final String id;
        private final List<Pipe> incomingPipes = new ArrayList<>();
        private final List<Pipe> outgoingPipes = new ArrayList<>();
        private double pressure;

        public Node(String id) {
            this.id = id;
        }

        public void addIncomingPipe(Pipe pipe) {
            incomingPipes.add(pipe);
        }

        public void addOutgoingPipe(Pipe pipe) {
            outgoingPipes.add(pipe);
        }

        public void setPressure(double pressure) {
            this.pressure = pressure;
        }

        public String getId() {
            return id;
        }

        public double getPressure() {
            return pressure;
        }

        public List<Pipe> getIncomingPipes() {
            return incomingPipes;
        }

        public List<Pipe> getOutgoingPipes() {
            return outgoingPipes;
        }
    }

    private final List<Node> nodes = new ArrayList<>();
    private final List<Pipe> pipes = new ArrayList<>();

    /**
     * Adds a node to the network.
     * @param node The node to add
     * @throws IllegalArgumentException if node is null
     */
    public void addNode(Node node) {
        if (node == null) {
            throw new IllegalArgumentException("Node cannot be null");
        }
        nodes.add(node);
    }

    /**
     * Adds a pipe to the network.
     * @param pipe The pipe to add
     * @throws IllegalArgumentException if pipe is null
     */
    public void addPipe(Pipe pipe) {
        if (pipe == null) {
            throw new IllegalArgumentException("Pipe cannot be null");
        }
        pipes.add(pipe);
    }

    /**
     * Simulates the hydraulic network with given flow rates.
     * @param flowRate The initial flow rate at the source node
     * @throws IllegalStateException if network is not properly configured
     */
    public void simulate(double flowRate) {
        if (nodes.isEmpty() || pipes.isEmpty()) {
            throw new IllegalStateException("Network must contain at least one node and one pipe");
        }

        // Simple simulation: assumes single source and sink
        Node source = nodes.get(0);
        source.setPressure(100); // Arbitrary initial pressure

        for (Pipe pipe : pipes) {
            pipe.calculatePressureDrop(flowRate);
        }

        // Calculate node pressures based on pipe pressure drops
        for (int i = 1; i < nodes.size(); i++) {
            Node node = nodes.get(i);
            Node previousNode = nodes.get(i - 1);
            Pipe connectingPipe = findConnectingPipe(previousNode, node);
            if (connectingPipe != null) {
                node.setPressure(previousNode.getPressure() - connectingPipe.getPressureDrop());
            }
        }
    }

    private Pipe findConnectingPipe(Node from, Node to) {
        for (Pipe pipe : pipes) {
            if (from.getOutgoingPipes().contains(pipe) && to.getIncomingPipes().contains(pipe)) {
                return pipe;
            }
        }
        return null;
    }

    /**
     * Prints the network simulation results.
     */
    public void printResults() {
        System.out.println("Hydraulic Network Simulation Results:");
        System.out.println("------------------------------------");
        
        for (Node node : nodes) {
            System.out.printf("Node %s: Pressure = %.2f kPa%n", node.getId(), node.getPressure());
        }
        
        System.out.println();
        
        for (Pipe pipe : pipes) {
            System.out.printf("Pipe %s: Flow Rate = %.2f m³/s, Pressure Drop = %.2f kPa%n",
                    pipe.getId(), pipe.getFlowRate(), pipe.getPressureDrop());
        }
    }

    public static void main(String[] args) {
        HydraulicNetworkModel model = new HydraulicNetworkModel();

        // Create nodes
        Node source = new Node("Source");
        Node junction1 = new Node("Junction1");
        Node sink = new Node("Sink");

        // Create pipes
        Pipe pipe1 = new Pipe("Pipe1", 100, 0.1, 0.0001);
        Pipe pipe2 = new Pipe("Pipe2", 50, 0.08, 0.0001);

        // Build network
        model.addNode(source);
        model.addNode(junction1);
        model.addNode(sink);

        source.addOutgoingPipe(pipe1);
        junction1.addIncomingPipe(pipe1);
        junction1.addOutgoingPipe(pipe2);
        sink.addIncomingPipe(pipe2);

        model.addPipe(pipe1);
        model.addPipe(pipe2);

        // Simulate with initial flow rate of 0.05 m³/s
        model.simulate(0.05);
        model.printResults();
    }
}
```
