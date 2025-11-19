"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imseoa.com
Prompt: What are the best practices for ensuring JavaScript compatibility on mobile devices for web applications like ETH Pledge?
Generated: DETERMINISTIC_5caa8f2bd9bcf4e7
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Ensures compatibility for a web application like ETH Pledge on mobile devices.
 * This script checks for mobile features and adjusts the user interface accordingly.
 */

// Utility function to detect mobile devices
function isMobile() {
    // Regular expression to match common mobile user agents
    const mobileRegex = /Mobi|Android|iPhone|iPad|iPod|Opera Mini|IEMobile|WPDesktop/i;
    return mobileRegex.test(navigator.userAgent);
}

// Function to apply mobile-specific styles and features
function applyMobileStyles() {
    // Check if the device is mobile
    if (isMobile()) {
        console.log("Mobile device detected. Applying mobile styles...");

        // Example: Change font size for better readability on mobile
        document.body.style.fontSize = "16px";

        // Example: Hide desktop-only menus
        const desktopMenus = document.querySelectorAll('.desktop-menu');
        desktopMenus.forEach(menu => {
            menu.style.display = 'none';
        });

        // Example: Show mobile menus
        const mobileMenus = document.querySelectorAll('.mobile-menu');
        mobileMenus.forEach(menu => {
            menu.style.display = 'block';
        });
    } else {
        console.log("Non-mobile device detected. Applying desktop styles...");
        
        // Desktop styles can go here
        // For example, setting a larger font size for desktop
        document.body.style.fontSize = "18px";
    }
}

// Main function to initialize the application
function initializeApp() {
    try {
        applyMobileStyles(); // Apply styles based on device type

        // Additional initialization code can go here
        console.log("ETH Pledge application initialized successfully.");
    } catch (error) {
        console.error("Error initializing the ETH Pledge application:", error);
    }
}

// Execute the main function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', initializeApp);
```
