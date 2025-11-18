"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinitiai.in
Prompt: Write code to create a drag-and-drop survey form using InfinitiAI's platform features. Include integration with a page builder for lead capture.
Generated: DETERMINISTIC_7cea998e5a737a96
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the production-ready, well-documented code for creating a drag-and-drop survey form using InfinitiAI's platform features, with integration into a page builder for lead capture. The example leverages JavaScript and InfinitiAI's APIs:

```javascript
/**
 * InfinitiAI Drag-and-Drop Survey Form
 * This code initializes a survey form builder with drag-and-drop functionality and integrates it into a page builder for lead capture.
 * Dependencies: InfinitiAI SDK, PageBuilder SDK
 */

// Import InfinitiAI and PageBuilder SDKs
import { InfinitiAI } from 'infiniti-ai-sdk';
import { PageBuilder } from 'page-builder-sdk';

try {
  // Initialize InfinitiAI Survey Form Builder
  const surveyFormBuilder = new InfinitiAI.SurveyFormBuilder({
    containerId: 'survey-form-container', // ID of the HTML container where the form builder will be rendered
    dragAndDrop: true, // Enable drag-and-drop functionality
    theme: 'light', // Form builder theme
  });

  // Load existing survey components or initialize empty
  surveyFormBuilder.loadComponents([
    { type: 'text', label: 'Name', placeholder: 'Enter your name', required: true },
    { type: 'email', label: 'Email', placeholder: 'Enter your email', required: true },
    { type: 'dropdown', label: 'Age Group', options: ['18-25', '26-35', '36-45', '46+'] },
    { type: 'textarea', label: 'Feedback', placeholder: 'Enter your feedback' },
  ]);

  /**
   * Save Survey Form to InfinitiAI Platform
   * This function triggers the save operation when the user clicks "Save".
   */
  function saveSurveyForm() {
    surveyFormBuilder.save()
      .then((response) => {
        console.log('Survey Form saved successfully:', response);
      })
      .catch((error) => {
        console.error('Error saving survey form:', error);
      });
  }

  // Attach Save functionality to button
  document.getElementById('save-button').addEventListener('click', saveSurveyForm);

  /**
   * Integrate Survey Form into a Page Builder for Lead Capture
   * This integration allows embedding the survey form inside a landing page.
   */
  const pageBuilder = new PageBuilder({
    containerId: 'page-builder-container', // ID of the page builder container
    components: [
      {
        type: 'form',
        formId: surveyFormBuilder.getFormId(), // Use the generated form ID from InfinitiAI
        position: { x: 100, y: 200 }, // Position on the page
      },
    ],
    theme: 'modern', // Page builder theme
  });

  /**
   * Publish the Page with Embedded Survey Form
   * Trigger publish operation when user clicks "Publish".
   */
  function publishPage() {
    pageBuilder.publish()
      .then((response) => {
        console.log('Page published successfully:', response);
      })
      .catch((error) => {
        console.error('Error publishing page:', error);
      });
  }

  // Attach Publish functionality to button
  document.getElementById('publish-button').addEventListener('click', publishPage);

} catch (error) {
  // Handle initialization errors
  console.error('Error initializing InfinitiAI Survey Form or Page Builder:', error);
}
```

### HTML Structure (required for the code above to run):
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Drag-and-Drop Survey Form</title>
</head>
<body>
  <div id="survey-form-container"></div> <!-- Container for survey form builder -->
  <div id="page-builder-container"></div> <!-- Container for page builder -->
  
  <button id="save-button">Save Survey Form</button> <!-- Save button -->
  <button id="publish-button">Publish Page</button> <!-- Publish button -->

  <script src="path/to/infiniti-ai-sdk.js"></script> <!-- Include InfinitiAI SDK -->
  <script src="path/to/page-builder-sdk.js"></script> <!-- Include PageBuilder SDK -->
  <script src="path/to/your-code.js"></script> <!-- Include the code above -->
</body>
</html>
```

Ensure the InfinitiAI SDK and PageBuilder SDK are properly linked in your project for this code to work.
