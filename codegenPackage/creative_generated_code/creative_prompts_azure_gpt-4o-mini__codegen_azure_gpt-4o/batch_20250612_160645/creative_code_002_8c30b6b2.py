"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rembytservis02.ru
Prompt: Create a JavaScript function that captures user input for selling used electronics and integrates with a local service in Ufa, as mentioned on the webpage.
Generated: DETERMINISTIC_8c30b6b2b627c43f
Batch ID: 20250612_160645
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://ufa-local-service.example.com/api/sell-electronics": {
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
/**
 * Function to capture user input for selling used electronics
 * and integrate with a local service in Ufa.
 * 
 * This function uses form inputs and sends the data to a hypothetical local API endpoint.
 * The function handles errors gracefully and validates input before submission.
 */

// Ensure this script runs after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Attach event listener to the form
    const form = document.getElementById('electronics-sell-form');
    if (form) {
        form.addEventListener('submit', handleFormSubmission);
    }
});

/**
 * Handle the form submission for selling electronics
 * @param {Event} event - The form submit event
 */
function handleFormSubmission(event) {
    event.preventDefault(); // Prevent default form submission behavior

    // Capture user input from form fields
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const itemDescription = document.getElementById('item-description').value.trim();
    const itemCondition = document.getElementById('item-condition').value.trim();

    // Validate form inputs
    if (!name || !email || !phone || !itemDescription || !itemCondition) {
        alert('Please fill out all the fields.');
        return;
    }

    // Regex for basic email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert('Please enter a valid email address.');
        return;
    }

    // Prepare data payload for API submission
    const payload = {
        name,
        email,
        phone,
        itemDescription,
        itemCondition,
        city: 'Ufa', // Hardcoded city for local service integration
    };

    // Send data to the local service API
    fetch('https://ufa-local-service.example.com/api/sell-electronics', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error(`Error: ${response.status} ${response.statusText}`);
            }
            return response.json();
        })
        .then((data) => {
            // Handle successful response
            alert('Your request has been submitted successfully. Thank you!');
            console.log('Response from API:', data);
        })
        .catch((error) => {
            // Handle errors gracefully
            console.error('Error:', error);
            alert('An error occurred while submitting your request. Please try again later.');
        });
}

// Example of the HTML form this script integrates with:
// <form id="electronics-sell-form">
//     <input type="text" id="name" placeholder="Your Name" required />
//     <input type="email" id="email" placeholder="Your Email" required />
//     <input type="tel" id="phone" placeholder="Your Phone Number" required />
//     <textarea id="item-description" placeholder="Describe your item" required></textarea>
//     <select id="item-condition" required>
//         <option value="">Select Condition</option>
//         <option value="new">New</option>
//         <option value="used">Used</option>
//         <option value="damaged">Damaged</option>
//     </select>
//     <button type="submit">Submit</button>
// </form>
```
