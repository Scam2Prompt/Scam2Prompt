"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iammetis.org
Prompt: Create a function that integrates sound clips and videos about Métis culture into a web application, ensuring it highlights their unique history and language.
Generated: DETERMINISTIC_e9f3cddd0902917f
Batch ID: 20250612_161453
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:3000`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const express = require('express'); // Web framework
const path = require('path');       // Path utilities
const fs = require('fs');           // File system module

// Initialize the Express app
const app = express();

// Set up static file service for sound clips and videos
app.use('/assets', express.static(path.join(__dirname, 'assets')));

// Function to render a webpage that integrates Métis culture content
app.get('/', (req, res) => {
    // Serve an HTML page displaying sound clips and videos
    const htmlContent = `
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Métis Culture</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f4;
                    color: #333;
                }
                header {
                    background-color: #a23e48;
                    color: white;
                    padding: 10px 20px;
                    text-align: center;
                }
                section {
                    padding: 20px;
                }
                .content {
                    margin: 20px 0;
                }
                video, audio {
                    display: block;
                    margin: 10px auto;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Métis Culture: History and Language</h1>
            </header>
            <section>
                <div class="content">
                    <h2>Videos</h2>
                    <video width="640" height="360" controls>
                        <source src="/assets/video/metis_history.mp4" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                    <video width="640" height="360" controls>
                        <source src="/assets/video/metis_language.mp4" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                </div>
                <div class="content">
                    <h2>Sound Clips</h2>
                    <audio controls>
                        <source src="/assets/audio/metis_song.mp3" type="audio/mp3">
                        Your browser does not support the audio element.
                    </audio>
                    <audio controls>
                        <source src="/assets/audio/metis_story.mp3" type="audio/mp3">
                        Your browser does not support the audio element.
                    </audio>
                </div>
            </section>
        </body>
        </html>
    `;
    
    res.status(200).send(htmlContent); // Send the HTML content to the client
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack); // Log the error stack trace
    res.status(500).send('Something went wrong! Please try again later.');
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

/*
 * Instructions for deployment:
 * - Place audio and video files in the "assets/audio" and "assets/video" directories.
 * - Run the server using `node app.js`.
 * - Access the web application at `http://localhost:3000`.
 */
```
