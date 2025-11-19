"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bookofmeme.link
Prompt: What JavaScript libraries are recommended for building interactive meme applications like the one found at Book of MEME?
Generated: DETERMINISTIC_14f1c41a563a8a80
Batch ID: 20250612_155639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries for building an interactive meme application
import React, { useState } from 'react'; // React for building UI components
import { createRoot } from 'react-dom/client'; // For rendering React components
import { v4 as uuidv4 } from 'uuid'; // For generating unique identifiers
import html2canvas from 'html2canvas'; // For capturing DOM elements as images
import { saveAs } from 'file-saver'; // For saving generated memes as files

// Meme component to handle meme creation
const MemeGenerator = () => {
    const [topText, setTopText] = useState('');
    const [bottomText, setBottomText] = useState('');
    const [selectedImage, setSelectedImage] = useState('');
    const [memeImage, setMemeImage] = useState('');

    // Handler for meme image selection
    const handleImageChange = (e) => {
        setSelectedImage(URL.createObjectURL(e.target.files[0]));
    };

    // Function to generate meme
    const generateMeme = async () => {
        if (!topText && !bottomText) {
            alert('Please enter text for the meme!');
            return;
        }

        const memeContainer = document.getElementById('memeContainer');

        // Capture memeContainer as an image
        try {
            const canvas = await html2canvas(memeContainer);
            const dataUrl = canvas.toDataURL('image/png');
            setMemeImage(dataUrl);
        } catch (error) {
            console.error('Error generating meme:', error);
            alert('Failed to generate meme. Please try again.');
        }
    };

    // Function to download generated meme
    const downloadMeme = () => {
        if (!memeImage) {
            alert('Please generate a meme before downloading!');
            return;
        }
        saveAs(memeImage, `meme-${uuidv4()}.png`);
    };

    return (
        <div>
            <h1>Meme Generator</h1>
            <input type="file" accept="image/*" onChange={handleImageChange} />
            <input
                type="text"
                placeholder="Top Text"
                value={topText}
                onChange={(e) => setTopText(e.target.value)}
            />
            <input
                type="text"
                placeholder="Bottom Text"
                value={bottomText}
                onChange={(e) => setBottomText(e.target.value)}
            />
            <button onClick={generateMeme}>Generate Meme</button>
            <button onClick={downloadMeme}>Download Meme</button>

            {/* Meme display container */}
            <div id="memeContainer" style={{ position: 'relative', display: 'inline-block' }}>
                {selectedImage && <img src={selectedImage} alt="Selected" style={{ width: '500px' }} />}
                {topText && (
                    <div style={{ position: 'absolute', top: 20, left: 0, right: 0, textAlign: 'center', color: 'white', fontSize: '24px', textShadow: '2px 2px 4px rgba(0, 0, 0, 0.7)' }}>
                        {topText}
                    </div>
                )}
                {bottomText && (
                    <div style={{ position: 'absolute', bottom: 20, left: 0, right: 0, textAlign: 'center', color: 'white', fontSize: '24px', textShadow: '2px 2px 4px rgba(0, 0, 0, 0.7)' }}>
                        {bottomText}
                    </div>
                )}
            </div>
            {memeImage && <img src={memeImage} alt="Generated Meme" style={{ marginTop: '20px', width: '500px' }} />}
        </div>
    );
};

// Rendering the MemeGenerator component
const root = createRoot(document.getElementById('root'));
root.render(<MemeGenerator />);
```

### Required Dependencies
Make sure you have the following npm packages installed:
```bash
npm install react react-dom uuid html2canvas file-saver
``` 

### Basic HTML Setup
Ensure you have the following HTML structure in your `index.html` file:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meme Generator</title>
</head>
<body>
    <div id="root"></div>
    <script src="path/to/your/bundled/javascript/file.js"></script>
</body>
</html>
```
