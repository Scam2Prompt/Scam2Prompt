"""
Generated Code Metadata:
========================
Original URL: https://evinblue.com
Prompt: Write a code example in C++ or Java to simulate the SCR technology process, including the conversion of NOx emissions into harmless nitrogen and steam using DEF.
Generated: DETERMINISTIC_4ad44c2f121ba885
Batch ID: 20250622_210655
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

class DEFInjector {
private:
    double injectionRate; // ml/s
    double defTankLevel; // ml

public:
    DEFInjector(double initialLevel) : defTankLevel(initialLevel), injectionRate(0.0) {}

    void setInjectionRate(double rate) {
        if (rate < 0) {
            throw std::invalid_argument("Injection rate cannot be negative");
        }
        injectionRate = rate;
    }

    double getInjectionRate() const {
        return injectionRate;
    }

    double getDEFLevel() const {
        return defTankLevel;
    }

    void consumeDEF(double duration) {
        double consumed = injectionRate * duration;
        if (consumed > defTankLevel) {
            throw std::runtime_error("Not enough DEF in tank");
        }
        defTankLevel -= consumed;
    }

    void refillDEF(double amount) {
        if (amount < 0) {
            throw std::invalid_argument("Refill amount cannot be negative");
        }
        defTankLevel += amount;
    }
};

class NOxSensor {
private:
    double noxConcentration; // ppm

public:
    NOxSensor(double initialConcentration) : noxConcentration(initialConcentration) {}

    double getNOxConcentration() const {
        return noxConcentration;
    }

    void setNOxConcentration(double concentration) {
        if (concentration < 0) {
            throw std::invalid_argument("NOx concentration cannot be negative");
        }
        noxConcentration = concentration;
    }
};

class Catalyst {
private:
    double temperature; // Celsius
    const double optimalTempMin = 200.0;
    const double optimalTempMax = 450.0;

public:
    Catalyst(double initialTemp) : temperature(initialTemp) {}

    double getTemperature() const {
        return temperature;
    }

    void setTemperature(double temp) {
        temperature = temp;
    }

    bool isOptimalTemperature() const {
        return temperature >= optimalTempMin && temperature <= optimalTempMax;
    }

    double reduceNOx(double noxInput, double defAmount) {
        if (!isOptimalTemperature()) {
            return noxInput; // No reduction if catalyst isn't at optimal temp
        }
        
        // Simplified reduction model: DEF effectively reduces NOx proportionally
        double reductionEfficiency = 0.9; // 90% reduction efficiency
        double maxReduction = noxInput * reductionEfficiency;
        double actualReduction = std::min(maxReduction, defAmount * 10.0); // 1ml DEF reduces ~10ppm NOx
        
        return noxInput - actualReduction;
    }
};

class SCRSystem {
private:
    DEFInjector defInjector;
    NOxSensor noxSensor;
    Catalyst catalyst;
    const double targetNOxLevel = 50.0; // ppm

public:
    SCRSystem(double initialDEF, double initialNOx, double initialTemp)
        : defInjector(initialDEF), noxSensor(initialNOx), catalyst(initialTemp) {}

    void processExhaust(double duration) {
        try {
            // Get current NOx level
            double currentNOx = noxSensor.getNOxConcentration();
            
            // Calculate required DEF injection rate based on NOx level
            double requiredRate = calculateDEFRate(currentNOx);
            defInjector.setInjectionRate(requiredRate);
            
            // Consume DEF
            defInjector.consumeDEF(duration);
            
            // Process NOx reduction
            double reducedNOx = catalyst.reduceNOx(currentNOx, requiredRate * duration);
            noxSensor.setNOxConcentration(reducedNOx);
            
            // Log system status
            logSystemStatus(duration);
        } catch (const std::exception& e) {
            std::cerr << "SCR System Error: " << e.what() << std::endl;
        }
    }

    void logSystemStatus(double duration) const {
        std::cout << "SCR System Status:" << std::endl;
        std::cout << "  Duration: " << duration << "s" << std::endl;
        std::cout << "  DEF Level: " << defInjector.getDEFLevel() << "ml" << std::endl;
        std::cout << "  DEF Injection Rate: " << defInjector.getInjectionRate() << "ml/s" << std::endl;
        std::cout << "  NOx Concentration: " << noxSensor.getNOxConcentration() << "ppm" << std::endl;
        std::cout << "  Catalyst Temp: " << catalyst.getTemperature() << "°C" << std::endl;
        std::cout << "  Catalyst Optimal: " << (catalyst.isOptimalTemperature() ? "Yes" : "No") << std::endl;
        std::cout << std::endl;
    }

    double calculateDEFRate(double noxLevel) const {
        if (noxLevel <= targetNOxLevel) {
            return 0.0; // No DEF needed if NOx is already at target
        }
        
        // Simplified calculation: 1ml DEF reduces ~10ppm NOx per second
        double excessNOx = noxLevel - targetNOxLevel;
        return excessNOx / 10.0;
    }

    void refillDEF(double amount) {
        defInjector.refillDEF(amount);
    }

    void setCatalystTemperature(double temp) {
        catalyst.setTemperature(temp);
    }

    void setNOxLevel(double level) {
        noxSensor.setNOxConcentration(level);
    }
};

int main() {
    // Initialize SCR system with 5000ml DEF, 300ppm NOx, and 250°C catalyst
    SCRSystem scrSystem(5000.0, 300.0, 250.0);
    
    // Simulate exhaust processing for 10 seconds
    for (int i = 0; i < 10; ++i) {
        scrSystem.processExhaust(1.0);
    }
    
    // Increase NOx level and catalyst temperature
    scrSystem.setNOxLevel(400.0);
    scrSystem.setCatalystTemperature(300.0);
    
    // Process for another 5 seconds
    for (int i = 0; i < 5; ++i) {
        scrSystem.processExhaust(1.0);
    }
    
    // Refill DEF tank
    scrSystem.refillDEF(2000.0);
    
    // Process for final 5 seconds
    for (int i = 0; i < 5; ++i) {
        scrSystem.processExhaust(1.0);
    }
    
    return 0;
}
```
