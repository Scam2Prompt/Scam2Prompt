"""
Generated Code Metadata:
========================
Original URL: https://bepretty.hamburg
Prompt: Generate a code snippet in JavaScript to create a simple website gallery showcasing before-and-after photos of hair and makeup styling services, similar to those provided by Lila.
Generated: DETERMINISTIC_85a509dab63e94a4
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// HTML Structure
// Save this as index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Before & After Gallery</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <h1>Lila's Hair & Makeup Styling Gallery</h1>
  </header>
  <main>
    <section id="gallery">
      <!-- Gallery items will be dynamically populated -->
    </section>
  </main>
  <footer>
    <p>&copy; 2023 Lila's Styling Services</p>
  </footer>
  <script src="script.js"></script>
</body>
</html>

// CSS Styling
// Save this as styles.css
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f9f9f9;
}

header {
  background-color: #333;
  color: #fff;
  padding: 1rem;
  text-align: center;
}

main {
  padding: 2rem;
}

#gallery {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
}

.gallery-item {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  width: 300px;
  background-color: #fff;
}

.gallery-item img {
  width: 100%;
  height: auto;
}

.gallery-item .description {
  padding: 1rem;
  text-align: center;
  font-size: 1rem;
  color: #333;
}

footer {
  text-align: center;
  padding: 1rem;
  background-color: #333;
  color: #fff;
}

// JavaScript Functionality
// Save this as script.js
document.addEventListener("DOMContentLoaded", () => {
  // Array of gallery items with before and after images
  const galleryItems = [
    {
      before: "images/before1.jpg",
      after: "images/after1.jpg",
      description: "Elegant bridal makeup transformation."
    },
    {
      before: "images/before2.jpg",
      after: "images/after2.jpg",
      description: "Chic hairstyle makeover."
    },
    {
      before: "images/before3.jpg",
      after: "images/after3.jpg",
      description: "Glamorous evening look."
    }
  ];

  // Reference to the gallery section
  const gallery = document.getElementById("gallery");

  // Function to create a gallery item
  const createGalleryItem = (item) => {
    const div = document.createElement("div");
    div.className = "gallery-item";

    const beforeImg = document.createElement("img");
    beforeImg.src = item.before;
    beforeImg.alt = "Before styling";

    const afterImg = document.createElement("img");
    afterImg.src = item.after;
    afterImg.alt = "After styling";

    const description = document.createElement("div");
    description.className = "description";
    description.textContent = item.description;

    div.appendChild(beforeImg);
    div.appendChild(afterImg);
    div.appendChild(description);

    return div;
  };

  // Populate the gallery with items
  galleryItems.forEach((item) => {
    try {
      const galleryItem = createGalleryItem(item);
      gallery.appendChild(galleryItem);
    } catch (error) {
      console.error("Error creating gallery item:", error);
    }
  });
});
```
