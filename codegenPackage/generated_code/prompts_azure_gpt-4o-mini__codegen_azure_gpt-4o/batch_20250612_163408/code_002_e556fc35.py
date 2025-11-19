"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: Can you provide an example of implementing a form using Ant Design in React?
Generated: DETERMINISTIC_e556fc3503148975
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary modules and components
import React from 'react';
import { Form, Input, Button, Checkbox, message } from 'antd';

// Define the functional component
const AntDesignForm = () => {
  // Form submission handler
  const onFinish = (values) => {
    // Display success message with form values
    message.success('Form submitted successfully!');
    console.log('Form Values:', values);
  };

  // Form submission failure handler
  const onFinishFailed = (errorInfo) => {
    // Display error message
    message.error('Form submission failed. Please check the fields.');
    console.error('Form Errors:', errorInfo);
  };

  return (
    <div style={{ maxWidth: 400, margin: '0 auto', padding: '20px' }}>
      {/* Ant Design Form */}
      <Form
        name="basicForm"
        layout="vertical"
        initialValues={{ remember: true }}
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
      >
        {/* Username Field */}
        <Form.Item
          label="Username"
          name="username"
          rules={[
            { required: true, message: 'Please input your username!' },
            { min: 3, message: 'Username must be at least 3 characters long.' },
          ]}
        >
          <Input placeholder="Enter your username" />
        </Form.Item>

        {/* Password Field */}
        <Form.Item
          label="Password"
          name="password"
          rules={[
            { required: true, message: 'Please input your password!' },
            { min: 6, message: 'Password must be at least 6 characters long.' },
          ]}
        >
          <Input.Password placeholder="Enter your password" />
        </Form.Item>

        {/* Remember Me Checkbox */}
        <Form.Item name="remember" valuePropName="checked">
          <Checkbox>Remember me</Checkbox>
        </Form.Item>

        {/* Submit Button */}
        <Form.Item>
          <Button type="primary" htmlType="submit" style={{ width: '100%' }}>
            Submit
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
};

// Export the component
export default AntDesignForm;
```
