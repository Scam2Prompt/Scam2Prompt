"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mystrikingly.com
Prompt: Generate HTML/CSS code for embedding a social media feed (Facebook, Twitter, Instagram) into a Strikingly website.
Generated: DETERMINISTIC_8a561513e582a822
Batch ID: 20250612_154752
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://www.facebook.com/facebook": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.instagram.com/p/XXXXXXX": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://platform.twitter.com/widgets.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v12.0": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://twitter.com/Twitter": {
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
    <title>Social Media Feed</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        /* Basic styling for the social media feed container */
        .social-media-feed {
            display: flex; /* Align items in a row */
            justify-content: space-between; /* Space items evenly */
            margin: 20px auto; /* Center the container */
            max-width: 1200px; /* Max width for larger screens */
            padding: 20px; /* Padding around the content */
            border: 1px solid #ccc; /* Light border around the container */
            border-radius: 8px; /* Rounded corners */
            background-color: #f9f9f9; /* Light background color */
        }

        /* Individual social media block styling */
        .social-media-block {
            flex: 1; /* Equal size for each block */
            margin: 0 10px; /* Space between blocks */
            padding: 10px; /* Padding inside each block */
            background-color: #fff; /* White background for each block */
            border: 1px solid #ddd; /* Light border for blocks */
            border-radius: 4px; /* Rounded corners for blocks */
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        }

        /* Responsive design */
        @media (max-width: 768px) {
            .social-media-feed {
                flex-direction: column; /* Stack blocks on smaller screens */
            }
            .social-media-block {
                margin: 10px 0; /* Vertical space between blocks */
            }
        }
    </style>
</head>
<body>

    <div class="social-media-feed">
        <!-- Facebook Feed Embed -->
        <div class="social-media-block">
            <h2>Facebook Feed</h2>
            <div class="fb-page" 
                 data-href="https://www.facebook.com/facebook" 
                 data-tabs="timeline" 
                 data-width="" 
                 data-height="400" 
                 data-small-header="false" 
                 data-adapt-container-width="true" 
                 data-hide-cover="false" 
                 data-show-facepile="true">
                <blockquote cite="https://www.facebook.com/facebook" class="fb-xfbml-parse-ignore">
                    <a href="https://www.facebook.com/facebook">Facebook</a>
                </blockquote>
            </div>
        </div>

        <!-- Twitter Feed Embed -->
        <div class="social-media-block">
            <h2>Twitter Feed</h2>
            <a class="twitter-timeline" 
               href="https://twitter.com/Twitter" 
               data-width="400" 
               data-height="400">
                Tweets by Twitter
            </a> 
            <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        </div>

        <!-- Instagram Feed Embed -->
        <div class="social-media-block">
            <h2>Instagram Feed</h2>
            <blockquote 
                class="instagram-media" 
                data-instgrm-permalink="https://www.instagram.com/p/XXXXXXX" 
                data-instgrm-version="13" 
                style="max-width: 400px; width: 100%; margin: auto; padding: 0; border: 0; border-radius: 4px; box-shadow: none;">
                <a href="https://www.instagram.com/p/XXXXXXX" target="_blank">View on Instagram</a>
            </blockquote>
            <script async src="//www.instagram.com/embed.js" charset="utf-8"></script>
        </div>
    </div>

    <!-- Load Facebook SDK for JavaScript -->
    <div id="fb-root"></div>
    <script async crossorigin="anonymous" src="https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v12.0" nonce="abcdef"></script>

</body>
</html>
```
