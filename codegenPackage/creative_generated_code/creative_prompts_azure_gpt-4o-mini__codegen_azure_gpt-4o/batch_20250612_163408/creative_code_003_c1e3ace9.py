"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Generate a sample form using Ant Design's Form component with validation rules.
Generated: DETERMINISTIC_c1e3ace9ad2a5fb6
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React from "react";
import { Form, Input, Button } from "antd";

const SampleForm = () => {
  const [form] = Form.useForm();

  // Function to handle form submission
  const onFinish = (values) => {
    console.log("Form Values: ", values);
  };

  // Function to handle form submission errors
  const onFinishFailed = (errorInfo) => {
    console.error("Form Errors: ", errorInfo);
  };

  return (
    <Form
      form={form}
      name="sampleForm"
      layout="vertical"
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
      autoComplete="off"
    >
      {/* Input field for 'Name' with validation rules */}
      <Form.Item
        label="Name"
        name="name"
        rules={[
          {
            required: true,
            message: "Please enter your name!",
          },
          {
            min: 3,
            message: "Name must be at least 3 characters long.",
          },
          {
            max: 50,
            message: "Name cannot exceed 50 characters.",
          },
        ]}
      >
        <Input placeholder="Enter your name" />
      </Form.Item>

      {/* Input field for 'Email' with validation rules */}
      <Form.Item
        label="Email"
        name="email"
        rules={[
          {
            required: true,
            message: "Please enter your email!",
          },
          {
            type: "email",
            message: "Please enter a valid email address!",
          },
        ]}
      >
        <Input placeholder="Enter your email" />
      </Form.Item>

      {/* Input field for 'Password' with validation rules */}
      <Form.Item
        label="Password"
        name="password"
        rules={[
          {
            required: true,
            message: "Please enter your password!",
          },
          {
            min: 6,
            message: "Password must be at least 6 characters long.",
          },
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

export default SampleForm;
```
