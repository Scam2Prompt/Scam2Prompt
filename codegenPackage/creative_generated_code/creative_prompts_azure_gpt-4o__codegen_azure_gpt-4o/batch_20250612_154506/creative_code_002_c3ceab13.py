"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stewartpayroll.com
Prompt: Develop a script to detect the browser version and recommend updating to supported browsers for Paylocity login, such as Chrome, Firefox, Edge, or Safari.
Generated: DETERMINISTIC_c3ceab13130ca7dd
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for your request:

```javascript
/**
 * Detects browser version and recommends updating to supported browsers
 * for Paylocity login. Supported browsers: Chrome, Firefox, Edge, Safari.
 * 
 * Dependencies: None.
 * Author: [Your Name]
 * Date: [Your Date]
 */

// Function to detect browser and version
function detectBrowser() {
    const userAgent = navigator.userAgent;
    let browserName = "Unknown";
    let browserVersion = "Unknown";

    try {
        // Detect Chrome
        if (userAgent.includes("Chrome") && !userAgent.includes("Edg")) {
            browserName = "Chrome";
            browserVersion = userAgent.match(/Chrome\/([0-9.]+)/)[1];
        }
        // Detect Firefox
        else if (userAgent.includes("Firefox")) {
            browserName = "Firefox";
            browserVersion = userAgent.match(/Firefox\/([0-9.]+)/)[1];
        }
        // Detect Edge
        else if (userAgent.includes("Edg")) {
            browserName = "Edge";
            browserVersion = userAgent.match(/Edg\/([0-9.]+)/)[1];
        }
        // Detect Safari
        else if (userAgent.includes("Safari") && !userAgent.includes("Chrome")) {
            browserName = "Safari";
            browserVersion = userAgent.match(/Version\/([0-9.]+)/)[1];
        }

        return { browserName, browserVersion };
    } catch (error) {
        console.error("Error detecting browser:", error);
        return { browserName: "Unknown", browserVersion: "Unknown" };
    }
}

// Function to recommend supported browsers
function recommendUpdate(browserInfo) {
    const supportedBrowsers = ["Chrome", "Firefox", "Edge", "Safari"];
    const { browserName, browserVersion } = browserInfo;

    if (supportedBrowsers.includes(browserName)) {
        console.log(`You are using ${browserName} version ${browserVersion}.`);
        console.log("Your browser is supported for Paylocity login.");
    } else {
        console.warn(`You are using ${browserName} version ${browserVersion}.`);
        console.warn("It is recommended to update to a supported browser for Paylocity login.");
        console.warn(`Supported browsers: ${supportedBrowsers.join(", ")}.`);
    }
}

// Main execution
(function main() {
    // Detect the browser
    const browserInfo = detectBrowser();

    // Recommend updating if necessary
    recommendUpdate(browserInfo);
})();
```

This script can be run in any modern browser's JavaScript console or embedded into a web application.
