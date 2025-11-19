"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-542--determined-carson-5e0aa9.netlify.app
Prompt: Write React code using Ant Design components to create a responsive form with validation rules for user input.
Generated: DETERMINISTIC_011122043b7e31ee
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
import { 
  Form, 
  Input, 
  Button, 
  Space, 
  message, 
  Row, 
  Col 
} from 'antd';

/**
 * User registration form component.
 * 
 * @returns {JSX.Element} The registration form.
 */
const RegistrationForm = () => {
  const [form] = Form.useForm();

  const onFinish = async (values) => {
    try {
      // Submit form data to server
      const response = await fetch('/api/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(values),
      });

      if (response.ok) {
        message.success('Registration successful!');
        form.resetFields();
      } else {
        message.error('Registration failed. Please try again.');
      }
    } catch (error) {
      console.error(error);
      message.error('An error occurred. Please try again.');
    }
  };

  const onFinishFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
    message.error('Please fill in all required fields.');
  };

  return (
    <Row justify="center">
      <Col xs={22} sm={16} md={12} lg={8}>
        <Form 
          form={form} 
          layout="vertical" 
          name="register_form" 
          onFinish={onFinish} 
          onFinishFailed={onFinishFailed}
        >
          <Form.Item 
            label="Username" 
            name="username" 
            rules={[
              {
                required: true,
                message: 'Please input your username!',
              },
              {
                min: 3,
                message: 'Username must be at least 3 characters.',
              },
              {
                max: 20,
                message: 'Username must be no more than 20 characters.',
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
                message: 'Password must be at least 8 characters.',
              },
            ]}
          >
            <Input.Password />
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
                  if (value !== form.getFieldValue('password')) {
                    return Promise.reject('Passwords do not match.');
                  }
                  return Promise.resolve();
                },
              },
            ]}
          >
            <Input.Password />
          </Form.Item>

          <Form.Item>
            <Space>
              <Button type="primary" htmlType="submit">
                Register
              </Button>
              <Button type="link" onClick={() => form.resetFields()}>
                Reset
              </Button>
            </Space>
          </Form.Item>
        </Form>
      </Col>
    </Row>
  );
};

export default RegistrationForm;
```
