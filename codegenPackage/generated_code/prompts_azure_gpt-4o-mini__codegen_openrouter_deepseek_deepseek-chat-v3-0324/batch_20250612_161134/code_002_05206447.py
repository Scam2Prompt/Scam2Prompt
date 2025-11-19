"""
Generated Code Metadata:
========================
Original URL: https://cloudflare-cftc-us25-eqq.pages.dev
Prompt: Generate a script that prompts users to enable JavaScript and cookies for a seamless experience, inspired by the verification process on namada.foundation.
Generated: DETERMINISTIC_05206447ec1899d3
Batch ID: 20250612_161134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enable JavaScript & Cookies</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: #333;
        }
        .verification-container {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            padding: 2rem;
            max-width: 500px;
            width: 90%;
            text-align: center;
        }
        .verification-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
            color: #e74c3c;
        }
        h1 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }
        p {
            margin-bottom: 1.5rem;
            line-height: 1.5;
        }
        .instructions {
            text-align: left;
            background-color: #f9f9f9;
            padding: 1rem;
            border-radius: 4px;
            margin-bottom: 1.5rem;
        }
        .refresh-btn {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 4px;
            font-size: 1rem;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .refresh-btn:hover {
            background-color: #2980b9;
        }
        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <div class="verification-container" id="verificationContainer">
        <div class="verification-icon">⚠️</div>
        <h1>JavaScript & Cookies Required</h1>
        <p>For a seamless experience, please enable JavaScript and cookies in your browser settings.</p>
        
        <div class="instructions">
            <h3>How to enable:</h3>
            <ol>
                <li><strong>JavaScript:</strong> Check your browser settings under "Site Settings" or "Privacy and Security"</li>
                <li><strong>Cookies:</strong> Ensure cookies are not blocked for this site</li>
                <li>Refresh the page after making changes</li>
            </ol>
        </div>
        
        <button class="refresh-btn" id="refreshBtn">Refresh Page</button>
    </div>

    <div class="verification-container hidden" id="successContainer">
        <div class="verification-icon">✅</div>
        <h1>Verification Complete</h1>
        <p>JavaScript and cookies are enabled. You can now enjoy the full experience.</p>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const verificationContainer = document.getElementById('verificationContainer');
            const successContainer = document.getElementById('successContainer');
            const refreshBtn = document.getElementById('refreshBtn');
            
            // Check if JavaScript is enabled (this code wouldn't run if it wasn't)
            // Check if cookies are enabled
            function areCookiesEnabled() {
                try {
                    document.cookie = 'testCookie=1; SameSite=Lax';
                    return document.cookie.indexOf('testCookie=') !== -1;
                } catch (e) {
                    return false;
                }
            }
            
            // Initial check
            function checkRequirements() {
                if (areCookiesEnabled()) {
                    verificationContainer.classList.add('hidden');
                    successContainer.classList.remove('hidden');
                    
                    // Optionally redirect or continue with the application
                    // window.location.href = '/app';
                }
            }
            
            // Check on page load
            checkRequirements();
            
            // Refresh button handler
            refreshBtn.addEventListener('click', function() {
                checkRequirements();
            });
            
            // Periodically check (every 5 seconds)
            setInterval(checkRequirements, 5000);
        });
    </script>
</body>
</html>
```
