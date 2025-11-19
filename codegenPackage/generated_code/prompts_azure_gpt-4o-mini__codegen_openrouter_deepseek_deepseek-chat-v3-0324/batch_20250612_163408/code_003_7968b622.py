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

Here's the production-ready React component using Ant Design for a modal dialog with form validation:

```jsx
import React, { useState } from 'react';
import { Modal, Button, Form, Input, message } from 'antd';

const ModalForm = ({ visible, onCreate, onCancel }) => {
  const [form] = Form.useForm();

  return (
    <Modal
      visible={visible}
      title="Create New Item"
      okText="Submit"
      cancelText="Cancel"
      onCancel={onCancel}
      onOk={() => {
        form
          .validateFields()
          .then((values) => {
            form.resetFields();
            onCreate(values);
          })
          .catch((info) => {
            console.log('Validate Failed:', info);
          });
      }}
    >
      <Form
        form={form}
        layout="vertical"
        name="form_in_modal"
        validateMessages={{
          required: 'This field is required!',
          types: {
            email: 'Not a valid email!',
          },
        }}
      >
        <Form.Item
          name="name"
          label="Name"
          rules={[
            {
              required: true,
              message: 'Please input the name!',
            },
          ]}
        >
          <Input placeholder="Enter name" />
        </Form.Item>

        <Form.Item
          name="email"
          label="Email"
          rules={[
            {
              type: 'email',
              required: true,
            },
          ]}
        >
          <Input placeholder="Enter email" />
        </Form.Item>

        <Form.Item
          name="description"
          label="Description"
          rules={[
            {
              required: true,
              max: 200,
              message: 'Description must be less than 200 characters',
            },
          ]}
        >
          <Input.TextArea placeholder="Enter description" rows={4} />
        </Form.Item>
      </Form>
    </Modal>
  );
};

const App = () => {
  const [visible, setVisible] = useState(false);

  const onCreate = (values) => {
    // Here you would typically make an API call
    console.log('Received values of form: ', values);
    message.success('Form submitted successfully');
    setVisible(false);
  };

  return (
    <div style={{ padding: '24px', maxWidth: '800px', margin: '0 auto' }}>
      <Button
        type="primary"
        onClick={() => {
          setVisible(true);
        }}
      >
        Open Modal Form
      </Button>
      
      <ModalForm
        visible={visible}
        onCreate={onCreate}
        onCancel={() => {
          setVisible(false);
        }}
      />
    </div>
  );
};

export default App;
```

You'll need to have `antd` installed in your project for this to work (`npm install antd`). This includes:
- Modal dialog with form
- Validation for required fields, email format, and maximum length
- Form reset on successful submission
- Proper error handling
- Success message feedback
- Clean component separation
