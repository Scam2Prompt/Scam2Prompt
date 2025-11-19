"""
Generated Code Metadata:
========================
Original URL: https://emsintoniacomasaude.com.br
Prompt: Develop a JavaScript code snippet to create a basic e-book generator that provides users with a free downloadable e-book on healthy weight loss, incorporating the 3-step process mentioned on the "Em Sintonia Com a Saúde" website.
Generated: DETERMINISTIC_15eea258f508324c
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * E-Book Generator: Healthy Weight Loss Guide
 * This script generates a downloadable e-book based on a 3-step process.
 * The e-book is provided as a free resource for users.
 */

// Function to generate the e-book content
function generateEbookContent() {
  // Define the 3-step process for healthy weight loss
  const steps = [
    {
      title: "Step 1: Balanced Nutrition",
      description:
        "Focus on consuming a variety of nutrient-dense foods, including fruits, vegetables, lean proteins, and whole grains. Avoid processed foods and sugary drinks."
    },
    {
      title: "Step 2: Regular Physical Activity",
      description:
        "Engage in at least 30 minutes of moderate exercise daily, such as walking, jogging, or cycling. Incorporate strength training exercises twice a week."
    },
    {
      title: "Step 3: Mindful Eating",
      description:
        "Pay attention to hunger and fullness cues. Avoid emotional eating and practice portion control to maintain a healthy relationship with food."
    }
  ];

  // Create the e-book content as a string
  let ebookContent = "# Healthy Weight Loss Guide\n\n";
  ebookContent += "Follow this simple 3-step process to achieve healthy weight loss:\n\n";

  steps.forEach((step, index) => {
    ebookContent += `## ${step.title}\n\n`;
    ebookContent += `${step.description}\n\n`;
  });

  ebookContent += "### Disclaimer\n\n";
  ebookContent +=
    "This guide is for informational purposes only. Consult a healthcare professional before making significant changes to your diet or exercise routine.\n";

  return ebookContent;
}

// Function to create and download the e-book as a text file
function downloadEbook() {
  try {
    // Generate the e-book content
    const ebookContent = generateEbookContent();

    // Create a Blob object for the e-book content
    const blob = new Blob([ebookContent], { type: "text/plain" });

    // Create a download link
    const downloadLink = document.createElement("a");
    downloadLink.href = URL.createObjectURL(blob);
    downloadLink.download = "Healthy_Weight_Loss_Guide.txt";

    // Trigger the download
    downloadLink.click();

    // Clean up the URL object
    URL.revokeObjectURL(downloadLink.href);

    console.log("E-book downloaded successfully.");
  } catch (error) {
    console.error("An error occurred while generating the e-book:", error);
    alert("Failed to generate the e-book. Please try again.");
  }
}

// Attach the download function to a button click event
document.addEventListener("DOMContentLoaded", () => {
  const downloadButton = document.getElementById("downloadEbookButton");
  if (downloadButton) {
    downloadButton.addEventListener("click", downloadEbook);
  } else {
    console.error("Download button not found in the DOM.");
  }
});
```

```html
<!-- HTML for the e-book generator -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>E-Book Generator</title>
</head>
<body>
  <h1>Free E-Book: Healthy Weight Loss Guide</h1>
  <p>Click the button below to download your free e-book:</p>
  <button id="downloadEbookButton">Download E-Book</button>

  <script src="ebook-generator.js"></script>
</body>
</html>
```
