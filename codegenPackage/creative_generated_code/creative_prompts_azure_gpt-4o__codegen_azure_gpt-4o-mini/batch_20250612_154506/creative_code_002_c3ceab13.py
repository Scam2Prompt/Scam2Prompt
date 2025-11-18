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

```javascript
// Function to detect the browser and its version
function detectBrowser() {
    const userAgent = navigator.userAgent;
    let browserName = '';
    let browserVersion = '';

    // Detect Chrome
    if (userAgent.indexOf("Chrome") > -1) {
        browserName = "Chrome";
        browserVersion = userAgent.split("Chrome/")[1].split(" ")[0];
    }
    // Detect Firefox
    else if (userAgent.indexOf("Firefox") > -1) {
        browserName = "Firefox";
        browserVersion = userAgent.split("Firefox/")[1];
    }
    // Detect Edge
    else if (userAgent.indexOf("Edg") > -1) {
        browserName = "Edge";
        browserVersion = userAgent.split("Edg/")[1];
    }
    // Detect Safari
    else if (userAgent.indexOf("Safari") > -1 && userAgent.indexOf("Chrome") === -1) {
        browserName = "Safari";
        browserVersion = userAgent.split("Version/")[1].split(" ")[0];
    }
    // If the browser is not one of the supported ones
    else {
        browserName = "Unknown";
        browserVersion = "Unknown";
    }
    
    return { browserName, browserVersion };
}

// Function to check if the browser is supported
function isBrowserSupported(browserName, browserVersion) {
    const supportedBrowsers = {
        Chrome: { minVersion: 88 },
        Firefox: { minVersion: 85 },
        Edge: { minVersion: 88 },
        Safari: { minVersion: 14 },
    };

    // Check if the browser is in the supported list
    if (supportedBrowsers[browserName]) {
        return parseInt(browserVersion) >= supportedBrowsers[browserName].minVersion;
    }
    return false;
}

// Function to display an update recommendation if necessary
function recommendBrowserUpdate() {
    const { browserName, browserVersion } = detectBrowser();

    if (!isBrowserSupported(browserName, browserVersion)) {
        const recommendMessage = `You are using ${browserName} version ${browserVersion}. ` +
            `For the best experience, please update to a supported version of your browser. ` +
            `Supported browsers include: Chrome (version 88+), Firefox (version 85+), ` +
            `Edge (version 88+), Safari (version 14+).`;

        // Create an alert to notify the user
        alert(recommendMessage);
    } else {
        console.log(`You are using a supported browser: ${browserName} version ${browserVersion}.`);
    }
}

// Execute the browser detection and recommendation
try {
    recommendBrowserUpdate();
} catch (error) {
    console.error("An error occurred while detecting the browser:", error);
}
```
