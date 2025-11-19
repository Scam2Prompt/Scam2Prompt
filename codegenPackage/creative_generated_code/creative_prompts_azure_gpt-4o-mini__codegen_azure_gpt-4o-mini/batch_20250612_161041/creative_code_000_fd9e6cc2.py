"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cqzh5.com
Prompt: How can I enable JavaScript in my mobile browser to access the BTC Pledge site?
Generated: DETERMINISTIC_fd9e6cc232e6763e
Batch ID: 20250612_161041
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enable JavaScript</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        .error-message {
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <h1>Enable JavaScript</h1>
    <p>This page contains instructions to enable JavaScript on your mobile browser to access the BTC Pledge site.</p>

    <div id="instructions">
        <!-- Instructions will be dynamically generated -->
    </div>

    <script>
        // Function to detect the user's browser type
        function detectBrowser() {
            const userAgent = navigator.userAgent;
            let browser = 'Unknown';

            // Check for different mobile browsers
            if (/android/i.test(userAgent)) {
                browser = 'Android';
            } else if (/iPad|iPhone|iPod/.test(userAgent) && !window.MSStream) {
                browser = 'iOS';
            } else if (/windows phone/i.test(userAgent)) {
                browser = 'Windows Phone';
            }

            return browser;
        }

        // Function to provide instructions based on browser type
        function provideInstructions(browser) {
            const instructionsContainer = document.getElementById('instructions');
            let instructions;

            switch (browser) {
                case 'Android':
                    instructions = `
                        <h2>For Android Browsers:</h2>
                        <ol>
                            <li>Open the Chrome app.</li>
                            <li>Tap the three dots in the upper right corner.</li>
                            <li>Select <strong>Settings</strong>.</li>
                            <li>Scroll down to <strong>Site settings</strong>.</li>
                            <li>Tap <strong>JavaScript</strong>.</li>
                            <li>Toggle the switch to enable JavaScript.</li>
                        </ol>
                    `;
                    break;
                case 'iOS':
                    instructions = `
                        <h2>For iOS Browsers:</h2>
                        <ol>
                            <li>Open the Settings app on your device.</li>
                            <li>Scroll down and select <strong>Safari</strong>.</li>
                            <li>Tap <strong>Advanced</strong>.</li>
                            <li>Toggle the switch to enable <strong>JavaScript</strong>.</li>
                        </ol>
                    `;
                    break;
                case 'Windows Phone':
                    instructions = `
                        <h2>For Windows Phone:</h2>
                        <ol>
                            <li>Open the Internet Explorer app.</li>
                            <li>Tap the three dots in the bottom right corner.</li>
                            <li>Select <strong>Settings</strong>.</li>
                            <li>Toggle the switch to enable <strong>JavaScript</strong>.</li>
                        </ol>
                    `;
                    break;
                default:
                    instructions = `<p class="error-message">Unable to detect your browser. Please manually enable JavaScript in your browser settings.</p>`;
            }

            instructionsContainer.innerHTML = instructions;
        }

        // Main execution
        try {
            const browser = detectBrowser();
            provideInstructions(browser);
        } catch (error) {
            console.error('Error detecting browser:', error);
            document.getElementById('instructions').innerHTML = `
                <p class="error-message">
                    An error occurred while trying to provide instructions. Please check your browser settings.
                </p>
            `;
        }
    </script>

</body>
</html>
```
