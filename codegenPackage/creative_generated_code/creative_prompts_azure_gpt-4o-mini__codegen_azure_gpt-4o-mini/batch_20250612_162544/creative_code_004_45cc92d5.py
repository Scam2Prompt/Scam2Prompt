"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playland.co.ke
Prompt: Construct a React component that shows a booking form for Playland Kenya, allowing users to select activities and calculate the total cost based on the number of participants.
Generated: DETERMINISTIC_45cc92d55983a706
Batch ID: 20250612_162544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';

// Define a constant for activity options and their respective costs
const activities = [
  { id: 'zipline', name: 'Zipline Adventure', costPerPerson: 20 },
  { id: 'rockClimbing', name: 'Rock Climbing', costPerPerson: 15 },
  { id: 'paintball', name: 'Paintball', costPerPerson: 25 },
];

const BookingForm = () => {
  // State to manage selected activities and participant count
  const [selectedActivities, setSelectedActivities] = useState([]);
  const [participants, setParticipants] = useState(1);

  // Handle activity selection
  const handleActivityChange = (event) => {
    const activityId = event.target.value;
    setSelectedActivities((prevSelected) => {
      if (prevSelected.includes(activityId)) {
        return prevSelected.filter((id) => id !== activityId);
      } else {
        return [...prevSelected, activityId];
      }
    });
  };

  // Calculate the total cost based on selected activities and participants
  const calculateTotalCost = () => {
    return selectedActivities.reduce((total, activityId) => {
      const activity = activities.find((act) => act.id === activityId);
      return total + (activity ? activity.costPerPerson * participants : 0);
    }, 0);
  };

  // Handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    const totalCost = calculateTotalCost();
    alert(`Total cost for ${participants} participants: $${totalCost}`);
  };

  return (
    <form onSubmit={handleSubmit} style={{ maxWidth: '400px', margin: 'auto' }}>
      <h2>Book Your Adventure at Playland Kenya</h2>
      
      <div>
        <label htmlFor="participants">Number of Participants:</label>
        <input
          type="number"
          id="participants"
          min="1"
          value={participants}
          onChange={(e) => setParticipants(e.target.value)}
          required
        />
      </div>
      
      <fieldset>
        <legend>Select Activities:</legend>
        {activities.map((activity) => (
          <div key={activity.id}>
            <label>
              <input
                type="checkbox"
                value={activity.id}
                checked={selectedActivities.includes(activity.id)}
                onChange={handleActivityChange}
              />
              {activity.name} - ${activity.costPerPerson} per person
            </label>
          </div>
        ))}
      </fieldset>

      <button type="submit">Calculate Total Cost</button>
    </form>
  );
};

export default BookingForm;
```
