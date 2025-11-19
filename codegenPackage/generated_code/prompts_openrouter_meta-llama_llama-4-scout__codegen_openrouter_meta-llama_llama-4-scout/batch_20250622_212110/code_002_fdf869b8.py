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
/**
 * @file check_id_validator.cpp
 * @brief Validates a Check ID string.
 */

#include <iostream>
#include <regex>
#include <stdexcept>
#include <string>

/**
 * @brief Validates a Check ID string.
 * 
 * The Check ID string is considered valid if it matches the following format:
 * - It starts with "CHK" or "chk".
 * - It is followed by a 10-digit number.
 * 
 * @param checkId The Check ID string to validate.
 * @return True if the Check ID string is valid, false otherwise.
 */
bool validateCheckId(const std::string& checkId) {
    // Regular expression pattern to match the Check ID format
    static const std::regex pattern("^([cC][hH][kK])\\d{10}$");

    // Use the regex_match function to check if the entire string matches the pattern
    return std::regex_match(checkId, pattern);
}

/**
 * @brief Parses a Check ID string and extracts its components.
 * 
 * @param checkId The Check ID string to parse.
 * @param[out] prefix The prefix of the Check ID string (e.g., "CHK" or "chk").
 * @param[out] number The 10-digit number part of the Check ID string.
 * 
 * @return True if the Check ID string is valid and parsed successfully, false otherwise.
 */
bool parseCheckId(const std::string& checkId, std::string& prefix, std::string& number) {
    // Regular expression pattern to match the Check ID format
    static const std::regex pattern("^([cC][hH][kK])(\\d{10})$");

    // Use the regex_match function to check if the entire string matches the pattern
    std::smatch match;
    if (std::regex_match(checkId, match, pattern)) {
        // Extract the prefix and number from the match
        prefix = match[1].str();
        number = match[2].str();
        return true;
    }

    return false;
}

int main() {
    try {
        std::string checkId = "CHK1234567890";
        if (validateCheckId(checkId)) {
            std::cout << "Check ID is valid." << std::endl;

            std::string prefix;
            std::string number;
            if (parseCheckId(checkId, prefix, number)) {
                std::cout << "Prefix: " << prefix << std::endl;
                std::cout << "Number: " << number << std::endl;
            } else {
                std::cerr << "Failed to parse Check ID." << std::endl;
            }
        } else {
            std::cerr << "Invalid Check ID." << std::endl;
        }
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
