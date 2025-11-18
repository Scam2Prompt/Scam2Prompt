"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaks.xyz
Prompt: Develop a React component for showcasing a video gallery of architectural designs, similar to the "Video Galeri" section on Ayoft's website.
Generated: DETERMINISTIC_2a623c28e3a701cf
Batch ID: 20250612_151355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState, useEffect } from "react";

// VideoGallery Component
const VideoGallery = ({ videoData }) => {
  // State for selected video
  const [selectedVideo, setSelectedVideo] = useState(null);

  // Error state
  const [error, setError] = useState(null);

  // Effect to handle initial video selection
  useEffect(() => {
    if (videoData && videoData.length > 0) {
      setSelectedVideo(videoData[0]); // Set the first video as the default
    } else {
      setError("No videos available.");
    }
  }, [videoData]);

  // Handler for selecting a video
  const handleVideoSelect = (video) => {
    setSelectedVideo(video);
  };

  return (
    <div className="video-gallery">
      <h2 className="gallery-title">Architectural Designs Video Gallery</h2>
      
      {/* Error Handling */}
      {error ? (
        <p className="error-message">{error}</p>
      ) : (
        <>
          {/* Video Player */}
          <div className="video-player">
            {selectedVideo ? (
              <video
                src={selectedVideo.url}
                controls
                className="main-video"
                alt={selectedVideo.title}
              />
            ) : (
              <p>Loading video...</p>
            )}
          </div>

          {/* Video Thumbnails */}
          <div className="video-thumbnails">
            {videoData.map((video, index) => (
              <div
                key={index}
                className={`thumbnail ${
                  selectedVideo && selectedVideo.url === video.url
                    ? "selected"
                    : ""
                }`}
                onClick={() => handleVideoSelect(video)}
              >
                <img
                  src={video.thumbnail}
                  alt={video.title}
                  className="thumbnail-image"
                />
                <p className="thumbnail-title">{video.title}</p>
              </div>
            ))}
          </div>
        </>
      )}
    </div>
  );
};

export default VideoGallery;

/*
 * Usage Example:
 * const videoData = [
 *   { url: "video1.mp4", thumbnail: "thumb1.jpg", title: "Design 1" },
 *   { url: "video2.mp4", thumbnail: "thumb2.jpg", title: "Design 2" },
 * ];
 * <VideoGallery videoData={videoData} />
 */

/*
 * CSS (to be added for styling):
 *
 * .video-gallery {
 *   padding: 20px;
 * }
 * .gallery-title {
 *   font-size: 24px;
 *   margin-bottom: 10px;
 * }
 * .video-player {
 *   margin-bottom: 20px;
 * }
 * .main-video {
 *   width: 100%;
 *   max-height: 500px;
 * }
 * .video-thumbnails {
 *   display: flex;
 *   flex-wrap: wrap;
 *   gap: 10px;
 * }
 * .thumbnail {
 *   cursor: pointer;
 *   border: 2px solid transparent;
 *   transition: border-color 0.3s;
 * }
 * .thumbnail.selected {
 *   border-color: #007bff;
 * }
 * .thumbnail-image {
 *   width: 150px;
 *   height: 100px;
 *   object-fit: cover;
 * }
 * .thumbnail-title {
 *   text-align: center;
 *   font-size: 14px;
 * }
 * .error-message {
 *   color: red;
 * }
 */
```
