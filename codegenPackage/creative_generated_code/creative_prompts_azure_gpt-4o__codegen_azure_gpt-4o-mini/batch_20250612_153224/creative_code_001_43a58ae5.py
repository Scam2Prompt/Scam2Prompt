"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hsrenterprises.co.in
Prompt: Generate a script to display a virtual tour of a Royal Enfield showroom using HTML and JavaScript, with interactive navigation features.
Generated: DETERMINISTIC_43a58ae5380f2798
Batch ID: 20250612_153224
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
    <title>Royal Enfield Showroom Virtual Tour</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            overflow: hidden;
        }
        #tour-container {
            position: relative;
            width: 100%;
            height: 100vh;
            background-color: #f4f4f4;
            overflow: hidden;
        }
        #image-display {
            width: 100%;
            height: 100%;
            background-size: cover;
            background-position: center;
            transition: background-image 0.5s ease;
        }
        .navigation {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            justify-content: space-between;
            width: 100%;
            padding: 10px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border: none;
            background-color: #007BFF;
            color: white;
            border-radius: 5px;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>

<div id="tour-container">
    <div id="image-display"></div>
    <div class="navigation">
        <button id="prevBtn">Previous</button>
        <button id="nextBtn">Next</button>
    </div>
</div>

<script>
    // Array of showroom images
    const showroomImages = [
        'image1.jpg', // Replace with actual image paths
        'image2.jpg',
        'image3.jpg',
        'image4.jpg'
    ];

    let currentImageIndex = 0; // Keep track of the current image index

    // Function to update the displayed image
    function updateImage() {
        const imageDisplay = document.getElementById('image-display');
        // Validate the current index
        if (currentImageIndex < 0 || currentImageIndex >= showroomImages.length) {
            console.error('Current image index is out of bounds.');
            return;
        }
        // Set the background image
        imageDisplay.style.backgroundImage = `url(${showroomImages[currentImageIndex]})`;
    }

    // Function to navigate to the next image
    function nextImage() {
        if (currentImageIndex < showroomImages.length - 1) {
            currentImageIndex++;
            updateImage();
        } else {
            alert('You are at the last image.');
        }
    }

    // Function to navigate to the previous image
    function previousImage() {
        if (currentImageIndex > 0) {
            currentImageIndex--;
            updateImage();
        } else {
            alert('You are at the first image.');
        }
    }

    // Event listeners for button clicks
    document.getElementById('nextBtn').addEventListener('click', nextImage);
    document.getElementById('prevBtn').addEventListener('click', previousImage);

    // Initialize the first image on page load
    window.onload = updateImage;
</script>

</body>
</html>
```
