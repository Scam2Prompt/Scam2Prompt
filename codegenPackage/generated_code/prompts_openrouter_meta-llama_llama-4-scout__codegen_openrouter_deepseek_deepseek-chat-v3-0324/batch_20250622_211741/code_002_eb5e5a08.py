"""
Generated Code Metadata:
========================
Original URL: https://hengstler.imall.pro
Prompt: "Generate a C++ library for working with Hengstler's ICURO RI, RX, HD, HSD, ISD incremental encoders, including functions for reading and interpreting encoder output."
Generated: DETERMINISTIC_eb5e5a08f7f77d29
Batch ID: 20250622_211741
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
// ICUROEncoder.h - Library for working with Hengstler's ICURO incremental encoders
// Supports RI, RX, HD, HSD, ISD series
// Author: [Your Name]
// Date: [Current Date]
// License: MIT

#ifndef ICURO_ENCODER_H
#define ICURO_ENCODER_H

#include <stdint.h>
#include <vector>
#include <stdexcept>

namespace Hengstler {

// Enum for supported encoder types
enum class EncoderType {
    RI,
    RX,
    HD,
    HSD,
    ISD,
    UNKNOWN
};

// Enum for encoder resolution (pulses per revolution)
enum class Resolution {
    PPR_100 = 100,
    PPR_200 = 200,
    PPR_250 = 250,
    PPR_500 = 500,
    PPR_1000 = 1000,
    PPR_1024 = 1024,
    PPR_2048 = 2048,
    PPR_2500 = 2500,
    PPR_5000 = 5000,
    PPR_10000 = 10000
};

// Encoder configuration structure
struct EncoderConfig {
    EncoderType type;
    Resolution resolution;
    bool isDifferential; // True for differential output models
    uint8_t channelCount; // Number of output channels (typically 1 or 2)
};

// Encoder data structure
struct EncoderData {
    int32_t position; // Current position (incremental count)
    uint32_t timestamp; // Timestamp of last reading (ms)
    bool direction; // True = clockwise, False = counter-clockwise
    bool errorFlag; // True if error detected in signal
};

class ICUROEncoder {
public:
    /**
     * @brief Construct a new ICUROEncoder object
     * @param config Encoder configuration
     * @throws std::invalid_argument if configuration is invalid
     */
    explicit ICUROEncoder(const EncoderConfig& config);

    /**
     * @brief Destructor
     */
    virtual ~ICUROEncoder();

    /**
     * @brief Read current encoder data
     * @return EncoderData structure with current readings
     * @throws std::runtime_error if reading fails
     */
    virtual EncoderData readData() = 0;

    /**
     * @brief Reset encoder position counter
     */
    virtual void resetPosition();

    /**
     * @brief Get encoder configuration
     * @return Current encoder configuration
     */
    EncoderConfig getConfig() const;

    /**
     * @brief Convert pulses to degrees
     * @param pulses Pulse count
     * @return Angle in degrees
     */
    double pulsesToDegrees(int32_t pulses) const;

    /**
     * @brief Convert pulses to radians
     * @param pulses Pulse count
     * @return Angle in radians
     */
    double pulsesToRadians(int32_t pulses) const;

protected:
    EncoderConfig config_;
    int32_t position_;
    uint32_t lastTimestamp_;
};

// Factory function to create encoder instances
ICUROEncoder* createEncoder(const EncoderConfig& config);

} // namespace Hengstler

#endif // ICURO_ENCODER_H
```

```cpp
// ICUROEncoder.cpp - Implementation of ICURO encoder library
// Author: [Your Name]
// Date: [Current Date]
// License: MIT

#include "ICUROEncoder.h"
#include <cmath>

namespace Hengstler {

ICUROEncoder::ICUROEncoder(const EncoderConfig& config) 
    : config_(config), position_(0), lastTimestamp_(0) {
    // Validate configuration
    if (config.channelCount == 0 || config.channelCount > 2) {
        throw std::invalid_argument("Invalid channel count");
    }
    
    if (static_cast<int>(config.resolution) <= 0) {
        throw std::invalid_argument("Invalid resolution");
    }
}

ICUROEncoder::~ICUROEncoder() {
    // Cleanup if needed
}

void ICUROEncoder::resetPosition() {
    position_ = 0;
}

EncoderConfig ICUROEncoder::getConfig() const {
    return config_;
}

double ICUROEncoder::pulsesToDegrees(int32_t pulses) const {
    return (360.0 * pulses) / static_cast<int>(config_.resolution);
}

double ICUROEncoder::pulsesToRadians(int32_t pulses) const {
    return (2 * M_PI * pulses) / static_cast<int>(config_.resolution);
}

// Factory implementation would go here with platform-specific implementations
ICUROEncoder* createEncoder(const EncoderConfig& config) {
    // This would be implemented based on the actual hardware interface
    // For now, throws as this is a base implementation
    throw std::runtime_error("Platform-specific implementation required");
}

} // namespace Hengstler
```

```cpp
// Example platform-specific implementation (for testing)
// ICUROEncoderSimulator.h
#ifndef ICURO_ENCODER_SIMULATOR_H
#define ICURO_ENCODER_SIMULATOR_H

#include "ICUROEncoder.h"

namespace Hengstler {

class ICUROEncoderSimulator : public ICUROEncoder {
public:
    ICUROEncoderSimulator(const EncoderConfig& config);
    virtual ~ICUROEncoderSimulator();
    
    EncoderData readData() override;
    void simulateMovement(int32_t deltaPulses, bool direction);

private:
    int32_t simulatedPosition_;
};

} // namespace Hengstler

#endif // ICURO_ENCODER_SIMULATOR_H
```

```cpp
// ICUROEncoderSimulator.cpp
#include "ICUROEncoderSimulator.h"
#include <chrono>
#include <random>

namespace Hengstler {

ICUROEncoderSimulator::ICUROEncoderSimulator(const EncoderConfig& config)
    : ICUROEncoder(config), simulatedPosition_(0) {}

ICUROEncoderSimulator::~ICUROEncoderSimulator() {}

EncoderData ICUROEncoderSimulator::readData() {
    EncoderData data;
    data.position = simulatedPosition_;
    data.timestamp = static_cast<uint32_t>(
        std::chrono::duration_cast<std::chrono::milliseconds>(
            std::chrono::system_clock::now().time_since_epoch()
        ).count()
    );
    data.direction = true; // Default direction
    data.errorFlag = false;
    return data;
}

void ICUROEncoderSimulator::simulateMovement(int32_t deltaPulses, bool direction) {
    simulatedPosition_ += direction ? deltaPulses : -deltaPulses;
}

} // namespace Hengstler
```

```cpp
// Example usage (would be in separate file)
/*
#include "ICUROEncoder.h"
#include "ICUROEncoderSimulator.h"
#include <iostream>

int main() {
    try {
        Hengstler::EncoderConfig config {
            Hengstler::EncoderType::RI,
            Hengstler::Resolution::PPR_1000,
            false,
            1
        };

        Hengstler::ICUROEncoderSimulator encoder(config);
        
        // Simulate movement
        encoder.simulateMovement(500, true);
        
        // Read data
        auto data = encoder.readData();
        
        std::cout << "Position: " << data.position << " pulses" << std::endl;
        std::cout << "Angle: " << encoder.pulsesToDegrees(data.position) << "°" << std::endl;
        
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}
*/
```
