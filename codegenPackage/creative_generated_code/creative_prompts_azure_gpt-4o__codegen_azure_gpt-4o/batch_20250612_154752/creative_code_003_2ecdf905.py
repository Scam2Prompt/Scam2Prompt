"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mystrikingly.com
Prompt: Provide code examples for creating a contact form that integrates with Strikingly's built-in analytics tools.
Generated: DETERMINISTIC_2ecdf90593d1a57b
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Contact Form Integration with Strikingly Analytics

// HTML: Create a simple contact form
/* 
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Form</title>
</head>
<body>
  <form id="contactForm">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    <br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    <br>
    <label for="message">Message:</label>
    <textarea id="message" name="message" required></textarea>
    <br>
    <button type="submit">Submit</button>
  </form>
  <script src="contactForm.js"></script>
</body>
</html>
*/

// JavaScript: Handle form submission and integrate with Strikingly Analytics

document.addEventListener("DOMContentLoaded", () => {
  // Select the contact form element
  const contactForm = document.getElementById("contactForm");

  // Attach submit event listener
  contactForm.addEventListener("submit", async (event) => {
    event.preventDefault(); // Prevent default form submission

    // Collect form data
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const message = document.getElementById("message").value.trim();

    // Validate form inputs
    if (!name || !email || !message) {
      alert("All fields are required.");
      return;
    }

    try {
      // Simulate sending form data to API (Replace with your backend logic)
      const response = await simulateApiRequest({ name, email, message });

      if (response.status === "success") {
        // Track successful form submission event with Strikingly Analytics
        trackStrikinglyEvent("ContactFormSubmission", {
          name,
          email,
          message,
        });

        alert("Thank you for your message! We will get back to you soon.");
        contactForm.reset(); // Clear the form
      } else {
        throw new Error("Failed to submit the form.");
      }
    } catch (error) {
      console.error("Error submitting form:", error);
      alert("An error occurred while submitting the form. Please try again.");
    }
  });

  // Simulated API request (Replace with actual backend logic)
  async function simulateApiRequest(data) {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve({ status: "success", data });
      }, 1000); // Simulated delay
    });
  }

  // Track events using Strikingly Analytics (Assumes Strikingly tracking script is loaded)
  function trackStrikinglyEvent(eventName, eventData) {
    if (window.Strikingly) {
      window.Strikingly.track(eventName, eventData);
    } else {
      console.warn("Strikingly analytics tools are not loaded.");
    }
  }
});
```
