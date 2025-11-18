"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hsrenterprises.co.in
Prompt: Generate code to implement a "Roadside Assistance" call-to-action button on a website, which triggers a phone call to the number 1800 2100 007 when clicked.
Generated: DETERMINISTIC_90a0bc7821a268e9
Batch ID: 20250612_153224
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
  <title>Roadside Assistance</title>
  <style>
    /* Basic styling for the button */
    .call-button {
      background-color: #ff5722; /* Bright color for visibility */
      color: white;
      padding: 15px 25px;
      font-size: 16px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    .call-button:hover {
      background-color: #e64a19; /* Slightly darker shade on hover */
    }
  </style>
</head>
<body>
  <!-- Call-to-action button -->
  <button class="call-button" onclick="triggerPhoneCall()">Call Roadside Assistance</button>

  <script>
    /**
     * Function to initiate a phone call to Roadside Assistance
     */
    function triggerPhoneCall() {
      try {
        // Direct the browser to the phone link
        window.location.href = 'tel:18002100007';
      } catch (error) {
        // Log the error (optional: display a user-friendly message)
        console.error('Error initiating phone call:', error);
        alert('An issue occurred while trying to make the call. Please try again.');
      }
    }
  </script>
</body>
</html>
```
