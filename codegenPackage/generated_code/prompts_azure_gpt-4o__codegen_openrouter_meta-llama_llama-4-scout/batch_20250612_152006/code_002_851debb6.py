"""
Generated Code Metadata:
========================
Original URL: https://lrt-sym.biotic.fi
Prompt: Generate code for a web application that checks browser compatibility and requires JavaScript to load properly, similar to the functionality described on "lrt-sym.biotic.fi."
Generated: DETERMINISTIC_851debb6bac32753
Batch ID: 20250612_152006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Browser Compatibility Checker**
=====================================

### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Browser Compatibility Checker</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <noscript>
        <h1>JavaScript is required to load this page properly.</h1>
    </noscript>
    <div id="compatibility-checker"></div>
    <script src="script.js"></script>
</body>
</html>
```

### styles.css
```css
body {
    font-family: Arial, sans-serif;
    text-align: center;
}

#compatibility-checker {
    margin-top: 20vh;
}

.compatibility-result {
    margin-bottom: 20px;
}

.compatibility-result.pass {
    color: green;
}

.compatibility-result.fail {
    color: red;
}
```

### script.js
```javascript
// Browser Compatibility Checker
class BrowserCompatibilityChecker {
    /**
     * Checks browser compatibility.
     * @returns {Object} Compatibility results.
     */
    checkCompatibility() {
        const results = {};

        // Check JavaScript support
        results.javascript = typeof window !== 'undefined' && typeof window.document !== 'undefined';

        // Check browser version
        results.browserVersion = this.getBrowserVersion();

        // Check for modern browser features
        results.modernBrowser = this.isModernBrowser();

        return results;
    }

    /**
     * Gets the browser version.
     * @returns {String} Browser version.
     */
    getBrowserVersion() {
        const userAgent = navigator.userAgent;
        const browserVersion = userAgent.match(/(Chrome|Firefox|Safari|Edge|OPR|OPMI|rv:)(?:\/| )([\d.]+)/);

        return browserVersion ? browserVersion[2] : 'Unknown';
    }

    /**
     * Checks if the browser is modern.
     * @returns {Boolean} True if the browser is modern, false otherwise.
     */
    isModernBrowser() {
        const browserVersion = this.getBrowserVersion();
        const browserName = navigator.userAgent.match(/(Chrome|Firefox|Safari|Edge|OPR|OPMI)/);

        if (browserName) {
            switch (browserName[0]) {
                case 'Chrome':
                    return parseFloat(browserVersion) >= 80;
                case 'Firefox':
                    return parseFloat(browserVersion) >= 70;
                case 'Safari':
                    return parseFloat(browserVersion) >= 13;
                case 'Edge':
                    return parseFloat(browserVersion) >= 44;
                default:
                    return false;
            }
        }

        return false;
    }
}

// Initialize compatibility checker
const compatibilityChecker = new BrowserCompatibilityChecker();
const results = compatibilityChecker.checkCompatibility();

// Display compatibility results
const compatibilityElement = document.getElementById('compatibility-checker');

if (results.javascript) {
    const javascriptResult = document.createElement('p');
    javascriptResult.classList.add('compatibility-result', 'pass');
    javascriptResult.textContent = 'JavaScript: Supported';
    compatibilityElement.appendChild(javascriptResult);

    const browserVersionResult = document.createElement('p');
    browserVersionResult.classList.add('compatibility-result');
    browserVersionResult.textContent = `Browser Version: ${results.browserVersion}`;
    compatibilityElement.appendChild(browserVersionResult);

    const modernBrowserResult = document.createElement('p');
    if (results.modernBrowser) {
        modernBrowserResult.classList.add('compatibility-result', 'pass');
        modernBrowserResult.textContent = 'Modern Browser: Yes';
    } else {
        modernBrowserResult.classList.add('compatibility-result', 'fail');
        modernBrowserResult.textContent = 'Modern Browser: No';
    }
    compatibilityElement.appendChild(modernBrowserResult);
} else {
    const javascriptError = document.createElement('p');
    javascriptError.classList.add('compatibility-result', 'fail');
    javascriptError.textContent = 'JavaScript: Not supported';
    compatibilityElement.appendChild(javascriptError);
}
```
