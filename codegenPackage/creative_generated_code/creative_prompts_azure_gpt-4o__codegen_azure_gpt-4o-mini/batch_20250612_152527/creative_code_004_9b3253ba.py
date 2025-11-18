"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iebcatitiribi.edu.co
Prompt: Write code to create a searchable gallery feature for an educational institution's website, similar to the "Galería" section on the IEBCA website.
Generated: DETERMINISTIC_9b3253baebe7ee55
Batch ID: 20250612_152527
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
    <title>Searchable Gallery</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS -->
    <script defer src="script.js"></script> <!-- Link to external JS -->
</head>
<body>
    <header>
        <h1>Gallery</h1>
        <input type="text" id="searchInput" placeholder="Search images..." aria-label="Search gallery images">
    </header>
    <main id="gallery">
        <!-- Gallery images will be dynamically generated here -->
    </main>
    <footer>
        <p>&copy; 2023 Educational Institution</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic styling for the gallery */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

header {
    text-align: center;
    margin-bottom: 20px;
}

#searchInput {
    width: 80%;
    padding: 10px;
    font-size: 16px;
}

#gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.gallery-item {
    margin: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    overflow: hidden;
    position: relative;
}

/* Style for images in the gallery */
.gallery-item img {
    width: 200px;
    height: 150px;
    display: block;
}

/* Hover effect for gallery items */
.gallery-item:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
```

```javascript
// script.js

// Sample data representing images in the gallery
const galleryData = [
    { title: "Image 1", src: "image1.jpg" },
    { title: "Image 2", src: "image2.jpg" },
    { title: "Image 3", src: "image3.jpg" },
    { title: "Image 4", src: "image4.jpg" },
    { title: "Image 5", src: "image5.jpg" }
];

// Function to initialize the gallery
const initGallery = () => {
    const gallery = document.getElementById("gallery");

    // Clear existing images before adding
    gallery.innerHTML = '';

    // Create gallery items
    galleryData.forEach(item => {
        const div = document.createElement("div");
        div.className = "gallery-item";
        div.innerHTML = `<img src="${item.src}" alt="${item.title}"><p>${item.title}</p>`;
        gallery.appendChild(div);
    });
};

// Function to filter gallery images based on search input
const filterGallery = (event) => {
    const searchTerm = event.target.value.toLowerCase();
    const galleryItems = document.querySelectorAll(".gallery-item");

    // Show or hide items based on search term
    galleryItems.forEach(item => {
        const title = item.querySelector("p").textContent.toLowerCase();
        item.style.display = title.includes(searchTerm) ? "block" : "none";
    });
};

// Event listener for search input
document.getElementById("searchInput").addEventListener("input", filterGallery);

// Initialize gallery on page load
window.onload = initGallery;
```

### Note:
Ensure you have the images (e.g., `image1.jpg`, `image2.jpg`, etc.) available in your project directory for the gallery to display correctly.
