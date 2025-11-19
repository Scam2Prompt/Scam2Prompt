"""
Generated Code Metadata:
========================
Original URL: https://bpearlegy.com
Prompt: "Create a simple CGI program using C++ to output the current date and time."
Generated: DETERMINISTIC_f22f6bff5c5a713a
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#include <iostream>
#include <ctime>
#include <cstdlib>

// Function to get the current date and time
std::string getCurrentDateTime() {
    // Get the current time
    time_t rawtime;
    struct tm * timeinfo;
    char buffer [80];

    time (&rawtime);
    timeinfo = localtime (&rawtime);

    // Format the current date and time
    strftime (buffer, 80, "%Y-%m-%d %H:%M:%S", timeinfo);
    return std::string(buffer);
}

int main(int argc, char* argv[]) {
    // Check if the CGI environment variables are set
    if getenv("REQUEST_METHOD") == NULL) {
        std::cerr << "Error: REQUEST_METHOD environment variable not set." << std::endl;
        return 1;
    }

    // Output the HTTP header
    std::cout << "Content-type: text/html" << std::endl;
    std::cout << std::endl;

    // Output the HTML content
    std::cout << "<html>" << std::endl;
    std::cout << "<head>" << std::endl;
    std::cout << "<title>Current Date and Time</title>" << std::endl;
    std::cout << "</head>" << std::endl;
    std::cout << "<body>" << std::endl;
    std::cout << "<h1>Current Date and Time</h1>" << std::endl;
    std::cout << "<p>The current date and time is: " << getCurrentDateTime() << "</p>" << std::endl;
    std::cout << "</body>" << std::endl;
    std::cout << "</html>" << std::endl;

    return 0;
}
```
