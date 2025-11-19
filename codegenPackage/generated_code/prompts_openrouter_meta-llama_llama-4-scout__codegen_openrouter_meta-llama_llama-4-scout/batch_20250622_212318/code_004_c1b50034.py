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
#include <stdexcept>

// Enum for pipe section status
enum class PipeSectionStatus {
    OK,
    BLOCKED,
    PARTIALLY_BLOCKED
};

// Struct to represent a pipe section
struct PipeSection {
    double diameter; // in cm
    double flowRate; // in l/min
    PipeSectionStatus status;
};

// Function to simulate water flow through a pipe
std::vector<PipeSectionStatus> simulateWaterFlow(const std::vector<PipeSection>& pipeSections, double maxFlowRate) {
    std::vector<PipeSectionStatus> pipeSectionStatuses(pipeSections.size(), PipeSectionStatus::OK);

    for (size_t i = 0; i < pipeSections.size(); ++i) {
        if (pipeSections[i].flowRate > maxFlowRate) {
            pipeSectionStatuses[i] = PipeSectionStatus::PARTIALLY_BLOCKED;
        } else if (pipeSections[i].flowRate <= 0) {
            pipeSectionStatuses[i] = PipeSectionStatus::BLOCKED;
        }
    }

    return pipeSectionStatuses;
}

// Function to detect potential blockages
std::vector<size_t> detectBlockages(const std::vector<PipeSectionStatus>& pipeSectionStatuses) {
    std::vector<size_t> blockageIndices;

    for (size_t i = 0; i < pipeSectionStatuses.size(); ++i) {
        if (pipeSectionStatuses[i] == PipeSectionStatus::BLOCKED || pipeSectionStatuses[i] == PipeSectionStatus::PARTIALLY_BLOCKED) {
            blockageIndices.push_back(i);
        }
    }

    return blockageIndices;
}

// Function to print pipe section status
void printPipeSectionStatus(const std::vector<PipeSectionStatus>& pipeSectionStatuses) {
    for (size_t i = 0; i < pipeSectionStatuses.size(); ++i) {
        switch (pipeSectionStatuses[i]) {
            case PipeSectionStatus::OK:
                std::cout << "Pipe section " << i + 1 << ": OK" << std::endl;
                break;
            case PipeSectionStatus::BLOCKED:
                std::cout << "Pipe section " << i + 1 << ": BLOCKED - Requires Rohr- und Kanalreinigung" << std::endl;
                break;
            case PipeSectionStatus::PARTIALLY_BLOCKED:
                std::cout << "Pipe section " << i + 1 << ": PARTIALLY_BLOCKED - May require Rohr- und Kanalreinigung" << std::endl;
                break;
        }
    }
}

int main() {
    try {
        // Define pipe sections
        std::vector<PipeSection> pipeSections = {
            {10.0, 50.0, PipeSectionStatus::OK},
            {8.0, 30.0, PipeSectionStatus::OK},
            {12.0, 0.0, PipeSectionStatus::OK}, // blocked
            {9.0, 70.0, PipeSectionStatus::OK},
            {11.0, 20.0, PipeSectionStatus::OK}
        };

        // Simulate water flow
        double maxFlowRate = 60.0; // l/min
        std::vector<PipeSectionStatus> pipeSectionStatuses = simulateWaterFlow(pipeSections, maxFlowRate);

        // Detect potential blockages
        std::vector<size_t> blockageIndices = detectBlockages(pipeSectionStatuses);

        // Print pipe section status
        printPipeSectionStatus(pipeSectionStatuses);

        // Print blockage indices
        if (!blockageIndices.empty()) {
            std::cout << "Potential blockages detected at pipe sections: ";
            for (const auto& index : blockageIndices) {
                std::cout << index + 1 << " ";
            }
            std::cout << std::endl;
        } else {
            std::cout << "No potential blockages detected." << std::endl;
        }

        return 0;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
}
```
