"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: Can you provide an example of implementing a form using Ant Design in React?
Generated: DETERMINISTIC_e556fc3503148975
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
import React, { useState } from "react";
import { Form, Input, Button, message } from "antd";

// Define the form layout and functionality
const MyForm = () => {
  const [form] = Form.useForm(); // Ant Design Form instance
  const [loading, setLoading] = useState(false); // Loading state for button

  // Handle form submission
  const onFinish = async (values) => {
    try {
      setLoading(true); // Set loading state when form is submitting
      console.log("Form Submitted:", values); // Log submitted values
      
      // Simulate API call (replace with actual API logic)
      await new Promise((resolve) => setTimeout(resolve, 1000));
      
      message.success("Form submitted successfully!"); // Success notification
      form.resetFields(); // Reset form fields after successful submission
    } catch (error) {
      message.error("Failed to submit the form."); // Error notification
    } finally {
      setLoading(false); // Reset loading state
    }
  };

  // Handle form submission failure
  const onFinishFailed = (errorInfo) => {
    console.error("Form Submission Failed:", errorInfo);
    message.error("Please correct the errors in the form and try again.");
  };

  return (
    <div style={{ maxWidth: 400, margin: "0 auto", padding: "20px" }}>
      <h2 style={{ textAlign: "center" }}>Ant Design Form Example</h2>
      
      {/* Ant Design Form component */}
      <Form
        form={form}
        layout="vertical" // Vertical layout for form items
        name="my_form"
        onFinish={onFinish} // Callback when form submission is successful
        onFinishFailed={onFinishFailed} // Callback when form submission fails
        autoComplete="off"
      >
        {/* Username input field */}
        <Form.Item
          label="Username"
          name="username"
          rules={[
            { required: true, message: "Please enter your username!" },
            { min: 3, message: "Username must be at least 3 characters long!" },
          ]}
        >
          <Input placeholder="Enter your username" />
        </Form.Item>

        {/* Email input field */}
        <Form.Item
          label="Email"
          name="email"
          rules={[
            { required: true, message: "Please enter your email!" },
            { type: "email", message: "Please enter a valid email address!" },
          ]}
        >
          <Input placeholder="Enter your email" />
        </Form.Item>

        {/* Password input field */}
        <Form.Item
          label="Password"
          name="password"
          rules={[
            { required: true, message: "Please enter your password!" },
            { min: 6, message: "Password must be at least 6 characters long!" },
          ]}
        >
          <Input.Password placeholder="Enter your password" />
        </Form.Item>

        {/* Submit button */}
        <Form.Item>
          <Button
            type="primary"
            htmlType="submit"
            loading={loading} // Show loading state while form submission is in progress
            block // Full-width button
          >
            Submit
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
};

export default MyForm;
```
