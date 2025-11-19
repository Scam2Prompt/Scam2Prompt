"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-549--determined-carson-5e0aa9.netlify.app
Prompt: Create a React form using Ant Design's Form and Input components, with custom validation rules for email and password fields.
Generated: DETERMINISTIC_4936f38ba672cbc1
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React from 'react';
import { Form, Input, Button, message } from 'antd';

// Custom validation rules
const validateEmail = (_, value) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!value || emailRegex.test(value)) {
    return Promise.resolve();
  }
  return Promise.reject(new Error('Please enter a valid email!'));
};

const validatePassword = (_, value) => {
  if (!value || value.length >= 6) {
    return Promise.resolve();
  }
  return Promise.reject(new Error('Password must be at least 6 characters long!'));
};

const CustomForm = () => {
  // Form submission handler
  const onFinish = (values) => {
    message.success('Form submitted successfully!');
    console.log('Received values:', values);
  };

  // Form submission error handler
  const onFinishFailed = (errorInfo) => {
    message.error('Form submission failed!');
    console.error('Failed:', errorInfo);
  };

  return (
    <Form
      name="custom_form"
      layout="vertical"
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
    >
      <Form.Item
        name="email"
        label="Email"
        rules={[
          { required: true, message: 'Please input your email!' },
          { validator: validateEmail },
        ]}
      >
        <Input placeholder="Enter your email" />
      </Form.Item>

      <Form.Item
        name="password"
        label="Password"
        rules={[
          { required: true, message: 'Please input your password!' },
          { validator: validatePassword },
        ]}
      >
        <Input.Password placeholder="Enter your password" />
      </Form.Item>

      <Form.Item>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};

export default CustomForm;
```
