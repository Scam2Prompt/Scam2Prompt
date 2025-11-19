"""
Generated Code Metadata:
========================
Original URL: https://attntoken.xyz
Prompt: Explain the implications of using `document.write()` after the page has loaded and how to avoid potential issues in modern web development.
Generated: DETERMINISTIC_be5b2cefdbfb483b
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a code example demonstrating the implications of `document.write()` and modern alternatives:

```javascript
// Modern approach to dynamically add content to the DOM
function safeContentInjection() {
    // Check if document is still loading
    if (document.readyState === 'loading') {
        console.warn('document.write() should still be avoided during loading phase');
        return;
    }

    try {
        // Preferred modern methods:
        
        // 1. Using DOM manipulation
        const container1 = document.createElement('div');
        container1.textContent = 'This is safely added content (Method 1)';
        document.body.appendChild(container1);

        // 2. Using insertAdjacentHTML
        const container2 = document.getElementById('content-container') || document.body;
        container2.insertAdjacentHTML('beforeend', 
            '<div>This is safely added content (Method 2)</div>');

        // 3. Using textContent/innerHTML with proper sanitization
        const sanitizeHTML = (str) => {
            const div = document.createElement('div');
            div.textContent = str;
            return div.innerHTML;
        };
        
        const safeContent = sanitizeHTML('<script>alert("XSS")</script> Safe content');
        document.getElementById('safe-content').innerHTML = safeContent;

    } catch (error) {
        console.error('Error injecting content:', error);
        // Fallback or error handling logic here
    }
}

// Event listener to ensure DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Demonstration of what NOT to do
    function dangerousWrite() {
        try {
            // This will overwrite the entire document if called after load
            document.write('<p>This will overwrite the page</p>');
            console.warn('This code should never run as it destroys the page');
        } catch (e) {
            console.error('document.write() failed:', e);
        }
    }

    // Button to demonstrate safe methods
    const safeBtn = document.createElement('button');
    safeBtn.textContent = 'Add Content Safely';
    safeBtn.addEventListener('click', safeContentInjection);
    document.body.appendChild(safeBtn);

    // Button to demonstrate dangerous method (for educational purposes)
    const dangerBtn = document.createElement('button');
    dangerBtn.textContent = 'DANGER: document.write()';
    dangerBtn.style.background = 'red';
    dangerBtn.style.color = 'white';
    dangerBtn.addEventListener('click', () => {
        if (confirm('This will destroy the current page. Continue?')) {
            dangerousWrite();
        }
    });
    document.body.appendChild(dangerBtn);

    // Create containers for demonstration
    const container = document.createElement('div');
    container.id = 'content-container';
    document.body.appendChild(container);

    const safeContainer = document.createElement('div');
    safeContainer.id = 'safe-content';
    document.body.appendChild(safeContainer);
});
```
