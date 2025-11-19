"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gonetwork.eu
Prompt: Can you provide code snippets for enabling JavaScript in different web browsers for sites like GoNetwork?
Generated: DETERMINISTIC_0f7efada85eac3ad
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check if JavaScript is enabled
function isJavaScriptEnabled() {
    return typeof window !== 'undefined' && typeof window.alert === 'function';
}

// Notify user if JavaScript is disabled
if (!isJavaScriptEnabled()) {
    document.body.innerHTML = `
        <div style="background-color: #f8d7da; color: #721c24; padding: 15px; border: 1px solid #f5c6cb; margin: 20px; border-radius: 5px;">
            <strong>JavaScript is disabled!</strong> <br>
            To use this site, please enable JavaScript in your browser settings.
            <ul>
                <li><strong>Chrome:</strong> Go to Settings > Privacy and Security > Site Settings > JavaScript, then enable it.</li>
                <li><strong>Firefox:</strong> Go to Options > Privacy & Security > Permissions > Enable JavaScript.</li>
                <li><strong>Safari:</strong> Go to Preferences > Security > Enable JavaScript.</li>
                <li><strong>Edge:</strong> Go to Settings > Cookies and site permissions > JavaScript, then enable it.</li>
            </ul>
        </div>
    `;
}
```

This code snippet will check if JavaScript is enabled in the user's browser. If it is not enabled, it will display a message with instructions on how to enable JavaScript in popular web browsers.
