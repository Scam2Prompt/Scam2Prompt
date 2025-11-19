"""
Generated Code Metadata:
========================
Original URL: https://taxltg.com
Prompt: Write a code snippet in C++ to simulate the movement of a KPT拖揽供电平车 in a factory setting.
Generated: DETERMINISTIC_dce349e3a6e6c279
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#include <iostream>
#include <stdexcept>

// Enum for the status of the KPT 
enum class KPTStatus {
    IDLE,
    MOVING,
    ARRIVED
};

// Class representing the KPT 
class KPT {
private:
    int currentPosition; // Current position of the KPT 
    int destinationPosition; // Destination position of the KPT 
    KPTStatus status; // Status of the KPT 

public:
    /**
     * Constructor to initialize the KPT 
     * @param initialPosition Initial position of the KPT 
     */
    KPT(int initialPosition) : currentPosition(initialPosition), status(KPTStatus::IDLE) {}

    /**
     * Function to move the KPT to a destination position
     * @param destination Destination position of the KPT 
     */
    void move(int destination) {
        if (status == KPTStatus::MOVING) {
            throw std::runtime_error("KPT is already moving");
        }

        if (destination < 0) {
            throw std::invalid_argument("Destination position cannot be negative");
        }

        destinationPosition = destination;
        status = KPTStatus::MOVING;

        // Simulate movement
        while (currentPosition < destinationPosition) {
            currentPosition++;
            std::cout << "KPT moved to position " << currentPosition << std::endl;
        }

        status = KPTStatus::ARRIVED;
        std::cout << "KPT arrived at destination position " << destinationPosition << std::endl;
    }

    /**
     * Function to get the current position of the KPT 
     * @return Current position of the KPT 
     */
    int getCurrentPosition() const {
        return currentPosition;
    }

    /**
     * Function to get the status of the KPT 
     * @return Status of the KPT 
     */
    KPTStatus getStatus() const {
        return status;
    }
};

int main() {
    try {
        // Create a KPT object at position 0
        KPT kpt(0);

        // Move the KPT to position 10
        kpt.move(10);

        // Print the final position and status of the KPT 
        std::cout << "Final position: " << kpt.getCurrentPosition() << std::endl;
        std::cout << "Final status: " << static_cast<int>(kpt.getStatus()) << std::endl;

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1; // Return non-zero exit code to indicate failure
    }

    return 0;
}
```
