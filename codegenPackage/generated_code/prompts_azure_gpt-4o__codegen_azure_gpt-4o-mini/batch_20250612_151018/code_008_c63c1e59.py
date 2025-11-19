"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-542--determined-carson-5e0aa9.netlify.app
Prompt: Generate code to implement a multi-step form using Ant Design's Steps and Form components.
Generated: DETERMINISTIC_c63c1e59a9f4a189
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';
import { Steps, Button, Form, Input, message } from 'antd';

const { Step } = Steps;

// MultiStepForm component
const MultiStepForm = () => {
  // State to manage the current step
  const [current, setCurrent] = useState(0);
  // State to hold form data
  const [formData, setFormData] = useState({});

  // Handler for form submission
  const onFinish = (values) => {
    // Update form data with the current step's values
    setFormData({ ...formData, ...values });
    // Move to the next step
    setCurrent(current + 1);
  };

  // Handler for going back to the previous step
  const handlePrev = () => {
    setCurrent(current - 1);
  };

  // Handler for form submission on the last step
  const handleSubmit = () => {
    // Here you can send formData to your API or handle it as needed
    message.success('Form submitted successfully!');
    console.log('Final Form Data:', formData);
  };

  // Steps configuration
  const steps = [
    {
      title: 'Step 1',
      content: (
        <Form onFinish={onFinish}>
          <Form.Item
            name="name"
            label="Name"
            rules={[{ required: true, message: 'Please input your name!' }]}
          >
            <Input />
          </Form.Item>
          <Form.Item>
            <Button type="primary" htmlType="submit">
              Next
            </Button>
          </Form.Item>
        </Form>
      ),
    },
    {
      title: 'Step 2',
      content: (
        <Form onFinish={onFinish}>
          <Form.Item
            name="email"
            label="Email"
            rules={[{ required: true, message: 'Please input your email!' }]}
          >
            <Input />
          </Form.Item>
          <Form.Item>
            <Button type="default" onClick={handlePrev}>
              Previous
            </Button>
            <Button type="primary" htmlType="submit">
              Next
            </Button>
          </Form.Item>
        </Form>
      ),
    },
    {
      title: 'Step 3',
      content: (
        <Form onFinish={handleSubmit}>
          <Form.Item
            name="address"
            label="Address"
            rules={[{ required: true, message: 'Please input your address!' }]}
          >
            <Input />
          </Form.Item>
          <Form.Item>
            <Button type="default" onClick={handlePrev}>
              Previous
            </Button>
            <Button type="primary" htmlType="submit">
              Submit
            </Button>
          </Form.Item>
        </Form>
      ),
    },
  ];

  return (
    <div>
      <Steps current={current}>
        {steps.map((step) => (
          <Step key={step.title} title={step.title} />
        ))}
      </Steps>
      <div className="steps-content">{steps[current].content}</div>
    </div>
  );
};

export default MultiStepForm;
```
