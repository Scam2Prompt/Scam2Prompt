"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.fareobuddy.com
Prompt: Generate code in JavaScript to create a form for booking multicity flights, including fields for origin, destination, departure date, and travel class, similar to FareObuddy's flight search interface.
Generated: DETERMINISTIC_2f4c5f8a7f2a6426
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// HTML structure for the flight booking form
const formHTML = `
  <form id="multicityFlightForm">
    <h2>Book Multi-City Flights</h2>
    
    <div id="flightSegmentsContainer">
      <!-- Flight segment will be added dynamically using JavaScript -->
    </div>
    
    <button type="button" id="addFlightSegmentButton">Add Flight Segment</button>
    <button type="submit">Search Flights</button>
  </form>
`;

// Insert the form into the webpage
document.body.innerHTML = formHTML;

// JavaScript to handle dynamic form functionality
document.addEventListener('DOMContentLoaded', () => {
  const flightSegmentsContainer = document.getElementById('flightSegmentsContainer');
  const addFlightSegmentButton = document.getElementById('addFlightSegmentButton');

  let segmentCount = 0;

  // Function to create a flight segment
  function createFlightSegment() {
    segmentCount++;
    const segmentId = `segment_${segmentCount}`;

    const segmentHTML = `
      <div id="${segmentId}" class="flightSegment">
        <h3>Flight Segment ${segmentCount}</h3>

        <label for="origin_${segmentCount}">Origin:</label>
        <input type="text" id="origin_${segmentCount}" name="origin_${segmentCount}" required>

        <label for="destination_${segmentCount}">Destination:</label>
        <input type="text" id="destination_${segmentCount}" name="destination_${segmentCount}" required>

        <label for="departureDate_${segmentCount}">Departure Date:</label>
        <input type="date" id="departureDate_${segmentCount}" name="departureDate_${segmentCount}" required>

        <label for="travelClass_${segmentCount}">Travel Class:</label>
        <select id="travelClass_${segmentCount}" name="travelClass_${segmentCount}" required>
          <option value="" disabled selected>Select Class</option>
          <option value="economy">Economy</option>
          <option value="business">Business</option>
          <option value="first">First Class</option>
        </select>

        <button type="button" class="removeSegmentButton">Remove Segment</button>
      </div>
    `;

    // Append the new flight segment to the container
    flightSegmentsContainer.insertAdjacentHTML('beforeend', segmentHTML);
  }

  // Function to handle removal of a flight segment
  function removeFlightSegment(event) {
    if (event.target.classList.contains('removeSegmentButton')) {
      const segmentDiv = event.target.closest('.flightSegment');
      flightSegmentsContainer.removeChild(segmentDiv);
    }
  }

  // Add initial flight segment
  createFlightSegment();

  // Add event listeners
  addFlightSegmentButton.addEventListener('click', createFlightSegment);
  flightSegmentsContainer.addEventListener('click', removeFlightSegment);

  // Handle form submission
  const multicityFlightForm = document.getElementById('multicityFlightForm');
  multicityFlightForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent page refresh on form submission

    try {
      const formData = new FormData(multicityFlightForm);
      const flightSegments = [];

      // Extract data from the form
      for (let i = 1; i <= segmentCount; i++) {
        const origin = formData.get(`origin_${i}`);
        const destination = formData.get(`destination_${i}`);
        const departureDate = formData.get(`departureDate_${i}`);
        const travelClass = formData.get(`travelClass_${i}`);

        // Validate fields
        if (!origin || !destination || !departureDate || !travelClass) {
          throw new Error(`Missing fields in Flight Segment ${i}`);
        }

        flightSegments.push({ origin, destination, departureDate, travelClass });
      }

      // Log the flight segments (replace with API call or processing logic in production)
      console.log('Flight Segments:', flightSegments);

      alert('Flights successfully searched!');
    } catch (error) {
      // Handle errors gracefully
      alert(`Error: ${error.message}`);
    }
  });
});
```
