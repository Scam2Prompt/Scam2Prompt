"""
Generated Code Metadata:
========================
Original URL: https://tabriz3dprint.ir
Prompt: Generate a C++ code for optimizing 3D printing parameters, such as layer thickness and infill density, for printing a specific industrial part using Tabriz 3D Print's FDM technology.
Generated: DETERMINISTIC_047ad9049252d4bd
Batch ID: 20250622_210027
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
#include <algorithm>
#include <limits>
#include <stdexcept>
#include <fstream>
#include <sstream>
#include <string>

// Structure to represent 3D printing parameters
struct PrintingParameters {
    double layerThickness;    // in mm
    double infillDensity;     // percentage (0-100)
    double printSpeed;        // mm/s
    double nozzleTemperature; // °C
    double bedTemperature;    // °C

    PrintingParameters(double lt, double id, double ps, double nt, double bt)
        : layerThickness(lt), infillDensity(id), printSpeed(ps),
          nozzleTemperature(nt), bedTemperature(bt) {}
};

// Structure to represent part quality metrics
struct PartQuality {
    double strength;          // relative strength (0-1)
    double surfaceFinish;     // surface quality (0-1)
    double dimensionalAccuracy; // accuracy (0-1)
    double printTime;         // in minutes

    PartQuality(double s, double sf, double da, double pt)
        : strength(s), surfaceFinish(sf), 
          dimensionalAccuracy(da), printTime(pt) {}
};

// Class to optimize 3D printing parameters
class PrintingOptimizer {
private:
    std::vector<PrintingParameters> parameterHistory;
    std::vector<PartQuality> qualityHistory;
    double targetStrength;
    double targetSurfaceFinish;
    double targetDimensionalAccuracy;
    double maxPrintTime;

    // Objective function to evaluate parameter set
    double evaluateParameters(const PrintingParameters& params) {
        // Simulate printing with these parameters (in a real scenario, this would interface with the printer)
        PartQuality quality = simulatePrint(params);

        // Store history
        parameterHistory.push_back(params);
        qualityHistory.push_back(quality);

        // Calculate score (lower is better)
        double strengthDiff = std::abs(quality.strength - targetStrength);
        double surfaceDiff = std::abs(quality.surfaceFinish - targetSurfaceFinish);
        double accuracyDiff = std::abs(quality.dimensionalAccuracy - targetDimensionalAccuracy);
        double timePenalty = (quality.printTime > maxPrintTime) ? (quality.printTime - maxPrintTime) * 10 : 0;

        return strengthDiff + surfaceDiff + accuracyDiff + timePenalty;
    }

    // Simulate printing (placeholder - in reality this would use actual printer data)
    PartQuality simulatePrint(const PrintingParameters& params) {
        // These formulas are simplified approximations
        double strength = 0.7 * (params.infillDensity / 100.0) * (1.0 - (params.layerThickness / 0.3));
        double surfaceFinish = 1.0 - (params.layerThickness / 0.3);
        double dimensionalAccuracy = 1.0 - (params.printSpeed / 120.0);
        double printTime = 60.0 * (1.0 / params.layerThickness) * (1.0 + params.infillDensity / 100.0);

        return PartQuality(
            std::max(0.0, std::min(1.0, strength)),
            std::max(0.0, std::min(1.0, surfaceFinish)),
            std::max(0.0, std::min(1.0, dimensionalAccuracy)),
            printTime
        );
    }

public:
    PrintingOptimizer(double tStr, double tSf, double tDa, double maxPt)
        : targetStrength(tStr), targetSurfaceFinish(tSf),
          targetDimensionalAccuracy(tDa), maxPrintTime(maxPt) {}

    // Optimize parameters using a simple grid search
    PrintingParameters optimizeParameters() {
        // Parameter ranges
        const std::vector<double> layerThicknesses = {0.1, 0.15, 0.2, 0.25, 0.3};
        const std::vector<double> infillDensities = {20, 30, 40, 50, 60, 70, 80, 90, 100};
        const std::vector<double> printSpeeds = {30, 40, 50, 60, 70, 80, 90, 100};
        const double nozzleTemp = 210.0; // Fixed for this material
        const double bedTemp = 60.0;     // Fixed for this material

        PrintingParameters bestParams(0.1, 20, 30, nozzleTemp, bedTemp);
        double bestScore = std::numeric_limits<double>::max();

        // Grid search through parameter space
        for (double lt : layerThicknesses) {
            for (double id : infillDensities) {
                for (double ps : printSpeeds) {
                    PrintingParameters currentParams(lt, id, ps, nozzleTemp, bedTemp);
                    double currentScore = evaluateParameters(currentParams);

                    if (currentScore < bestScore) {
                        bestScore = currentScore;
                        bestParams = currentParams;
                    }
                }
            }
        }

        return bestParams;
    }

    // Save optimization history to CSV file
    void saveHistoryToCSV(const std::string& filename) {
        std::ofstream file(filename);
        if (!file.is_open()) {
            throw std::runtime_error("Failed to open file for writing");
        }

        // Write header
        file << "LayerThickness,InfillDensity,PrintSpeed,NozzleTemp,BedTemp,Strength,SurfaceFinish,DimensionalAccuracy,PrintTime\n";

        // Write data
        for (size_t i = 0; i < parameterHistory.size(); ++i) {
            const auto& params = parameterHistory[i];
            const auto& quality = qualityHistory[i];

            file << params.layerThickness << ","
                 << params.infillDensity << ","
                 << params.printSpeed << ","
                 << params.nozzleTemperature << ","
                 << params.bedTemperature << ","
                 << quality.strength << ","
                 << quality.surfaceFinish << ","
                 << quality.dimensionalAccuracy << ","
                 << quality.printTime << "\n";
        }
    }
};

int main() {
    try {
        // Set target quality metrics (values between 0 and 1)
        const double targetStrength = 0.8;
        const double targetSurfaceFinish = 0.7;
        const double targetDimensionalAccuracy = 0.9;
        const double maxPrintTime = 180.0; // 3 hours

        PrintingOptimizer optimizer(targetStrength, targetSurfaceFinish, 
                                  targetDimensionalAccuracy, maxPrintTime);

        // Run optimization
        PrintingParameters bestParams = optimizer.optimizeParameters();

        // Output results
        std::cout << "Optimized Printing Parameters:\n";
        std::cout << "Layer Thickness: " << bestParams.layerThickness << " mm\n";
        std::cout << "Infill Density: " << bestParams.infillDensity << "%\n";
        std::cout << "Print Speed: " << bestParams.printSpeed << " mm/s\n";
        std::cout << "Nozzle Temperature: " << bestParams.nozzleTemperature << "°C\n";
        std::cout << "Bed Temperature: " << bestParams.bedTemperature << "°C\n";

        // Save optimization history
        optimizer.saveHistoryToCSV("optimization_history.csv");
        std::cout << "Optimization history saved to optimization_history.csv\n";

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
