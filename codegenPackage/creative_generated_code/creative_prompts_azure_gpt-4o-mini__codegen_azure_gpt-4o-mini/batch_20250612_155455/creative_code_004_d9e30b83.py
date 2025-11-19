"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stether.net
Prompt: Create a sample HTML code for a Clickadu banner ad (300x250) that can be embedded on a publisher's website.
Generated: DETERMINISTIC_d9e30b83d64cfdd2
Batch ID: 20250612_155455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clickadu Banner Ad Example</title>
    <style>
        /* Ensure the ad container is centered on the page */
        .ad-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh; /* Full viewport height for demonstration */
        }

        /* Style for the banner ad */
        .banner-ad {
            width: 300px; /* Ad width */
            height: 250px; /* Ad height */
            border: 1px solid #ccc; /* Optional border for visibility */
            overflow: hidden; /* Ensures content does not overflow */
        }
    </style>
</head>
<body>

    <div class="ad-container">
        <!-- Clickadu banner ad embed code -->
        <div class="banner-ad">
            <script async src="//cdn.clickadu.com/ads.js"></script>
            <!-- Replace 'your-ad-id' with the actual ad ID provided by Clickadu -->
            <div id="clickadu-ad" data-ad-id="your-ad-id" data-ad-width="300" data-ad-height="250"></div>
            <script>
                // Initialize the Clickadu ad
                try {
                    if (window.Clickadu) {
                        Clickadu.renderAd('clickadu-ad');
                    } else {
                        throw new Error('Clickadu library not loaded.');
                    }
                } catch (error) {
                    console.error('Error rendering Clickadu ad:', error);
                    // Optionally display a fallback message or image
                    document.getElementById('clickadu-ad').innerText = 'Ad failed to load. Please check back later.';
                }
            </script>
        </div>
    </div>

</body>
</html>
```
