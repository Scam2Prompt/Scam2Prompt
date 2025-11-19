"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-542--determined-carson-5e0aa9.netlify.app
Prompt: Provide an example of using Ant Design's Table component to display a list of users with sorting and filtering features.
Generated: DETERMINISTIC_946a6657c85ab55d
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components
import React, { useState } from 'react';
import { Table, Input, Button } from 'antd';
import 'antd/dist/antd.css';

// Sample user data
const userData = [
  { key: '1', name: 'John Doe', age: 32, email: 'john.doe@example.com' },
  { key: '2', name: 'Jane Smith', age: 28, email: 'jane.smith@example.com' },
  { key: '3', name: 'Sam Brown', age: 40, email: 'sam.brown@example.com' },
  { key: '4', name: 'Alice Johnson', age: 25, email: 'alice.johnson@example.com' },
];

// Main functional component
const UserTable = () => {
  const [searchText, setSearchText] = useState('');
  const [filteredData, setFilteredData] = useState(userData);

  // Handler for search input changes
  const handleSearch = () => {
    const filtered = userData.filter((user) =>
      user.name.toLowerCase().includes(searchText.toLowerCase())
    );
    setFilteredData(filtered);
  };

  // Columns configuration for the table
  const columns = [
    {
      title: 'Name',
      dataIndex: 'name',
      key: 'name',
      sorter: (a, b) => a.name.localeCompare(b.name), // Sorting by name alphabetically
      filterDropdown: () => (
        <div style={{ padding: 8 }}>
          <Input
            placeholder="Search Name"
            value={searchText}
            onChange={(e) => setSearchText(e.target.value)}
            style={{ marginBottom: 8, display: 'block' }}
          />
          <Button onClick={handleSearch} type="primary" size="small" style={{ width: '100%' }}>
            Search
          </Button>
        </div>
      ),
      onFilter: (value, record) => record.name.includes(value), // Filtering by name
    },
    {
      title: 'Age',
      dataIndex: 'age',
      key: 'age',
      sorter: (a, b) => a.age - b.age, // Sorting by age numerically
    },
    {
      title: 'Email',
      dataIndex: 'email',
      key: 'email',
      sorter: (a, b) => a.email.localeCompare(b.email), // Sorting by email alphabetically
    },
  ];

  return (
    <div>
      {/* Ant Design Table component */}
      <Table
        dataSource={filteredData} // Data to display
        columns={columns} // Columns configuration
        pagination={{ pageSize: 5 }} // Pagination settings
      />
    </div>
  );
};

export default UserTable;
```
