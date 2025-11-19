"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoassetfinance.com
Prompt: Develop a JavaScript application that allows users to submit asset finance proposals for marine craft and light aircraft.
Generated: DETERMINISTIC_77233bb083e9e25a
Batch ID: 20250612_155712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Asset Finance Proposal Application for Marine Craft and Light Aircraft
// This application allows users to submit finance proposals for marine craft and light aircraft.

class Proposal {
    constructor(type, description, amount, duration) {
        this.type = type; // Type of asset: 'Marine Craft' or 'Light Aircraft'
        this.description = description; // Description of the asset
        this.amount = amount; // Proposed finance amount
        this.duration = duration; // Duration in months
        this.submissionDate = new Date(); // Date of proposal submission
    }

    // Method to validate the proposal data
    validate() {
        if (!this.type || !this.description || !this.amount || !this.duration) {
            throw new Error('All fields are required');
        }
        if (isNaN(this.amount) || this.amount <= 0) {
            throw new Error('Amount must be a positive number');
        }
        if (isNaN(this.duration) || this.duration <= 0) {
            throw new Error('Duration must be a positive number');
        }
    }

    // Method to submit the proposal
    submit() {
        this.validate();
        // Here you would typically send the proposal to a server
        console.log('Proposal submitted:', this);
        return true; // Indicating successful submission
    }
}

// Function to handle form submission
function handleSubmit(event) {
    event.preventDefault(); // Prevent default form submission

    // Get form values
    const type = document.getElementById('type').value;
    const description = document.getElementById('description').value;
    const amount = parseFloat(document.getElementById('amount').value);
    const duration = parseInt(document.getElementById('duration').value, 10);

    try {
        // Create a new proposal
        const proposal = new Proposal(type, description, amount, duration);
        
        // Submit the proposal
        proposal.submit();
        
        // Clear form inputs
        document.getElementById('proposalForm').reset();
        alert('Proposal submitted successfully!');
    } catch (error) {
        // Handle validation and submission errors
        alert('Error: ' + error.message);
    }
}

// Function to initialize the application
function init() {
    // Add event listener to the form
    const form = document.getElementById('proposalForm');
    form.addEventListener('submit', handleSubmit);
}

// Execute the init function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', init);
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Asset Finance Proposal</title>
</head>
<body>
    <h1>Asset Finance Proposal Submission</h1>
    <form id="proposalForm">
        <label for="type">Asset Type:</label>
        <select id="type" required>
            <option value="">Select</option>
            <option value="Marine Craft">Marine Craft</option>
            <option value="Light Aircraft">Light Aircraft</option>
        </select><br>

        <label for="description">Asset Description:</label>
        <input type="text" id="description" required><br>

        <label for="amount">Proposed Amount ($):</label>
        <input type="number" id="amount" required step="0.01"><br>

        <label for="duration">Duration (months):</label>
        <input type="number" id="duration" required min="1"><br>

        <button type="submit">Submit Proposal</button>
    </form>

    <script src="app.js"></script> <!-- Link to the JavaScript file -->
</body>
</html>
```
