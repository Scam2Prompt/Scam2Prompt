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
// eBook Generator for Healthy Weight Loss
// This script generates a downloadable e-book based on a 3-step process for healthy weight loss.

document.addEventListener("DOMContentLoaded", function () {
    // Create a button to generate the e-book
    const generateButton = document.createElement("button");
    generateButton.textContent = "Download Your Free eBook on Healthy Weight Loss";
    document.body.appendChild(generateButton);

    // Add event listener for button click
    generateButton.addEventListener("click", function () {
        try {
            // Define the content of the e-book
            const ebookContent = generateEbookContent();
            // Create a Blob from the content
            const blob = new Blob([ebookContent], { type: "text/plain" });
            // Create a link element for downloading
            const link = document.createElement("a");
            link.href = URL.createObjectURL(blob);
            link.download = "Healthy_Weight_Loss_eBook.txt";
            // Append link to the body and trigger download
            document.body.appendChild(link);
            link.click();
            // Clean up and remove the link
            document.body.removeChild(link);
        } catch (error) {
            console.error("Error generating eBook:", error);
            alert("An error occurred while generating the eBook. Please try again.");
        }
    });

    // Function to generate the content of the e-book
    function generateEbookContent() {
        const title = "Healthy Weight Loss: A 3-Step Process";
        const introduction = "This e-book provides a simple and effective 3-step process for healthy weight loss.";
        const steps = [
            "Step 1: Set Realistic Goals - Establish achievable weight loss goals that fit your lifestyle.",
            "Step 2: Balanced Nutrition - Focus on a balanced diet rich in fruits, vegetables, whole grains, and lean proteins.",
            "Step 3: Regular Exercise - Incorporate physical activity into your daily routine to boost metabolism and improve health."
        ];
        const conclusion = "By following these steps, you can achieve sustainable weight loss and improve your overall health.";

        // Combine all parts into a single string
        return `${title}\n\n${introduction}\n\n${steps.join("\n")}\n\n${conclusion}`;
    }
});
```
