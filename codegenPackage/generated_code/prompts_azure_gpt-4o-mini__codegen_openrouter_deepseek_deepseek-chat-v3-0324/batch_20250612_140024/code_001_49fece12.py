"""
Generated Code Metadata:
========================
Original URL: https://kraken.media
Prompt: Write a code snippet for a web application that integrates video content to boost user engagement, inspired by Kraken Media's approach to video production.
Generated: DETERMINISTIC_49fece1264b9d966
Batch ID: 20250612_140024
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://${process.env.S3_BUCKET_NAME}.s3.amazonaws.com/${key}`,": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const express = require('express');
const path = require('path');
const fs = require('fs');
const { v4: uuidv4 } = require('uuid');
const ffmpeg = require('fluent-ffmpeg');
const AWS = require('aws-sdk');

// Initialize AWS S3 for video storage
const s3 = new AWS.S3({
  accessKeyId: process.env.AWS_ACCESS_KEY_ID,
  secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
  region: process.env.AWS_REGION
});

// Initialize Express app
const app = express();
app.use(express.json());
app.use(express.static('public'));

// Video processing configuration
const VIDEO_CONFIG = {
  maxFileSize: 100 * 1024 * 1024, // 100MB
  allowedFormats: ['mp4', 'mov', 'avi', 'mkv'],
  thumbnailTime: '00:00:05',
  resolutions: [
    { width: 1280, height: 720 },
    { width: 854, height: 480 },
    { width: 640, height: 360 }
  ]
};

// Endpoint to upload video
app.post('/api/videos', async (req, res) => {
  try {
    if (!req.files || !req.files.video) {
      return res.status(400).json({ error: 'No video file uploaded' });
    }

    const videoFile = req.files.video;
    const fileExt = path.extname(videoFile.name).toLowerCase().substring(1);

    // Validate file
    if (!VIDEO_CONFIG.allowedFormats.includes(fileExt)) {
      return res.status(400).json({ error: 'Invalid file format' });
    }

    if (videoFile.size > VIDEO_CONFIG.maxFileSize) {
      return res.status(400).json({ error: 'File size exceeds limit' });
    }

    // Generate unique ID for video
    const videoId = uuidv4();
    const tempPath = `./temp/${videoId}.${fileExt}`;
    const outputDir = `./processed/${videoId}`;

    // Save temp file
    await videoFile.mv(tempPath);

    // Process video (transcode, generate thumbnails)
    const processedFiles = await processVideo(tempPath, outputDir, videoId);

    // Upload to S3
    const uploadResults = await Promise.all(
      processedFiles.map(file => uploadToS3(file, videoId))
    );

    // Clean up temp files
    fs.unlinkSync(tempPath);
    fs.rmSync(outputDir, { recursive: true, force: true });

    // Return video metadata
    res.status(201).json({
      id: videoId,
      formats: uploadResults.filter(r => r.type === 'video'),
      thumbnail: uploadResults.find(r => r.type === 'thumbnail').url
    });

  } catch (error) {
    console.error('Video upload error:', error);
    res.status(500).json({ error: 'Failed to process video' });
  }
});

// Video processing function
async function processVideo(inputPath, outputDir, videoId) {
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  const outputFiles = [];

  // Generate thumbnail
  const thumbnailPath = `${outputDir}/thumbnail.jpg`;
  await new Promise((resolve, reject) => {
    ffmpeg(inputPath)
      .screenshots({
        timestamps: [VIDEO_CONFIG.thumbnailTime],
        filename: 'thumbnail.jpg',
        folder: outputDir
      })
      .on('end', resolve)
      .on('error', reject);
  });
  outputFiles.push({ path: thumbnailPath, type: 'thumbnail' });

  // Transcode to multiple resolutions
  for (const resolution of VIDEO_CONFIG.resolutions) {
    const outputPath = `${outputDir}/${resolution.width}x${resolution.height}.mp4`;
    await new Promise((resolve, reject) => {
      ffmpeg(inputPath)
        .size(`${resolution.width}x${resolution.height}`)
        .videoCodec('libx264')
        .audioCodec('aac')
        .output(outputPath)
        .on('end', resolve)
        .on('error', reject)
        .run();
    });
    outputFiles.push({ 
      path: outputPath, 
      type: 'video',
      resolution: `${resolution.width}x${resolution.height}`
    });
  }

  return outputFiles;
}

// S3 Upload function
async function uploadToS3(file, videoId) {
  const fileStream = fs.createReadStream(file.path);
  const fileExt = path.extname(file.path).substring(1);
  const contentType = file.type === 'video' ? 'video/mp4' : 'image/jpeg';
  const key = `${file.type}s/${videoId}/${file.resolution || 'thumbnail'}.${fileExt}`;

  const uploadParams = {
    Bucket: process.env.S3_BUCKET_NAME,
    Key: key,
    Body: fileStream,
    ContentType: contentType
  };

  await s3.upload(uploadParams).promise();

  return {
    type: file.type,
    url: `https://${process.env.S3_BUCKET_NAME}.s3.amazonaws.com/${key}`,
    resolution: file.resolution
  };
}

// Video player endpoint
app.get('/videos/:id', (req, res) => {
  const videoId = req.params.id;
  res.sendFile(path.join(__dirname, 'public', 'player.html'));
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```
