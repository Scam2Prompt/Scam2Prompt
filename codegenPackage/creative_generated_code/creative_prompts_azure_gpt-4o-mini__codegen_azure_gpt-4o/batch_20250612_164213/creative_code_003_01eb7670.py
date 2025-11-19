"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mwxoq1840.ukit.me
Prompt: Generate code to display a message when a uKit website's trial period has expired.
Generated: DETERMINISTIC_01eb76707c2e9692
Batch ID: 20250612_164213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Code to display a message when a uKit website's trial period has expired

// Function to check if the trial period has expired
function hasTrialExpired(trialStartDate, trialDays) {
    try {
        const currentDate = new Date(); // Get current date
        const trialEndDate = new Date(trialStartDate); // Convert trial start date to Date object
        trialEndDate.setDate(trialEndDate.getDate() + trialDays); // Calculate trial end date

        return currentDate > trialEndDate; // Check if current date is past the trial end date
    } catch (error) {
        console.error("Error checking trial expiration:", error);
        return false; // Fallback to prevent disruption
    }
}

// Function to display expiration message
function displayExpirationMessage() {
    try {
        // Create a modal element for the trial expiration message
        const modal = document.createElement("div");
        modal.style.position = "fixed";
        modal.style.top = "0";
        modal.style.left = "0";
        modal.style.width = "100%";
        modal.style.height = "100%";
        modal.style.backgroundColor = "rgba(0, 0, 0, 0.8)";
        modal.style.color = "#fff";
        modal.style.display = "flex";
        modal.style.justifyContent = "center";
        modal.style.alignItems = "center";
        modal.style.zIndex = "9999";
        modal.style.textAlign = "center";
        modal.style.padding = "20px";

        // Add message text to the modal
        const message = document.createElement("div");
        message.textContent = "Your trial period has expired. Please upgrade your plan to continue using the website.";
        message.style.fontSize = "1.5em";

        // Add a button to redirect to the upgrade page
        const button = document.createElement("button");
        button.textContent = "Upgrade Now";
        button.style.marginTop = "20px";
        button.style.padding = "10px 20px";
        button.style.fontSize = "1em";
        button.style.cursor = "pointer";
        button.style.backgroundColor = "#007bff";
        button.style.color = "#fff";
        button.style.border = "none";
        button.style.borderRadius = "5px";

        // Add click event to redirect user to the upgrade page
        button.addEventListener("click", () => {
            window.location.href = "/upgrade"; // Change to the actual upgrade URL
        });

        // Append message and button to the modal
        modal.appendChild(message);
        modal.appendChild(button);

        // Append modal to the body
        document.body.appendChild(modal);
    } catch (error) {
        console.error("Error displaying expiration message:", error);
    }
}

// Main function to handle trial expiration check and display message
function handleTrialExpiration() {
    // Example trial start date and trial duration
    const trialStartDate = "2023-09-01"; // Format: YYYY-MM-DD
    const trialDays = 14; // Length of the trial period in days

    if (hasTrialExpired(trialStartDate, trialDays)) {
        displayExpirationMessage(); // Display expiration message if trial is expired
    }
}

// Execute the trial expiration check on page load
document.addEventListener("DOMContentLoaded", handleTrialExpiration);
```
