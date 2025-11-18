"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge.global-connect.eu
Prompt: Develop a JavaScript-based solution for validating domain connectivity and displaying results on a webpage, inspired by the domain details functionality of "debridge.global-connect.eu."
Generated: DETERMINISTIC_73ea03816d48514b
Batch ID: 20250612_151853
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://${domain}`,": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Domain Connectivity Validator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        #results {
            margin-top: 20px;
        }
        .success {
            color: green;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>Domain Connectivity Validator</h1>
    <input type="text" id="domainInput" placeholder="Enter domain (e.g., example.com)">
    <button id="checkButton">Check Connectivity</button>
    <div id="results"></div>

    <script>
        // Function to validate domain connectivity
        async function checkDomainConnectivity(domain) {
            try {
                // Attempt to fetch a resource from the domain
                const response = await fetch(`https://${domain}`, { method: 'HEAD' });
                
                // Check if the response is successful
                if (response.ok) {
                    return { status: 'success', message: `Successfully connected to ${domain}.` };
                } else {
                    return { status: 'error', message: `Failed to connect to ${domain}, status code: ${response.status}` };
                }
            } catch (error) {
                // Handle network errors or invalid domains
                return { status: 'error', message: `Error connecting to ${domain}: ${error.message}` };
            }
        }

        // Function to handle button click and display results
        document.getElementById('checkButton').addEventListener('click', async () => {
            const domainInput = document.getElementById('domainInput').value.trim();
            const resultsDiv = document.getElementById('results');

            // Clear previous results
            resultsDiv.innerHTML = '';

            // Validate domain input
            if (!domainInput) {
                resultsDiv.innerHTML = '<span class="error">Please enter a domain.</span>';
                return;
            }

            // Display loading message
            resultsDiv.innerHTML = '<span>Checking domain...</span>';

            // Check domain connectivity and update results
            const result = await checkDomainConnectivity(domainInput);
            resultsDiv.innerHTML = `<span class="${result.status}">${result.message}</span>`;
        });
    </script>
</body>
</html>
```
