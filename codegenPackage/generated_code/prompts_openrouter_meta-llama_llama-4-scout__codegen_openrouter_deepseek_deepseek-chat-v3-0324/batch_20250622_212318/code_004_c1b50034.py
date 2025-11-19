"""
Generated Code Metadata:
========================
Original URL: https://förderohr.de
Prompt: Write a code snippet in C++ to simulate the flow of water through a pipe and detect potential blockages that require Rohr- und Kanalreinigung.
Generated: DETERMINISTIC_c1b50034685f4ae7
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <stdexcept>
#include <limits>

// Constants for water properties and pipe characteristics
const double WATER_DENSITY = 997.0;       // kg/m³
const double DYNAMIC_VISCOSITY = 0.001;   // Pa·s
const double GRAVITY = 9.81;              // m/s²
const double PRESSURE_THRESHOLD = 1.5;    // Pressure increase factor to detect blockage
const double FLOW_RATE_THRESHOLD = 0.7;   // Flow rate reduction factor to detect blockage

class PipeSegment {
public:
    double diameter;    // meters
    double length;      // meters
    double roughness;   // roughness coefficient (dimensionless)
    double pressure;    // Pascals
    double flow_rate;   // m³/s

    PipeSegment(double d, double l, double r, double p, double q)
        : diameter(d), length(l), roughness(r), pressure(p), flow_rate(q) {
        if (diameter <= 0 || length <= 0 || roughness < 0) {
            throw std::invalid_argument("Pipe parameters must be positive");
        }
    }

    // Calculate Reynolds number to determine flow regime
    double calculate_reynolds_number() const {
        if (flow_rate <= 0 || diameter <= 0) return 0.0;
        double velocity = flow_rate / (M_PI * pow(diameter/2, 2));
        return (WATER_DENSITY * velocity * diameter) / DYNAMIC_VISCOSITY;
    }

    // Calculate friction factor using Colebrook equation
    double calculate_friction_factor() const {
        double Re = calculate_reynolds_number();
        if (Re < 1) return 0.0;  // No flow

        double relative_roughness = roughness / diameter;
        double f = 0.0;
        
        // Initial guess for friction factor
        if (Re < 2000) {
            f = 64.0 / Re;  // Laminar flow
        } else {
            // Turbulent flow - Colebrook approximation
            double a = relative_roughness / 3.7;
            double b = 2.51 / Re;
            double x0 = 0.01;  // Initial guess
            double x1 = 0.0;
            double epsilon = 1e-6;
            int max_iter = 100;
            
            for (int i = 0; i < max_iter; ++i) {
                double log_term = log10(a + b * x0);
                x1 = 1.0 / (1.73718 * log_term * log_term);
                
                if (fabs(x1 - x0) < epsilon) break;
                x0 = x1;
            }
            f = x1;
        }
        return f;
    }

    // Calculate pressure drop across the pipe segment
    double calculate_pressure_drop() const {
        double f = calculate_friction_factor();
        double velocity = flow_rate / (M_PI * pow(diameter/2, 2));
        return f * (length / diameter) * (WATER_DENSITY * pow(velocity, 2)) / 2;
    }
};

class PipeSystem {
private:
    std::vector<PipeSegment> segments;
    double initial_pressure;
    double initial_flow_rate;

public:
    PipeSystem(double initial_p, double initial_q)
        : initial_pressure(initial_p), initial_flow_rate(initial_q) {}

    void add_segment(const PipeSegment& segment) {
        segments.push_back(segment);
    }

    // Simulate flow through the pipe system
    void simulate_flow() {
        if (segments.empty()) {
            throw std::runtime_error("No pipe segments in the system");
        }

        double current_pressure = initial_pressure;
        double current_flow_rate = initial_flow_rate;
        double total_pressure_drop = 0.0;

        for (auto& segment : segments) {
            segment.flow_rate = current_flow_rate;
            double pressure_drop = segment.calculate_pressure_drop();
            segment.pressure = current_pressure - pressure_drop;
            total_pressure_drop += pressure_drop;
            current_pressure = segment.pressure;
        }

        analyze_blockages();
    }

    // Detect potential blockages based on pressure and flow rate changes
    void analyze_blockages() const {
        if (segments.size() < 2) return;

        double base_pressure_drop = segments[0].calculate_pressure_drop();
        double base_flow_rate = segments[0].flow_rate;

        for (size_t i = 1; i < segments.size(); ++i) {
            double current_pressure_drop = segments[i].calculate_pressure_drop();
            double current_flow_rate = segments[i].flow_rate;

            // Check for significant pressure increase or flow rate reduction
            if (current_pressure_drop > base_pressure_drop * PRESSURE_THRESHOLD ||
                current_flow_rate < base_flow_rate * FLOW_RATE_THRESHOLD) {
                std::cout << "Warning: Potential blockage detected in segment " << i 
                          << " (Pressure drop: " << current_pressure_drop 
                          << " Pa, Flow rate: " << current_flow_rate << " m³/s)\n";
                std::cout << "Recommendation: Rohr- und Kanalreinigung required\n";
            }

            // Update baseline to current segment for next comparison
            base_pressure_drop = current_pressure_drop;
            base_flow_rate = current_flow_rate;
        }
    }

    // Print system status
    void print_status() const {
        std::cout << "Pipe System Status:\n";
        std::cout << "Initial Pressure: " << initial_pressure << " Pa\n";
        std::cout << "Initial Flow Rate: " << initial_flow_rate << " m³/s\n\n";

        for (size_t i = 0; i < segments.size(); ++i) {
            std::cout << "Segment " << i << ":\n";
            std::cout << "  Diameter: " << segments[i].diameter << " m\n";
            std::cout << "  Length: " << segments[i].length << " m\n";
            std::cout << "  Roughness: " << segments[i].roughness << "\n";
            std::cout << "  Pressure: " << segments[i].pressure << " Pa\n";
            std::cout << "  Flow Rate: " << segments[i].flow_rate << " m³/s\n";
            std::cout << "  Reynolds Number: " << segments[i].calculate_reynolds_number() << "\n";
            std::cout << "  Friction Factor: " << segments[i].calculate_friction_factor() << "\n";
            std::cout << "  Pressure Drop: " << segments[i].calculate_pressure_drop() << " Pa\n\n";
        }
    }
};

int main() {
    try {
        // Create a pipe system with initial conditions
        PipeSystem system(101325.0, 0.05);  // 1 atm pressure, 0.05 m³/s flow

        // Add pipe segments (diameter, length, roughness, initial pressure, initial flow)
        system.add_segment(PipeSegment(0.1, 10.0, 0.00015, 101325.0, 0.05));
        system.add_segment(PipeSegment(0.1, 15.0, 0.00015, 101325.0, 0.05));
        system.add_segment(PipeSegment(0.08, 8.0, 0.0002, 101325.0, 0.05));  // Narrower pipe
        system.add_segment(PipeSegment(0.1, 12.0, 0.00015, 101325.0, 0.05));

        // Simulate flow and detect blockages
        system.simulate_flow();
        system.print_status();

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
