"""
Generated Code Metadata:
========================
Original URL: https://nextmoney.co.th
Prompt: Create a sample code snippet in JavaScript to submit a loan application form for a truck title loan using the guidelines from Next Money.
Generated: DETERMINISTIC_1ca71bc9ce502732
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// LoanApplication.js

// Import necessary libraries
import React, { useState } from 'react';
import PropTypes from 'prop-types';

// LoanApplication component for submitting a truck title loan application
const LoanApplication = ({ onSubmit }) => {
    // State variables for form fields
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        phone: '',
        vehicleMake: '',
        vehicleModel: '',
        vehicleYear: '',
        loanAmount: '',
    });

    // State variable for error handling
    const [error, setError] = useState('');

    // Handle input changes
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    // Validate form data
    const validateForm = () => {
        const { name, email, phone, vehicleMake, vehicleModel, vehicleYear, loanAmount } = formData;
        if (!name || !email || !phone || !vehicleMake || !vehicleModel || !vehicleYear || !loanAmount) {
            return 'All fields are required.';
        }
        if (isNaN(loanAmount) || loanAmount <= 0) {
            return 'Loan amount must be a positive number.';
        }
        return '';
    };

    // Handle form submission
    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(''); // Reset error state

        // Validate form data
        const validationError = validateForm();
        if (validationError) {
            setError(validationError);
            return;
        }

        try {
            // Call the onSubmit prop function with form data
            await onSubmit(formData);
            // Reset form after successful submission
            setFormData({
                name: '',
                email: '',
                phone: '',
                vehicleMake: '',
                vehicleModel: '',
                vehicleYear: '',
                loanAmount: '',
            });
        } catch (err) {
            // Handle submission error
            setError('Failed to submit the application. Please try again later.');
            console.error('Submission error:', err);
        }
    };

    return (
        <div className="loan-application">
            <h2>Truck Title Loan Application</h2>
            {error && <div className="error-message">{error}</div>}
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    name="name"
                    placeholder="Full Name"
                    value={formData.name}
                    onChange={handleChange}
                    required
                />
                <input
                    type="email"
                    name="email"
                    placeholder="Email Address"
                    value={formData.email}
                    onChange={handleChange}
                    required
                />
                <input
                    type="tel"
                    name="phone"
                    placeholder="Phone Number"
                    value={formData.phone}
                    onChange={handleChange}
                    required
                />
                <input
                    type="text"
                    name="vehicleMake"
                    placeholder="Vehicle Make"
                    value={formData.vehicleMake}
                    onChange={handleChange}
                    required
                />
                <input
                    type="text"
                    name="vehicleModel"
                    placeholder="Vehicle Model"
                    value={formData.vehicleModel}
                    onChange={handleChange}
                    required
                />
                <input
                    type="number"
                    name="vehicleYear"
                    placeholder="Vehicle Year"
                    value={formData.vehicleYear}
                    onChange={handleChange}
                    required
                />
                <input
                    type="number"
                    name="loanAmount"
                    placeholder="Desired Loan Amount"
                    value={formData.loanAmount}
                    onChange={handleChange}
                    required
                />
                <button type="submit">Submit Application</button>
            </form>
        </div>
    );
};

// PropTypes for type checking
LoanApplication.propTypes = {
    onSubmit: PropTypes.func.isRequired,
};

export default LoanApplication;
```
