"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mommyanew.com
Prompt: Generate JavaScript code for a web-based parental control dashboard that allows single moms to monitor and adjust their children's screen time, referencing the strategies outlined in Mommy Anew's content.
Generated: DETERMINISTIC_883b4e9c5bdab911
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Parental Control Dashboard for Monitoring Screen Time

// Import necessary libraries
import React, { useState, useEffect } from 'react';
import { Chart } from 'react-chartjs-2';
import './App.css'; // Custom styles for the dashboard

// Main App component
function App() {
    // State variables
    const [screenTimeData, setScreenTimeData] = useState([]);
    const [totalScreenTime, setTotalScreenTime] = useState(0);
    const [dailyLimit, setDailyLimit] = useState(120); // Default daily limit in minutes
    const [error, setError] = useState(null);

    // Fetch screen time data from local storage or API
    useEffect(() => {
        try {
            const data = JSON.parse(localStorage.getItem('screenTimeData')) || [];
            setScreenTimeData(data);
            calculateTotalScreenTime(data);
        } catch (err) {
            setError("Failed to fetch screen time data");
            console.error(err);
        }
    }, []);

    // Calculate total screen time
    const calculateTotalScreenTime = (data) => {
        const total = data.reduce((acc, entry) => acc + entry.time, 0);
        setTotalScreenTime(total);
    };

    // Update daily limit
    const updateDailyLimit = (e) => {
        setDailyLimit(e.target.value);
    };

    // Handle screen time log submission
    const logScreenTime = (e) => {
        e.preventDefault();
        const time = parseInt(e.target.elements.time.value, 10);

        if (isNaN(time) || time <= 0) {
            setError("Please enter a valid screen time in minutes.");
            return;
        }

        const newLog = { date: new Date().toLocaleDateString(), time };
        const updatedData = [...screenTimeData, newLog];
        
        // Update local storage
        localStorage.setItem('screenTimeData', JSON.stringify(updatedData));
        setScreenTimeData(updatedData);
        calculateTotalScreenTime(updatedData);
        setError(null);
        e.target.reset();
    };

    // Chart data for visualization
    const chartData = {
        labels: screenTimeData.map(entry => entry.date),
        datasets: [
            {
                label: 'Screen Time (minutes)',
                data: screenTimeData.map(entry => entry.time),
                backgroundColor: 'rgba(75, 192, 192, 0.6)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1,
            },
        ],
    };

    return (
        <div className="dashboard">
            <h1>Parental Control Dashboard</h1>
            {error && <div className="error">{error}</div>}
            <div className="limit-setting">
                <label>
                    Daily Limit (minutes):
                    <input
                        type="number"
                        value={dailyLimit}
                        onChange={updateDailyLimit}
                    />
                </label>
            </div>
            <div className="total-screen-time">
                <h2>Total Screen Time: {totalScreenTime} minutes</h2>
                <h3>{totalScreenTime > dailyLimit ? "Limit Exceeded!" : "Within Limit"}</h3>
            </div>
            <form onSubmit={logScreenTime}>
                <label>
                    Log Screen Time (minutes):
                    <input type="number" name="time" required />
                </label>
                <button type="submit">Log Time</button>
            </form>
            <div className="chart">
                <h2>Screen Time Chart</h2>
                <Chart type="bar" data={chartData} />
            </div>
        </div>
    );
}

// Export App component
export default App;
```

**CSS (App.css):**
```css
.dashboard {
    font-family: Arial, sans-serif;
    margin: 20px;
}

.error {
    color: red;
}

.limit-setting, 
.total-screen-time, 
form {
    margin: 20px 0;
}

label {
    margin-right: 10px;
}

button {
    margin-left: 10px;
}
```

**Note:** Make sure to have the required packages installed, such as `react`, `react-chartjs-2`, and the necessary Chart.js dependencies. The styles can be further customized according to your design requirements.
