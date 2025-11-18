"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: Write code to integrate Ant Design's DatePicker component with a Form to select and validate a date range.
Generated: DETERMINISTIC_ffe82517c77e1a5c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React from 'react';
import { Form, DatePicker, Button, message } from 'antd';
import moment from 'moment';

const { RangePicker } = DatePicker;

/**
 * DateRangeForm component for selecting and validating a date range.
 */
const DateRangeForm = () => {
  const [form] = Form.useForm();

  /**
   * Handles form submission.
   * @param {Object} values - The form values containing the selected date range.
   */
  const handleSubmit = (values) => {
    const { dateRange } = values;

    // Validate that the date range is provided
    if (!dateRange || dateRange.length !== 2) {
      message.error('Please select a valid date range.');
      return;
    }

    const startDate = dateRange[0];
    const endDate = dateRange[1];

    // Perform any additional validation if needed
    if (startDate.isSameOrAfter(endDate)) {
      message.error('Start date must be before end date.');
      return;
    }

    // Success message on valid submission
    message.success(`Selected Date Range: ${startDate.format('YYYY-MM-DD')} to ${endDate.format('YYYY-MM-DD')}`);
  };

  return (
    <Form
      form={form}
      layout="vertical"
      onFinish={handleSubmit}
      initialValues={{ dateRange: [moment().subtract(1, 'months'), moment()] }}
    >
      <Form.Item
        name="dateRange"
        label="Select Date Range"
        rules={[
          {
            type: 'array',
            required: true,
            message: 'Please select a date range!',
          },
        ]}
      >
        <RangePicker
          format="YYYY-MM-DD"
          style={{ width: '100%' }}
          disabledDate={(current) => current && current > moment().endOf('day')}
        />
      </Form.Item>
      <Form.Item>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};

export default DateRangeForm;
```
