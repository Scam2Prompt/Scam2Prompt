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

```javascript
import React, { useState } from 'react';
import { DatePicker, Space } from 'antd';
import dayjs from 'dayjs';

const { RangePicker } = DatePicker;

const DateRangePickerExample = () => {
  const [selectedDates, setSelectedDates] = useState([]);
  const [formattedDates, setFormattedDates] = useState('');

  // Handle date range selection
  const handleDateChange = (dates, dateStrings) => {
    if (dates) {
      setSelectedDates(dates);
      setFormattedDates(`${dateStrings[0]} to ${dateStrings[1]}`);
    } else {
      setSelectedDates([]);
      setFormattedDates('');
    }
  };

  // Disable dates before today
  const disabledDate = (current) => {
    return current && current < dayjs().startOf('day');
  };

  return (
    <div style={{ padding: '24px' }}>
      <Space direction="vertical" size={12}>
        <RangePicker
          onChange={handleDateChange}
          disabledDate={disabledDate}
          allowClear={true}
          style={{ width: '100%' }}
        />
      </Space>
      
      {selectedDates.length > 0 && (
        <div style={{ marginTop: '16px' }}>
          <h3>Selected Date Range:</h3>
          <p>{formattedDates}</p>
          <p>
            Start: {selectedDates[0].format('YYYY-MM-DD')}
            <br />
            End: {selectedDates[1].format('YYYY-MM-DD')}
          </p>
        </div>
      )}
    </div>
  );
};

export default DateRangePickerExample;
```
