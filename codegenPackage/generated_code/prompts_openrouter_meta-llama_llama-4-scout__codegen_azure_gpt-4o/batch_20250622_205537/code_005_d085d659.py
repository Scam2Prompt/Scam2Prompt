"""
Generated Code Metadata:
========================
Original URL: https://kineticairdrop.typeform.com
Prompt: Develop a script to export Typeform data to Google Sheets using Zapier or a similar integration tool.
Generated: DETERMINISTIC_d085d65929d2c344
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Script to export Typeform data to Google Sheets using Zapier Webhooks.
 * This script is designed to be used within a Zapier workflow.
 * 
 * Prerequisites:
 * - A Typeform account with forms set up.
 * - A Google Sheet created to store the exported data.
 * - A Zapier account with access to Webhooks and Google Sheets integrations.
 * 
 * This script assumes Zapier is configured to trigger on Typeform submission
 * and send the data to this webhook.
 */

// Import required modules (Zapier handles this internally, no need for explicit imports)

// Main function to handle incoming Typeform data
module.exports = async (request, response) => {
  try {
    // Parse incoming Typeform data from the webhook payload
    const typeformData = request.body;

    // Validate the incoming data
    if (!typeformData || !typeformData.form_response) {
      throw new Error("Invalid Typeform data received.");
    }

    // Extract relevant data from the Typeform response
    const formResponse = typeformData.form_response;
    const answers = formResponse.answers; // Array of answers
    const formId = formResponse.form_id; // Form ID
    const submittedAt = formResponse.submitted_at; // Submission timestamp

    // Prepare data for Google Sheets
    const rowData = answers.map((answer) => {
      return {
        question: answer.field.title, // Question text
        answer: answer.text || answer.choice.label || answer.number || "", // Answer value
      };
    });

    // Add metadata (form ID and submission timestamp)
    rowData.push({
      question: "Form ID",
      answer: formId,
    });
    rowData.push({
      question: "Submitted At",
      answer: submittedAt,
    });

    // Send data to Google Sheets (Zapier handles this via its Google Sheets integration)
    // Example: Use Zapier's Google Sheets action to append the rowData to a specific sheet.

    response.status(200).send({
      success: true,
      message: "Data processed successfully.",
      data: rowData,
    });
  } catch (error) {
    // Handle errors gracefully
    console.error("Error processing Typeform data:", error.message);

    response.status(500).send({
      success: false,
      message: "An error occurred while processing the data.",
      error: error.message,
    });
  }
};
```

This script is designed to be used within a Zapier webhook integration. It processes incoming Typeform data, formats it, and sends it to Google Sheets using Zapier's built-in Google Sheets integration.
