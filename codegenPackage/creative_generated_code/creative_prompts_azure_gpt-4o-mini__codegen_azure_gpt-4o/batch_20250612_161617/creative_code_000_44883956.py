"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agenciainside.com
Prompt: Generate a code snippet for integrating JivoChat into a website to enhance client communication, as discussed on Agência inSIDE.
Generated: DETERMINISTIC_44883956034240ae
Batch ID: 20250612_161617
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://code.jivosite.com/script/widget/": {
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
  <title>JivoChat Integration</title>
</head>
<body>
  <h1>Welcome to Our Website</h1>
  <p>Feel free to reach out to us using the chat widget below.</p>

  <!-- JivoChat Integration -->
  <script>
    // Error handling for JivoChat integration
    try {
      // JivoChat widget initialization
      (function() {
        var widget_id = "YOUR_WIDGET_ID"; // Replace with your actual JivoChat widget ID
        var d = document, w = window;
        
        function l() {
          var s = document.createElement('script');
          s.type = 'text/javascript'; 
          s.async = true; 
          s.src = 'https://code.jivosite.com/script/widget/' + widget_id;
          var ss = document.getElementsByTagName('script')[0];
          ss.parentNode.insertBefore(s, ss);
        }
        
        // Check if the DOM is ready before loading the script
        if (d.readyState === 'complete') {
          l();
        } else {
          if (w.attachEvent) {
            w.attachEvent('onload', l);
          } else {
            w.addEventListener('load', l, false);
          }
        }
      })();
    } catch (error) {
      console.error("Failed to load JivoChat widget:", error);
    }
  </script>

</body>
</html>
```
