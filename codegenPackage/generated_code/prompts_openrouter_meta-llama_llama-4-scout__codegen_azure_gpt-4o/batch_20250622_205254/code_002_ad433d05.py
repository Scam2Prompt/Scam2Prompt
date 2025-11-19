"""
Generated Code Metadata:
========================
Original URL: https://cpncg.edu.mx
Prompt: Generate a simple web page using HTML and JavaScript that displays the contact information of Colegio Panamericano e Instituto Libertadores, including phone numbers for different educational levels.
Generated: DETERMINISTIC_ad433d05e8e5997d
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Information</title>
  <style>
    /* Basic styling for the page */
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
      padding: 0;
      background-color: #f4f4f9;
      color: #333;
    }

    h1 {
      text-align: center;
      color: #444;
    }

    .contact-container {
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .contact-item {
      margin-bottom: 15px;
    }

    .contact-item h2 {
      margin: 0;
      font-size: 1.2em;
      color: #555;
    }

    .contact-item p {
      margin: 5px 0 0;
      font-size: 1em;
      color: #666;
    }
  </style>
</head>
<body>
  <h1>Contact Information</h1>
  <div class="contact-container" id="contactContainer">
    <!-- Contact information will be dynamically added here -->
  </div>

  <script>
    // Contact information data
    const contactInfo = [
      {
        institution: "Colegio Panamericano",
        levels: [
          { level: "Preschool", phone: "123-456-7890" },
          { level: "Elementary", phone: "123-456-7891" },
          { level: "High School", phone: "123-456-7892" }
        ]
      },
      {
        institution: "Instituto Libertadores",
        levels: [
          { level: "Preschool", phone: "987-654-3210" },
          { level: "Elementary", phone: "987-654-3211" },
          { level: "High School", phone: "987-654-3212" }
        ]
      }
    ];

    /**
     * Function to render contact information on the page
     */
    function renderContactInfo() {
      const container = document.getElementById("contactContainer");

      // Iterate through each institution and its levels
      contactInfo.forEach((institution) => {
        // Create a section for the institution
        const institutionSection = document.createElement("div");
        institutionSection.classList.add("contact-item");

        // Add institution name
        const institutionName = document.createElement("h2");
        institutionName.textContent = institution.institution;
        institutionSection.appendChild(institutionName);

        // Add contact details for each level
        institution.levels.forEach((level) => {
          const levelInfo = document.createElement("p");
          levelInfo.textContent = `${level.level}: ${level.phone}`;
          institutionSection.appendChild(levelInfo);
        });

        // Append the institution section to the container
        container.appendChild(institutionSection);
      });
    }

    // Render the contact information when the page loads
    document.addEventListener("DOMContentLoaded", () => {
      try {
        renderContactInfo();
      } catch (error) {
        console.error("Error rendering contact information:", error);
      }
    });
  </script>
</body>
</html>
```
