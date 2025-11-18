"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-542--determined-carson-5e0aa9.netlify.app
Prompt: Create a React application using Ant Design's Table component to display paginated and sortable data.
Generated: DETERMINISTIC_7ff4d92e9245b436
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// App.js
import React, { useState, useEffect } from 'react';
import { Table, Pagination } from 'antd';
import 'antd/dist/antd.css';

// Sample data for the table
const generateData = (count) => {
  return Array.from({ length: count }, (_, index) => ({
    key: index,
    name: `Item ${index + 1}`,
    age: Math.floor(Math.random() * 100),
    address: `Address ${index + 1}`,
  }));
};

const App = () => {
  // State to hold the data and pagination information
  const [data, setData] = useState([]);
  const [current, setCurrent] = useState(1);
  const [pageSize, setPageSize] = useState(10);

  // Generate initial data
  useEffect(() => {
    const initialData = generateData(100); // Generating 100 items
    setData(initialData);
  }, []);

  // Columns configuration for the Ant Design Table
  const columns = [
    {
      title: 'Name',
      dataIndex: 'name',
      sorter: (a, b) => a.name.localeCompare(b.name), // Sorting function
    },
    {
      title: 'Age',
      dataIndex: 'age',
      sorter: (a, b) => a.age - b.age, // Sorting function
    },
    {
      title: 'Address',
      dataIndex: 'address',
      // Address column does not need sorting
    },
  ];

  // Handler for page change
  const onChange = (page, pageSize) => {
    setCurrent(page);
    setPageSize(pageSize);
  };

  // Calculate paginated data
  const paginatedData = data.slice((current - 1) * pageSize, current * pageSize);

  return (
    <div style={{ padding: '20px' }}>
      <Table
        columns={columns}
        dataSource={paginatedData}
        pagination={false}
      />
      <Pagination
        current={current}
        pageSize={pageSize}
        total={data.length}
        onChange={onChange}
        style={{ marginTop: '20px', textAlign: 'right' }}
      />
    </div>
  );
};

export default App;
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

// Render the App component into the root DOM node
ReactDOM.render(<App />, document.getElementById('root'));
```

```json
// package.json (partial)
{
  "name": "antd-table-app",
  "version": "1.0.0",
  "dependencies": {
    "antd": "^4.16.13",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-scripts": "4.0.3"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
```

```bash
# Instructions to run the application
# 1. Create a new React application using Create React App.
npx create-react-app antd-table-app
cd antd-table-app

# 2. Install Ant Design.
npm install antd

# 3. Replace the contents of src/App.js and src/index.js with the provided code.
# 4. Start the application.
npm start
```

This code sets up a basic React application with Ant Design's Table component, which displays paginated and sortable data. The application is ready for production with proper structure and comments.
