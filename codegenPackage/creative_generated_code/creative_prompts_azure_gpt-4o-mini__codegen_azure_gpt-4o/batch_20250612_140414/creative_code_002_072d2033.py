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
// Define job roles and responsibilities
const jobDetails = {
  "Chat Service Representative": {
    role: "Chat Service Representative",
    responsibilities: [
      "Provide exceptional customer service via chat.",
      "Resolve customer inquiries and issues promptly.",
      "Maintain accurate records of customer interactions.",
      "Collaborate with team members to improve service delivery.",
      "Adhere to company policies and procedures."
    ]
  },
  // Add more roles here if needed in the future
};

// Function to dynamically display job role and responsibilities
function displayJobDetails(role) {
  // Select the output container elements
  const roleElement = document.getElementById("role");
  const responsibilitiesElement = document.getElementById("responsibilities");

  if (!jobDetails[role]) {
    // Handle error if the role is not found
    roleElement.textContent = "Role not found.";
    responsibilitiesElement.innerHTML = "";
    return;
  }

  const { role: jobRole, responsibilities } = jobDetails[role];
  
  // Display the role
  roleElement.textContent = jobRole;

  // Display the responsibilities
  responsibilitiesElement.innerHTML = responsibilities
    .map(responsibility => `<li>${responsibility}</li>`)
    .join(""); // Convert array to list items
}

// Event listener for user selection of role
document.getElementById("jobSelector").addEventListener("change", function () {
  const selectedRole = this.value; // Get the selected value
  displayJobDetails(selectedRole); // Call function to display details
});

/* HTML Structure Example:
<select id="jobSelector">
  <option value="Chat Service Representative">Chat Service Representative</option>
</select>
<h2 id="role"></h2>
<ul id="responsibilities"></ul>
*/

/* Ensure this script is linked to an HTML file with the corresponding ID elements */
```
