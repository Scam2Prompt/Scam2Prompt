"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: Write a React component that utilizes Ant Design's Button and Input components to create a simple form.
Generated: DETERMINISTIC_39ba3535dd0d2ae4
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState } from "react";
import { Button, Input, Form, message } from "antd";

// Functional React component utilizing Ant Design's Button and Input components
const SimpleForm = () => {
  // State to manage form input value
  const [inputValue, setInputValue] = useState("");

  // Event handler for form submission
  const handleSubmit = () => {
    if (!inputValue.trim()) {
      // Show error message if input is empty
      message.error("Please enter a value!");
      return;
    }

    // Show success message on valid submission
    message.success(`Form submitted with value: ${inputValue}`);
    // Reset the input field
    setInputValue("");
  };

  // Event handler for input change
  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  return (
    <div style={{ maxWidth: "400px", margin: "50px auto" }}>
      <Form
        layout="vertical"
        onFinish={handleSubmit} // Ant Design's form submission handler
      >
        {/* Input field for user input */}
        <Form.Item
          label="Your Input"
          rules={[
            {
              required: true,
              message: "Input cannot be empty!",
            },
          ]}
        >
          <Input
            placeholder="Type something..."
            value={inputValue}
            onChange={handleInputChange}
          />
        </Form.Item>

        {/* Submit button */}
        <Form.Item>
          <Button type="primary" htmlType="submit">
            Submit
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
};

export default SimpleForm;
```
