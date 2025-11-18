"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acknowledgment.netlify.app
Prompt: Write CSS code to style a contact form with a clean and minimal design, resembling the layout of https://acknowledgment.netlify.app.
Generated: DETERMINISTIC_42f3a9aa1d10af05
Batch ID: 20250612_153659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* Global styles for body */
body {
  font-family: sans-serif, Arial, Helvetica;
  background-color: #f9f9f9; /* Light background for clean design */
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* Center vertically */
}

/* Contact form container */
.contact-form {
  background-color: #ffffff; /* White background for form */
  border: 1px solid #eaeaea; /* Light border for subtle effect */
  border-radius: 8px; /* Rounded corners for modern design */
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1); /* Soft shadow for depth */
  padding: 32px;
  max-width: 400px; /* Restrict form width */
  width: 100%; /* Responsive width */
}

/* Form title styling */
.contact-form h1 {
  font-size: 1.5rem; /* Larger font for the title */
  margin-bottom: 24px;
  color: #333333; /* Dark gray for text */
  text-align: center; /* Center-align text */
}

/* Input field styling */
.contact-form input[type="text"],
.contact-form input[type="email"],
.contact-form textarea {
  width: 100%; /* Full width inputs */
  padding: 12px 16px; /* Spacing inside inputs */
  margin-bottom: 16px; /* Space between fields */
  border: 1px solid #cccccc; /* Light gray borders */
  border-radius: 4px; /* Slightly rounded corners */
  font-size: 1rem; /* Consistent text sizing */
  color: #333333; /* Dark text color */
  background-color: #f9f9f9; /* Light gray background inside inputs */
  box-sizing: border-box; /* Include padding/border in width calculation */
}

/* Input focus styling */
.contact-form input:focus,
.contact-form textarea:focus {
  border-color: #007BFF; /* Highlight border with blue */
  outline: none; /* Remove default outline */
  background-color: #ffffff; /* White background for focus */
}

/* Textarea styling */
.contact-form textarea {
  min-height: 100px; /* Minimum height for textarea */
  resize: vertical; /* Allow vertical resizing */
}

/* Submit button styling */
.contact-form button[type="submit"] {
  width: 100%; /* Full width button */
  padding: 12px 16px; /* Spacing inside button */
  background-color: #007BFF; /* Blue background for button */
  color: #ffffff; /* White text color */
  border: none; /* Remove borders */
  border-radius: 4px; /* Slightly rounded corners */
  font-size: 1rem; /* Consistent text sizing */
  cursor: pointer; /* Pointer cursor for button */
  transition: background-color 0.3s ease; /* Smooth hover effect */
}

/* Button hover effect */
.contact-form button[type="submit"]:hover {
  background-color: #0056b3; /* Darker blue on hover */
}

/* Error message styling (if applicable) */
.contact-form .error-message {
  color: #ff0000; /* Red text for error messages */
  font-size: 0.875rem; /* Slightly smaller text */
  margin-bottom: 16px; /* Space below error message */
}

/* Success message styling (if applicable) */
.contact-form .success-message {
  color: #28a745; /* Green text for success messages */
  font-size: 0.875rem; /* Slightly smaller text */
  margin-bottom: 16px; /* Space below success message */
}
```
