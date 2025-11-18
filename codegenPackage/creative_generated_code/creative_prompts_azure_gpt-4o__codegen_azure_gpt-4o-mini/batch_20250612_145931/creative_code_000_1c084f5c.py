"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v-tempe.online
Prompt: Write JavaScript code to dynamically display a link or text based on the presence of UTM parameters in the URL, as described on the "v-tempe.online" webpage.
Generated: DETERMINISTIC_1c084f5cd910872d
Batch ID: 20250612_145931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to get UTM parameters from the current URL
function getUTMParameters() {
    const urlParams = new URLSearchParams(window.location.search);
    const utmParams = {
        utm_source: urlParams.get('utm_source'),
        utm_medium: urlParams.get('utm_medium'),
        utm_campaign: urlParams.get('utm_campaign'),
        utm_term: urlParams.get('utm_term'),
        utm_content: urlParams.get('utm_content')
    };
    return utmParams;
}

// Function to display content based on UTM parameters
function displayContentBasedOnUTM() {
    const utmParams = getUTMParameters();
    const outputElement = document.getElementById('utm-output');

    // Clear previous content
    outputElement.innerHTML = '';

    // Check if any UTM parameters are present
    if (utmParams.utm_source || utmParams.utm_medium || utmParams.utm_campaign) {
        // Construct the output message
        const utmMessage = `
            <p>Thank you for visiting from:</p>
            <ul>
                ${utmParams.utm_source ? `<li>Source: ${utmParams.utm_source}</li>` : ''}
                ${utmParams.utm_medium ? `<li>Medium: ${utmParams.utm_medium}</li>` : ''}
                ${utmParams.utm_campaign ? `<li>Campaign: ${utmParams.utm_campaign}</li>` : ''}
                ${utmParams.utm_term ? `<li>Term: ${utmParams.utm_term}</li>` : ''}
                ${utmParams.utm_content ? `<li>Content: ${utmParams.utm_content}</li>` : ''}
            </ul>
        `;
        outputElement.innerHTML = utmMessage;
    } else {
        // Default message if no UTM parameters are found
        outputElement.innerHTML = '<p>No UTM parameters found.</p>';
    }
}

// Ensure the DOM is fully loaded before executing the script
document.addEventListener('DOMContentLoaded', (event) => {
    try {
        displayContentBasedOnUTM();
    } catch (error) {
        console.error('Error displaying UTM parameters:', error);
    }
});
```

<!-- HTML sample to use with the above JavaScript code -->
<!-- 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UTM Display Example</title>
    <script src="path/to/your/javascript/file.js" defer></script>
</head>
<body>
    <div id="utm-output"></div>
</body>
</html>
 -->
