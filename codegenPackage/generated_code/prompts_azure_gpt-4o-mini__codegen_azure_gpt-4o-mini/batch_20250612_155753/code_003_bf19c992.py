"""
Generated Code Metadata:
========================
Original URL: https://hrtsforstrky.carrd.co
Prompt: Provide an example of how to embed Spotify and Instagram links on a Carrd page, inspired by the layout of HRTSFORSTRKY.
Generated: DETERMINISTIC_bf19c992fedcee36
Batch ID: 20250612_155753
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.instagram.com/YOUR_INSTAGRAM_HANDLE": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://open.spotify.com/embed/track/YOUR_TRACK_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Embed Spotify and Instagram</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .embed-container {
            margin: 20px;
            border: 1px solid #ccc;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        iframe {
            width: 300px;
            height: 380px;
            border: none;
        }
        .instagram-link {
            text-align: center;
            margin: 20px;
        }
    </style>
</head>
<body>

    <!-- Spotify Embed -->
    <div class="embed-container">
        <iframe src="https://open.spotify.com/embed/track/YOUR_TRACK_ID" 
                allow="encrypted-media" 
                title="Spotify Track Embed">
        </iframe>
    </div>

    <!-- Instagram Link -->
    <div class="instagram-link">
        <a href="https://www.instagram.com/YOUR_INSTAGRAM_HANDLE" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" 
                 alt="Instagram" 
                 width="50" height="50">
            <p>Follow us on Instagram</p>
        </a>
    </div>

    <script>
        // Error handling for iframe loading
        const iframe = document.querySelector('iframe');
        iframe.onload = function() {
            console.log('Spotify iframe loaded successfully.');
        };
        iframe.onerror = function() {
            console.error('Error loading Spotify iframe. Please check the track ID.');
        };
    </script>

</body>
</html>
```

**Note:** Replace `YOUR_TRACK_ID` with the actual Spotify track ID and `YOUR_INSTAGRAM_HANDLE` with your Instagram username.
