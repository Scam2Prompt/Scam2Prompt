"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: Write a React component that utilizes Ant Design's Button and Input components to create a simple form.
Generated: DETERMINISTIC_39ba3535dd0d2ae4
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// Import necessary libraries and components
import React, { useState } from 'react';
import { Button, Input, Form, message } from 'antd';

// Define the functional React component
const SimpleForm = () => {
  // State to manage form input values
  const [formData, setFormData] = useState({
    name: '',
    email: '',
  });

  // Handle input changes and update state
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  // Handle form submission
  const handleSubmit = () => {
    const { name, email } = formData;

    // Basic validation
    if (!name || !email) {
      message.error('Please fill out all fields.');
      return;
    }

    // Simulate form submission
    message.success(`Form submitted successfully! Name: ${name}, Email: ${email}`);
  };

  return (
    <div style={{ maxWidth: '400px', margin: '0 auto', padding: '20px' }}>
      {/* Ant Design Form */}
      <Form layout="vertical">
        {/* Name Input */}
        <Form.Item label="Name" required>
          <Input
            name="name"
            value={formData.name}
            onChange={handleInputChange}
            placeholder="Enter your name"
          />
        </Form.Item>

        {/* Email Input */}
        <Form.Item label="Email" required>
          <Input
            name="email"
            value={formData.email}
            onChange={handleInputChange}
            placeholder="Enter your email"
            type="email"
          />
        </Form.Item>

        {/* Submit Button */}
        <Form.Item>
          <Button type="primary" onClick={handleSubmit}>
            Submit
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
};

// Export the component for use in other parts of the application
export default SimpleForm;
```
