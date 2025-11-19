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
/**
 * @file TicoTimer.cpp
 * @brief Implementation of a timer using Hengstler's Tico multifunctional counters
 */

#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <chrono>
#include <thread>

// Mock Tico SDK header (replace with actual SDK header)
#include "TicoSDK.h"

/**
 * @class TicoTimer
 * @brief Wrapper class for Hengstler Tico timer functionality
 */
class TicoTimer {
public:
    /**
     * @brief Constructor initializes the Tico device
     * @param deviceName The name/address of the Tico device
     * @throws std::runtime_error if device initialization fails
     */
    explicit TicoTimer(const std::string& deviceName) {
        // Initialize device connection
        deviceHandle = Tico_OpenDevice(deviceName.c_str());
        if (deviceHandle == nullptr) {
            throw std::runtime_error("Failed to open Tico device: " + deviceName);
        }

        // Configure counter mode (assuming channel 0 for timer)
        if (Tico_SetCounterMode(deviceHandle, 0, TICO_MODE_TIMER) != TICO_SUCCESS) {
            Tico_CloseDevice(deviceHandle);
            throw std::runtime_error("Failed to set timer mode on Tico device");
        }
    }

    /**
     * @brief Destructor cleans up device connection
     */
    ~TicoTimer() {
        if (deviceHandle != nullptr) {
            Tico_CloseDevice(deviceHandle);
        }
    }

    /**
     * @brief Start the timer
     * @throws std::runtime_error if timer start fails
     */
    void start() {
        if (Tico_StartCounter(deviceHandle, 0) != TICO_SUCCESS) {
            throw std::runtime_error("Failed to start Tico timer");
        }
        isRunning = true;
    }

    /**
     * @brief Stop the timer
     * @return Elapsed time in milliseconds
     * @throws std::runtime_error if timer stop fails
     */
    double stop() {
        if (!isRunning) {
            throw std::runtime_error("Timer was not running");
        }

        uint32_t counts;
        if (Tico_StopCounter(deviceHandle, 0, &counts) != TICO_SUCCESS) {
            throw std::runtime_error("Failed to stop Tico timer");
        }

        isRunning = false;
        return static_cast<double>(counts) / frequencyHz * 1000.0;
    }

    /**
     * @brief Check if timer is running
     * @return True if timer is active
     */
    bool running() const {
        return isRunning;
    }

private:
    TICO_HANDLE deviceHandle = nullptr;
    bool isRunning = false;
    const double frequencyHz = 1000000.0; // Assuming 1MHz counter frequency
};

// Example usage
int main() {
    try {
        // Initialize timer (replace "COM1" with actual device name)
        TicoTimer timer("COM1");

        std::cout << "Starting timer..." << std::endl;
        timer.start();

        // Simulate work (replace with actual operations)
        std::this_thread::sleep_for(std::chrono::seconds(1));

        double elapsed = timer.stop();
        std::cout << "Elapsed time: " << elapsed << " ms" << std::endl;

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
