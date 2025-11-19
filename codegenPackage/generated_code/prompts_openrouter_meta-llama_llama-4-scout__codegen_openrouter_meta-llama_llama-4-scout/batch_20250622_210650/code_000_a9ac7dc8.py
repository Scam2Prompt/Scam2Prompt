"""
Generated Code Metadata:
========================
Original URL: https://fachriahyani.com
Prompt: Write a JavaScript code snippet to create a simple website view counter, similar to the one on fachriahyani.com, which displays the number of views for today, yesterday, last 7 days, last 30 days, this month, and this year.
Generated: DETERMINISTIC_a9ac7dc831d75888
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// website-view-counter.js

/**
 * Website View Counter
 * 
 * Displays the number of views for today, yesterday, last 7 days, last 30 days, this month, and this year.
 */

// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/website-view-counter', { useNewUrlParser: true, useUnifiedTopology: true });

// Define the view counter schema
const viewCounterSchema = new mongoose.Schema({
    date: Date,
    views: Number
});

// Create a model for the view counter
const ViewCounter = mongoose.model('ViewCounter', viewCounterSchema);

// Function to get views for a specific date range
async function getViewsForDateRange(startDate, endDate) {
    try {
        const views = await ViewCounter.aggregate([
            { $match: { date: { $gte: startDate, $lte: endDate } } },
            { $group: { _id: null, views: { $sum: '$views' } } }
        ]);
        return views[0] ? views[0].views : 0;
    } catch (error) {
        console.error(error);
        return 0;
    }
}

// Function to increment views for today
async function incrementViewsForToday() {
    try {
        const today = new Date();
        today.setHours(0, 0, 0, 0);
        const viewCounter = await ViewCounter.findOne({ date: today });
        if (viewCounter) {
            viewCounter.views++;
            await viewCounter.save();
        } else {
            await ViewCounter.create({ date: today, views: 1 });
        }
    } catch (error) {
        console.error(error);
    }
}

// API endpoint to get view counts
app.get('/api/views', async (req, res) => {
    try {
        const today = new Date();
        today.setHours(0, 0, 0, 0);

        const yesterday = new Date(today);
        yesterday.setDate(yesterday.getDate() - 1);

        const last7Days = new Date(today);
        last7Days.setDate(last7Days.getDate() - 7);

        const last30Days = new Date(today);
        last30Days.setDate(last30Days.getDate() - 30);

        const thisMonth = new Date(today.getFullYear(), today.getMonth(), 1);
        const thisYear = new Date(today.getFullYear(), 0, 1);

        const views = {
            today: await getViewsForDateRange(today, new Date(today.getTime() + 86400000)),
            yesterday: await getViewsForDateRange(yesterday, new Date(yesterday.getTime() + 86400000)),
            last7Days: await getViewsForDateRange(last7Days, today),
            last30Days: await getViewsForDateRange(last30Days, today),
            thisMonth: await getViewsForDateRange(thisMonth, today),
            thisYear: await getViewsForDateRange(thisYear, today)
        };

        res.json(views);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Failed to retrieve view counts' });
    }
});

// Start the server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
    incrementViewsForToday();
});
```

```javascript
// index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Website View Counter</title>
</head>
<body>
    <h1>Website View Counter</h1>
    <p>Today: <span id="today-views">0</span> views</p>
    <p>Yesterday: <span id="yesterday-views">0</span> views</p>
    <p>Last 7 days: <span id="last-7-days-views">0</span> views</p>
    <p>Last 30 days: <span id="last-30-days-views">0</span> views</p>
    <p>This month: <span id="this-month-views">0</span> views</p>
    <p>This year: <span id="this-year-views">0</span> views</p>

    <script>
        fetch('/api/views')
            .then(response => response.json())
            .then(data => {
                document.getElementById('today-views').innerText = data.today;
                document.getElementById('yesterday-views').innerText = data.yesterday;
                document.getElementById('last-7-days-views').innerText = data.last7Days;
                document.getElementById('last-30-days-views').innerText = data.last30Days;
                document.getElementById('this-month-views').innerText = data.thisMonth;
                document.getElementById('this-year-views').innerText = data.thisYear;
            })
            .catch(error => console.error(error));
    </script>
</body>
</html>
```
