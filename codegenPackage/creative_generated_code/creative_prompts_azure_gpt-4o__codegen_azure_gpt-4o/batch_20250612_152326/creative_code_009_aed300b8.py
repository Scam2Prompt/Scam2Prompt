"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.events
Prompt: Generate code for a mobile-friendly webpage that showcases event details and allows users to apply for roles like staff, volunteers, or lead positions for a festival like Celestia.
Generated: DETERMINISTIC_aed300b834a75f0f
Batch ID: 20250612_152326
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
  <meta name="description" content="Celestia Festival Event Details and Role Application">
  <title>Celestia Festival</title>
  <style>
    /* Mobile-first design approach */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f8f9fa;
      color: #333;
    }

    header {
      background-color: #4caf50;
      color: white;
      padding: 1em;
      text-align: center;
    }

    main {
      padding: 1em;
    }

    .event-details {
      margin-bottom: 2em;
    }

    .event-details h1 {
      font-size: 1.5em;
      margin-bottom: 0.5em;
    }

    .event-details p {
      margin: 0.5em 0;
    }

    .application-form {
      background: white;
      padding: 1em;
      border-radius: 5px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    .application-form h2 {
      font-size: 1.25em;
      margin-bottom: 1em;
    }

    .form-group {
      margin-bottom: 1em;
    }

    .form-group label {
      display: block;
      margin-bottom: 0.5em;
    }

    .form-group input, .form-group select, .form-group textarea {
      width: 100%;
      padding: 0.5em;
      border: 1px solid #ccc;
      border-radius: 5px;
    }

    .form-group textarea {
      resize: vertical;
    }

    .form-actions {
      text-align: center;
    }

    .form-actions button {
      padding: 0.75em 1.5em;
      border: none;
      border-radius: 5px;
      background-color: #4caf50;
      color: white;
      font-size: 1em;
      cursor: pointer;
    }

    .form-actions button:hover {
      background-color: #45a049;
    }

    footer {
      text-align: center;
      padding: 1em;
      background-color: #333;
      color: white;
      margin-top: 2em;
    }

    /* Media query for larger screens */
    @media (min-width: 768px) {
      .event-details h1 {
        font-size: 2em;
      }

      .application-form {
        width: 50%;
        margin: 0 auto;
      }
    }
  </style>
</head>
<body>
  <!-- Page Header -->
  <header>
    <h1>Celestia Festival</h1>
  </header>

  <!-- Main Content -->
  <main>
    <!-- Event Details Section -->
    <section class="event-details">
      <h1>About the Festival</h1>
      <p>Date: March 25-27, 2024</p>
      <p>Location: Sunset Park, San Francisco</p>
      <p>Celestia Festival is a celebration of art, music, and culture. Join us for three days of unforgettable experiences!</p>
    </section>

    <!-- Application Form Section -->
    <section class="application-form">
      <h2>Apply for a Role</h2>
      <form id="applicationForm">
        <!-- Name Field -->
        <div class="form-group">
          <label for="name">Full Name:</label>
          <input type="text" id="name" name="name" placeholder="Your full name" required>
        </div>

        <!-- Email Field -->
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" id="email" name="email" placeholder="Your email address" required>
        </div>

        <!-- Role Selection -->
        <div class="form-group">
          <label for="role">Role:</label>
          <select id="role" name="role" required>
            <option value="">Select a role</option>
            <option value="staff">Staff</option>
            <option value="volunteer">Volunteer</option>
            <option value="lead">Lead</option>
          </select>
        </div>

        <!-- Additional Comments -->
        <div class="form-group">
          <label for="comments">Additional Comments (Optional):</label>
          <textarea id="comments" name="comments" rows="4" placeholder="Any additional information you'd like to share"></textarea>
        </div>

        <!-- Submit Button -->
        <div class="form-actions">
          <button type="submit">Apply</button>
        </div>
      </form>
    </section>
  </main>

  <!-- Footer -->
  <footer>
    <p>&copy; 2024 Celestia Festival. All rights reserved.</p>
  </footer>

  <script>
    // JavaScript for form submission handling
    document.getElementById('applicationForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent the default form submission behavior

      try {
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const role = document.getElementById('role').value;

        // Basic validation
        if (!name || !email || !role) {
          alert('Please fill out all required fields.');
          return;
        }

        // Simulating form submission (Replace with actual server-side logic in production)
        alert(`Thank you, ${name}! Your application for the "${role}" role has been submitted.`);
        document.getElementById('applicationForm').reset(); // Clear the form
      } catch (error) {
        console.error('Error during form submission:', error);
        alert('An unexpected error occurred. Please try again later.');
      }
    });
  </script>
</body>
</html>
```
