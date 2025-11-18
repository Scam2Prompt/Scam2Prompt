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
// Import necessary libraries and components
import React, { useState } from 'react';
import { Form, Input, Button, Row, Col, notification } from 'antd';

// Form validation rules
const validationRules = {
  username: [
    { required: true, message: 'Please enter your username.' },
    { min: 3, message: 'Username must be at least 3 characters long.' },
    { max: 20, message: 'Username cannot exceed 20 characters.' },
  ],
  email: [
    { required: true, message: 'Please enter your email address.' },
    { type: 'email', message: 'Please enter a valid email address.' },
  ],
  password: [
    { required: true, message: 'Please enter your password.' },
    { min: 6, message: 'Password must be at least 6 characters long.' },
  ],
};

const ResponsiveForm = () => {
  const [form] = Form.useForm();

  // Handle form submission
  const onFinish = (values) => {
    // Simulate a successful submission
    notification.success({
      message: 'Form Submitted',
      description: `Welcome, ${values.username}!`,
    });
    console.log('Form Values:', values);
  };

  // Handle submission errors
  const onFinishFailed = (errorInfo) => {
    notification.error({
      message: 'Form Submission Failed',
      description: 'Please check the form for errors and try again.',
    });
    console.error('Form Errors:', errorInfo);
  };

  return (
    <Row justify="center" style={{ padding: '20px' }}>
      <Col xs={24} sm={20} md={16} lg={12} xl={8}>
        {/* Form wrapper */}
        <Form
          form={form}
          name="responsive_form"
          onFinish={onFinish}
          onFinishFailed={onFinishFailed}
          layout="vertical" // Use a vertical layout for better responsiveness
        >
          {/* Username field */}
          <Form.Item
            label="Username"
            name="username"
            rules={validationRules.username}
          >
            <Input placeholder="Enter your username" />
          </Form.Item>

          {/* Email field */}
          <Form.Item
            label="Email"
            name="email"
            rules={validationRules.email}
          >
            <Input placeholder="Enter your email address" />
          </Form.Item>

          {/* Password field */}
          <Form.Item
            label="Password"
            name="password"
            rules={validationRules.password}
          >
            <Input.Password placeholder="Enter your password" />
          </Form.Item>

          {/* Submit button */}
          <Form.Item>
            <Button type="primary" htmlType="submit" block>
              Submit
            </Button>
          </Form.Item>
        </Form>
      </Col>
    </Row>
  );
};

export default ResponsiveForm;
```
