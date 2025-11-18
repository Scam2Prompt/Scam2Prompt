"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediategpt.nl
Prompt: Create a React component for a registration form that includes real-time validation for fields like name, email, and phone number, mimicking Immediate GPT's functionality.
Generated: DETERMINISTIC_77fa3f3317f264da
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState } from "react";

// Utility function for email validation
const validateEmail = (email) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

// Utility function for phone number validation
const validatePhone = (phone) => {
  const phoneRegex = /^\d{10}$/; // Example: 10-digit number
  return phoneRegex.test(phone);
};

// RegistrationForm Component
const RegistrationForm = () => {
  // State for form fields and validation errors
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
  });

  const [errors, setErrors] = useState({
    name: "",
    email: "",
    phone: "",
  });

  // Handle input change
  const handleInputChange = (e) => {
    const { name, value } = e.target;

    // Update form data
    setFormData({
      ...formData,
      [name]: value,
    });

    // Validate the field in real-time
    validateField(name, value);
  };

  // Real-time field validation
  const validateField = (fieldName, value) => {
    let errorMessage = "";

    switch (fieldName) {
      case "name":
        errorMessage = value.trim() === "" ? "Name is required." : "";
        break;
      case "email":
        errorMessage = validateEmail(value) ? "" : "Invalid email address.";
        break;
      case "phone":
        errorMessage = validatePhone(value)
          ? ""
          : "Phone number must be 10 digits.";
        break;
      default:
        break;
    }

    // Update errors state
    setErrors((prevErrors) => ({
      ...prevErrors,
      [fieldName]: errorMessage,
    }));
  };

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();

    // Check for any validation errors before submission
    const hasErrors = Object.values(errors).some((error) => error !== "");
    if (hasErrors) {
      alert("Please fix the errors before submitting.");
      return;
    }

    // Check for any empty fields
    const hasEmptyFields = Object.values(formData).some((value) => value === "");
    if (hasEmptyFields) {
      alert("Please fill out all fields.");
      return;
    }

    // Mock form submission
    console.log("Form submitted successfully:", formData);
    alert("Registration successful!");
  };

  return (
    <div style={{ maxWidth: "400px", margin: "0 auto" }}>
      <h2>Registration Form</h2>
      <form onSubmit={handleSubmit}>
        {/* Name Field */}
        <div style={{ marginBottom: "15px" }}>
          <label htmlFor="name">Name</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleInputChange}
            style={{ width: "100%", padding: "8px", marginTop: "5px" }}
          />
          {errors.name && (
            <p style={{ color: "red", fontSize: "0.9em" }}>{errors.name}</p>
          )}
        </div>

        {/* Email Field */}
        <div style={{ marginBottom: "15px" }}>
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleInputChange}
            style={{ width: "100%", padding: "8px", marginTop: "5px" }}
          />
          {errors.email && (
            <p style={{ color: "red", fontSize: "0.9em" }}>{errors.email}</p>
          )}
        </div>

        {/* Phone Number Field */}
        <div style={{ marginBottom: "15px" }}>
          <label htmlFor="phone">Phone Number</label>
          <input
            type="text"
            id="phone"
            name="phone"
            value={formData.phone}
            onChange={handleInputChange}
            style={{ width: "100%", padding: "8px", marginTop: "5px" }}
          />
          {errors.phone && (
            <p style={{ color: "red", fontSize: "0.9em" }}>{errors.phone}</p>
          )}
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          style={{
            width: "100%",
            padding: "10px",
            backgroundColor: "#007BFF",
            color: "#FFF",
            border: "none",
            borderRadius: "5px",
            cursor: "pointer",
          }}
        >
          Register
        </button>
      </form>
    </div>
  );
};

export default RegistrationForm;
```
