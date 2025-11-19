"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Generate a sample form using Ant Design's Form component with validation rules.
Generated: DETERMINISTIC_c1e3ace9ad2a5fb6
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

// SampleForm component definition
const SampleForm = () => {
  // Form submission handler
  const onFinish = (values) => {
    // Simulating an API call
    console.log('Received values:', values);
    message.success('Form submitted successfully!');
  };

  // Form submission failure handler
  const onFinishFailed = (errorInfo) => {
    console.error('Failed:', errorInfo);
    message.error('Form submission failed. Please check the fields.');
  };

  return (
    <Form
      name="sample_form"
      layout="vertical"
      initialValues={{ remember: true }}
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
      autoComplete="off"
    >
      {/* Username Field */}
      <Form.Item
        label="Username"
        name="username"
        rules={[
          { required: true, message: 'Please input your username!' },
          { min: 3, message: 'Username must be at least 3 characters long!' },
        ]}
      >
        <Input placeholder="Enter your username" />
      </Form.Item>

      {/* Email Field */}
      <Form.Item
        label="Email"
        name="email"
        rules={[
          { required: true, message: 'Please input your email!' },
          { type: 'email', message: 'Please enter a valid email!' },
        ]}
      >
        <Input placeholder="Enter your email" />
      </Form.Item>

      {/* Password Field */}
      <Form.Item
        label="Password"
        name="password"
        rules={[
          { required: true, message: 'Please input your password!' },
          { min: 6, message: 'Password must be at least 6 characters long!' },
        ]}
      >
        <Input.Password placeholder="Enter your password" />
      </Form.Item>

      {/* Submit Button */}
      <Form.Item>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};

// Exporting the SampleForm component
export default SampleForm;
```
