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
import { Modal, Form, Input, Button, message } from 'antd';

// Main Component
const ModalWithForm = () => {
  const [isModalVisible, setIsModalVisible] = useState(false);
  const [form] = Form.useForm();

  // Function to show the modal
  const showModal = () => {
    setIsModalVisible(true);
  };

  // Function to handle modal close
  const handleCancel = () => {
    setIsModalVisible(false);
    form.resetFields(); // Clear form fields when modal is closed
  };

  // Function to handle form submission
  const handleOk = async () => {
    try {
      // Validate form fields
      const values = await form.validateFields();
      console.log('Form Submitted:', values);
      message.success('Form submitted successfully!');
      setIsModalVisible(false); // Close the modal on successful submission
      form.resetFields(); // Clear form fields
    } catch (error) {
      // Validation error handling
      console.log('Validation Failed:', error);
    }
  };

  return (
    <>
      {/* Button to trigger modal */}
      <Button type="primary" onClick={showModal}>
        Open Modal
      </Button>

      {/* Modal Component */}
      <Modal
        title="Modal Form"
        visible={isModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
        okText="Submit"
        cancelText="Cancel"
      >
        {/* Form inside the Modal */}
        <Form
          form={form}
          layout="vertical"
          name="modalForm"
          initialValues={{
            username: '',
            email: '',
          }}
        >
          {/* Username Field */}
          <Form.Item
            label="Username"
            name="username"
            rules={[
              {
                required: true,
                message: 'Please enter your username!',
              },
            ]}
          >
            <Input placeholder="Enter your username" />
          </Form.Item>

          {/* Email Field */}
          <Form.Item
            label="Email"
            name="email"
            rules={[
              {
                required: true,
                message: 'Please enter your email!',
              },
              {
                type: 'email',
                message: 'Please enter a valid email!',
              },
            ]}
          >
            <Input placeholder="Enter your email" />
          </Form.Item>
        </Form>
      </Modal>
    </>
  );
};

export default ModalWithForm;
```
