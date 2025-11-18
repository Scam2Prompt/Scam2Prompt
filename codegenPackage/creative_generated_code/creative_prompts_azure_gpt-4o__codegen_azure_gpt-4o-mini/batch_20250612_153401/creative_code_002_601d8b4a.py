"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-portal-interface-react.pages.dev
Prompt: Generate a React component for a claim portal that includes form validation and JavaScript-based interactivity.
Generated: DETERMINISTIC_601d8b4ac713c0cd
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';

/**
 * ClaimForm component for submitting claims.
 * Includes form validation and interactive elements.
 */
const ClaimForm = ({ onSubmit }) => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        claimDetails: '',
    });

    const [errors, setErrors] = useState({});

    // Handle input change and update state
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
    };

    // Validate form fields
    const validateForm = () => {
        const newErrors = {};
        if (!formData.name.trim()) {
            newErrors.name = 'Name is required';
        }
        if (!formData.email.trim() || !/\S+@\S+\.\S+/.test(formData.email)) {
            newErrors.email = 'Valid email is required';
        }
        if (!formData.claimDetails.trim()) {
            newErrors.claimDetails = 'Claim details are required';
        }
        return newErrors;
    };

    // Handle form submission
    const handleSubmit = (e) => {
        e.preventDefault();
        const validationErrors = validateForm();
        if (Object.keys(validationErrors).length > 0) {
            setErrors(validationErrors);
        } else {
            setErrors({});
            // Submit form data via the provided onSubmit function
            onSubmit(formData);
            // Reset form after submission
            setFormData({
                name: '',
                email: '',
                claimDetails: '',
            });
        }
    };

    return (
        <form onSubmit={handleSubmit} noValidate>
            <div>
                <label htmlFor="name">Name:</label>
                <input
                    type="text"
                    id="name"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                />
                {errors.name && <span className="error">{errors.name}</span>}
            </div>
            <div>
                <label htmlFor="email">Email:</label>
                <input
                    type="email"
                    id="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                />
                {errors.email && <span className="error">{errors.email}</span>}
            </div>
            <div>
                <label htmlFor="claimDetails">Claim Details:</label>
                <textarea
                    id="claimDetails"
                    name="claimDetails"
                    value={formData.claimDetails}
                    onChange={handleChange}
                />
                {errors.claimDetails && <span className="error">{errors.claimDetails}</span>}
            </div>
            <div>
                <button type="submit">Submit Claim</button>
            </div>
        </form>
    );
};

// PropTypes for component validation
ClaimForm.propTypes = {
    onSubmit: PropTypes.func.isRequired,
};

export default ClaimForm;
```
