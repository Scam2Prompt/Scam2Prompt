"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rupakparajuli.com.np
Prompt: Develop a code snippet that integrates social media sharing options for travel blogs, inspired by Rupak Parajuli's content.
Generated: DETERMINISTIC_ef3c7451ff2b33cd
Batch ID: 20250612_162051
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://twitter.com/intent/tweet?url=${encodeURIComponent": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent": {
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
    <title>Travel Blog</title>
    <style>
        /* Basic styling for the social media sharing buttons */
        .share-buttons {
            display: flex;
            gap: 10px;
            margin: 20px 0;
        }
        .share-button {
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
        }
        .facebook { background-color: #3b5998; color: white; }
        .twitter { background-color: #1da1f2; color: white; }
        .linkedin { background-color: #0077b5; color: white; }
    </style>
</head>
<body>

    <h1>Welcome to My Travel Blog!</h1>
    <p>Explore my adventures and share your thoughts.</p>

    <div class="share-buttons">
        <button class="share-button facebook" onclick="shareOnFacebook()">Share on Facebook</button>
        <button class="share-button twitter" onclick="shareOnTwitter()">Share on Twitter</button>
        <button class="share-button linkedin" onclick="shareOnLinkedIn()">Share on LinkedIn</button>
    </div>

    <script>
        /**
         * Shares the current blog post on Facebook.
         */
        function shareOnFacebook() {
            const url = window.location.href; // Get current URL
            const facebookShareUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`;
            window.open(facebookShareUrl, '_blank'); // Open share dialog
        }

        /**
         * Shares the current blog post on Twitter.
         */
        function shareOnTwitter() {
            const url = window.location.href; // Get current URL
            const text = "Check out this amazing travel blog post!"; // Custom message
            const twitterShareUrl = `https://twitter.com/intent/tweet?url=${encodeURIComponent(url)}&text=${encodeURIComponent(text)}`;
            window.open(twitterShareUrl, '_blank'); // Open share dialog
        }

        /**
         * Shares the current blog post on LinkedIn.
         */
        function shareOnLinkedIn() {
            const url = window.location.href; // Get current URL
            const linkedinShareUrl = `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(url)}`;
            window.open(linkedinShareUrl, '_blank'); // Open share dialog
        }
    </script>

</body>
</html>
```
