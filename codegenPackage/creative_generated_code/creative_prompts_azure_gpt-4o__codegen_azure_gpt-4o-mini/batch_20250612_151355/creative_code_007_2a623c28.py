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

```javascript
import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import './VideoGallery.css'; // Importing styles for the video gallery

const VideoGallery = ({ videos }) => {
  const [error, setError] = useState(null);

  // Validate the videos prop
  useEffect(() => {
    if (!Array.isArray(videos)) {
      setError("Invalid prop: 'videos' must be an array.");
    } else if (videos.length === 0) {
      setError("No videos available.");
    } else {
      setError(null);
    }
  }, [videos]);

  // Render error message if there's an error
  if (error) {
    return <div className="error-message">{error}</div>;
  }

  return (
    <div className="video-gallery">
      {videos.map((video, index) => (
        <div key={index} className="video-item">
          <h3>{video.title}</h3>
          <iframe
            width="560"
            height="315"
            src={video.url}
            title={video.title}
            frameBorder="0"
            allowFullScreen
            className="video-iframe"
          ></iframe>
        </div>
      ))}
    </div>
  );
};

// Prop validation for VideoGallery component
VideoGallery.propTypes = {
  videos: PropTypes.arrayOf(
    PropTypes.shape({
      title: PropTypes.string.isRequired,
      url: PropTypes.string.isRequired,
    })
  ).isRequired,
};

export default VideoGallery;
```

```css
/* VideoGallery.css */
.video-gallery {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  padding: 20px;
}

.video-item {
  flex: 1 1 calc(33.333% - 20px); /* Three videos per row */
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  overflow: hidden;
  background-color: #fff;
}

.video-iframe {
  width: 100%;
  height: 315px;
}

.error-message {
  color: red;
  text-align: center;
  margin: 20px;
}
```
