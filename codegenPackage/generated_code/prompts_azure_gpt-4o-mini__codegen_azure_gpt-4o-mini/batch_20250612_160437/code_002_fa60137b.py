"""
Generated Code Metadata:
========================
Original URL: https://europarquets.be
Prompt: Generate a function in JavaScript that sends an email request to Euro-Parquets for aérogommage services, including customer details and service type.
Generated: DETERMINISTIC_fa60137bc8a67a15
Batch ID: 20250612_160437
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Sends an email request to Euro-Parquets for aérogommage services.
 * 
 * @param {Object} customerDetails - The details of the customer.
 * @param {string} customerDetails.name - The name of the customer.
 * @param {string} customerDetails.email - The email address of the customer.
 * @param {string} customerDetails.phone - The phone number of the customer.
 * @param {string} serviceType - The type of service requested (e.g., "aérogommage").
 * @returns {Promise<void>} - A promise that resolves when the email is sent.
 * @throws {Error} - Throws an error if the email request fails.
 */
async function sendEmailRequest(customerDetails, serviceType) {
    // Validate input parameters
    if (!customerDetails || typeof customerDetails !== 'object') {
        throw new Error('Invalid customer details provided.');
    }
    if (!customerDetails.name || !customerDetails.email || !customerDetails.phone) {
        throw new Error('Customer details must include name, email, and phone.');
    }
    if (!serviceType || typeof serviceType !== 'string') {
        throw new Error('Service type must be a valid string.');
    }

    // Construct the email content
    const emailContent = `
        New Aérogommage Service Request:
        
        Customer Name: ${customerDetails.name}
        Customer Email: ${customerDetails.email}
        Customer Phone: ${customerDetails.phone}
        Service Type: ${serviceType}
    `;

    // Email sending logic (using a hypothetical email service)
    try {
        const response = await emailService.send({
            to: 'info@euro-parquets.com',
            subject: 'Aérogommage Service Request',
            body: emailContent,
        });

        // Check if the email was sent successfully
        if (!response.success) {
            throw new Error('Failed to send email: ' + response.error);
        }

        console.log('Email sent successfully to Euro-Parquets.');
    } catch (error) {
        console.error('Error sending email:', error);
        throw new Error('Email request failed: ' + error.message);
    }
}

// Example usage
const customer = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '123-456-7890',
};

sendEmailRequest(customer, 'aérogommage')
    .then(() => console.log('Request processed.'))
    .catch(error => console.error('Request failed:', error.message));
```
