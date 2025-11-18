"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-542--determined-carson-5e0aa9.netlify.app
Prompt: Write React code using Ant Design components to create a responsive form with validation rules for user input.
Generated: DETERMINISTIC_011122043b7e31ee
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

// Create a functional component for the User Form
const UserForm = () => {
  // Form submission handler
  const onFinish = (values) => {
    // Display a success message
    message.success('Form submitted successfully!', values);
  };

  // Form submission error handler
  const onFinishFailed = (errorInfo) => {
    // Display the error information
    message.error('Form submission failed:', errorInfo);
  };

  return (
    <Form
      name="user_form"
      layout="vertical"
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
      initialValues={{
        username: '',
        email: '',
        password: '',
      }}
    >
      {/* Username field */}
      <Form.Item
        label="Username"
        name="username"
        rules={[
          { required: true, message: 'Please input your username!' },
          { min: 3, message: 'Username must be at least 3 characters.' },
        ]}
      >
        <Input placeholder="Enter your username" />
      </Form.Item>

      {/* Email field */}
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

      {/* Password field */}
      <Form.Item
        label="Password"
        name="password"
        rules={[
          { required: true, message: 'Please input your password!' },
          { min: 6, message: 'Password must be at least 6 characters.' },
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

// Export the UserForm component
export default UserForm;
```

Make sure to install the Ant Design library before running this code:

```bash
npm install antd
```

You can then import and use the `UserForm` component in your application.
