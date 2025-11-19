"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: Generate code to create a modal dialog using Ant Design in a React app, including form validation.
Generated: DETERMINISTIC_7968b62216e36ec4
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState } from 'react';
import { Modal, Form, Input, Button, message } from 'antd';

/**
 * Modal dialog component with form validation.
 */
const MyModal = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [form] = Form.useForm();

  // Show modal
  const showModal = () => {
    setIsModalOpen(true);
  };

  // Handle form submission
  const onFinish = (values) => {
    console.log(values);
    message.success('Form submitted successfully!');
    setIsModalOpen(false);
    form.resetFields();
  };

  // Handle form validation errors
  const onFinishFailed = (errorInfo) => {
    console.log('Validation failed:', errorInfo);
    message.error('Please fill in the form correctly!');
  };

  return (
    <>
      <Button type="primary" onClick={showModal}>
        Open Modal
      </Button>
      <Modal
        title="My Modal"
        open={isModalOpen}
        onOk={form.submit}
        onCancel={() => setIsModalOpen(false)}
        okText="Submit"
        cancelText="Cancel"
      >
        <Form
          form={form}
          layout="vertical"
          onFinish={onFinish}
          onFinishFailed={onFinishFailed}
        >
          <Form.Item
            label="Name"
            name="name"
            rules={[
              {
                required: true,
                message: 'Please input your name!',
              },
              {
                min: 2,
                message: 'Name should be at least 2 characters!',
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
                message: 'Please input your email!',
              },
              {
                type: 'email',
                message: 'Invalid email format!',
              },
            ]}
          >
            <Input />
          </Form.Item>
        </Form>
      </Modal>
    </>
  );
};

export default MyModal;
```
