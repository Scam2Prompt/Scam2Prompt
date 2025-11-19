"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: What are the key components of the Ant Design library for building modern web applications?
Generated: DETERMINISTIC_1c317c0bef81333c
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing React and the necessary components from Ant Design
import React from 'react';
import { Layout, Menu, Button, Form, Input, Table, Modal, notification } from 'antd';

// Import Ant Design styles
import 'antd/dist/antd.css';

// Key Components Demonstration
const App = () => {
  // State management for the Modal visibility
  const [isModalVisible, setIsModalVisible] = React.useState(false);

  // Sample data for the Table component
  const sampleData = [
    {
      key: '1',
      name: 'John Doe',
      age: 32,
      address: '123 Main Street',
    },
    {
      key: '2',
      name: 'Jane Smith',
      age: 28,
      address: '456 Elm Street',
    },
  ];

  // Column definitions for the Table component
  const columns = [
    {
      title: 'Name',
      dataIndex: 'name',
      key: 'name',
    },
    {
      title: 'Age',
      dataIndex: 'age',
      key: 'age',
    },
    {
      title: 'Address',
      dataIndex: 'address',
      key: 'address',
    },
  ];

  // Function to handle form submission
  const handleFormSubmit = (values) => {
    notification.success({
      message: 'Form Submitted',
      description: `Hello, ${values.username}. Your form has been successfully submitted.`,
    });
  };

  // Function to handle Modal visibility
  const showModal = () => {
    setIsModalVisible(true);
  };

  const handleModalOk = () => {
    setIsModalVisible(false);
  };

  const handleModalCancel = () => {
    setIsModalVisible(false);
  };

  return (
    <Layout>
      {/* Header Section */}
      <Layout.Header>
        <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['1']}>
          <Menu.Item key="1">Home</Menu.Item>
          <Menu.Item key="2">About</Menu.Item>
          <Menu.Item key="3">Contact</Menu.Item>
        </Menu>
      </Layout.Header>

      {/* Content Section */}
      <Layout.Content style={{ padding: '20px' }}>
        <h1>Welcome to the Ant Design Demo</h1>

        {/* Form Component */}
        <Form
          layout="vertical"
          style={{ maxWidth: '300px', marginBottom: '20px' }}
          onFinish={handleFormSubmit}
        >
          <Form.Item
            label="Username"
            name="username"
            rules={[{ required: true, message: 'Please input your username!' }]}
          >
            <Input placeholder="Enter your username" />
          </Form.Item>
          <Form.Item
            label="Password"
            name="password"
            rules={[{ required: true, message: 'Please input your password!' }]}
          >
            <Input.Password placeholder="Enter your password" />
          </Form.Item>
          <Button type="primary" htmlType="submit">
            Submit
          </Button>
        </Form>

        {/* Table Component */}
        <Table dataSource={sampleData} columns={columns} />

        {/* Button to trigger Modal */}
        <Button type="primary" onClick={showModal} style={{ marginTop: '20px' }}>
          Show Modal
        </Button>

        {/* Modal Component */}
        <Modal
          title="Sample Modal"
          visible={isModalVisible}
          onOk={handleModalOk}
          onCancel={handleModalCancel}
        >
          <p>This is a sample modal content.</p>
        </Modal>
      </Layout.Content>

      {/* Footer Section */}
      <Layout.Footer style={{ textAlign: 'center' }}>
        Ant Design Demo ©2023 Created by Developer
      </Layout.Footer>
    </Layout>
  );
};

// Exporting the App component as the default export
export default App;
```

This code snippet creates a React application that showcases key components from the Ant Design library, such as `Layout`, `Menu`, `Form`, `Input`, `Table`, `Button`, `Modal`, and `notification`. It provides a clean and reusable example for building modern web applications.
