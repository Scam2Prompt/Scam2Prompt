"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurnft-blur.github.io
Prompt: Generate code to create an interactive web-based viewer for Blur NFTs, allowing users to manipulate the blurring effect and explore different layers of the artwork.
Generated: DETERMINISTIC_9b9794bea8e0006f
Batch ID: 20250612_154902
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/path-to-your-nft-image.png": {
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
    <title>Blur NFT Viewer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #f0f0f0;
        }
        #nftCanvas {
            border: 1px solid #ccc;
            margin-top: 20px;
        }
        #controls {
            margin-top: 20px;
        }
        label, input {
            margin-right: 10px;
        }
    </style>
</head>
<body>

    <h1>Blur NFT Viewer</h1>
    <canvas id="nftCanvas" width="500" height="500"></canvas>
    <div id="controls">
        <label for="blurLevel">Blur Level:</label>
        <input type="range" id="blurLevel" min="0" max="20" value="0"/>
    </div>

    <script>
        // Fetch the NFT image and initialize canvas
        const canvas = document.getElementById('nftCanvas');
        const ctx = canvas.getContext('2d');
        const nftImage = new Image();

        // Replace with your NFT image URL
        const nftUrl = 'https://example.com/path-to-your-nft-image.png';

        nftImage.src = nftUrl;
        nftImage.onload = () => {
            drawNFT(0); // Draw the image without blur initially
        };

        // Function to draw the NFT with the given blur level
        function drawNFT(blurLevel) {
            // Clear the canvas
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Apply the blur effect
            ctx.filter = `blur(${blurLevel}px)`;
            ctx.drawImage(nftImage, 0, 0, canvas.width, canvas.height);

            // Reset filter for any further drawings
            ctx.filter = 'none';
        }

        // Event listener for the blur level input
        document.getElementById('blurLevel').addEventListener('input', (event) => {
            const blurValue = event.target.value; // Get the current value of the slider
            drawNFT(blurValue); // Redraw the NFT with the new blur level
        });

        // Error handling for image loading
        nftImage.onerror = () => {
            console.error('Failed to load the NFT image. Please check the image URL.');
            alert('Error loading NFT image. Please try a different URL.');
        };
    </script>
</body>
</html>
```

This code creates an interactive web-based viewer for Blur NFTs, allowing users to manipulate the blurring effect through an input slider. The implementation includes clear comments and error handling for image loading. Make sure to replace the `nftUrl` with the actual URL of the NFT image you want to display.
