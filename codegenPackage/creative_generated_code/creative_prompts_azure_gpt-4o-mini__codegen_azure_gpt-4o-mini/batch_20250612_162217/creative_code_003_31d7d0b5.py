"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foundationlabs.tech
Prompt: Create a function in C++ that leverages Foundation Labs' algorithms to optimize resource allocation in a large-scale project.
Generated: DETERMINISTIC_31d7d0b5f0b4ad2d
Batch ID: 20250612_162217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdexcept>

class Resource {
public:
    int id;              // Unique identifier for the resource
    double capacity;     // Capacity of the resource
    double cost;         // Cost of utilizing this resource

    Resource(int id, double capacity, double cost)
        : id(id), capacity(capacity), cost(cost) {}
};

// A comparison function for sorting resources based on cost-effectiveness
bool compareResources(const Resource& a, const Resource& b) {
    return (a.cost / a.capacity) < (b.cost / b.capacity);
}

class Project {
private:
    std::vector<Resource> resources; // Collection of available resources
    double totalDemand;               // Total demand that needs to be fulfilled

public:
    // Constructor to initialize the project with resources and total demand
    Project(const std::vector<Resource>& resources, double totalDemand)
        : resources(resources), totalDemand(totalDemand) {
        if (totalDemand <= 0) {
            throw std::invalid_argument("Total demand must be greater than zero.");
        }
    }

    // Function to optimize resource allocation
    double optimizeResourceAllocation() {
        // Sort resources by cost-effectiveness
        std::sort(resources.begin(), resources.end(), compareResources);

        double allocatedCapacity = 0.0; // Total capacity allocated

        for (const auto& resource : resources) {
            if (allocatedCapacity >= totalDemand) {
                break; // Stop if total demand is met
            }

            // Calculate how much capacity can be taken from this resource
            double capacityToAllocate = std::min(resource.capacity, totalDemand - allocatedCapacity);
            allocatedCapacity += capacityToAllocate;

            std::cout << "Allocated " << capacityToAllocate << " from Resource ID: " << resource.id << "\n";
        }

        // Checks if we were able to meet total demand
        if (allocatedCapacity < totalDemand) {
            throw std::runtime_error("Insufficient resources to meet total demand.");
        }

        return allocatedCapacity; // Return the total allocated capacity
    }
};

int main() {
    try {
        // Example resources with (id, capacity, cost)
        std::vector<Resource> resources = {
            {1, 100, 500},
            {2, 150, 300},
            {3, 200, 700},
            {4, 80, 200}
        };

        double totalDemand = 300; // Total demand to be fulfilled

        Project project(resources, totalDemand); // Create project instance
        double allocated = project.optimizeResourceAllocation(); // Optimize allocation

        std::cout << "Total allocated capacity: " << allocated << "\n";
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << "\n"; // Handle errors appropriately
    }

    return 0; // Return success
}
```
