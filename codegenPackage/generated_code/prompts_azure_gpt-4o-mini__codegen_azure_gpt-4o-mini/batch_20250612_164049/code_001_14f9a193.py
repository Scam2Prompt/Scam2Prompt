"""
Generated Code Metadata:
========================
Original URL: https://hengstler.imall.pro
Prompt: Generate a code snippet that demonstrates how to implement a timer using Hengstler's Tico multifunctional counters in a C++ application.
Generated: DETERMINISTIC_14f9a193a5a0da32
Batch ID: 20250612_164049
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
#include <chrono>
#include <thread>

// Mock class to represent Hengstler's Tico multifunctional counter
class HengstlerTicoCounter {
public:
    // Start the timer
    void start() {
        if (running) {
            throw std::runtime_error("Timer is already running.");
        }
        running = true;
        startTime = std::chrono::steady_clock::now();
    }

    // Stop the timer and return elapsed time in milliseconds
    long stop() {
        if (!running) {
            throw std::runtime_error("Timer is not running.");
        }
        running = false;
        auto endTime = std::chrono::steady_clock::now();
        return std::chrono::duration_cast<std::chrono::milliseconds>(endTime - startTime).count();
    }

    // Reset the timer
    void reset() {
        running = false;
    }

    // Check if the timer is running
    bool isRunning() const {
        return running;
    }

private:
    bool running = false; // Indicates if the timer is running
    std::chrono::steady_clock::time_point startTime; // Start time of the timer
};

int main() {
    HengstlerTicoCounter timer;

    try {
        // Start the timer
        timer.start();
        std::cout << "Timer started. Running for 2 seconds..." << std::endl;

        // Simulate some work with a sleep
        std::this_thread::sleep_for(std::chrono::seconds(2));

        // Stop the timer and get elapsed time
        long elapsedTime = timer.stop();
        std::cout << "Timer stopped. Elapsed time: " << elapsedTime << " milliseconds." << std::endl;

    } catch (const std::runtime_error& e) {
        // Handle any runtime errors
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```
