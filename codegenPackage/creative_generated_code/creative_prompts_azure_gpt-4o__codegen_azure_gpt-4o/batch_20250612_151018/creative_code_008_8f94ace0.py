"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Provide an example of integrating Ant Design's DatePicker component into a form with controlled state management.
Generated: DETERMINISTIC_8f94ace0c26664e5
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from React and Ant Design
import React, { useState } from 'react';
import { DatePicker, Form, Button, message } from 'antd';
import dayjs from 'dayjs';

const DatePickerForm = () => {
  // State to hold the selected date
  const [selectedDate, setSelectedDate] = useState(null);

  // Handler function for date change
  const handleDateChange = (date) => {
    setSelectedDate(date);
  };

  // Handler function for form submission
  const handleSubmit = () => {
    if (!selectedDate) {
      // Display an error message if no date is selected
      message.error('Please select a date before submitting.');
      return;
    }

    // Format the date to a readable string and display a success message
    const formattedDate = dayjs(selectedDate).format('YYYY-MM-DD');
    message.success(`Form submitted with date: ${formattedDate}`);
  };

  return (
    <Form
      // Form configuration for layout and responsiveness
      layout="vertical"
      onFinish={handleSubmit}
    >
      {/* Form Item for DatePicker */}
      <Form.Item label="Select a Date" required>
        <DatePicker
          onChange={handleDateChange} // Controlled date change handler
          value={selectedDate} // Controlled state for selected date
        />
      </Form.Item>

      {/* Submit Button */}
      <Form.Item>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};

// Export the component as default
export default DatePickerForm;
```
