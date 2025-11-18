"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-542--determined-carson-5e0aa9.netlify.app
Prompt: Generate code to implement a multi-step form using Ant Design's Steps and Form components.
Generated: DETERMINISTIC_c63c1e59a9f4a189
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// MultiStepForm.jsx
import React, { useState } from 'react';
import { Steps, Form, Input, Button, message } from 'antd';

const { Step } = Steps;

const MultiStepForm = () => {
  // State management for current step
  const [currentStep, setCurrentStep] = useState(0);

  // Form state to hold data across steps
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
  });

  const steps = [
    {
      title: 'Step 1',
      content: (
        <Form
          layout="vertical"
          initialValues={{ name: formData.name }}
          onFinish={(values) => handleNext(values)}
        >
          <Form.Item
            label="Name"
            name="name"
            rules={[{ required: true, message: 'Please enter your name' }]}
          >
            <Input placeholder="Enter your name" />
          </Form.Item>
          <Button type="primary" htmlType="submit">
            Next
          </Button>
        </Form>
      ),
    },
    {
      title: 'Step 2',
      content: (
        <Form
          layout="vertical"
          initialValues={{ email: formData.email }}
          onFinish={(values) => handleNext(values)}
        >
          <Form.Item
            label="Email"
            name="email"
            rules={[
              { required: true, message: 'Please enter your email' },
              { type: 'email', message: 'Please enter a valid email address' },
            ]}
          >
            <Input placeholder="Enter your email" />
          </Form.Item>
          <Button
            onClick={handlePrevious}
            style={{ marginRight: '10px' }}
          >
            Previous
          </Button>
          <Button type="primary" htmlType="submit">
            Next
          </Button>
        </Form>
      ),
    },
    {
      title: 'Step 3',
      content: (
        <Form
          layout="vertical"
          initialValues={{ password: formData.password }}
          onFinish={(values) => handleSubmit(values)}
        >
          <Form.Item
            label="Password"
            name="password"
            rules={[{ required: true, message: 'Please enter your password' }]}
          >
            <Input.Password placeholder="Enter your password" />
          </Form.Item>
          <Button
            onClick={handlePrevious}
            style={{ marginRight: '10px' }}
          >
            Previous
          </Button>
          <Button type="primary" htmlType="submit">
            Submit
          </Button>
        </Form>
      ),
    },
  ];

  // Handles moving to the next step
  const handleNext = (values) => {
    setFormData({ ...formData, ...values });
    setCurrentStep((prevStep) => prevStep + 1);
  };

  // Handles moving to the previous step
  const handlePrevious = () => {
    setCurrentStep((prevStep) => prevStep - 1);
  };

  // Handles final form submission
  const handleSubmit = (values) => {
    setFormData({ ...formData, ...values });
    message.success('Form submitted successfully!');
    console.log('Final Form Data:', { ...formData, ...values });
  };

  return (
    <div style={{ maxWidth: '600px', margin: '0 auto' }}>
      <Steps current={currentStep} style={{ marginBottom: '30px' }}>
        {steps.map((step, index) => (
          <Step key={index} title={step.title} />
        ))}
      </Steps>
      <div>{steps[currentStep].content}</div>
    </div>
  );
};

export default MultiStepForm;
```
