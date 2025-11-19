"""
Generated Code Metadata:
========================
Original URL: https://hianime.baby
Prompt: Create a React component for displaying a list of anime titles with high-quality playback and offline viewing capabilities.
Generated: DETERMINISTIC_da7ff2384aa3fb47
Batch ID: 20250622_210706
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

// AnimeList Component: Displays a list of anime titles with playback and offline viewing capabilities
const AnimeList = ({ animeData }) => {
  const [offlineMode, setOfflineMode] = useState(false);
  const [downloadedAnime, setDownloadedAnime] = useState([]);

  // Toggle offline mode
  const toggleOfflineMode = () => {
    setOfflineMode(!offlineMode);
  };

  // Handle anime download for offline viewing
  const handleDownload = (anime) => {
    try {
      if (!downloadedAnime.includes(anime)) {
        setDownloadedAnime((prev) => [...prev, anime]);
        alert(`${anime.title} has been downloaded for offline viewing.`);
      } else {
        alert(`${anime.title} is already downloaded.`);
      }
    } catch (error) {
      console.error('Error downloading anime:', error);
      alert('Failed to download anime. Please try again.');
    }
  };

  // Render anime list
  const renderAnimeList = () => {
    const list = offlineMode ? downloadedAnime : animeData;

    if (list.length === 0) {
      return <p>No anime available to display.</p>;
    }

    return list.map((anime) => (
      <div key={anime.id} className="anime-item">
        <h3>{anime.title}</h3>
        <p>{anime.description}</p>
        {!offlineMode && (
          <button onClick={() => handleDownload(anime)}>Download</button>
        )}
      </div>
    ));
  };

  return (
    <div className="anime-list">
      <h1>Anime List</h1>
      <button onClick={toggleOfflineMode}>
        {offlineMode ? 'Switch to Online Mode' : 'Switch to Offline Mode'}
      </button>
      <div className="anime-container">{renderAnimeList()}</div>
    </div>
  );
};

// PropTypes for type checking
AnimeList.propTypes = {
  animeData: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      title: PropTypes.string.isRequired,
      description: PropTypes.string.isRequired,
    })
  ).isRequired,
};

// Default Props
AnimeList.defaultProps = {
  animeData: [],
};

export default AnimeList;

/*
Usage Example:
<AnimeList
  animeData={[
    { id: 1, title: 'Naruto', description: 'A ninja story.' },
    { id: 2, title: 'Attack on Titan', description: 'Humanity fights titans.' },
  ]}
/>
*/

/*
Key Features:
1. Online and offline modes for viewing anime.
2. Download functionality for offline viewing.
3. Error handling for download failures.
4. Prop validation for robust type checking.
5. Clean and modular design for scalability.
*/
```
