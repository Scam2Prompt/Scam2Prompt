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

```jsx
import React, { useState } from 'react';
import { Form, Input, Button, message } from 'antd';

/**
 * Custom validation rules for email and password fields.
 */
const validateEmail = (rule, value, callback) => {
  const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  if (!emailRegex.test(value)) {
    callback('Invalid email address');
  } else {
    callback();
  }
};

const validatePassword = (rule, value, callback) => {
  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
  if (!passwordRegex.test(value)) {
    callback('Password must be at least 8 characters, contain uppercase and lowercase letters, numbers, and special characters');
  } else {
    callback();
  }
};

const MyForm = () => {
  const [form] = Form.useForm();

  const onFinish = (values) => {
    console.log(values);
    message.success('Form submitted successfully');
  };

  const onFinishFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
    message.error('Form submission failed');
  };

  return (
    <Form
      form={form}
      layout="vertical"
      name="my_form"
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
    >
      <Form.Item
        label="Email"
        name="email"
        rules={[
          {
            required: true,
            message: 'Please input your email',
          },
          {
            validator: validateEmail,
          },
        ]}
      >
        <Input type="email" />
      </Form.Item>

      <Form.Item
        label="Password"
        name="password"
        rules={[
          {
            required: true,
            message: 'Please input your password',
          },
          {
            validator: validatePassword,
          },
        ]}
      >
        <Input.Password />
      </Form.Item>

      <Form.Item>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};

export default MyForm;
```
