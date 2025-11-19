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
#include <numeric>

// Quality Control Class
class QualityControl {
private:
    std::vector<double> productSamples; // Stores the quality scores of samples
    double acceptableThreshold;         // Minimum acceptable quality score

public:
    // Constructor
    QualityControl(double threshold) : acceptableThreshold(threshold) {
        if (threshold <= 0) {
            throw std::invalid_argument("Threshold must be greater than zero.");
        }
    }

    // Add a sample quality score
    void addSample(double score) {
        if (score < 0 || score > 100) {
            throw std::out_of_range("Quality score must be between 0 and 100.");
        }
        productSamples.push_back(score);
    }

    // Calculate the average quality score
    double calculateAverage() const {
        if (productSamples.empty()) {
            throw std::runtime_error("No samples available to calculate average.");
        }
        return std::accumulate(productSamples.begin(), productSamples.end(), 0.0) / productSamples.size();
    }

    // Determine if the batch passes quality control
    bool isBatchAcceptable() const {
        double averageScore = calculateAverage();
        return averageScore >= acceptableThreshold;
    }

    // Display quality control results
    void displayResults() const {
        try {
            double averageScore = calculateAverage();
            std::cout << "Average Quality Score: " << averageScore << std::endl;
            std::cout << "Batch Status: " << (isBatchAcceptable() ? "Acceptable" : "Rejected") << std::endl;
        } catch (const std::exception& e) {
            std::cerr << "Error: " << e.what() << std::endl;
        }
    }
};

int main() {
    try {
        // Initialize QualityControl with an acceptable threshold
        QualityControl qc(75.0);

        // Add sample quality scores
        qc.addSample(80.5);
        qc.addSample(72.3);
        qc.addSample(78.0);
        qc.addSample(85.0);

        // Display the results
        qc.displayResults();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1; // Return non-zero exit code for error
    }

    return 0; // Return zero exit code for success
}
```
