"""
Generated Code Metadata:
========================
Original URL: https://shishehbalkon.ir
Prompt: "Develop a ReactJS component to display a gallery of images showcasing various glass balcony and shower cabin projects completed by Akbarzadeh."
Generated: DETERMINISTIC_68a05c782929a883
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './Gallery.css';

/**
 * Gallery component to display images of glass balcony and shower cabin projects.
 * @param {Object} props - Component props.
 * @param {Array} props.images - Array of image objects to display.
 * @param {string} props.title - Title for the gallery section.
 */
const Gallery = ({ images, title }) => {
  const [currentImageIndex, setCurrentImageIndex] = useState(0);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Preload images for better user experience
    const loadImages = async () => {
      try {
        await Promise.all(
          images.map((img) => {
            return new Promise((resolve, reject) => {
              const image = new Image();
              image.src = img.url;
              image.onload = resolve;
              image.onerror = reject;
            });
          })
        );
        setLoading(false);
      } catch (error) {
        console.error('Error loading images:', error);
        setLoading(false);
      }
    };

    loadImages();
  }, [images]);

  const handleNext = () => {
    setCurrentImageIndex((prevIndex) =>
      prevIndex === images.length - 1 ? 0 : prevIndex + 1
    );
  };

  const handlePrev = () => {
    setCurrentImageIndex((prevIndex) =>
      prevIndex === 0 ? images.length - 1 : prevIndex - 1
    );
  };

  const openModal = (index) => {
    setCurrentImageIndex(index);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  if (loading) {
    return <div className="gallery-loading">Loading gallery...</div>;
  }

  if (!images || images.length === 0) {
    return <div className="gallery-error">No images to display</div>;
  }

  return (
    <section className="gallery-container">
      <h2 className="gallery-title">{title}</h2>
      
      <div className="gallery-grid">
        {images.map((image, index) => (
          <div 
            key={image.id} 
            className="gallery-item"
            onClick={() => openModal(index)}
          >
            <img
              src={image.url}
              alt={image.alt || `Project ${index + 1}`}
              className="gallery-thumbnail"
              loading="lazy"
            />
            {image.caption && (
              <div className="gallery-caption">{image.caption}</div>
            )}
          </div>
        ))}
      </div>

      {isModalOpen && (
        <div className="gallery-modal">
          <div className="modal-content">
            <span className="close-button" onClick={closeModal}>&times;</span>
            <img
              src={images[currentImageIndex].url}
              alt={images[currentImageIndex].alt || `Project ${currentImageIndex + 1}`}
              className="modal-image"
            />
            <div className="modal-navigation">
              <button onClick={handlePrev} className="nav-button">❮</button>
              <button onClick={handleNext} className="nav-button">❯</button>
            </div>
            {images[currentImageIndex].description && (
              <div className="modal-description">
                {images[currentImageIndex].description}
              </div>
            )}
          </div>
        </div>
      )}
    </section>
  );
};

Gallery.propTypes = {
  images: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      url: PropTypes.string.isRequired,
      alt: PropTypes.string,
      caption: PropTypes.string,
      description: PropTypes.string,
    })
  ).isRequired,
  title: PropTypes.string.isRequired,
};

export default Gallery;
```

```css
/* Gallery.css */
.gallery-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.gallery-title {
  text-align: center;
  margin-bottom: 2rem;
  color: #333;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
}

.gallery-item {
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.gallery-item:hover {
  transform: scale(1.03);
}

.gallery-thumbnail {
  width: 100%;
  height: 200px;
  object-fit: cover;
  display: block;
}

.gallery-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 0.5rem;
  text-align: center;
}

.gallery-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.9);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  position: relative;
  max-width: 90%;
  max-height: 90%;
}

.modal-image {
  max-width: 100%;
  max-height: 80vh;
  display: block;
  margin: 0 auto;
}

.close-button {
  position: absolute;
  top: -40px;
  right: 0;
  color: white;
  font-size: 2rem;
  cursor: pointer;
}

.modal-navigation {
  display: flex;
  justify-content: space-between;
  margin-top: 1rem;
}

.nav-button {
  background: none;
  border: none;
  color: white;
  font-size: 2rem;
  cursor: pointer;
  padding: 0 1rem;
}

.modal-description {
  color: white;
  text-align: center;
  margin-top: 1rem;
  padding: 0.5rem;
  background: rgba(0, 0, 0, 0.5);
  border-radius: 4px;
}

.gallery-loading,
.gallery-error {
  text-align: center;
  padding: 2rem;
  font-size: 1.2rem;
  color: #666;
}
```
