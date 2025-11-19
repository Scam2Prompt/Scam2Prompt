"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-549--determined-carson-5e0aa9.netlify.app
Prompt: Generate a React component using Ant Design's UI design language.
Generated: DETERMINISTIC_ec7925510f57c9c9
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';
import { Button, Input, Form, message } from 'antd';

// Define a functional component named UserForm
const UserForm = () => {
  // State to manage form data
  const [form] = Form.useForm();

  // Function to handle form submission
  const onFinish = async (values) => {
    try {
      // Simulate an API call
      await new Promise((resolve) => setTimeout(resolve, 1000));
      message.success('Form submitted successfully!');
      console.log('Received values:', values);
      form.resetFields(); // Reset form fields after successful submission
    } catch (error) {
      message.error('Failed to submit form. Please try again.');
      console.error('Submission error:', error);
    }
  };

  // Function to handle form submission failure
  const onFinishFailed = (errorInfo) => {
    message.error('Please fill in all required fields.');
    console.error('Form submission failed:', errorInfo);
  };

  return (
    <Form
      form={form}
      name="userForm"
      layout="vertical"
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
    >
      <Form.Item
        label="Name"
        name="name"
        rules={[{ required: true, message: 'Please input your name!' }]}
      >
        <Input placeholder="Enter your name" />
      </Form.Item>

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
