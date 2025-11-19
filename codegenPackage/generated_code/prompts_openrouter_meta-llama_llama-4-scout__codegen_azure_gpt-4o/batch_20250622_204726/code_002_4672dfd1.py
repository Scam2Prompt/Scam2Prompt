"""
Generated Code Metadata:
========================
Original URL: https://gastrolife.net
Prompt: Generate a code snippet in JavaScript to create a simple patient registration form for a gastroenterology clinic, including fields for patient details and appointment scheduling for procedures like hepatology and nutricion.
Generated: DETERMINISTIC_4672dfd1e357e026
Batch ID: 20250622_204726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Patient Registration Form for Gastroenterology Clinic
// This code creates a simple HTML form using JavaScript and includes validation and error handling.

document.addEventListener("DOMContentLoaded", () => {
  // Create the form element
  const form = document.createElement("form");
  form.id = "patientRegistrationForm";
  form.style.maxWidth = "500px";
  form.style.margin = "0 auto";

  // Create a helper function to generate input fields
  const createInputField = (labelText, inputType, inputName, isRequired = false) => {
    const fieldWrapper = document.createElement("div");
    fieldWrapper.style.marginBottom = "15px";

    const label = document.createElement("label");
    label.textContent = labelText;
    label.htmlFor = inputName;
    label.style.display = "block";
    label.style.marginBottom = "5px";

    const input = document.createElement("input");
    input.type = inputType;
    input.name = inputName;
    input.id = inputName;
    input.style.width = "100%";
    input.style.padding = "8px";
    input.style.boxSizing = "border-box";
    if (isRequired) {
      input.required = true;
    }

    fieldWrapper.appendChild(label);
    fieldWrapper.appendChild(input);
    return fieldWrapper;
  };

  // Create input fields for patient details
  form.appendChild(createInputField("Full Name", "text", "fullName", true));
  form.appendChild(createInputField("Date of Birth", "date", "dob", true));
  form.appendChild(createInputField("Email Address", "email", "email", true));
  form.appendChild(createInputField("Phone Number", "tel", "phone", true));

  // Create a dropdown for procedure selection
  const procedureWrapper = document.createElement("div");
  procedureWrapper.style.marginBottom = "15px";

  const procedureLabel = document.createElement("label");
  procedureLabel.textContent = "Select Procedure";
  procedureLabel.htmlFor = "procedure";
  procedureLabel.style.display = "block";
  procedureLabel.style.marginBottom = "5px";

  const procedureSelect = document.createElement("select");
  procedureSelect.name = "procedure";
  procedureSelect.id = "procedure";
  procedureSelect.style.width = "100%";
  procedureSelect.style.padding = "8px";
  procedureSelect.style.boxSizing = "border-box";
  procedureSelect.required = true;

  const procedures = ["Hepatology", "Nutrition"];
  procedures.forEach((procedure) => {
    const option = document.createElement("option");
    option.value = procedure.toLowerCase();
    option.textContent = procedure;
    procedureSelect.appendChild(option);
  });

  procedureWrapper.appendChild(procedureLabel);
  procedureWrapper.appendChild(procedureSelect);
  form.appendChild(procedureWrapper);

  // Create input field for appointment date
  form.appendChild(createInputField("Appointment Date", "date", "appointmentDate", true));

  // Create a submit button
  const submitButton = document.createElement("button");
  submitButton.type = "submit";
  submitButton.textContent = "Register";
  submitButton.style.padding = "10px 20px";
  submitButton.style.backgroundColor = "#007BFF";
  submitButton.style.color = "#FFF";
  submitButton.style.border = "none";
  submitButton.style.borderRadius = "5px";
  submitButton.style.cursor = "pointer";

  form.appendChild(submitButton);

  // Add form submission event listener
  form.addEventListener("submit", (event) => {
    event.preventDefault(); // Prevent default form submission

    // Collect form data
    const formData = new FormData(form);
    const data = {};
    formData.forEach((value, key) => {
      data[key] = value;
    });

    // Simulate form submission (e.g., send data to server)
    try {
      console.log("Form submitted successfully:", data);
      alert("Patient registered successfully!");
      form.reset(); // Reset the form after submission
    } catch (error) {
      console.error("Error submitting form:", error);
      alert("An error occurred while submitting the form. Please try again.");
    }
  });

  // Append the form to the body
  document.body.appendChild(form);
});
```
