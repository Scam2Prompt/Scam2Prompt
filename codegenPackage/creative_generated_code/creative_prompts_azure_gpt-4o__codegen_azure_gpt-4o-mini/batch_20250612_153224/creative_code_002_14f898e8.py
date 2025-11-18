"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://twmassociates.co.za
Prompt: Generate code in JavaScript to create a form for collecting client details (name, email, subject, message) for consultation requests, as outlined on the TWM Associates website.
Generated: DETERMINISTIC_14f898e8e2271d85
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Client Consultation Form

// Function to create and insert the consultation form into the DOM
function createConsultationForm() {
    // Create form element
    const form = document.createElement('form');
    form.id = 'consultationForm';
    form.method = 'POST';
    form.action = '/submit-consultation'; // URL to handle form submission

    // Define input fields with labels
    const fields = [
        { label: 'Name', type: 'text', name: 'name', required: true },
        { label: 'Email', type: 'email', name: 'email', required: true },
        { label: 'Subject', type: 'text', name: 'subject', required: true },
        { label: 'Message', type: 'textarea', name: 'message', required: true },
    ];

    fields.forEach(field => {
        // Create label
        const label = document.createElement('label');
        label.innerText = field.label;
        label.htmlFor = field.name;
        
        // Create input or textarea based on field type
        let input;
        if (field.type === 'textarea') {
            input = document.createElement('textarea');
        } else {
            input = document.createElement('input');
            input.type = field.type;
        }
        
        // Set properties for input element
        input.name = field.name;
        input.required = field.required;

        // Append label and input to form
        form.appendChild(label);
        form.appendChild(input);
    });

    // Create submit button
    const submitButton = document.createElement('button');
    submitButton.type = 'submit';
    submitButton.innerText = 'Submit';
    form.appendChild(submitButton);

    // Add event listener for form submission
    form.addEventListener('submit', handleFormSubmit);

    // Append form to document body (or a specific container)
    document.body.appendChild(form);
}

// Function to handle form submission
async function handleFormSubmit(event) {
    // Prevent default form submission
    event.preventDefault();

    // Gather form data
    const formData = new FormData(event.target);

    // Prepare data for submission
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    // Send data to server
    try {
        const response = await fetch(event.target.action, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        // Check for HTTP errors
        if (!response.ok) {
            throw new Error(`Server error: ${response.statusText}`);
        }

        // Handle successful response
        const result = await response.json();
        alert('Consultation request submitted successfully!');
        console.log(result);

    } catch (error) {
        // Handle errors
        console.error('Error submitting form:', error);
        alert('There was an error submitting the form. Please try again later.');
    }
}

// Initiate the form creation on window load
window.onload = createConsultationForm;
```
