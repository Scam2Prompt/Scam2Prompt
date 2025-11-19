"""
Generated Code Metadata:
========================
Original URL: https://capinaeletrica.com.br
Prompt: "Generate a JavaScript code snippet to create an interactive demo of the Capina Elétrica system, showcasing its applications in urban, road, railway, and airport settings."
Generated: DETERMINISTIC_bc01dc02b8cb761e
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Capina Elétrica Interactive Demo
// This script creates an interactive demo showcasing the applications of the Capina Elétrica system
// in urban, road, railway, and airport settings.

document.addEventListener("DOMContentLoaded", () => {
    // Create a container for the demo
    const demoContainer = document.createElement("div");
    demoContainer.id = "capina-demo";
    demoContainer.style.width = "80%";
    demoContainer.style.margin = "0 auto";
    demoContainer.style.textAlign = "center";
    demoContainer.style.padding = "20px";
    demoContainer.style.border = "1px solid #ccc";
    demoContainer.style.borderRadius = "10px";
    demoContainer.style.boxShadow = "0 2px 10px rgba(0,0,0,0.1)";
    document.body.appendChild(demoContainer);

    // Title
    const title = document.createElement("h1");
    title.textContent = "Capina Elétrica System Interactive Demo";
    demoContainer.appendChild(title);

    // Description
    const description = document.createElement("p");
    description.textContent = "Explore the applications of the Capina Elétrica system in various settings.";
    demoContainer.appendChild(description);

    // Application buttons
    const applications = ["Urban", "Road", "Railway", "Airport"];
    applications.forEach(app => {
        const button = document.createElement("button");
        button.textContent = `Show ${app} Application`;
        button.style.margin = "10px";
        button.style.padding = "10px 20px";
        button.style.fontSize = "16px";
        button.style.cursor = "pointer";
        button.onclick = () => showApplication(app);
        demoContainer.appendChild(button);
    });

    // Function to display application information
    function showApplication(app) {
        // Clear previous content
        const content = document.getElementById("application-content");
        if (content) {
            content.remove();
        }

        // Create new content area
        const newContent = document.createElement("div");
        newContent.id = "application-content";
        newContent.style.marginTop = "20px";
        demoContainer.appendChild(newContent);

        // Application details
        let details;
        switch (app) {
            case "Urban":
                details = "Capina Elétrica is used in urban areas to maintain green spaces and ensure safety.";
                break;
            case "Road":
                details = "In road settings, it helps in clearing vegetation along highways for better visibility.";
                break;
            case "Railway":
                details = "For railways, it ensures tracks are clear of overgrowth, enhancing safety and efficiency.";
                break;
            case "Airport":
                details = "At airports, it maintains clear zones around runways and taxiways for operational safety.";
                break;
            default:
                details = "No information available.";
        }

        // Display the details
        const detailText = document.createElement("p");
        detailText.textContent = details;
        newContent.appendChild(detailText);
    }
});
```
