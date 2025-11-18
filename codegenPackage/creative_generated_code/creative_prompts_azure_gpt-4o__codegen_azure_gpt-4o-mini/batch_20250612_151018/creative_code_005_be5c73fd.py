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

```javascript
import React, { useState } from 'react';
import { DatePicker, message } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design styles

const { RangePicker } = DatePicker;

/**
 * DateRangePickerComponent allows users to select a date range using Ant Design's RangePicker.
 * It displays the selected start and end dates below the date picker.
 */
const DateRangePickerComponent = () => {
    // State to hold the selected date range
    const [dates, setDates] = useState([]);

    /**
     * Handles the date change event from the RangePicker.
     * @param {moment.Moment[]} selectedDates - Array containing the start and end date or nulls
     */
    const onChange = (selectedDates) => {
        if (selectedDates) {
            setDates(selectedDates);
            message.success(`Selected dates: ${selectedDates[0].format('YYYY-MM-DD')} to ${selectedDates[1].format('YYYY-MM-DD')}`);
        } else {
            setDates([]);
            message.warning('Date range cleared.');
        }
    };

    return (
        <div style={{ padding: '20px' }}>
            <h2>Select a Date Range</h2>
            <RangePicker onChange={onChange} />
            {dates.length > 0 && (
                <div style={{ marginTop: '20px' }}>
                    <h3>Selected Date Range:</h3>
                    <p>Start Date: {dates[0].format('YYYY-MM-DD')}</p>
                    <p>End Date: {dates[1].format('YYYY-MM-DD')}</p>
                </div>
            )}
        </div>
    );
};

export default DateRangePickerComponent;
```

To use this component, ensure you have `antd` and `moment` installed in your project:

```bash
npm install antd moment
```

Then, you can import and use `DateRangePickerComponent` in your main application file.
