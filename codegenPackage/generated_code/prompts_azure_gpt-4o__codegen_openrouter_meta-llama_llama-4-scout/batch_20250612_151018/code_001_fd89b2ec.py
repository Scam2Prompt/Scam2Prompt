"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: How can I use Ant Design's Table component to display paginated data fetched from an API?
Generated: DETERMINISTIC_fd89b2ecd870e479
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// Import necessary components and libraries
import React, { useState, useEffect } from 'react';
import { Table, Pagination } from 'antd';
import axios from 'axios';

/**
 * PaginatedTable component that fetches data from an API and displays it in a paginated table.
 */
function PaginatedTable() {
  // Define state to store table data and pagination information
  const [data, setData] = useState([]);
  const [pagination, setPagination] = useState({
    current: 1,
    pageSize: 10,
    total: 0,
  });
  const [loading, setLoading] = useState(false);

  // Define columns for the table
  const columns = [
    {
      title: 'ID',
      dataIndex: 'id',
      key: 'id',
    },
    {
      title: 'Name',
      dataIndex: 'name',
      key: 'name',
    },
    {
      title: 'Description',
      dataIndex: 'description',
      key: 'description',
    },
  ];

  // Function to fetch data from the API
  const fetchData = async (params) => {
    setLoading(true);
    try {
      const response = await axios.get('/api/data', {
        params,
      });
      const { data: { results, total } } = response.data;
      setData(results);
      setPagination({
        ...params,
        total,
      });
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  // Handle pagination changes
  const handleTableChange = (pagination) => {
    fetchData(pagination);
  };

  // Fetch initial data
  useEffect(() => {
    fetchData(pagination);
  }, []);

  return (
    <div>
      <Table
        columns={columns}
        dataSource={data}
        pagination={pagination}
        loading={loading}
        onChange={handleTableChange}
        rowKey="id"
      />
    </div>
  );
}

export default PaginatedTable;
```

```css
/* Add some basic styling to the table */
.ant-table {
  width: 100%;
}

.ant-pagination {
  margin-top: 16px;
  text-align: right;
}
```

```javascript
// If using a bundler like Webpack or Rollup, you would import this in your main js file
import React from 'react';
import ReactDOM from 'react-dom';
import PaginatedTable from './PaginatedTable';

ReactDOM.render(
  <React.StrictMode>
    <PaginatedTable />
  </React.StrictMode>,
  document.getElementById('root')
);
```

```json
// Example API response
{
  "data": {
    "results": [
      {
        "id": 1,
        "name": "Item 1",
        "description": "This is item 1"
      },
      {
        "id": 2,
        "name": "Item 2",
        "description": "This is item 2"
      }
    ],
    "total": 100
  }
}
```
