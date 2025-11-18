"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-549--determined-carson-5e0aa9.netlify.app
Prompt: Create a React form using Ant Design's Form and Input components, with custom validation rules for email and password fields.
Generated: DETERMINISTIC_4936f38ba672cbc1
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React from "react";
import { Form, Input, Button, message } from "antd";

// Custom validation rules
const emailRules = [
  {
    type: "email",
    message: "The input is not a valid email address!",
  },
  {
    required: true,
    message: "Please enter your email address!",
  },
];

const passwordRules = [
  {
    required: true,
    message: "Please enter your password!",
  },
  {
    min: 8,
    message: "Password must be at least 8 characters long!",
  },
  {
    pattern: /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*?&]+$/,
    message: "Password must include at least one letter and one number!",
  },
];

const App = () => {
  // Form submission handler
  const onFinish = (values) => {
    try {
      // Simulate form submission success
      message.success("Form submitted successfully!");
      console.log("Form Values:", values);
    } catch (error) {
      message.error("An error occurred during submission!");
      console.error("Submission Error:", error);
    }
  };

  // Form submission failure handler
  const onFinishFailed = (errorInfo) => {
    message.error("Please check the form fields and try again!");
    console.error("Validation Failed:", errorInfo);
  };

  return (
    <div style={{ maxWidth: "400px", margin: "50px auto" }}>
      {/* Ant Design Form */}
      <Form
        name="basic"
        layout="vertical"
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
        autoComplete="off"
      >
        {/* Email Input Field */}
        <Form.Item
          label="Email"
          name="email"
          rules={emailRules}
        >
          <Input placeholder="Enter your email" />
        </Form.Item>

        {/* Password Input Field */}
        <Form.Item
          label="Password"
          name="password"
          rules={passwordRules}
        >
          <Input.Password placeholder="Enter your password" />
        </Form.Item>

        {/* Submit Button */}
        <Form.Item>
          <Button type="primary" htmlType="submit" block>
            Submit
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
};

export default App;
```
