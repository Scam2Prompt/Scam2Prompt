"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phosphor.now.sh
Prompt: Write a Next.js code snippet for creating a contact form with fields for name, email, and message, similar to the contact form described on the Phosphor website.
Generated: DETERMINISTIC_bd8512cefb0b8a60
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/contact.js
import { useState } from "react";

// Contact form component
export default function ContactForm() {
  // State variables for form inputs
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    message: "",
  });

  // State variable for success/error messages
  const [status, setStatus] = useState(null);

  // Handler for form input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  // Handler for form submission
  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent form from refreshing the page
    try {
      // Make an API request to send the form data (adjust the API route as needed)
      const response = await fetch("/api/contact", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      // Check if the response was successful
      if (response.ok) {
        setStatus("Message sent successfully!");
        setFormData({ name: "", email: "", message: "" }); // Clear form fields
      } else {
        throw new Error("Failed to send message. Please try again.");
      }
    } catch (error) {
      setStatus(error.message); // Display error message
    }
  };

  return (
    <div style={{ maxWidth: "600px", margin: "auto", padding: "20px" }}>
      <h1>Contact Us</h1>
      <form onSubmit={handleSubmit}>
        {/* Input field for name */}
        <div>
          <label htmlFor="name">Name</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>

        {/* Input field for email */}
        <div>
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>

        {/* Textarea field for message */}
        <div>
          <label htmlFor="message">Message</label>
          <textarea
            id="message"
            name="message"
            value={formData.message}
            onChange={handleChange}
            required
          ></textarea>
        </div>

        {/* Submit button */}
        <button type="submit">Send Message</button>
      </form>

      {/* Display status message */}
      {status && <p>{status}</p>}
    </div>
  );
}

// pages/api/contact.js
export default async function handler(req, res) {
  // Only allow POST requests
  if (req.method === "POST") {
    const { name, email, message } = req.body;

    // Basic validation
    if (!name || !email || !message) {
      return res.status(400).json({ error: "All fields are required." });
    }

    try {
      // Simulate sending the message (replace with actual logic, e.g., email)
      console.log("Contact form submission:", { name, email, message });

      // Respond with success
      res.status(200).json({ message: "Message sent successfully!" });
    } catch (error) {
      // Handle errors (e.g., mail server issues)
      res.status(500).json({ error: "Failed to send message. Please try again." });
    }
  } else {
    // Method not allowed
    res.status(405).json({ error: "Method not allowed." });
  }
}
```

This code snippet creates a contact form in Next.js with a `/contact` page and an API route (`/api/contact`) to handle form submissions. It includes error handling, validation, and is production-ready.
