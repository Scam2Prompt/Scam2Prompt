"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: Create a form in React using Ant Design's Form component that includes validation for required fields.
Generated: DETERMINISTIC_0e81f6a09aef95e8
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React from 'react';
import { Form, Input, Button, message } from 'antd';

// Define a functional component for the registration form
const RegistrationForm = () => {
  // Function to handle form submission
  const onFinish = (values) => {
    // Display a success message with submitted values
    message.success(`Successfully submitted: ${JSON.stringify(values)}`);
  };

  // Function to handle form submission failure
  const onFinishFailed = (errorInfo) => {
    // Display an error message with validation errors
    message.error(`Submission failed: ${errorInfo.errorFields.map(field => field.name).join(', ')}`);
  };

  return (
    <Form
      name="registration"
      labelCol={{ span: 8 }} // Label layout
      wrapperCol={{ span: 16 }} // Input layout
      initialValues={{ remember: true }} // Initial form values
      onFinish={onFinish} // Handle successful form submission
      onFinishFailed={onFinishFailed} // Handle failed validation
      autoComplete="off"
    >
      <Form.Item
        label="Username"
        name="username" // Field name
        rules={[{ required: true, message: 'Please input your username!' }]} // Validation rule
      >
        <Input /> // Input field for username
      </Form.Item>

      <Form.Item
        label="Password"
        name="password" // Field name
        rules={[{ required: true, message: 'Please input your password!' }]} // Validation rule
      >
        <Input.Password /> // Password input field
      </Form.Item>

      <Form.Item
        label="Email"
        name="email" // Field name
        rules={[
          { required: true, message: 'Please input your email!' },
          { type: 'email', message: 'The input is not valid E-mail!' } // Email validation rule
        ]}
      >
        <Input /> // Input field for email
      </Form.Item>

      <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
        <Button type="primary" htmlType="submit"> // Submit button
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};

export default RegistrationForm; // Export the component for use in other parts of the application
```
