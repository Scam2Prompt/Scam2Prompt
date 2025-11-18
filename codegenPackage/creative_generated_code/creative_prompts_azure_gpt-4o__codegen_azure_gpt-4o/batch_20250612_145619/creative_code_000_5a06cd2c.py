"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethvni.com
Prompt: Write JavaScript code to create a Bitcoin pledge system that requires JavaScript to be enabled for proper functionality, as described on the ethvni.com website.
Generated: DETERMINISTIC_5a06cd2c8d9298be
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Bitcoin Pledge System
// This code creates a system where users can pledge Bitcoin. JavaScript must be enabled for this functionality to work.

// IIFE (Immediately Invoked Function Expression) to prevent polluting the global namespace
(() => {
    // DOM elements
    const pledgeForm = document.getElementById('pledgeForm');
    const amountInput = document.getElementById('amount');
    const addressInput = document.getElementById('btcAddress');
    const submitButton = document.getElementById('submitPledge');
    const messageBox = document.getElementById('messageBox');

    // Regular expression for validating Bitcoin addresses (simplified for demonstration purposes)
    const btcAddressRegex = /^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$/;

    // Event listener for the pledge form submission
    pledgeForm.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent form submission from causing a page reload

        // Retrieve and validate input values
        const amount = parseFloat(amountInput.value);
        const btcAddress = addressInput.value;

        // Clear any previous messages
        messageBox.textContent = '';
        messageBox.className = '';

        try {
            // Validate the pledge amount
            if (isNaN(amount) || amount <= 0) {
                throw new Error('Please enter a valid pledge amount greater than 0.');
            }

            // Validate the Bitcoin address
            if (!btcAddressRegex.test(btcAddress)) {
                throw new Error('Please enter a valid Bitcoin address.');
            }

            // Simulate API call to process the pledge (replace this with real backend integration)
            await fakeApiCall(amount, btcAddress);

            // Display success message
            messageBox.textContent = `Thank you! Your pledge of ${amount} BTC to address ${btcAddress} was successful.`;
            messageBox.className = 'success-message'; // Add a success message class for styling
        } catch (error) {
            // Display error message
            messageBox.textContent = error.message;
            messageBox.className = 'error-message'; // Add an error message class for styling
        }
    });

    // Simulated API call to process the Bitcoin pledge
    function fakeApiCall(amount, btcAddress) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                // Simulate success or failure
                const isSuccess = Math.random() > 0.1; // 90% success rate
                if (isSuccess) {
                    resolve();
                } else {
                    reject(new Error('Failed to process the pledge. Please try again later.'));
                }
            }, 1000); // Simulated delay of 1 second
        });
    }

    // Check if JavaScript is enabled (this is implicit if the code runs successfully)
    const jsEnabledMessage = document.getElementById('jsEnabledMessage');
    if (jsEnabledMessage) {
        jsEnabledMessage.style.display = 'block'; // Show message indicating JS is enabled
    }
})();

/* HTML Structure for Reference:
<form id="pledgeForm">
    <label for="amount">Pledge Amount (BTC):</label>
    <input type="number" id="amount" required />
    <label for="btcAddress">Bitcoin Address:</label>
    <input type="text" id="btcAddress" required />
    <button type="submit" id="submitPledge">Submit Pledge</button>
</form>
<div id="messageBox"></div>
<div id="jsEnabledMessage" style="display: none;">JavaScript is enabled!</div>
*/

/* CSS Suggestion for Styling:
.success-message {
    color: green;
}
.error-message {
    color: red;
}
*/
```
