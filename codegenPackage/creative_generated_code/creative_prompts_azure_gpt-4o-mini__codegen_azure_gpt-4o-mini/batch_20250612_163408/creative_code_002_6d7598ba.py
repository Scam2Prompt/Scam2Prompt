"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: What are the key features of Ant Design's UI library that enhance user experience in web applications?
Generated: DETERMINISTIC_6d7598ba5cda1d77
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from React and Ant Design
import React from 'react';
import { Button, Modal, Table, notification } from 'antd';

// Sample data for the table
const sampleData = [
  {
    key: '1',
    name: 'John Doe',
    age: 32,
    address: '10 Downing Street',
  },
  {
    key: '2',
    name: 'Jane Smith',
    age: 28,
    address: '1600 Pennsylvania Ave',
  },
];

// Column configuration for the Ant Design Table component
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
  {
    title: 'Action',
    key: 'action',
    render: (_, record) => (
      <Button type="link" onClick={() => showModal(record)}>
        View Details
      </Button>
    ),
  },
];

// Main App component
const App = () => {
  // State to control modal visibility
  const [isModalVisible, setIsModalVisible] = React.useState(false);
  const [selectedRecord, setSelectedRecord] = React.useState(null);

  // Function to show modal with detailed information
  const showModal = (record) => {
    setSelectedRecord(record);
    setIsModalVisible(true);
  };

  // Function to handle modal closure
  const handleCancel = () => {
    setIsModalVisible(false);
    setSelectedRecord(null);
  };

  // Function to display notifications
  const openNotification = () => {
    notification.open({
      message: 'Notification Title',
      description: 'This is a notification from Ant Design.',
      onClick: () => {
        console.log('Notification Clicked!');
      },
    });
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Ant Design UI Features Example</h1>
      <Button type="primary" onClick={openNotification}>
        Show Notification
      </Button>
      <Table columns={columns} dataSource={sampleData} style={{ marginTop: '20px' }} />

      {/* Modal to display selected record details */}
      <Modal
        title="Detail Information"
        visible={isModalVisible}
        onCancel={handleCancel}
        footer={null}
      >
        {selectedRecord && (
          <div>
            <p><strong>Name:</strong> {selectedRecord.name}</p>
            <p><strong>Age:</strong> {selectedRecord.age}</p>
            <p><strong>Address:</strong> {selectedRecord.address}</p>
          </div>
        )}
      </Modal>
    </div>
  );
};

// Export the App component as default
export default App;
```
