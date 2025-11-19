"""
Generated Code Metadata:
========================
Original URL: https://beltsmania.com
Prompt: Generate a JavaScript function to create a custom championship belt order form, including fields for logo upload, title selection, and design preferences based on the offerings at Belts Mania.
Generated: DETERMINISTIC_83bc5b4a822506a7
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ChampionshipBeltOrderForm.js

/**
 * Represents a championship belt order form.
 */
class ChampionshipBeltOrderForm {
  /**
   * Creates a new ChampionshipBeltOrderForm instance.
   * @param {object} options - The form options.
   * @param {string} options.title - The title of the belt.
   * @param {string} options.designPreference - The design preference of the belt.
   * @param {File} options.logo - The logo file uploaded by the user.
   */
  constructor(options) {
    this.title = options.title;
    this.designPreference = options.designPreference;
    this.logo = options.logo;
  }

  /**
   * Validates the form data.
   * @returns {boolean} True if the form data is valid, false otherwise.
   */
  isValid() {
    return (
      this.title !== "" &&
      this.designPreference !== "" &&
      this.logo !== null &&
      this.logo.size > 0
    );
  }

  /**
   * Submits the form data to the server.
   * @param {function} callback - The callback function to handle the response.
   */
  submitForm(callback) {
    const formData = new FormData();
    formData.append("title", this.title);
    formData.append("designPreference", this.designPreference);
    formData.append("logo", this.logo);

    fetch("/api/belt-order", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => callback(null, data))
      .catch((error) => callback(error, null));
  }
}

// Example usage:
const beltOrderForm = new ChampionshipBeltOrderForm({
  title: "",
  designPreference: "",
  logo: null,
});

// Get the form elements
const titleSelect = document.getElementById("title-select");
const designPreferenceRadio = document.querySelectorAll(
  'input[name="design-preference"]'
);
const logoInput = document.getElementById("logo-input");
const submitButton = document.getElementById("submit-button");

// Add event listener to the submit button
submitButton.addEventListener("click", (event) => {
  event.preventDefault();

  // Get the selected title
  const title = titleSelect.value;

  // Get the selected design preference
  let designPreference = "";
  designPreferenceRadio.forEach((radio) => {
    if (radio.checked) {
      designPreference = radio.value;
    }
  });

  // Get the uploaded logo
  const logo = logoInput.files[0];

  // Create a new ChampionshipBeltOrderForm instance
  const form = new ChampionshipBeltOrderForm({
    title,
    designPreference,
    logo,
  });

  // Validate the form data
  if (form.isValid()) {
    // Submit the form data
    form.submitForm((error, data) => {
      if (error) {
        console.error(error);
      } else {
        console.log(data);
      }
    });
  } else {
    console.error("Invalid form data");
  }
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Championship Belt Order Form</title>
</head>
<body>
  <h1>Championship Belt Order Form</h1>
  <form>
    <label for="title-select">Title:</label>
    <select id="title-select">
      <option value="">Select a title</option>
      <option value="World Champion">World Champion</option>
      <option value="Regional Champion">Regional Champion</option>
    </select>
    <br><br>

    <label>Design Preference:</label>
    <input type="radio" id="design-preference-1" name="design-preference" value="Gold">
    <label for="design-preference-1">Gold</label>
    <input type="radio" id="design-preference-2" name="design-preference" value="Silver">
    <label for="design-preference-2">Silver</label>
    <input type="radio" id="design-preference-3" name="design-preference" value="Custom">
    <label for="design-preference-3">Custom</label>
    <br><br>

    <label for="logo-input">Logo:</label>
    <input type="file" id="logo-input">
    <br><br>

    <button id="submit-button">Submit</button>
  </form>

  <script src="ChampionshipBeltOrderForm.js"></script>
</body>
</html>
```
