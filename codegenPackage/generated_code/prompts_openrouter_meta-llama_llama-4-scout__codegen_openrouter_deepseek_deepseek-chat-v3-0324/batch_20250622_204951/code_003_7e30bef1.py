"""
Generated Code Metadata:
========================
Original URL: https://ysc.com.br
Prompt: "Develop a simple algorithm to determine the quality control measures for YSC's menthol products, and provide a code example in C++ to implement this algorithm."
Generated: DETERMINISTIC_7e30bef1b9289ada
Batch ID: 20250622_204951
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
#include <stdexcept>
#include <cmath>

// Quality thresholds for menthol products
const double MIN_PURITY = 98.5;  // Minimum purity percentage
const double MAX_MOISTURE = 0.5; // Maximum moisture percentage
const double MAX_IMPURITIES = 1.0; // Maximum impurities percentage
const double MIN_MENTHOL_CONTENT = 95.0; // Minimum menthol content percentage

/**
 * Structure representing quality control test results
 */
struct QualityTestResults {
    double purity;
    double moisture;
    double impurities;
    double mentholContent;
    std::string batchId;
};

/**
 * Enum representing quality status
 */
enum class QualityStatus {
    PASS,
    FAIL,
    MARGINAL
};

/**
 * Class for quality control evaluation
 */
class MentholQualityControl {
public:
    /**
     * Evaluates the quality of a menthol product batch
     * @param testResults The test results to evaluate
     * @return QualityStatus indicating pass/fail/marginal status
     */
    QualityStatus evaluateQuality(const QualityTestResults& testResults) {
        if (!validateTestResults(testResults)) {
            throw std::invalid_argument("Invalid test results provided");
        }

        bool purityFail = testResults.purity < MIN_PURITY;
        bool moistureFail = testResults.moisture > MAX_MOISTURE;
        bool impuritiesFail = testResults.impurities > MAX_IMPURITIES;
        bool mentholFail = testResults.mentholContent < MIN_MENTHOL_CONTENT;

        if (purityFail || moistureFail || impuritiesFail || mentholFail) {
            return QualityStatus::FAIL;
        }

        // Check for marginal conditions (close to thresholds)
        bool marginalPurity = testResults.purity < (MIN_PURITY + 0.5);
        bool marginalMoisture = testResults.moisture > (MAX_MOISTURE - 0.1);
        bool marginalImpurities = testResults.impurities > (MAX_IMPURITIES - 0.2);
        bool marginalMenthol = testResults.mentholContent < (MIN_MENTHOL_CONTENT + 1.0);

        if (marginalPurity || marginalMoisture || marginalImpurities || marginalMenthol) {
            return QualityStatus::MARGINAL;
        }

        return QualityStatus::PASS;
    }

    /**
     * Generates a quality report for the batch
     * @param testResults The test results to report on
     * @return String containing the quality report
     */
    std::string generateQualityReport(const QualityTestResults& testResults) {
        QualityStatus status = evaluateQuality(testResults);
        std::string report = "Quality Report for Batch: " + testResults.batchId + "\n";
        report += "----------------------------------------\n";
        report += "Purity: " + std::to_string(testResults.purity) + "%\n";
        report += "Moisture: " + std::to_string(testResults.moisture) + "%\n";
        report += "Impurities: " + std::to_string(testResults.impurities) + "%\n";
        report += "Menthol Content: " + std::to_string(testResults.mentholContent) + "%\n";
        report += "----------------------------------------\n";
        
        switch (status) {
            case QualityStatus::PASS:
                report += "STATUS: PASS - All parameters within specifications\n";
                break;
            case QualityStatus::MARGINAL:
                report += "STATUS: MARGINAL - Some parameters close to thresholds\n";
                break;
            case QualityStatus::FAIL:
                report += "STATUS: FAIL - One or more parameters out of specification\n";
                break;
        }

        return report;
    }

private:
    /**
     * Validates that test results are within reasonable ranges
     * @param testResults The results to validate
     * @return true if results are valid, false otherwise
     */
    bool validateTestResults(const QualityTestResults& testResults) {
        if (testResults.batchId.empty()) {
            return false;
        }

        if (testResults.purity < 0 || testResults.purity > 100 ||
            testResults.moisture < 0 || testResults.moisture > 100 ||
            testResults.impurities < 0 || testResults.impurities > 100 ||
            testResults.mentholContent < 0 || testResults.mentholContent > 100) {
            return false;
        }

        return true;
    }
};

// Example usage
int main() {
    try {
        MentholQualityControl qc;

        // Test case 1: Good quality batch
        QualityTestResults goodBatch = {
            99.2,    // purity
            0.3,     // moisture
            0.2,     // impurities
            96.5,    // menthol content
            "BATCH-2023-001"
        };

        // Test case 2: Marginal quality batch
        QualityTestResults marginalBatch = {
            98.6,    // purity
            0.45,    // moisture
            0.9,     // impurities
            95.1,    // menthol content
            "BATCH-2023-002"
        };

        // Test case 3: Failed quality batch
        QualityTestResults failedBatch = {
            97.8,    // purity
            0.6,     // moisture
            1.2,     // impurities
            94.0,    // menthol content
            "BATCH-2023-003"
        };

        std::cout << qc.generateQualityReport(goodBatch) << "\n";
        std::cout << qc.generateQualityReport(marginalBatch) << "\n";
        std::cout << qc.generateQualityReport(failedBatch) << "\n";

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
