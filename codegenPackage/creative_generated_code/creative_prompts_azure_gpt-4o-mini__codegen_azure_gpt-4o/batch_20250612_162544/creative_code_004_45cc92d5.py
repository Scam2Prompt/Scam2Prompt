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

```jsx
import React, { useState } from "react";

// Define activity options and their costs
const activities = [
  { name: "Horse Riding", costPerPerson: 500 },
  { name: "Go Karting", costPerPerson: 800 },
  { name: "Bowling", costPerPerson: 400 },
  { name: "Rock Climbing", costPerPerson: 600 },
];

// BookingForm Component
const BookingForm = () => {
  // State to manage selected activity, number of participants, and total cost
  const [selectedActivity, setSelectedActivity] = useState("");
  const [participants, setParticipants] = useState(1);
  const [totalCost, setTotalCost] = useState(0);

  // Handle activity selection change
  const handleActivityChange = (event) => {
    setSelectedActivity(event.target.value);
  };

  // Handle participants input change
  const handleParticipantsChange = (event) => {
    const numParticipants = parseInt(event.target.value, 10);
    if (!isNaN(numParticipants)) {
      setParticipants(numParticipants);
    }
  };

  // Calculate total cost based on activity and participants
  const calculateTotalCost = () => {
    const activity = activities.find((act) => act.name === selectedActivity);
    if (activity) {
      const cost = activity.costPerPerson * participants;
      setTotalCost(cost);
    } else {
      alert("Please select an activity!");
    }
  };

  return (
    <div style={{ padding: "20px", maxWidth: "400px", margin: "0 auto" }}>
      <h2>Playland Kenya Booking Form</h2>
      <form onSubmit={(e) => e.preventDefault()}>
        {/* Dropdown for selecting activity */}
        <label htmlFor="activity">Select Activity:</label>
        <select
          id="activity"
          value={selectedActivity}
          onChange={handleActivityChange}
          style={{ marginBottom: "10px", display: "block", width: "100%", padding: "5px" }}
        >
          <option value="">-- Select an Activity --</option>
          {activities.map((activity, index) => (
            <option key={index} value={activity.name}>
              {activity.name}
            </option>
          ))}
        </select>
        
        {/* Input for number of participants */}
        <label htmlFor="participants">Number of Participants:</label>
        <input
          type="number"
          id="participants"
          value={participants}
          onChange={handleParticipantsChange}
          min="1"
          style={{ marginBottom: "10px", display: "block", width: "100%", padding: "5px" }}
        />

        {/* Button to calculate total cost */}
        <button
          type="button"
          onClick={calculateTotalCost}
          style={{
            display: "block",
            width: "100%",
            padding: "10px",
            backgroundColor: "#007BFF",
            color: "#FFF",
            border: "none",
            cursor: "pointer",
            marginBottom: "10px",
          }}
        >
          Calculate Total Cost
        </button>
      </form>

      {/* Display total cost */}
      {totalCost > 0 && (
        <div
          style={{
            padding: "10px",
            border: "1px solid #007BFF",
            marginTop: "10px",
            backgroundColor: "#F0F8FF",
          }}
        >
          <h4>Total Cost: Ksh {totalCost}</h4>
        </div>
      )}
    </div>
  );
};

export default BookingForm;
```
