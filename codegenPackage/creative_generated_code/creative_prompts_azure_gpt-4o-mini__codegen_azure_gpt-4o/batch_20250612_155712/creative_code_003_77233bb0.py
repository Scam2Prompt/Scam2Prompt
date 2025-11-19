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
// Application Entry Point

// HTML structure to dynamically inject into the DOM
const appHTML = `
  <div id="app">
    <h1>Asset Finance Proposal Submission</h1>
    <form id="proposalForm">
      <label for="assetType">Asset Type:</label>
      <select id="assetType" name="assetType" required>
        <option value="marine">Marine Craft</option>
        <option value="aircraft">Light Aircraft</option>
      </select>

      <label for="assetName">Asset Name:</label>
      <input type="text" id="assetName" name="assetName" placeholder="e.g., Yacht 3000" required />

      <label for="price">Price:</label>
      <input type="number" id="price" name="price" placeholder="e.g., 500000" required />

      <label for="username">Your Name:</label>
      <input type="text" id="username" name="username" placeholder="e.g., John Doe" required />

      <label for="email">Your Email:</label>
      <input type="email" id="email" name="email" placeholder="e.g., john.doe@example.com" required />

      <label for="comments">Additional Comments:</label>
      <textarea id="comments" name="comments" placeholder="Enter any additional details"></textarea>

      <button type="submit">Submit Proposal</button>
    </form>
    <div id="successMessage" style="display: none; color: green;">Proposal submitted successfully!</div>
  </div>
`;

// Inject the HTML into the body
document.body.innerHTML = appHTML;

// Utility function to validate email format
function validateEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

// Event listener for form submission
document.getElementById('proposalForm').addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent default form submission behavior

  const assetType = document.getElementById('assetType').value;
  const assetName = document.getElementById('assetName').value.trim();
  const price = parseFloat(document.getElementById('price').value);
  const username = document.getElementById('username').value.trim();
  const email = document.getElementById('email').value.trim();
  const comments = document.getElementById('comments').value.trim();

  // Basic validations
  if (!assetName || !username || !validateEmail(email) || isNaN(price) || price <= 0) {
    alert('Please fill out all required fields correctly.');
    return;
  }

  // Proposal object
  const proposal = {
    assetType,
    assetName,
    price,
    username,
    email,
    comments,
    submittedAt: new Date().toISOString(),
  };

  // Simulate saving the proposal (e.g., sending to a server via fetch)
  try {
    // Here you would typically make a network request like:
    // fetch('/api/proposals', { method: 'POST', body: JSON.stringify(proposal), headers: { 'Content-Type': 'application/json' } });

    console.log('Proposal submitted:', proposal);
    document.getElementById('successMessage').style.display = 'block';

    // Reset the form fields
    document.getElementById('proposalForm').reset();
  } catch (error) {
    console.error('Error submitting proposal:', error);
    alert('An error occurred while submitting your proposal. Please try again later.');
  }
});

// Note: In a production environment, this code would also include additional security measures,
// such as input sanitization, and would make use of a backend API to store data persistently.
```
