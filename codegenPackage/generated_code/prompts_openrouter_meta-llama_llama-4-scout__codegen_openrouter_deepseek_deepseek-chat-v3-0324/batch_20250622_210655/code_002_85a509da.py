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
/**
 * Simple Before-and-After Gallery for Hair & Makeup Services
 * Features:
 * - Responsive grid layout
 * - Image hover effects
 * - Lightbox for detailed view
 */

// Gallery data - replace with your actual images
const galleryData = [
  {
    id: 1,
    before: 'images/before1.jpg',
    after: 'images/after1.jpg',
    title: 'Bridal Makeover',
    description: 'Complete bridal transformation with natural look'
  },
  {
    id: 2,
    before: 'images/before2.jpg',
    after: 'images/after2.jpg',
    title: 'Hair Color Refresh',
    description: 'From faded color to vibrant blonde balayage'
  },
  {
    id: 3,
    before: 'images/before3.jpg',
    after: 'images/after3.jpg',
    title: 'Evening Glam',
    description: 'Day to night makeup transformation'
  }
];

document.addEventListener('DOMContentLoaded', () => {
  const galleryContainer = document.getElementById('gallery');
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightbox-img');
  const lightboxTitle = document.getElementById('lightbox-title');
  const lightboxDesc = document.getElementById('lightbox-desc');
  const closeBtn = document.querySelector('.close-btn');

  // Create gallery items
  function createGallery() {
    galleryData.forEach(item => {
      const galleryItem = document.createElement('div');
      galleryItem.className = 'gallery-item';
      galleryItem.dataset.id = item.id;

      galleryItem.innerHTML = `
        <div class="image-container">
          <img src="${item.before}" alt="Before ${item.title}" class="before-image">
          <img src="${item.after}" alt="After ${item.title}" class="after-image">
          <div class="overlay">
            <h3>${item.title}</h3>
            <p>${item.description}</p>
          </div>
        </div>
      `;

      galleryItem.addEventListener('click', () => openLightbox(item));
      galleryContainer.appendChild(galleryItem);
    });
  }

  // Open lightbox with selected image
  function openLightbox(item) {
    lightboxImg.src = item.after;
    lightboxTitle.textContent = item.title;
    lightboxDesc.textContent = item.description;
    lightbox.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }

  // Close lightbox
  function closeLightbox() {
    lightbox.style.display = 'none';
    document.body.style.overflow = 'auto';
  }

  // Event listeners
  closeBtn.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) closeLightbox();
  });

  // Initialize gallery
  createGallery();
});

// CSS should be added separately - here's the minimal required structure:
/*
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  padding: 20px;
}

.gallery-item {
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  cursor: pointer;
}

.image-container {
  position: relative;
  height: 0;
  padding-bottom: 100%;
}

.image-container img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: opacity 0.3s ease;
}

.after-image {
  opacity: 0;
}

.gallery-item:hover .after-image {
  opacity: 1;
}

.overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0,0,0,0.7);
  color: white;
  padding: 15px;
  transform: translateY(100%);
  transition: transform 0.3s ease;
}

.gallery-item:hover .overlay {
  transform: translateY(0);
}

.lightbox {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.9);
  z-index: 1000;
  justify-content: center;
  align-items: center;
}

.lightbox-content {
  max-width: 80%;
  max-height: 80%;
  position: relative;
}

.close-btn {
  position: absolute;
  top: 20px;
  right: 20px;
  color: white;
  font-size: 30px;
  cursor: pointer;
}
*/
```
