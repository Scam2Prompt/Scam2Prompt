"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mystrikingly.com
Prompt: Create a code example for adding a social media feed to a Strikingly site, showcasing Facebook and Instagram posts.
Generated: DETERMINISTIC_7de59c3dfd9714dd
Batch ID: 20250612_161059
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.facebook.com/plugins/page.php?href=https%3A%2F%2Fwww.facebook.com%2FYourPageNameHere&tabs=timeline&width=300&height=400&small_header=true&adapt_container_width=true&hide_cover=false&show_facepile=true&appId=YourAppIDHere": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.instagram.com/p/YourPostIDHere/embed": {
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
    <style>
        /* Style for the social media feed container */
        .social-feed {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: center;
        }

        .feed-item {
            border: 1px solid #ddd;
            border-radius: 8px;
            overflow: hidden;
            width: 300px;
        }

        .feed-item iframe {
            width: 100%;
            border: none;
        }
    </style>
</head>
<body>
    <h1>Social Media Feed</h1>
    <p>Check out the latest posts from Facebook and Instagram!</p>

    <div class="social-feed">
        <!-- Facebook Page Plugin Embed -->
        <div class="feed-item" id="facebook-feed">
            <iframe 
                src="https://www.facebook.com/plugins/page.php?href=https%3A%2F%2Fwww.facebook.com%2FYourPageNameHere&tabs=timeline&width=300&height=400&small_header=true&adapt_container_width=true&hide_cover=false&show_facepile=true&appId=YourAppIDHere" 
                width="300" 
                height="400" 
                allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share">
            </iframe>
        </div>

        <!-- Instagram Embedded Embed -->
        <div class="feed-item" id="instagram-feed">
            <iframe 
                src="https://www.instagram.com/p/YourPostIDHere/embed" 
                width="300" 
                height="400">
            </iframe>
        </div>
    </div>

    <script>
        // Error handling for embedded iframes
        document.addEventListener('DOMContentLoaded', () => {
            const facebookFeed = document.getElementById('facebook-feed');
            const instagramFeed = document.getElementById('instagram-feed');

            if (!facebookFeed) {
                console.error('Facebook feed could not be loaded. Please check the Page URL and App ID.');
            }

            if (!instagramFeed) {
                console.error('Instagram feed could not be loaded. Please check the Post ID.');
            }
        });
    </script>
</body>
</html>
```

### Notes:
- Replace `YourPageNameHere` with the Facebook page username.
- Replace `YourAppIDHere` with your Facebook App ID.
- Replace `YourPostIDHere` with the specific Instagram post ID you'd like to showcase.

Ensure that you have the necessary permissions from Facebook and Instagram to embed these feeds.
