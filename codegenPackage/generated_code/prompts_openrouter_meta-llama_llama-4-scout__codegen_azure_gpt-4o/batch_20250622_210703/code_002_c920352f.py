"""
Generated Code Metadata:
========================
Original URL: https://aasteeldetailing.co.uk.steel-edge.co.uk
Prompt: "Write a code snippet in JavaScript to create a site survey template for steel detailing projects, including fields for location, materials, and labor costs."
Generated: DETERMINISTIC_c920352f973bd83a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Site Survey Template for Steel Detailing Projects
// This script dynamically creates a survey form with fields for location, materials, and labor costs.

// Function to create the survey form
function createSiteSurveyForm() {
  try {
    // Create a form element
    const form = document.createElement('form');
    form.setAttribute('id', 'siteSurveyForm');
    form.setAttribute('method', 'post');
    form.setAttribute('action', '/submit-survey'); // Replace with actual endpoint

    // Create a field for location
    const locationField = document.createElement('div');
    locationField.innerHTML = `
      <label for="location">Location:</label>
      <input type="text" id="location" name="location" placeholder="Enter project location" required>
    `;
    form.appendChild(locationField);

    // Create a field for materials
    const materialsField = document.createElement('div');
    materialsField.innerHTML = `
      <label for="materials">Materials:</label>
      <textarea id="materials" name="materials" placeholder="List required materials" required></textarea>
    `;
    form.appendChild(materialsField);

    // Create a field for labor costs
    const laborCostsField = document.createElement('div');
    laborCostsField.innerHTML = `
      <label for="laborCosts">Labor Costs:</label>
      <input type="number" id="laborCosts" name="laborCosts" placeholder="Enter labor costs" required>
    `;
    form.appendChild(laborCostsField);

    // Create a submit button
    const submitButton = document.createElement('button');
    submitButton.setAttribute('type', 'submit');
    submitButton.textContent = 'Submit Survey';
    form.appendChild(submitButton);

    // Append the form to the body or a specific container
    const container = document.getElementById('formContainer') || document.body;
    container.appendChild(form);
  } catch (error) {
    console.error('Error creating site survey form:', error);
  }
}

// Call the function to create the form when the page loads
document.addEventListener('DOMContentLoaded', () => {
  createSiteSurveyForm();
});
```
