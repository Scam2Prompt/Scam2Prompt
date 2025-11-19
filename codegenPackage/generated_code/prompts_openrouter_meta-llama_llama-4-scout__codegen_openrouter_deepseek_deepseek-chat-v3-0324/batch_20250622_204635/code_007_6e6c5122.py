"""
Generated Code Metadata:
========================
Original URL: https://stbot.xyz
Prompt: "Generate a JavaScript function to upload a video to YouTube using the YouTube Data API, including setting video title, description, and privacy status."
Generated: DETERMINISTIC_6e6c512237580921
Batch ID: 20250622_204635
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const { google } = require('googleapis');
const fs = require('fs');
const path = require('path');

/**
 * Uploads a video to YouTube with specified metadata.
 * @param {string} videoPath - Path to the video file to upload
 * @param {Object} options - Video metadata options
 * @param {string} options.title - Video title
 * @param {string} options.description - Video description
 * @param {string} [options.privacyStatus='private'] - Privacy status (public, private, unlisted)
 * @param {string} [options.categoryId='22'] - YouTube category ID (default 22 for People & Blogs)
 * @param {string[]} [options.tags=[]] - Array of video tags
 * @param {Object} auth - Authenticated OAuth2 client
 * @returns {Promise<Object>} - Promise resolving to the uploaded video data
 */
async function uploadVideoToYouTube(videoPath, options, auth) {
  const youtube = google.youtube({ version: 'v3', auth });
  const fileSize = fs.statSync(videoPath).size;
  
  const requestParams = {
    part: 'snippet,status',
    requestBody: {
      snippet: {
        title: options.title,
        description: options.description,
        tags: options.tags || [],
        categoryId: options.categoryId || '22'
      },
      status: {
        privacyStatus: options.privacyStatus || 'private',
        selfDeclaredMadeForKids: false
      }
    },
    media: {
      body: fs.createReadStream(videoPath)
    }
  };

  try {
    const res = await youtube.videos.insert(requestParams, {
      // Use resumable upload for large files
      onUploadProgress: (evt) => {
        const progress = (evt.bytesRead / fileSize) * 100;
        console.log(`Upload progress: ${progress.toFixed(2)}%`);
      }
    });
    
    console.log('Video uploaded successfully:', res.data);
    return res.data;
  } catch (error) {
    console.error('Error uploading video:', error.message);
    throw error;
  }
}

// Example usage:
// (Note: You need to authenticate first using OAuth2)
/*
const oauth2Client = new google.auth.OAuth2(
  'YOUR_CLIENT_ID',
  'YOUR_CLIENT_SECRET',
  'YOUR_REDIRECT_URL'
);

oauth2Client.setCredentials({
  access_token: 'YOUR_ACCESS_TOKEN',
  refresh_token: 'YOUR_REFRESH_TOKEN'
});

uploadVideoToYouTube(
  './myvideo.mp4',
  {
    title: 'My Awesome Video',
    description: 'This is a test video uploaded via YouTube API',
    privacyStatus: 'public',
    tags: ['test', 'api', 'upload']
  },
  oauth2Client
).catch(console.error);
*/
```
