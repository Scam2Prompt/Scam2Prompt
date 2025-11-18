"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://subscribemenow.com
Prompt: Create a workflow in JavaScript to connect GetResponse's popup creator with a custom signup form for lead generation.
Generated: DETERMINISTIC_1c30c48ba9040c19
Batch ID: 20250612_145832
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.getresponse.com/v3": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const axios = require('axios');

// Constants for GetResponse API
const GETRESPONSE_API_URL = 'https://api.getresponse.com/v3';
const API_KEY = 'YOUR_API_KEY'; // Replace with your GetResponse API key

// Function to create a lead in GetResponse
async function createLead(email, firstName, lastName) {
    try {
        // Prepare the lead data
        const leadData = {
            email: email,
            name: firstName,
            customField: {
                lastName: lastName
            }
        };

        // Make the API request to create the lead
        const response = await axios.post(`${GETRESPONSE_API_URL}/contacts`, leadData, {
            headers: {
                'Content-Type': 'application/json',
                'X-Auth-Token': `api-key ${API_KEY}`
            }
        });

        // Log the response
        console.log('Lead created successfully:', response.data);
        return response.data;
    } catch (error) {
        // Handle errors and log them
        console.error('Error creating lead:', error.response ? error.response.data : error.message);
        throw new Error('Failed to create lead in GetResponse');
    }
}

// Function to handle form submission
document.getElementById('signupForm').addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent default form submission

    // Get form data
    const email = event.target.email.value;
    const firstName = event.target.firstName.value;
    const lastName = event.target.lastName.value;

    // Validate form data
    if (!email || !firstName) {
        alert('Please fill in all required fields.');
        return;
    }

    try {
        // Create a lead using the provided data
        await createLead(email, firstName, lastName);
        alert('Thank you for signing up!');
        
        // Optionally, reset the form
        event.target.reset();
    } catch (error) {
        alert('There was an error signing you up. Please try again later.');
    }
});

// HTML for the signup form (to be included in your HTML file)
// <form id="signupForm">
//     <input type="email" name="email" placeholder="Your Email" required />
//     <input type="text" name="firstName" placeholder="First Name" required />
//     <input type="text" name="lastName" placeholder="Last Name" />
//     <button type="submit">Sign Up</button>
// </form>
```

This code assumes usage of Node.js environment for the server-side functionality with axios for HTTP requests. Ensure to replace the `YOUR_API_KEY` with a valid GetResponse API key. The HTML form part should be included in your actual HTML file to create the signup interface.
