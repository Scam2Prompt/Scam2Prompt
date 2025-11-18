"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webstarstudio.com
Prompt: Provide code examples for embedding JivoSite chat functionality into a website, as mentioned in WebStar Studio's offerings.
Generated: DETERMINISTIC_f1246b5f483f636e
Batch ID: 20250612_150440
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://code.jivosite.com/widget/YOUR_WIDGET_ID": {
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
    <title>Website with JivoSite Chat</title>
</head>
<body>
    <!-- Main content of the website -->
    <h1>Welcome to Our Website!</h1>
    <p>Feel free to interact with us using the chat at the bottom right corner.</p>

    <!-- JivoSite Chat Widget Integration -->
    <script type="text/javascript">
        (function() {
            // Create a script element
            var widgetScript = document.createElement('script');

            // Set the type and async attributes for better performance
            widgetScript.type = 'text/javascript';
            widgetScript.async = true;

            // Provide the widget source URL (replace YOUR_WIDGET_ID with your actual widget ID)
            widgetScript.src = 'https://code.jivosite.com/widget/YOUR_WIDGET_ID';

            // Proper error handling for script loading
            widgetScript.onerror = function() {
                console.error('Failed to load JivoSite widget script.');
            };

            // Append the script to the document
            var firstScript = document.getElementsByTagName('script')[0];
            firstScript.parentNode.insertBefore(widgetScript, firstScript);
        })();
    </script>
    
    <!-- End of JivoSite Chat Widget Integration -->

</body>
</html>
```
