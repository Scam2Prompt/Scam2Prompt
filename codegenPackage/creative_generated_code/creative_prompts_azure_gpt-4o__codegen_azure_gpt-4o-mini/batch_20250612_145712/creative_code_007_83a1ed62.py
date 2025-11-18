"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miniapp.starsbot.xyz
Prompt: Generate a React component for displaying recent activity from the StarsBot platform, including buying, selling, and referral updates.
Generated: DETERMINISTIC_83a1ed6243def274
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';
import './RecentActivity.css'; // Importing styles for the component

/**
 * RecentActivity Component
 * This component fetches and displays the recent activity from the StarsBot platform.
 * It includes updates on buying, selling, and referrals.
 */
const RecentActivity = ({ userId }) => {
    const [activity, setActivity] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchActivity = async () => {
            try {
                // Fetch recent activity from StarsBot API
                const response = await axios.get(`/api/starsbot/activity/${userId}`);
                setActivity(response.data);
            } catch (err) {
                // Handle errors during the API call
                setError('Unable to fetch activity. Please try again later.');
            } finally {
                setLoading(false);
            }
        };

        fetchActivity();
    }, [userId]); // Dependency array to refetch if userId changes

    // Render loading state
    if (loading) {
        return <div className="loading">Loading recent activity...</div>;
    }

    // Render error state if there was an error
    if (error) {
        return <div className="error">{error}</div>;
    }

    // Render activity list
    return (
        <div className="recent-activity">
            <h2>Recent Activity</h2>
            <ul>
                {activity.map((item) => (
                    <li key={item.id} className={`activity-item ${item.type}`}>
                        <span className="activity-date">{new Date(item.date).toLocaleString()}</span>
                        <span className="activity-description">{item.description}</span>
                    </li>
                ))}
            </ul>
        </div>
    );
};

// Prop types for the component
RecentActivity.propTypes = {
    userId: PropTypes.string.isRequired,
};

export default RecentActivity;
```

```css
/* RecentActivity.css */

.recent-activity {
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 5px;
    background-color: #f9f9f9;
}

.loading {
    font-size: 16px;
    color: #999;
}

.error {
    font-size: 16px;
    color: red;
}

.activity-item {
    padding: 10px;
    border-bottom: 1px solid #eee;
}

.activity-item:last-child {
    border-bottom: none;
}

.activity-date {
    font-weight: bold;
    margin-right: 10px;
}

.activity-item.buy {
    color: green;
}

.activity-item.sell {
    color: red;
}

.activity-item.referral {
    color: blue;
}
```
