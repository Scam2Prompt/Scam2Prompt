"""
Generated Code Metadata:
========================
Original URL: https://p.b5z.net
Prompt: Generate a JavaScript function that utilizes SparkFX add-on features to batch process video files in Davinci Resolve.
Generated: DETERMINISTIC_c28b4622e800b63c
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Batch processes video files in DaVinci Resolve using SparkFX add-on features.
 * 
 * @param {Array<string>} videoPaths - Array of file paths to the video files to process.
 * @param {Object} options - Configuration options for the batch processing.
 * @param {string} [options.outputDir='./output'] - Output directory for processed files.
 * @param {string} [options.preset='default'] - SparkFX preset to apply.
 * @param {number} [options.quality=90] - Output quality (0-100).
 * @param {boolean} [options.overwrite=false] - Overwrite existing files.
 * @returns {Promise<Array<string>>} - Array of paths to processed files.
 * @throws {Error} - If processing fails or invalid input is provided.
 */
async function batchProcessVideos(videoPaths, options = {}) {
    // Validate inputs
    if (!Array.isArray(videoPaths) || videoPaths.length === 0) {
        throw new Error('videoPaths must be a non-empty array');
    }

    // Set default options
    const {
        outputDir = './output',
        preset = 'default',
        quality = 90,
        overwrite = false
    } = options;

    // Validate quality parameter
    if (quality < 0 || quality > 100) {
        throw new Error('quality must be between 0 and 100');
    }

    // Initialize SparkFX and Resolve
    try {
        const resolve = getResolve();
        if (!resolve) {
            throw new Error('DaVinci Resolve is not available');
        }

        const sparkFX = resolve.getSparkFX();
        if (!sparkFX) {
            throw new Error('SparkFX add-on is not available');
        }

        // Create output directory if it doesn't exist
        const fs = require('fs');
        if (!fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        const processedFiles = [];

        // Process each video file
        for (const videoPath of videoPaths) {
            try {
                // Verify input file exists
                if (!fs.existsSync(videoPath)) {
                    console.warn(`File not found: ${videoPath}`);
                    continue;
                }

                // Generate output path
                const outputPath = `${outputDir}/${path.basename(videoPath)}_processed.mp4`;

                // Skip if file exists and overwrite is false
                if (fs.existsSync(outputPath) && !overwrite) {
                    console.warn(`Skipping existing file: ${outputPath}`);
                    processedFiles.push(outputPath);
                    continue;
                }

                // Load video into SparkFX
                sparkFX.loadVideo(videoPath);
                
                // Apply preset
                sparkFX.applyPreset(preset);
                
                // Set output quality
                sparkFX.setOutputQuality(quality);
                
                // Process and save
                await sparkFX.processVideo(outputPath);
                
                processedFiles.push(outputPath);
                console.log(`Successfully processed: ${outputPath}`);
            } catch (error) {
                console.error(`Error processing ${videoPath}:`, error.message);
                // Continue with next file even if current fails
            }
        }

        return processedFiles;
    } catch (error) {
        console.error('Batch processing failed:', error.message);
        throw error;
    }
}

// Helper function to get Resolve instance
function getResolve() {
    try {
        return require('DaVinciResolve').getResolve();
    } catch (error) {
        return null;
    }
}

// Node.js path module for file path operations
const path = require('path');
```
