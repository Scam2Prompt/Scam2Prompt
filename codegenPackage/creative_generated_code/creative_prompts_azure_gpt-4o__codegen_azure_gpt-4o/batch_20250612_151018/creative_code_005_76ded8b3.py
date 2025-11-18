"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-522--determined-carson-5e0aa9.netlify.app
Prompt: Generate code to integrate Ant Design's DatePicker component into a form and handle date selection events.
Generated: DETERMINISTIC_76ded8b343ff163c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import { Form, DatePicker, Button } from 'antd';
import 'antd/dist/antd.css'; // Ant Design styles

// Main component
const DatePickerForm = () => {
  // State to store the selected date
  const [selectedDate, setSelectedDate] = useState(null);

  // Handler for date selection
  const handleDateChange = (date, dateString) => {
    setSelectedDate(dateString); // Save the dateString (formatted date) in state
    console.log(`Selected date: ${dateString}`); // Log the selected date
  };

  // Handler for form submission
  const handleSubmit = () => {
    if (selectedDate) {
      console.log(`Form submitted with date: ${selectedDate}`);
    } else {
      console.log('No date selected');
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      {/* Ant Design Form */}
      <Form layout="vertical" onFinish={handleSubmit}>
        {/* DatePicker Component */}
        <Form.Item
          label="Select a Date"
          name="date"
          rules={[{ required: true, message: 'Please select a date!' }]}
        >
          <DatePicker onChange={handleDateChange} />
        </Form.Item>

        {/* Submit Button */}
        <Form.Item>
          <Button type="primary" htmlType="submit">
            Submit
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
};

// Export the component
export default DatePickerForm;
```
