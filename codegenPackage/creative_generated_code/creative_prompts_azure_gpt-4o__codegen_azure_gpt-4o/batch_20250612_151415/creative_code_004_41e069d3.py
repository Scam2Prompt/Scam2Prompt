"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inbetweeners-blue.pages.dev
Prompt: Suggest a method to integrate DEXTools charts into a webpage, referencing the $BLUE inBetweeners project as an example.
Generated: DETERMINISTIC_41e069d3fba3da47
Batch ID: 20250612_151415
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.dextools.io/app/en/ether/pair-explorer/0x123456789abcdef0123456789abcdef": {
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
  <title>DEXTools Chart Integration</title>
  <style>
    /* Basic styling for iframe container */
    .chart-container {
      width: 100%;
      max-width: 800px;
      margin: 0 auto;
      border: 1px solid #ddd;
      border-radius: 8px;
      overflow: hidden;
    }

    iframe {
      width: 100%;
      height: 500px; /* Set height of the chart */
      border: none;
    }
  </style>
</head>
<body>
  <h1>DEXTools Chart Integration: $BLUE inBetweeners Project</h1>
  
  <!-- Container for the DEXTools chart -->
  <div class="chart-container">
    <!-- Embed the DEXTools chart via iframe -->
    <iframe 
      src="https://www.dextools.io/app/en/ether/pair-explorer/0x123456789abcdef0123456789abcdef" 
      title="DEXTools Chart for $BLUE inBetweeners Project"
      allowfullscreen>
    </iframe>
  </div>

  <script>
    // Example: Add error handling for iframe loading issues.
    document.querySelector('iframe').addEventListener('error', (event) => {
      console.error("Failed to load DEXTools chart:", event);
      alert("Failed to load the chart. Please check the URL or your network connection.");
    });
  </script>
</body>
</html>
```

Note:
- Replace `0x123456789abcdef0123456789abcdef` in the `src` attribute of the iframe with the actual pair address for the $BLUE inBetweeners project chart on DEXTools.
