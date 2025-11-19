"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Generate a sample form using Ant Design's Form component with validation rules.
Generated: DETERMINISTIC_c1e3ace9ad2a5fb6
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary modules from React and Ant Design
import React from 'react';
import { Form, Input, Button } from 'antd';

// Define the functional component
const SampleForm = () => {
  // Form submission handler
  const onFinish = (values) => {
    console.log('Form submitted successfully:', values);
  };

  // Form submission failure handler
  const onFinishFailed = (errorInfo) => {
    console.error('Form submission failed:', errorInfo);
  };

  return (
    <Form
      // Form layout configuration
      layout="vertical"
      name="sampleForm"
      initialValues={{ remember: true }}
      onFinish={onFinish} // Success handler
      onFinishFailed={onFinishFailed} // Failure handler
    >
      {/* Username field with validation rules */}
      <Form.Item
        label="Username"
        name="username"
        rules={[
          { required: true, message: 'Please input your username!' }, // Required field validation
          { min: 3, message: 'Username must be at least 3 characters long!' }, // Minimum length validation
        ]}
      >
        <Input placeholder="Enter your username" />
      </Form.Item>

      {/* Email field with validation rules */}
      <Form.Item
        label="Email"
        name="email"
        rules={[
          { required: true, message: 'Please input your email!' }, // Required field validation
          { type: 'email', message: 'Please enter a valid email address!' }, // Email format validation
        ]}
      >
        <Input placeholder="Enter your email" />
      </Form.Item>

      {/* Password field with validation rules */}
      <Form.Item
        label="Password"
        name="password"
        rules={[
          { required: true, message: 'Please input your password!' }, // Required field validation
          { min: 6, message: 'Password must be at least 6 characters long!' }, // Minimum length validation
        ]}
      >
        <Input.Password placeholder="Enter your password" />
      </Form.Item>

      {/* Submit button */}
      <Form.Item>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};

// Export the component for use in other parts of the application
export default SampleForm;
```
