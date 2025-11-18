"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freefinance.pages.dev
Prompt: Generate code for a React form to input and validate financial data, similar to the features on freefinance.pages.dev.
Generated: DETERMINISTIC_68a5ab148bb10e13
Batch ID: 20250612_154142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary libraries
import React, { useState } from "react";

// Define the FinancialDataForm component
const FinancialDataForm = () => {
  // State for form fields
  const [formData, setFormData] = useState({
    income: "",
    expenses: "",
    savings: "",
  });

  // State for validation errors
  const [errors, setErrors] = useState({});

  // Handle input change
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  // Validate form data
  const validate = () => {
    const newErrors = {};
    const { income, expenses, savings } = formData;

    // Ensure income is a positive number
    if (!income || isNaN(income) || parseFloat(income) <= 0) {
      newErrors.income = "Income must be a positive number.";
    }

    // Ensure expenses are a positive number
    if (!expenses || isNaN(expenses) || parseFloat(expenses) < 0) {
      newErrors.expenses = "Expenses must be a non-negative number.";
    }

    // Ensure savings are a positive number
    if (!savings || isNaN(savings) || parseFloat(savings) < 0) {
      newErrors.savings = "Savings must be a non-negative number.";
    }

    return newErrors;
  };

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault(); // Prevent default form submission behavior

    const newErrors = validate(); // Perform validation
    setErrors(newErrors);

    // If no errors exist, process the data
    if (Object.keys(newErrors).length === 0) {
      console.log("Form Data Submitted:", formData);
      alert("Form submitted successfully!");
    }
  };

  return (
    <div style={{ maxWidth: "400px", margin: "0 auto" }}>
      <h2>Financial Data Form</h2>
      <form onSubmit={handleSubmit}>
        {/* Income Input Field */}
        <div>
          <label htmlFor="income">Monthly Income ($):</label>
          <input
            type="text"
            id="income"
            name="income"
            value={formData.income}
            onChange={handleChange}
          />
          {errors.income && <p style={{ color: "red" }}>{errors.income}</p>}
        </div>

        {/* Expenses Input Field */}
        <div>
          <label htmlFor="expenses">Monthly Expenses ($):</label>
          <input
            type="text"
            id="expenses"
            name="expenses"
            value={formData.expenses}
            onChange={handleChange}
          />
          {errors.expenses && <p style={{ color: "red" }}>{errors.expenses}</p>}
        </div>

        {/* Savings Input Field */}
        <div>
          <label htmlFor="savings">Monthly Savings ($):</label>
          <input
            type="text"
            id="savings"
            name="savings"
            value={formData.savings}
            onChange={handleChange}
          />
          {errors.savings && <p style={{ color: "red" }}>{errors.savings}</p>}
        </div>

        {/* Submit Button */}
        <button type="submit" style={{ marginTop: "10px" }}>
          Submit
        </button>
      </form>
    </div>
  );
};

// Export the component
export default FinancialDataForm;
```
