"""
Generated Code Metadata:
========================
Original URL: https://hyperionliquidity.com
Prompt: Create a C++ program that simulates the evolution of electronic components, incorporating concepts from "The Evolution of Electronics: From Vacuum Tubes to Modern Microprocessors."
Generated: DETERMINISTIC_712c888623b7a480
Batch ID: 20250612_153925
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
#include <string>
#include <random>
#include <ctime>
#include <memory>
#include <algorithm>
#include <stdexcept>

// Enum representing different eras of electronic components
enum class Era {
    VACUUM_TUBE,
    TRANSISTOR,
    INTEGRATED_CIRCUIT,
    MICROPROCESSOR,
    MODERN
};

// Base class for electronic components
class ElectronicComponent {
protected:
    std::string name;
    Era era;
    double efficiency;
    double reliability;
    double cost;
    double size;

public:
    ElectronicComponent(const std::string& name, Era era, double efficiency, 
                       double reliability, double cost, double size)
        : name(name), era(era), efficiency(efficiency), 
          reliability(reliability), cost(cost), size(size) {}

    virtual ~ElectronicComponent() = default;

    // Virtual method for component operation
    virtual void operate() const {
        std::cout << name << " is operating with efficiency: " << efficiency 
                  << ", reliability: " << reliability << std::endl;
    }

    // Virtual method for mutation
    virtual std::unique_ptr<ElectronicComponent> mutate() const = 0;

    // Getters
    std::string getName() const { return name; }
    Era getEra() const { return era; }
    double getEfficiency() const { return efficiency; }
    double getReliability() const { return reliability; }
    double getCost() const { return cost; }
    double getSize() const { return size; }

    // Method to compare components for evolution
    bool isBetterThan(const ElectronicComponent& other) const {
        return (efficiency > other.efficiency) && 
               (reliability > other.reliability) && 
               (cost < other.cost) && 
               (size < other.size);
    }
};

// Vacuum tube component
class VacuumTube : public ElectronicComponent {
public:
    VacuumTube() 
        : ElectronicComponent("Vacuum Tube", Era::VACUUM_TUBE, 0.3, 0.5, 10.0, 100.0) {}

    void operate() const override {
        std::cout << "Glowing vacuum tube is operating (inefficient but historic!)" << std::endl;
        ElectronicComponent::operate();
    }

    std::unique_ptr<ElectronicComponent> mutate() const override {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_real_distribution<> dis(-0.1, 0.1);

        double newEff = std::clamp(efficiency + dis(gen), 0.1, 0.5);
        double newRel = std::clamp(reliability + dis(gen), 0.3, 0.7);
        double newCost = std::max(1.0, cost + dis(gen) * 5);
        double newSize = std::max(50.0, size + dis(gen) * 20);

        if (newEff > 0.4 && newRel > 0.6 && newCost < 7.0 && newSize < 70.0) {
            return std::make_unique<Transistor>();
        }

        return std::make_unique<VacuumTube>(*this);
    }
};

// Transistor component
class Transistor : public ElectronicComponent {
public:
    Transistor() 
        : ElectronicComponent("Transistor", Era::TRANSISTOR, 0.6, 0.7, 5.0, 10.0) {}

    void operate() const override {
        std::cout << "Transistor is switching (much better than tubes!)" << std::endl;
        ElectronicComponent::operate();
    }

    std::unique_ptr<ElectronicComponent> mutate() const override {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_real_distribution<> dis(-0.1, 0.1);

        double newEff = std::clamp(efficiency + dis(gen), 0.5, 0.8);
        double newRel = std::clamp(reliability + dis(gen), 0.6, 0.9);
        double newCost = std::max(0.5, cost + dis(gen) * 2);
        double newSize = std::max(1.0, size + dis(gen) * 5);

        if (newEff > 0.7 && newRel > 0.8 && newCost < 3.0 && newSize < 5.0) {
            return std::make_unique<IntegratedCircuit>();
        }

        return std::make_unique<Transistor>(*this);
    }
};

// Integrated circuit component
class IntegratedCircuit : public ElectronicComponent {
public:
    IntegratedCircuit() 
        : ElectronicComponent("Integrated Circuit", Era::INTEGRATED_CIRCUIT, 0.8, 0.9, 2.0, 2.0) {}

    void operate() const override {
        std::cout << "Integrated circuit is processing (many transistors in one!)" << std::endl;
        ElectronicComponent::operate();
    }

    std::unique_ptr<ElectronicComponent> mutate() const override {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_real_distribution<> dis(-0.05, 0.05);

        double newEff = std::clamp(efficiency + dis(gen), 0.7, 0.95);
        double newRel = std::clamp(reliability + dis(gen), 0.8, 0.99);
        double newCost = std::max(0.1, cost + dis(gen));
        double newSize = std::max(0.1, size + dis(gen));

        if (newEff > 0.9 && newRel > 0.95 && newCost < 1.0 && newSize < 0.5) {
            return std::make_unique<Microprocessor>();
        }

        return std::make_unique<IntegratedCircuit>(*this);
    }
};

// Microprocessor component
class Microprocessor : public ElectronicComponent {
public:
    Microprocessor() 
        : ElectronicComponent("Microprocessor", Era::MICROPROCESSOR, 0.95, 0.98, 1.0, 0.5) {}

    void operate() const override {
        std::cout << "Microprocessor is computing (the heart of modern computing!)" << std::endl;
        ElectronicComponent::operate();
    }

    std::unique_ptr<ElectronicComponent> mutate() const override {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_real_distribution<> dis(-0.02, 0.02);

        double newEff = std::clamp(efficiency + dis(gen), 0.9, 0.99);
        double newRel = std::clamp(reliability + dis(gen), 0.95, 0.999);
        double newCost = std::max(0.05, cost + dis(gen) * 0.5);
        double newSize = std::max(0.01, size + dis(gen) * 0.1);

        if (newEff > 0.98 && newRel > 0.99 && newCost < 0.2 && newSize < 0.1) {
            return std::make_unique<ModernComponent>();
        }

        return std::make_unique<Microprocessor>(*this);
    }
};

// Modern component
class ModernComponent : public ElectronicComponent {
public:
    ModernComponent() 
        : ElectronicComponent("Modern Nano-component", Era::MODERN, 0.99, 0.999, 0.1, 0.01) {}

    void operate() const override {
        std::cout << "Modern nano-component is operating (cutting edge technology!)" << std::endl;
        ElectronicComponent::operate();
    }

    std::unique_ptr<ElectronicComponent> mutate() const override {
        // Modern components don't evolve further in this simulation
        return std::make_unique<ModernComponent>(*this);
    }
};

// Simulation class
class ElectronicsEvolutionSimulator {
private:
    std::vector<std::unique_ptr<ElectronicComponent>> components;
    int generation;

public:
    ElectronicsEvolutionSimulator() : generation(0) {
        // Start with vacuum tubes
        components.push_back(std::make_unique<VacuumTube>());
    }

    void runSimulation(int generations) {
        if (generations <= 0) {
            throw std::invalid_argument("Number of generations must be positive");
        }

        for (int i = 0; i < generations; ++i) {
            simulateGeneration();
        }
    }

    void printCurrentState() const {
        std::cout << "\nGeneration " << generation << ":\n";
        for (const auto& comp : components) {
            comp->operate();
        }
    }

private:
    void simulateGeneration() {
        generation++;
        
        // Mutate each component
        for (auto& comp : components) {
            auto mutated = comp->mutate();
            comp = std::move(mutated);
