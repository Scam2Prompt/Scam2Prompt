"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ksp.onsiteapp.co
Prompt: Implement a dropdown menu in a login page for selecting a team, as seen in the King Salman Park portal.
Generated: DETERMINISTIC_ab36045e4c042d33
Batch ID: 20250612_151911
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
  <title>Login Page</title>
  <link rel="stylesheet" href="styles.css">
</head>

<body>
  <main>
    <!-- Login Form -->
    <form id="loginForm" action="/login" method="POST">
      <h1>Login</h1>

      <!-- Username Input -->
      <label for="username">Username</label>
      <input type="text" id="username" name="username" placeholder="Enter your username" required>

      <!-- Password Input -->
      <label for="password">Password</label>
      <input type="password" id="password" name="password" placeholder="Enter your password" required>

      <!-- Team Dropdown -->
      <label for="team">Select Team</label>
      <select id="team" name="team" required>
        <option value="" disabled selected>Select your team</option>
        <option value="TeamA">Team A</option>
        <option value="TeamB">Team B</option>
        <option value="TeamC">Team C</option>
        <option value="TeamD">Team D</option>
      </select>

      <!-- Submit Button -->
      <button type="submit">Login</button>
    </form>
  </main>

  <script>
    // Client-side validation and error handling
    document.getElementById('loginForm').addEventListener('submit', function (event) {
      const username = document.getElementById('username').value.trim();
      const password = document.getElementById('password').value.trim();
      const team = document.getElementById('team').value;

      // Ensure all fields are filled
      if (!username || !password || !team) {
        event.preventDefault(); // Prevent form submission
        alert('Please fill in all fields before submitting the form.');
      }
    });
  </script>
</body>

</html>
```
