"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Create a form using Ant Design's Form and Input components, including validation rules for email and password fields.
Generated: DETERMINISTIC_81eb82e9785d5274
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
import { Form, Input, Button } from 'antd';

// Define the layout for the form
const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};

// Define the tail layout for the submit button
const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

// Create a functional component for the form
const LoginForm = () => {
  // Handle form submission
  const onFinish = (values) => {
    console.log('Success:', values);
  };

  // Handle form submission failure
  const onFinishFailed = (errorInfo) => {
    console.error('Failed:', errorInfo);
  };

  return (
    <Form
      {...layout}
      name="login"
      initialValues={{ remember: true }}
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
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
            message: 'The input is not a valid email!',
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
            min: 6,
            message: 'Password must be at least 6 characters long!',
          },
        ]}
      >
        <Input.Password />
      </Form.Item>

      <Form.Item {...tailLayout}>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};

export default LoginForm;
```
