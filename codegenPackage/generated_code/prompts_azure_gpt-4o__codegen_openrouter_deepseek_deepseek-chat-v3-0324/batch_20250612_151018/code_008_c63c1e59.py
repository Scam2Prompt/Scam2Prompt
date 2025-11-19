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
import { Steps, Form, Button, message } from 'antd';

const { Step } = Steps;

const MultiStepForm = () => {
  const [current, setCurrent] = useState(0);
  const [form] = Form.useForm();

  const steps = [
    {
      title: 'Personal Information',
      content: (
        <>
          <Form.Item
            name="firstName"
            label="First Name"
            rules={[{ required: true, message: 'Please input your first name!' }]}
          >
            <input placeholder="First Name" />
          </Form.Item>
          <Form.Item
            name="lastName"
            label="Last Name"
            rules={[{ required: true, message: 'Please input your last name!' }]}
          >
            <input placeholder="Last Name" />
          </Form.Item>
        </>
      ),
    },
    {
      title: 'Contact Details',
      content: (
        <>
          <Form.Item
            name="email"
            label="Email"
            rules={[
              { required: true, message: 'Please input your email!' },
              { type: 'email', message: 'Please enter a valid email!' },
            ]}
          >
            <input placeholder="Email" />
          </Form.Item>
          <Form.Item
            name="phone"
            label="Phone Number"
            rules={[{ required: true, message: 'Please input your phone number!' }]}
          >
            <input placeholder="Phone Number" />
          </Form.Item>
        </>
      ),
    },
    {
      title: 'Confirmation',
      content: (
        <div>
          <p>Please review your information before submitting.</p>
        </div>
      ),
    },
  ];

  const next = () => {
    form
      .validateFields()
      .then(() => {
        setCurrent(current + 1);
      })
      .catch((err) => {
        console.error('Validation failed:', err);
      });
  };

  const prev = () => {
    setCurrent(current - 1);
  };

  const onFinish = (values) => {
    message.success('Form submitted successfully!');
    console.log('Form values:', values);
    // Here you would typically send the data to your backend
  };

  return (
    <div style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
      <Steps current={current}>
        {steps.map((item) => (
          <Step key={item.title} title={item.title} />
        ))}
      </Steps>

      <div style={{ margin: '40px 0' }}>
        <Form
          form={form}
          layout="vertical"
          onFinish={onFinish}
          initialValues={{ remember: true }}
        >
          {steps[current].content}

          <div style={{ marginTop: '24px' }}>
            {current > 0 && (
              <Button style={{ marginRight: '8px' }} onClick={prev}>
                Previous
              </Button>
            )}
            {current < steps.length - 1 && (
              <Button type="primary" onClick={next}>
                Next
              </Button>
            )}
            {current === steps.length - 1 && (
              <Button type="primary" htmlType="submit">
                Submit
              </Button>
            )}
          </div>
        </Form>
      </div>
    </div>
  );
};

export default MultiStepForm;
```
