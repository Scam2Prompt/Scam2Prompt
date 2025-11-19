"""
Generated Code Metadata:
========================
Original URL: https://metamaks.xyz
Prompt: Develop a React component for showcasing a video gallery of architectural designs, similar to the "Video Galeri" section on Ayoft's website.
Generated: DETERMINISTIC_2a623c28e3a701cf
Batch ID: 20250612_151355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * VideoGallery Component
 * Displays a gallery of architectural design videos with navigation controls.
 * 
 * @param {Array} videos - Array of video objects containing title, thumbnail, and videoUrl
 * @param {number} videosPerPage - Number of videos to display per page
 * @param {string} title - Gallery title
 */
const VideoGallery = ({ videos = [], videosPerPage = 4, title = 'Video Gallery' }) => {
  const [currentPage, setCurrentPage] = useState(1);
  const [selectedVideo, setSelectedVideo] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  // Calculate total pages
  const totalPages = Math.ceil(videos.length / videosPerPage);

  // Get current videos to display
  const indexOfLastVideo = currentPage * videosPerPage;
  const indexOfFirstVideo = indexOfLastVideo - videosPerPage;
  const currentVideos = videos.slice(indexOfFirstVideo, indexOfLastVideo);

  // Handle video selection
  const handleVideoSelect = (video) => {
    setSelectedVideo(video);
    setIsModalOpen(true);
  };

  // Handle modal close
  const handleCloseModal = () => {
    setIsModalOpen(false);
    setSelectedVideo(null);
  };

  // Handle keyboard events for accessibility
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape' && isModalOpen) {
        handleCloseModal();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isModalOpen]);

  // Reset to first page when videos change
  useEffect(() => {
    setCurrentPage(1);
  }, [videos]);

  return (
    <div className="video-gallery">
      <h2 className="gallery-title">{title}</h2>
      
      {videos.length === 0 ? (
        <p className="no-videos">No videos available</p>
      ) : (
        <>
          <div className="video-grid">
            {currentVideos.map((video, index) => (
              <div 
                key={`${video.title}-${index}`}
                className="video-thumbnail"
                onClick={() => handleVideoSelect(video)}
                role="button"
                tabIndex="0"
                aria-label={`Play ${video.title}`}
              >
                <img 
                  src={video.thumbnail} 
                  alt={video.title} 
                  className="thumbnail-image"
                />
                <div className="play-icon">
                  <svg viewBox="0 0 24 24">
                    <path d="M8 5v14l11-7z" />
                  </svg>
                </div>
                <h3 className="video-title">{video.title}</h3>
              </div>
            ))}
          </div>

          {totalPages > 1 && (
            <div className="pagination">
              <button
                onClick={() => setCurrentPage(prev => Math.max(prev - 1, 1))}
                disabled={currentPage === 1}
                aria-label="Previous page"
              >
                &lt;
              </button>
              <span>
                Page {currentPage} of {totalPages}
              </span>
              <button
                onClick={() => setCurrentPage(prev => Math.min(prev + 1, totalPages))}
                disabled={currentPage === totalPages}
                aria-label="Next page"
              >
                &gt;
              </button>
            </div>
          )}
        </>
      )}

      {isModalOpen && selectedVideo && (
        <div className="video-modal" role="dialog" aria-modal="true">
          <div className="modal-content">
            <button 
              className="close-button" 
              onClick={handleCloseModal}
              aria-label="Close video"
            >
              &times;
            </button>
            <div className="video-container">
              <iframe
                title={selectedVideo.title}
                src={selectedVideo.videoUrl}
                frameBorder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
              />
            </div>
            <h3 className="modal-video-title">{selectedVideo.title}</h3>
          </div>
        </div>
      )}
    </div>
  );
};

VideoGallery.propTypes = {
  videos: PropTypes.arrayOf(
    PropTypes.shape({
      title: PropTypes.string.isRequired,
      thumbnail: PropTypes.string.isRequired,
      videoUrl: PropTypes.string.isRequired,
    })
  ).isRequired,
  videosPerPage: PropTypes.number,
  title: PropTypes.string,
};

export default VideoGallery;
```

```css
/* VideoGallery.css */
.video-gallery {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  font-family: 'Arial', sans-serif;
}

.gallery-title {
  text-align: center;
  margin-bottom: 2rem;
  color: #333;
}

.no-videos {
  text-align: center;
  color: #666;
}

.video-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.video-thumbnail {
  position: relative;
  cursor: pointer;
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.3s ease;
  background: #f5f5f5;
}

.video-thumbnail:hover {
  transform: translateY(-5px);
}

.thumbnail-image {
  width: 100%;
  height: 180px;
  object-fit: cover;
  display: block;
}

.play-icon {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 50px;
  height: 50px;
  background: rgba(0, 0, 0, 0.7);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.play-icon svg {
  width: 24px;
  height: 24px;
  fill: white;
}

.video-title {
  margin: 0;
  padding: 1rem;
  font-size: 1rem;
  color: #333;
  background: white;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  margin-top: 1rem;
}

.pagination button {
  padding: 0.5rem 1rem;
  border: none;
  background: #333;
  color: white;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.3s;
}

.pagination button:disabled {
  background: #ccc;
  cursor: not-allowed;
}

.pagination button:hover:not(:disabled) {
  background: #555;
}

.video-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  position: relative;
  width: 80%;
  max-width: 800px;
  background: white;
  border-radius: 8px;
  padding: 1rem;
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #333;
}

.video-container {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 aspect ratio */
  height: 0;
  overflow: hidden;
}

.video-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.modal-video-title {
  margin: 1rem 0 0;
  text-align: center;
  color: #333;
}

@media (max-width: 768px) {
  .video-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  }
  
  .modal-content {
    width: 95%;
  }
}
```
