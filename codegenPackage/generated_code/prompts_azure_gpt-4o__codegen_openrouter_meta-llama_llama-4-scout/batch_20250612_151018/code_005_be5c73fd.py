"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-549--determined-carson-5e0aa9.netlify.app
Prompt: Provide an example of using Ant Design's DatePicker component to select a date range and display the selected dates.
Generated: DETERMINISTIC_be5c73fd14f67093
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState } from 'react';
import { DatePicker, Button } from 'antd';

/**
 * Date range picker example component.
 * 
 * @returns {JSX.Element} The date range picker component.
 */
const DateRangePicker = () => {
  // Initialize state to store the selected date range
  const [dateRange, setDateRange] = useState([null, null]);

  // Handle date range change
  const onChange = (dates) => {
    setDateRange(dates);
  };

  // Format date for display
  const formatDate = (date) => {
    if (!date) return '';
    return date.format('YYYY-MM-DD');
  };

  return (
    <div>
      <DatePicker.RangePicker
        // Bind date range change event
        onChange={onChange}
        // Use state to store selected dates
        value={dateRange}
        // Display date format
        format="YYYY-MM-DD"
      />
      <Button type="primary" style={{ margin: '0 8px' }}>
        Submit
      </Button>
      <span>
        Selected date range: {formatDate(dateRange[0])} - {formatDate(dateRange[1])}
      </span>
    </div>
  );
};

export default DateRangePicker;
```

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import DateRangePicker from './DateRangePicker';
import 'antd/dist/antd.css'; // Import Ant Design CSS

const App = () => {
  return (
    <div style={{ padding: '20px' }}>
      <DateRangePicker />
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));
```
