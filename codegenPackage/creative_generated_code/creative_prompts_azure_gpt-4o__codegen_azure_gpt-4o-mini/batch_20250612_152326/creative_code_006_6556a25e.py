"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rider-ad6.pages.dev
Prompt: Develop a code snippet to integrate Spotify links for content creators on an NFT-focused website, similar to the "Listen on Spotify" feature mentioned on NFT Daily.
Generated: DETERMINISTIC_6556a25ee25c0703
Batch ID: 20250612_152326
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
    <title>NFT Creator Spotify Integration</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="nft-creator">
        <h1>NFT Creator Profile</h1>
        <p>Discover more about our NFT creators and their music!</p>
        
        <!-- Spotify Link Section -->
        <div class="spotify-link">
            <h2>Listen on Spotify</h2>
            <input type="url" id="spotifyUrl" placeholder="Enter Spotify URL" required>
            <button id="openSpotifyBtn">Open Spotify</button>
        </div>
    </div>

    <script>
        // Function to validate and open Spotify link
        function openSpotify() {
            const urlInput = document.getElementById('spotifyUrl');
            const url = urlInput.value.trim();

            // Regular expression to validate Spotify URL
            const spotifyUrlPattern = /^(https?:\/\/)?(www\.)?(spotify\.com|open\.spotify\.com)\/.+/;

            // Check if the URL matches the Spotify format
            if (spotifyUrlPattern.test(url)) {
                window.open(url, '_blank'); // Open the URL in a new tab
            } else {
                alert('Please enter a valid Spotify link.'); // Error message for invalid URL
            }
        }

        // Event listener for the button click
        document.getElementById('openSpotifyBtn').addEventListener('click', openSpotify);
    </script>

    <style>
        /* Basic styling for the NFT creator section */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }

        .nft-creator {
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .spotify-link {
            margin-top: 20px;
        }

        input[type="url"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button {
            background-color: #1DB954; /* Spotify green */
            color: white;
            border: none;
            padding: 10px;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            background-color: #1ed760; /* Darker green on hover */
        }
    </style>
</body>
</html>
```
