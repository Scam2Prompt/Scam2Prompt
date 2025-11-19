"""
Generated Code Metadata:
========================
Original URL: https://villaandreas.gr
Prompt: "Generate a code snippet in JavaScript to implement a gallery viewer similar to the one used on villaandreas.gr, showcasing images of a luxury villa in Kefalonia."
Generated: DETERMINISTIC_3ca321bc442f2ec4
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Luxury Villa Gallery</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="gallery-container">
        <div class="thumbnail-container">
            <!-- Thumbnails for the gallery -->
            <img src="image1_thumb.jpg" alt="Villa Image 1" class="thumbnail" data-full="image1.jpg">
            <img src="image2_thumb.jpg" alt="Villa Image 2" class="thumbnail" data-full="image2.jpg">
            <img src="image3_thumb.jpg" alt="Villa Image 3" class="thumbnail" data-full="image3.jpg">
            <img src="image4_thumb.jpg" alt="Villa Image 4" class="thumbnail" data-full="image4.jpg">
        </div>
        <div class="full-image-container">
            <!-- Full image display -->
            <img id="full-image" src="image1.jpg" alt="Full View of Villa" />
        </div>
    </div>

    <script>
        // Select all thumbnail images
        const thumbnails = document.querySelectorAll('.thumbnail');
        const fullImage = document.getElementById('full-image');

        // Function to handle thumbnail click
        function handleThumbnailClick(event) {
            // Prevent default action
            event.preventDefault();

            // Get the full image URL from the clicked thumbnail's data attribute
            const fullImageUrl = event.target.getAttribute('data-full');

            // Update the full image source
            fullImage.src = fullImageUrl;
        }

        // Add click event listeners to each thumbnail
        thumbnails.forEach(thumbnail => {
            thumbnail.addEventListener('click', handleThumbnailClick);
        });

        // Error handling for image loading
        fullImage.onerror = function() {
            console.error('Error loading image:', fullImage.src);
            fullImage.src = 'placeholder.jpg'; // Fallback image
        };
    </script>
    <style>
        /* Basic styles for the gallery */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .gallery-container {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .thumbnail-container {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
        .thumbnail {
            width: 100px;
            height: auto;
            margin: 0 10px;
            cursor: pointer;
            transition: transform 0.2s;
        }
        .thumbnail:hover {
            transform: scale(1.05);
        }
        .full-image-container {
            max-width: 800px;
            width: 100%;
        }
        #full-image {
            width: 100%;
            height: auto;
            border: 2px solid #ccc;
            border-radius: 8px;
        }
    </style>
</body>
</html>
```
