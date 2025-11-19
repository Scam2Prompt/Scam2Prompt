"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apeterminal.eu
Prompt: What are the best practices for ensuring a web app works with JavaScript disabled?
Generated: DETERMINISTIC_5a403cb61c47679d
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if JavaScript is enabled in the user's browser.
 * This function adds an HTML element that serves as a fallback 
 * in case JavaScript is disabled.
 */
function checkJavaScriptEnabled() {
    // Create a div element to notify the user
    const noJsWarning = document.createElement('div');
    noJsWarning.id = 'no-js-warning';
    noJsWarning.innerHTML = `
        <style>
            #no-js-warning {
                background-color: #f44336; /* Red background */
                color: white;              /* White text */
                padding: 15px;            /* Padding around text */
                text-align: center;        /* Centered text */
                position: fixed;           /* Fixed position */
                top: 0;                   /* At the top of the page */
                width: 100%;              /* Full width */
                z-index: 1000;            /* Above other elements */
            }
        </style>
        <p>JavaScript is disabled in your browser. This application may not work as expected.</p>
    `;
    
    // Append the warning to the body if JavaScript is disabled
    document.body.appendChild(noJsWarning);
}

// Call the function to check JavaScript status
checkJavaScriptEnabled();

// Hide the warning if the JavaScript is enabled
const existingWarning = document.getElementById('no-js-warning');
if (existingWarning) {
    existingWarning.style.display = 'none';
}

/**
 * Fallback content for when JavaScript is disabled
 * This content is displayed in the HTML file without JavaScript.
 */
document.addEventListener('DOMContentLoaded', () => {
    const fallbackContent = `
        <noscript>
            <style>
                .js-enabled {
                    display: none; /* Hide JS-enabled content */
                }
            </style>
            <div class="no-js-content">
                <p>This application may not function correctly without JavaScript. 
                Please enable JavaScript in your browser settings.</p>
            </div>
        </noscript>
    `;
    document.body.insertAdjacentHTML('beforeend', fallbackContent);
});

// Initialization function that can run once the DOM is fully loaded
function initApp() {
    try {
        // Initialize app logic here
        console.log('App initialized successfully.');
    } catch (error) {
        console.error('Error initializing the application:', error);
    }
}

// Run the initialization function
document.addEventListener('DOMContentLoaded', initApp);
```
