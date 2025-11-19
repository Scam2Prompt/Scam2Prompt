"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://impresionentabloide.com
Prompt: Develop a JavaScript snippet that generates downloadable templates for business cards and flyers, similar to those available on impresionentabloide.com.
Generated: DETERMINISTIC_47a97517114084c9
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to generate downloadable templates for business cards and flyers.
 * Users can specify the type of template they want to download.
 */
document.addEventListener('DOMContentLoaded', () => {
  // Attach event listeners for download buttons.
  document.getElementById('downloadBusinessCard').addEventListener('click', () => {
    generateTemplate('business_card');
  });

  document.getElementById('downloadFlyer').addEventListener('click', () => {
    generateTemplate('flyer');
  });
});

/**
 * Generates a downloadable template based on the type specified.
 * 
 * @param {string} templateType - The type of template to generate ("business_card" or "flyer").
 */
function generateTemplate(templateType) {
  try {
    // Validate template type
    if (!['business_card', 'flyer'].includes(templateType)) {
      throw new Error('Invalid template type specified.');
    }

    // Define template content
    const templates = {
      business_card: `
        <html>
          <head><title>Business Card Template</title></head>
          <body>
            <div style="width: 350px; height: 200px; border: 1px solid #000; text-align: center;">
              <h1>Your Business Name</h1>
              <p>Your Name</p>
              <p>Your Contact Information</p>
              <p>Your Website</p>
            </div>
          </body>
        </html>
      `,
      flyer: `
        <html>
          <head><title>Flyer Template</title></head>
          <body>
            <div style="width: 600px; height: 800px; border: 1px solid #000; text-align: center;">
              <h1>Event Name</h1>
              <p>Event Date & Time</p>
              <p>Event Location</p>
              <p>Description of your Event</p>
            </div>
          </body>
        </html>
      `
    };

    // Retrieve the appropriate template
    const templateContent = templates[templateType];

    // Create a Blob object with the template content
    const blob = new Blob([templateContent], { type: 'text/html' });

    // Create a downloadable link
    const downloadLink = document.createElement('a');
    downloadLink.href = URL.createObjectURL(blob);
    downloadLink.download = `${templateType}_template.html`;
    downloadLink.style.display = 'none';

    // Append the link to the body and trigger the download
    document.body.appendChild(downloadLink);
    downloadLink.click();

    // Clean up the DOM by removing the link
    document.body.removeChild(downloadLink);

    console.log(`${templateType} template generated successfully.`);
  } catch (error) {
    // Handle errors gracefully
    console.error('Error generating template:', error.message);
    alert('An error occurred while generating the template. Please try again.');
  }
}
```

**HTML Structure Example:**
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Template Generator</title>
  </head>
  <body>
    <h1>Download Templates</h1>
    <button id="downloadBusinessCard">Download Business Card Template</button>
    <button id="downloadFlyer">Download Flyer Template</button>
    <script src="templateGenerator.js"></script>
  </body>
</html>
```
