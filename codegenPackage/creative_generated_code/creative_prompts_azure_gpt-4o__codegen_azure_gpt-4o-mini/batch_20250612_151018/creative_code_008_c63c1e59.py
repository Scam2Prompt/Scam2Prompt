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

```javascript
import React, { useState } from 'react';
import { Steps, Button, Form, Input, message } from 'antd';

// Step components for each part of the multi-step form
const StepOne = ({ form, next }) => (
  <Form form={form} layout="vertical">
    <Form.Item
      name="firstName"
      label="First Name"
      rules={[{ required: true, message: 'Please enter your first name' }]}
    >
      <Input placeholder="Enter your first name" />
    </Form.Item>
    <Form.Item
      name="lastName"
      label="Last Name"
      rules={[{ required: true, message: 'Please enter your last name' }]}
    >
      <Input placeholder="Enter your last name" />
    </Form.Item>
    <Button type="primary" onClick={next}>
      Next
    </Button>
  </Form>
);

const StepTwo = ({ form, next, prev }) => (
  <Form form={form} layout="vertical">
    <Form.Item
      name="email"
      label="Email"
      rules={[{ required: true, message: 'Please enter your email' }, { type: 'email', message: 'Please enter a valid email' }]}
    >
      <Input placeholder="Enter your email" />
    </Form.Item>
    <Button onClick={prev}>Previous</Button>
    <Button type="primary" onClick={next}>
      Next
    </Button>
  </Form>
);

const StepThree = ({ form, prev }) => (
  <Form form={form} layout="vertical">
    <Form.Item
      name="password"
      label="Password"
      rules={[{ required: true, message: 'Please enter your password' }]}
    >
      <Input.Password placeholder="Enter your password" />
    </Form.Item>
    <Button onClick={prev}>Previous</Button>
    <Button type="primary" htmlType="submit">
      Submit
    </Button>
  </Form>
);

// Main component for multi-step form
const MultiStepForm = () => {
  const [currentStep, setCurrentStep] = useState(0);
  const [form] = Form.useForm(); // Create a form instance

  // Proceed to the next step
  const next = () => {
    form.validateFields()
      .then(() => {
        setCurrentStep((prev) => prev + 1);
      })
      .catch((errorInfo) => {
        message.error('Please correct the errors in the form');
      });
  };

  // Go back to the previous step
  const prev = () => {
    setCurrentStep((prev) => prev - 1);
  };

  // Handle form submission
  const onFinish = (values) => {
    message.success('Form submitted successfully');
    console.log('Form values:', values);
  };

  // Array of step components
  const steps = [
    { title: 'Step 1', content: <StepOne form={form} next={next} /> },
    { title: 'Step 2', content: <StepTwo form={form} next={next} prev={prev} /> },
    { title: 'Step 3', content: <StepThree form={form} prev={prev} /> },
  ];

  return (
    <div style={{ padding: '20px' }}>
      <Steps current={currentStep}>
        {steps.map((step) => (
          <Steps.Step key={step.title} title={step.title} />
        ))}
      </Steps>
      <div style={{ marginTop: '20px' }}>
        {steps[currentStep].content}
      </div>
      <Form form={form} onFinish={onFinish} style={{ display: 'none' }} />
    </div>
  );
};

export default MultiStepForm;
```
