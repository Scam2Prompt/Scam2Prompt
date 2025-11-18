"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skifoundation.org
Prompt: Write JavaScript code to implement a donation form for SKI Foundation's website, including options for recurring donations and integration with payment gateways.
Generated: DETERMINISTIC_17c0f8ab0dfc3211
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Donation Form for SKI Foundation
// This code provides a user interface for donations, including recurring options,
// and integrates with a payment gateway (e.g., Stripe).

// HTML structure for reference:
// <div id="donation-form-container"></div>

// JavaScript Code Implementation:

// Wait until DOM content is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    // Initialize the donation form
    initializeDonationForm();
});

/**
 * Initializes the donation form and renders it into the DOM
 */
function initializeDonationForm() {
    const formContainer = document.getElementById("donation-form-container");

    // Ensure the container exists in the DOM
    if (!formContainer) {
        console.error("Donation form container not found.");
        return;
    }

    // Render the donation form
    formContainer.innerHTML = `
        <form id="donation-form">
            <h2>Support SKI Foundation</h2>
            <label for="donation-amount">Donation Amount ($):</label>
            <input type="number" id="donation-amount" name="donationAmount" min="1" required />

            <label for="recurring">Recurring Donation:</label>
            <select id="recurring" name="recurring">
                <option value="none">One-time</option>
                <option value="monthly">Monthly</option>
                <option value="yearly">Yearly</option>
            </select>

            <label for="payment-method">Payment Method:</label>
            <select id="payment-method" name="paymentMethod">
                <option value="credit-card">Credit Card</option>
                <option value="paypal">PayPal</option>
                <option value="stripe">Stripe</option>
            </select>

            <button type="submit">Donate</button>
        </form>
        <div id="form-message" style="margin-top: 1em;"></div>
    `;

    // Add event listener for form submission
    const donationForm = document.getElementById("donation-form");
    donationForm.addEventListener("submit", handleFormSubmission);
}

/**
 * Handles the submission of the donation form
 * @param {Event} event - The form submission event
 */
function handleFormSubmission(event) {
    event.preventDefault(); // Prevent form from refreshing the page

    // Collect form data
    const donationAmount = parseFloat(document.getElementById("donation-amount").value);
    const recurring = document.getElementById("recurring").value;
    const paymentMethod = document.getElementById("payment-method").value;

    // Basic validation
    if (isNaN(donationAmount) || donationAmount <= 0) {
        showMessage("Please enter a valid donation amount.", "error");
        return;
    }

    // Prepare data for payment processing
    const donationData = {
        amount: donationAmount,
        recurring,
        paymentMethod,
    };

    console.log("Processing donation data:", donationData);

    // Simulating payment gateway integration
    processPayment(donationData)
        .then((response) => {
            showMessage("Thank you for your donation!", "success");
            console.log("Payment processed successfully:", response);
        })
        .catch((error) => {
            showMessage("Something went wrong during payment processing.", "error");
            console.error("Payment processing error:", error);
        });
}

/**
 * Simulates integration with a payment gateway
 * @param {Object} donationData - The donation details
 * @returns {Promise<Object>} - Simulated response from payment gateway
 */
function processPayment(donationData) {
    return new Promise((resolve, reject) => {
        // Simulate delay for payment processing
        setTimeout(() => {
            // Simulate success or failure
            const isSuccess = Math.random() > 0.2; // 80% success rate
            if (isSuccess) {
                resolve({ status: "success", transactionId: "TX12345" });
            } else {
                reject({ status: "error", message: "Payment failed." });
            }
        }, 2000);
    });
}

/**
 * Displays a message to the user
 * @param {string} message - The message to display
 * @param {string} type - The type of message ('success', 'error')
 */
function showMessage(message, type) {
    const messageContainer = document.getElementById("form-message");
    messageContainer.textContent = message;

    // Apply styling based on type
    messageContainer.style.color = type === "success" ? "green" : "red";
}
```
