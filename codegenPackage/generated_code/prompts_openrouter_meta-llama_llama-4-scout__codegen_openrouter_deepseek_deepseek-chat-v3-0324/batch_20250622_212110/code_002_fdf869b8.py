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
#include <string>
#include <regex>
#include <stdexcept>

/**
 * @brief Validates a Check ID string based on specified format.
 * 
 * The Check ID must adhere to the following format:
 * - Starts with 'CHK'
 * - Followed by exactly 8 digits
 * - Ends with an uppercase letter
 * 
 * @param checkId The Check ID string to validate.
 * @return true if the Check ID is valid, false otherwise.
 * @throws std::invalid_argument if the input string is empty.
 */
bool validateCheckId(const std::string& checkId) {
    if (checkId.empty()) {
        throw std::invalid_argument("Check ID cannot be empty");
    }

    // Regular expression pattern for validation
    const std::regex pattern("^CHK\\d{8}[A-Z]$");
    
    return std::regex_match(checkId, pattern);
}
```
