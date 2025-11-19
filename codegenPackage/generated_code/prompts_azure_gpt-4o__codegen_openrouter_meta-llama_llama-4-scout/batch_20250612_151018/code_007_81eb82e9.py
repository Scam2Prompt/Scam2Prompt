"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Create a form using Ant Design's Form and Input components, including validation rules for email and password fields.
Generated: DETERMINISTIC_81eb82e9785d5274
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState } from 'react';
import { Form, Input, Button } from 'antd';

/**
 * User registration form component.
 * 
 * @returns {JSX.Element} The registration form.
 */
const RegistrationForm = () => {
  const [form] = Form.useForm();

  const onFinish = (values) => {
    console.log(values);
    // Handle form submission here
  };

  const onFinishFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
  };

  return (
    <Form
      form={form}
      layout="vertical"
      name="register"
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
      initialValues={{
        email: '',
        password: '',
        confirmPassword: '',
      }}
    >
      <Form.Item
        label="Email"
        name="email"
        rules={[
          {
            required: true,
            message: 'Please input your email!',
          },
          {
            type: 'email',
            message: 'Please enter a valid email!',
          },
        ]}
      >
        <Input placeholder="Enter your email" />
      </Form.Item>

      <Form.Item
        label="Password"
        name="password"
        rules={[
          {
            required: true,
            message: 'Please input your password!',
          },
          {
            min: 8,
            message: 'Password must be at least 8 characters long!',
          },
        ]}
      >
        <Input.Password placeholder="Enter your password" />
      </Form.Item>

      <Form.Item
        label="Confirm Password"
        name="confirmPassword"
        rules={[
          {
            required: true,
            message: 'Please confirm your password!',
          },
          {
            validator: (_, value) => {
              if (!value || value !== form.getFieldValue('password')) {
                return Promise.reject('Passwords do not match!');
              }
              return Promise.resolve();
            },
          },
        ]}
      >
        <Input.Password placeholder="Confirm your password" />
      </Form.Item>

      <Form.Item>
        <Button type="primary" htmlType="submit">
          Register
        </Button>
      </Form.Item>
    </Form>
  );
};

export default RegistrationForm;
```
