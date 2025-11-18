"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Write a React component using Ant Design's Button and Form components to create a user login form with validation.
Generated: DETERMINISTIC_8ccc7c39340c5412
Batch ID: 20250612_151018
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

// Define the LoginForm component
const LoginForm = () => {
  // Handle form submission
  const onFinish = (values) => {
    // Simulate a login API call
    console.log('Success:', values);
    message.success('Login successful!');
  };

  // Handle form submission failure
  const onFinishFailed = (errorInfo) => {
    console.error('Failed:', errorInfo);
    message.error('Login failed. Please check your credentials.');
  };

  return (
    <Form
      name="login"
      layout="vertical"
      initialValues={{ remember: true }}
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
      style={{ maxWidth: 300, margin: 'auto' }}
    >
      <Form.Item
        label="Username"
        name="username"
        rules={[
          { required: true, message: 'Please input your username!' },
          { min: 3, message: 'Username must be at least 3 characters.' }
        ]}
      >
        <Input placeholder="Enter your username" />
      </Form.Item>

      <Form.Item
        label="Password"
        name="password"
        rules={[
          { required: true, message: 'Please input your password!' },
          { min: 6, message: 'Password must be at least 6 characters.' }
        ]}
      >
        <Input.Password placeholder="Enter your password" />
      </Form.Item>

      <Form.Item>
        <Button type="primary" htmlType="submit" block>
          Login
        </Button>
      </Form.Item>
    </Form>
  );
};

export default LoginForm;
```
