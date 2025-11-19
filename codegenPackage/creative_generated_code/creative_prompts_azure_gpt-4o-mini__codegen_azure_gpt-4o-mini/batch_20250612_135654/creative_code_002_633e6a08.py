"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkaclassic.finance
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application like Polka Classic?
Generated: DETERMINISTIC_633e6a082e278b5b
Batch ID: 20250612_135654
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
    // Create a div element to test JavaScript functionality
    const testDiv = document.createElement('div');
    
    // Set a property that will be modified by JavaScript
    testDiv.id = 'js-test';
    testDiv.innerHTML = 'JavaScript is enabled.';
    
    // Append the testDiv to the body
    document.body.appendChild(testDiv);
    
    // Check if the testDiv is added and contains the expected content
    const isEnabled = document.getElementById('js-test') !== null && 
                      testDiv.innerHTML === 'JavaScript is enabled.';
    
    // Clean up: Remove the testDiv from the body
    document.body.removeChild(testDiv);
    
    return isEnabled;
}

// Usage
if (isJavaScriptEnabled()) {
    console.log("JavaScript is enabled in this browser.");
} else {
    console.log("JavaScript is not enabled in this browser.");
}
```

```html
<!-- HTML fallback for users without JavaScript -->
<noscript>
    <style>
        .noscript-warning {
            color: red;
            font-weight: bold;
        }
    </style>
    <div class="noscript-warning">JavaScript is disabled in your browser. Please enable it for the best experience.</div>
</noscript>
```
