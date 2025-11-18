"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meetagreatamerican.com
Prompt: Write code to integrate social media sharing buttons for promoting biographies and branding opportunities, similar to the features on "Meet A Great American."
Generated: DETERMINISTIC_a6f620c685e8be87
Batch ID: 20250612_145213
URLs Found: 4
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
  },
  "https://example.com/biography": {
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
    <title>Social Media Sharing Buttons</title>
    <style>
        /* Basic styling for the buttons */
        .social-share {
            display: inline-block;
            margin: 5px;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            color: white;
            text-decoration: none;
            font-weight: bold;
        }

        .facebook { background-color: #3b5998; }
        .twitter { background-color: #1da1f2; }
        .linkedin { background-color: #0077b5; }
        .email { background-color: #666; }
    </style>
</head>
<body>

    <h1>Promote Your Biography</h1>
    <p>Share this biography on your social media channels!</p>

    <div>
        <a href="#" id="facebook-share" class="social-share facebook" onclick="shareOnFacebook()">Share on Facebook</a>
        <a href="#" id="twitter-share" class="social-share twitter" onclick="shareOnTwitter()">Share on Twitter</a>
        <a href="#" id="linkedin-share" class="social-share linkedin" onclick="shareOnLinkedIn()">Share on LinkedIn</a>
        <a href="#" id="email-share" class="social-share email" onclick="shareViaEmail()">Share via Email</a>
    </div>

    <script>
        // URL and description to share
        const biographyURL = "https://example.com/biography";
        const biographyDescription = "Check out this amazing biography!";

        /**
         * Shares the biography on Facebook.
         */
        function shareOnFacebook() {
            const url = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(biographyURL)}`;
            window.open(url, 'Share on Facebook', 'width=600,height=400');
            return false; // Prevent default link behavior
        }

        /**
         * Shares the biography on Twitter.
         */
        function shareOnTwitter() {
            const url = `https://twitter.com/intent/tweet?url=${encodeURIComponent(biographyURL)}&text=${encodeURIComponent(biographyDescription)}`;
            window.open(url, 'Share on Twitter', 'width=600,height=400');
            return false; // Prevent default link behavior
        }

        /**
         * Shares the biography on LinkedIn.
         */
        function shareOnLinkedIn() {
            const url = `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(biographyURL)}`;
            window.open(url, 'Share on LinkedIn', 'width=600,height=400');
            return false; // Prevent default link behavior
        }

        /**
         * Shares the biography via Email.
         */
        function shareViaEmail() {
            const subject = "Check out this amazing biography!";
            const body = `Hey, I found this biography that you might like: ${biographyURL}`;
            const mailtoLink = `mailto:?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
            window.location.href = mailtoLink; // Open default email client
            return false; // Prevent default link behavior
        }
    </script>

</body>
</html>
```
