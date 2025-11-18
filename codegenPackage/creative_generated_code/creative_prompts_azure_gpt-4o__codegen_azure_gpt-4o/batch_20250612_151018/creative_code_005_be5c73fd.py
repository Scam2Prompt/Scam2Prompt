"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-549--determined-carson-5e0aa9.netlify.app
Prompt: Provide an example of using Ant Design's DatePicker component to select a date range and display the selected dates.
Generated: DETERMINISTIC_be5c73fd14f67093
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// File: DateRangePicker.js
// Description: A simple example of using Ant Design's DatePicker component to select a date range and display the selected dates.

import React, { useState } from 'react';
import { DatePicker, Typography, Space } from 'antd';
import 'antd/dist/antd.css';

// Destructure RangePicker from DatePicker
const { RangePicker } = DatePicker;
const { Text } = Typography;

const DateRangePicker = () => {
  // State to hold the selected date range
  const [selectedDates, setSelectedDates] = useState([]);

  /**
   * Handles the change in the date range picker.
   * @param {moment[]} dates - The array of selected start and end dates.
   * @param {string[]} dateStrings - The array of formatted date strings.
   */
  const handleDateChange = (dates, dateStrings) => {
    setSelectedDates(dateStrings); // Store formatted strings (e.g., "YYYY-MM-DD")
  };

  return (
    <Space direction="vertical" size="large">
      {/* Date range picker */}
      <RangePicker onChange={handleDateChange} />

      {/* Display the selected dates */}
      <Text>
        Selected Dates:{" "}
        {selectedDates.length > 0
          ? `${selectedDates[0]} to ${selectedDates[1]}`
          : "None"}
      </Text>
    </Space>
  );
};

export default DateRangePicker;
```
