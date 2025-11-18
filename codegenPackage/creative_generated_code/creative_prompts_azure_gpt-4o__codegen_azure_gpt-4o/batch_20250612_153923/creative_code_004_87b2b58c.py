"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theog.io
Prompt: Provide code examples for embedding Senja testimonial widgets on a website, ensuring compatibility with custom templates.
Generated: DETERMINISTIC_87b2b58c5fdaf4fd
Batch ID: 20250612_153923
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://senja.io/widgets/v1/embed.js": {
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
<!-- HTML Example: Embedding Senja Testimonial Widget -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Senja Testimonial Widget</title>
  
  <!-- Optional: Custom CSS for styling widget compatibility -->
  <style>
    .testimonial-widget-container {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      background-color: #f9f9f9;
      border-radius: 10px;
      box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
  </style>
</head>
<body>
  
  <!-- Container for the Senja Testimonial Widget -->
  <div class="testimonial-widget-container">
    <!-- Senja Widget Embed Script -->
    <script src="https://senja.io/widgets/v1/embed.js" async></script>
    <!-- Replace `YOUR_WIDGET_ID` with your actual widget ID -->
    <div data-senja-widget="YOUR_WIDGET_ID"></div>
  </div>

  <!-- Fallback for Error Handling -->
  <noscript>
    <p>
      JavaScript is required to display this testimonial widget. Please enable JavaScript in your browser and refresh the page.
    </p>
  </noscript>
</body>
</html>
```
