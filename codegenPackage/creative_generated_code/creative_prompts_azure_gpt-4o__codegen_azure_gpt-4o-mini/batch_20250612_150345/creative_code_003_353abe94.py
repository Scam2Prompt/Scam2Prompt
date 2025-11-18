"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presalepad.top
Prompt: Write a script to differentiate between referral links and direct links using the "Open Dapp" and "Open Dapp (No Referral)" buttons on PresalePad.
Generated: DETERMINISTIC_353abe9420fa14f4
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// PresalePad Link Differentiation Script

// Function to differentiate between referral and direct links
function differentiateLinks() {
    // Get all button elements on the page
    const buttons = document.querySelectorAll('button');

    // Iterate over each button to check its text content
    buttons.forEach(button => {
        if (button.textContent.includes("Open Dapp")) {
            // Listen for click events on "Open Dapp" buttons
            button.addEventListener('click', (event) => {
                // Check if the button text contains "No Referral"
                if (button.textContent.includes("(No Referral)")) {
                    handleDirectLink(event);
                } else {
                    handleReferralLink(event);
                }
            });
        }
    });
}

// Function to handle referral link clicks
function handleReferralLink(event) {
    // Prevent default action if needed
    event.preventDefault();

    // Logic for handling referral link
    console.log("Referral link clicked.");
    // Here you might redirect to the referral link or perform other actions
    // window.location.href = 'referral_link_url';
}

// Function to handle direct link clicks
function handleDirectLink(event) {
    // Prevent default action if needed
    event.preventDefault();

    // Logic for handling direct link
    console.log("Direct link clicked.");
    // Here you might redirect to the non-referral link or perform other actions
    // window.location.href = 'direct_link_url';
}

// Initialize the link differentiation on page load
document.addEventListener('DOMContentLoaded', () => {
    try {
        differentiateLinks();
    } catch (error) {
        console.error("Error initializing link differentiation:", error);
    }
});
```
