"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: Generate code to create a modal dialog using Ant Design in a React app, including form validation.
Generated: DETERMINISTIC_7968b62216e36ec4
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';
import { Modal, Button, Form, Input } from 'antd';

// Custom hook for form validation
const useFormValidation = () => {
  const [form] = Form.useForm();
  const [formError, setFormError] = useState(null);

  const validateForm = async () => {
    try {
      await form.validateFields();
      setFormError(null);
      return true;
    } catch (error) {
      setFormError(error);
      return false;
    }
  };

  return { form, formError, validateForm };
};

// Main component for the modal dialog
const ModalForm = () => {
  const [visible, setVisible] = useState(false);
  const { form, formError, validateForm } = useFormValidation();

  // Show modal dialog
  const showModal = () => setVisible(true);

  // Handle OK button click
  const handleOk = async () => {
    const isValid = await validateForm();
    if (isValid) {
      // Perform submit action here
      console.log('Form submitted successfully');
      setVisible(false);
    }
  };

  // Handle cancel button click
  const handleCancel = () => {
    setVisible(false);
  };

  return (
    <>
      <Button type="primary" onClick={showModal}>
        Open Modal
      </Button>
      <Modal
        title="Modal Form"
        visible={visible}
        onOk={handleOk}
        onCancel={handleCancel}
        okText="Submit"
        cancelText="Cancel"
      >
        <Form form={form} layout="vertical">
          <Form.Item
            name="username"
            label="Username"
            rules={[
              { required: true, message: 'Please input your username!' },
              { min: 3, message: 'Username must be at least 3 characters.' },
            ]}
          >
            <Input placeholder="Enter your username" />
          </Form.Item>
          <Form.Item
            name="email"
            label="Email"
            rules={[
              { required: true, message: 'Please input your email!' },
              { type: 'email', message: 'Please enter a valid email!' },
            ]}
          >
            <Input placeholder="Enter your email" />
          </Form.Item>
          {formError && <div style={{ color: 'red' }}>{formError.message}</div>}
        </Form>
      </Modal>
    </>
  );
};

export default ModalForm;
```
