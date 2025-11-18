"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-528--determined-carson-5e0aa9.netlify.app
Prompt: Write code to integrate Ant Design's DatePicker component into a React form with custom styling.
Generated: DETERMINISTIC_62d3a36390a6de6d
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';
import { DatePicker, Form, Button } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design styles
import './CustomDatePicker.css'; // Import custom styles

const { RangePicker } = DatePicker; // Destructure RangePicker from DatePicker

const CustomDatePickerForm = () => {
  const [dates, setDates] = useState(null); // State to hold selected dates
  const [error, setError] = useState(''); // State to hold error messages

  // Handler for date change
  const handleDateChange = (date, dateString) => {
    setDates(dateString);
    setError(''); // Reset error on valid selection
  };

  // Submit handler for the form
  const handleSubmit = (e) => {
    e.preventDefault();
    if (!dates) {
      setError('Please select a date range.'); // Set error if no dates are selected
      return;
    }
    // Handle form submission logic here
    console.log('Selected dates: ', dates);
  };

  return (
    <Form onSubmit={handleSubmit} className="date-picker-form">
      <Form.Item>
        <label htmlFor="date-picker">Select Date Range:</label>
        <RangePicker
          id="date-picker"
          onChange={handleDateChange} // Attach the date change handler
          className="custom-date-picker" // Apply custom styles
        />
        {error && <div className="error-message">{error}</div>} {/* Display error messages */}
      </Form.Item>
      <Form.Item>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};

export default CustomDatePickerForm;
```

```css
/* CustomDatePicker.css */
.date-picker-form {
  max-width: 400px;
  margin: 0 auto;
}

.custom-date-picker {
  width: 100%;
  border-radius: 5px; /* Rounded corners */
  border: 1px solid #d9d9d9; /* Border color */
}

.custom-date-picker:hover {
  border-color: #40a9ff; /* Border color on hover */
}

.error-message {
  color: red; /* Error text color */
  font-size: 12px; /* Error text size */
  margin-top: 8px; /* Margin for spacing */
}
```

Make sure to run `npm install antd` to install Ant Design before using the component.
