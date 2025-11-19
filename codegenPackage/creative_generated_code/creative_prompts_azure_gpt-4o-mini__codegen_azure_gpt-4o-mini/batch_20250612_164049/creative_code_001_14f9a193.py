"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hengstler.imall.pro
Prompt: Generate a code snippet that demonstrates how to implement a timer using Hengstler's Tico multifunctional counters in a C++ application.
Generated: DETERMINISTIC_14f9a193a5a0da32
Batch ID: 20250612_164049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cpp
#include <iostream>
#include <stdexcept>
#include <chrono>
#include <thread>

// Abstract class representing a generic Tico counter
class TicoCounter {
public:
    virtual void start() = 0; // Start the timer
    virtual void stop() = 0; // Stop the timer
    virtual long long elapsed() const = 0; // Get elapsed time in milliseconds
    virtual ~TicoCounter() = default; // Virtual destructor for cleanup
};

// Implementation of the TicoCounter using a high-resolution timer
class HengstlerTicoCounter : public TicoCounter {
private:
    std::chrono::steady_clock::time_point startTime;
    std::chrono::steady_clock::time_point endTime;
    bool running;

public:
    HengstlerTicoCounter() : running(false) {}

    // Start the timer
    void start() override {
        if (running) {
            throw std::runtime_error("Timer is already running.");
        }
        startTime = std::chrono::steady_clock::now();
        running = true;
    }

    // Stop the timer
    void stop() override {
        if (!running) {
            throw std::runtime_error("Timer is not running.");
        }
        endTime = std::chrono::steady_clock::now();
        running = false;
    }

    // Get elapsed time in milliseconds
    long long elapsed() const override {
        if (running) {
            auto now = std::chrono::steady_clock::now();
            return std::chrono::duration_cast<std::chrono::milliseconds>(now - startTime).count();
        }
        return std::chrono::duration_cast<std::chrono::milliseconds>(endTime - startTime).count();
    }
};

int main() {
    HengstlerTicoCounter timer;

    try {
        timer.start(); // Start the timer
        std::this_thread::sleep_for(std::chrono::seconds(2)); // Simulate work
        timer.stop(); // Stop the timer

        std::cout << "Elapsed time: " << timer.elapsed() << " ms" << std::endl; // Output elapsed time
    } catch (const std::exception &e) {
        std::cerr << "Error: " << e.what() << std::endl; // Handle any exceptions
    }

    return 0;
}
```
