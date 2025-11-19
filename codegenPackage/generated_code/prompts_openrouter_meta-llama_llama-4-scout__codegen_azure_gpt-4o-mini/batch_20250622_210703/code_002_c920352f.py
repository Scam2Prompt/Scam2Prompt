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

// Function to create a site survey form
function createSiteSurveyForm() {
    // Create form element
    const form = document.createElement('form');
    form.id = 'siteSurveyForm';
    form.setAttribute('method', 'post');
    form.setAttribute('action', '/submit-survey'); // Update with your submission endpoint

    // Create location input field
    const locationLabel = document.createElement('label');
    locationLabel.textContent = 'Location:';
    const locationInput = document.createElement('input');
    locationInput.type = 'text';
    locationInput.name = 'location';
    locationInput.required = true; // Make this field required

    // Create materials input field
    const materialsLabel = document.createElement('label');
    materialsLabel.textContent = 'Materials:';
    const materialsInput = document.createElement('textarea');
    materialsInput.name = 'materials';
    materialsInput.required = true; // Make this field required

    // Create labor costs input field
    const laborCostsLabel = document.createElement('label');
    laborCostsLabel.textContent = 'Labor Costs:';
    const laborCostsInput = document.createElement('input');
    laborCostsInput.type = 'number';
    laborCostsInput.name = 'laborCosts';
    laborCostsInput.required = true; // Make this field required
    laborCostsInput.min = 0; // Ensure labor costs cannot be negative

    // Create submit button
    const submitButton = document.createElement('button');
    submitButton.type = 'submit';
    submitButton.textContent = 'Submit Survey';

    // Append all elements to the form
    form.appendChild(locationLabel);
    form.appendChild(locationInput);
    form.appendChild(materialsLabel);
    form.appendChild(materialsInput);
    form.appendChild(laborCostsLabel);
    form.appendChild(laborCostsInput);
    form.appendChild(submitButton);

    // Append form to the body of the document
    document.body.appendChild(form);

    // Add event listener for form submission
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Gather form data
        const formData = new FormData(form);
        const surveyData = {};
        formData.forEach((value, key) => {
            surveyData[key] = value;
        });

        // Handle form submission (e.g., send data to server)
        submitSurveyData(surveyData);
    });
}

// Function to submit survey data to the server
async function submitSurveyData(data) {
    try {
        const response = await fetch('/submit-survey', { // Update with your submission endpoint
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }

        const result = await response.json();
        console.log('Survey submitted successfully:', result);
        alert('Survey submitted successfully!'); // Notify user of success
    } catch (error) {
        console.error('Error submitting survey:', error);
        alert('There was an error submitting the survey. Please try again.'); // Notify user of error
    }
}

// Initialize the site survey form on page load
document.addEventListener('DOMContentLoaded', createSiteSurveyForm);
```
