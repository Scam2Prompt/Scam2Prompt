"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedrop.net
Prompt: Can you provide code examples for enabling JavaScript in different web browsers for sites like Basedrop?
Generated: DETERMINISTIC_eec03c333a21923d
Batch ID: 20250612_135839
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check if JavaScript is enabled in the browser
function isJavaScriptEnabled() {
    return typeof window === "object" && typeof document === "object";
}

// Function to prompt users to enable JavaScript
function promptEnableJavaScript() {
    const message = `
        <div style="background-color: #f9c9c9; padding: 20px; border: 1px solid #f00;">
            <h2>JavaScript is Disabled</h2>
            <p>Please enable JavaScript to use this website.</p>
            <p>Here is how to enable JavaScript in different browsers:</p>
            <ul>
                <li><strong>Chrome:</strong> Go to Settings > Privacy and Security > Site Settings > JavaScript and toggle it on.</li>
                <li><strong>Firefox:</strong> Type 'about:config' in the address bar, search for 'javascript.enabled' and toggle it to true.</li>
                <li><strong>Safari:</strong> Go to Preferences > Security and check "Enable JavaScript".</li>
                <li><strong>Edge:</strong> Go to Settings > Cookies and site permissions > JavaScript and toggle it on.</li>
            </ul>
        </div>
    `;
    
    // Inject the message into the body if JavaScript is disabled
    document.body.innerHTML = message;
}

// Check if JavaScript is enabled and handle the result
if (!isJavaScriptEnabled()) {
    promptEnableJavaScript();
}
```

This code checks if JavaScript is enabled in the user's browser and, if not, prompts them with instructions on how to enable it for various popular browsers.
