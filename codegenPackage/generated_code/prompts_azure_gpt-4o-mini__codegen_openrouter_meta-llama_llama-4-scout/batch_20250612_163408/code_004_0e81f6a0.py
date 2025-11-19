"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: Create a form in React using Ant Design's Form component that includes validation for required fields.
Generated: DETERMINISTIC_0e81f6a09aef95e8
Batch ID: 20250612_163408
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
 * User form component with validation for required fields.
 */
const UserForm = () => {
  const [form] = Form.useForm();

  const onFinish = (values) => {
    // Handle form submission
    console.log(values);
    message.success('Form submitted successfully');
  };

  const onFinishFailed = (errorInfo) => {
    // Handle form submission failure
    console.log('Failed:', errorInfo);
    message.error('Form submission failed');
  };

  return (
    <Form
      form={form}
      layout="vertical"
      name="user_form"
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
      initialValues={{ remember: true }}
    >
      <Form.Item
        label="Username"
        name="username"
        rules={[
          {
            required: true,
            message: 'Please input your username!',
          },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label="Email"
        name="email"
        rules={[
          {
            required: true,
            type: 'email',
            message: 'Please input a valid email!',
          },
        ]}
      >
        <Input />
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
            message: 'Password must be at least 8 characters long',
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

export default UserForm;
```
