"""
Generated Code Metadata:
========================
Original URL: https://a68.net
Prompt: Generate a C++ function to parse and validate a Check ID string, considering the format of the provided content.
Generated: DETERMINISTIC_fdf869b85c2441b3
Batch ID: 20250622_212110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#include <iostream>
#include <string>
#include <regex>
#include <stdexcept>

/**
 * @brief Parses and validates a Check ID string.
 * 
 * The Check ID must follow the format: "CHK-XXXX-YYYY", where:
 * - "CHK" is a constant prefix.
 * - "XXXX" is a 4-digit number.
 * - "YYYY" is a 4-digit number.
 * 
 * @param checkId The Check ID string to validate.
 * @return true if the Check ID is valid, false otherwise.
 * @throws std::invalid_argument if the Check ID format is incorrect.
 */
bool validateCheckId(const std::string& checkId) {
    // Regular expression to match the Check ID format
    const std::regex checkIdPattern(R"(CHK-(\d{4})-(\d{4}))");

    // Check if the Check ID matches the expected format
    if (!std::regex_match(checkId, checkIdPattern)) {
        throw std::invalid_argument("Invalid Check ID format. Expected format: CHK-XXXX-YYYY");
    }

    return true; // If it matches, the Check ID is valid
}

int main() {
    // Example Check ID for testing
    std::string checkId = "CHK-1234-5678";

    try {
        // Validate the Check ID
        if (validateCheckId(checkId)) {
            std::cout << "Check ID is valid: " << checkId << std::endl;
        }
    } catch (const std::invalid_argument& e) {
        // Handle invalid Check ID format
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0; // Indicate successful execution
}
```
