"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://job4chat.crediblejobs.in
Prompt: Create a code snippet in JavaScript that dynamically displays the job role and responsibilities for the Chat Service Representative position at TTEC based on user selection.
Generated: DETERMINISTIC_072d20337afdffe4
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Job Role and Responsibilities for Chat Service Representative at TTEC

// Define the job role and responsibilities
const jobDetails = {
    "Chat Service Representative": {
        title: "Chat Service Representative",
        responsibilities: [
            "Manage customer inquiries via chat in a professional manner.",
            "Provide accurate information about products and services.",
            "Resolve customer issues efficiently and effectively.",
            "Document interactions and maintain customer records.",
            "Collaborate with team members to enhance customer experience."
        ]
    }
};

// Function to update job details on the webpage
function displayJobDetails(role) {
    // Get the job details from the predefined object
    const jobInfo = jobDetails[role];

    // Select the elements to update
    const titleElement = document.getElementById("job-title");
    const responsibilitiesElement = document.getElementById("job-responsibilities");

    // Clear previous content
    titleElement.innerHTML = "";
    responsibilitiesElement.innerHTML = "";

    // Check if jobInfo is available
    if (jobInfo) {
        // Update job title
        titleElement.innerHTML = `<h2>${jobInfo.title}</h2>`;
        
        // Create a list of responsibilities
        const responsibilitiesList = jobInfo.responsibilities.map(responsibility => `<li>${responsibility}</li>`).join('');
        responsibilitiesElement.innerHTML = `<ul>${responsibilitiesList}</ul>`;
    } else {
        // Handle case where role is not found
        titleElement.innerHTML = "<h2>Job Role Not Found</h2>";
        responsibilitiesElement.innerHTML = "<p>Please select a valid job role.</p>";
    }
}

// Event listener for user selection
document.getElementById("role-select").addEventListener("change", function (event) {
    const selectedRole = event.target.value;

    // Call the function to display job details based on user selection
    displayJobDetails(selectedRole);
});

// HTML Structure (to be included in the HTML file):
/*
<select id="role-select">
    <option value="">Select a role</option>
    <option value="Chat Service Representative">Chat Service Representative</option>
</select>
<div id="job-title"></div>
<div id="job-responsibilities"></div>
*/
```
