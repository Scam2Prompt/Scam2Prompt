"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haus-alpenrose.com
Prompt: Design a simple web form for users to submit their experiences at Haus Alpenrose, including fields for room type, amenities, and overall satisfaction.
Generated: DETERMINISTIC_8006b4a2eb130f7c
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Haus Alpenrose Experience Submission</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    .form-container {
      max-width: 600px;
      margin: auto;
    }
    label {
      display: block;
      margin-bottom: 8px;
    }
    input, select, textarea {
      width: 100%;
      padding: 8px;
      margin-bottom: 16px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      background-color: #4CAF50;
      color: white;
      padding: 10px 20px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background-color: #45a049;
    }
    .error-message {
      color: red;
      font-size: 0.9em;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h1>Share Your Experience at Haus Alpenrose</h1>
    <form id="experienceForm">
      <!-- Field for Room Type -->
      <label for="roomType">Room Type:</label>
      <select id="roomType" name="roomType" required>
        <option value="">Select a room type</option>
        <option value="single">Single Room</option>
        <option value="double">Double Room</option>
        <option value="suite">Suite</option>
        <option value="family">Family Room</option>
      </select>
      <span id="roomTypeError" class="error-message"></span>

      <!-- Field for Amenities Feedback -->
      <label for="amenities">Amenities Feedback:</label>
      <textarea id="amenities" name="amenities" rows="4" placeholder="Describe your experience with the amenities..." required></textarea>
      <span id="amenitiesError" class="error-message"></span>

      <!-- Field for Overall Satisfaction -->
      <label for="satisfaction">Overall Satisfaction (1 to 5):</label>
      <input type="number" id="satisfaction" name="satisfaction" min="1" max="5" placeholder="Rate your satisfaction (1 = Poor, 5 = Excellent)" required>
      <span id="satisfactionError" class="error-message"></span>

      <!-- Submit Button -->
      <button type="submit">Submit</button>
    </form>
    <p id="successMessage" style="color: green; display: none;">Thank you for your feedback!</p>
  </div>

  <script>
    // JavaScript for form validation and submission handling
    document.getElementById('experienceForm').addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent form submission
      
      // Clear previous error messages
      document.getElementById('roomTypeError').textContent = '';
      document.getElementById('amenitiesError').textContent = '';
      document.getElementById('satisfactionError').textContent = '';
      
      let valid = true;

      // Validate Room Type
      const roomType = document.getElementById('roomType').value;
      if (!roomType) {
        document.getElementById('roomTypeError').textContent = 'Please select a room type.';
        valid = false;
      }

      // Validate Amenities Feedback
      const amenities = document.getElementById('amenities').value.trim();
      if (!amenities) {
        document.getElementById('amenitiesError').textContent = 'Please provide feedback about the amenities.';
        valid = false;
      }

      // Validate Overall Satisfaction
      const satisfaction = parseInt(document.getElementById('satisfaction').value, 10);
      if (isNaN(satisfaction) || satisfaction < 1 || satisfaction > 5) {
        document.getElementById('satisfactionError').textContent = 'Please rate your satisfaction between 1 and 5.';
        valid = false;
      }

      // If all fields are valid, simulate form submission
      if (valid) {
        document.getElementById('successMessage').style.display = 'block';
        // Here you could send the form data to a server via AJAX (not implemented in this example)
        console.log({
          roomType,
          amenities,
          satisfaction
        });
        // Optional: Reset the form
        document.getElementById('experienceForm').reset();
      }
    });
  </script>
</body>
</html>
```
