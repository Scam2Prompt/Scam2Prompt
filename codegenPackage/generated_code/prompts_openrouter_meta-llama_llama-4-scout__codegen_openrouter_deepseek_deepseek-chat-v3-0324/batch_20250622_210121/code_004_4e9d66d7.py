"""
Generated Code Metadata:
========================
Original URL: https://wormhole-web.vercel.app
Prompt: "Design a simple file sharing interface with a 'select file' or 'drag it here' functionality using HTML and CSS."
Generated: DETERMINISTIC_4e9d66d779f40e50
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation of a file sharing interface with both file selection and drag-and-drop functionality:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Sharing Interface</title>
    <style>
        /* Reset and base styles */
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #f5f7fa;
            padding: 20px;
        }

        /* Main container */
        .file-upload-container {
            width: 100%;
            max-width: 500px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            padding: 30px;
            text-align: center;
        }

        h1 {
            color: #333;
            margin-bottom: 20px;
            font-size: 24px;
        }

        /* Drop zone styling */
        .drop-zone {
            border: 2px dashed #ccc;
            border-radius: 8px;
            padding: 40px 20px;
            margin-bottom: 20px;
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
        }

        .drop-zone:hover {
            border-color: #4a90e2;
            background-color: #f8faff;
        }

        .drop-zone.active {
            border-color: #4a90e2;
            background-color: #e8f0fe;
        }

        .drop-zone__icon {
            font-size: 48px;
            color: #4a90e2;
            margin-bottom: 15px;
        }

        .drop-zone__prompt {
            color: #666;
            margin-bottom: 15px;
        }

        .drop-zone__input {
            display: none;
        }

        /* Button styling */
        .btn {
            background-color: #4a90e2;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .btn:hover {
            background-color: #3a7bc8;
        }

        /* File info display */
        .file-info {
            margin-top: 20px;
            padding: 15px;
            background-color: #f0f4f8;
            border-radius: 6px;
            display: none;
        }

        .file-info__name {
            font-weight: bold;
            margin-bottom: 5px;
        }

        .file-info__size {
            color: #666;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="file-upload-container">
        <h1>Share Your Files</h1>
        
        <!-- Drop zone -->
        <div class="drop-zone" id="dropZone">
            <div class="drop-zone__icon">📁</div>
            <div class="drop-zone__prompt">Drag & drop your file here or</div>
            <input type="file" id="fileInput" class="drop-zone__input">
            <button class="btn" id="browseBtn">Select File</button>
        </div>
        
        <!-- File info display -->
        <div class="file-info" id="fileInfo">
            <div class="file-info__name" id="fileName"></div>
            <div class="file-info__size" id="fileSize"></div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const dropZone = document.getElementById('dropZone');
            const fileInput = document.getElementById('fileInput');
            const browseBtn = document.getElementById('browseBtn');
            const fileInfo = document.getElementById('fileInfo');
            const fileName = document.getElementById('fileName');
            const fileSize = document.getElementById('fileSize');

            // Handle file selection via button
            browseBtn.addEventListener('click', function() {
                fileInput.click();
            });

            // Handle file selection via input
            fileInput.addEventListener('change', function(e) {
                if (e.target.files.length) {
                    handleFile(e.target.files[0]);
                }
            });

            // Prevent default drag behaviors
            ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
                dropZone.addEventListener(eventName, preventDefaults, false);
                document.body.addEventListener(eventName, preventDefaults, false);
            });

            // Highlight drop zone when item is dragged over it
            ['dragenter', 'dragover'].forEach(eventName => {
                dropZone.addEventListener(eventName, highlight, false);
            });

            ['dragleave', 'drop'].forEach(eventName => {
                dropZone.addEventListener(eventName, unhighlight, false);
            });

            // Handle dropped files
            dropZone.addEventListener('drop', function(e) {
                const dt = e.dataTransfer;
                const file = dt.files[0];
                if (file) {
                    handleFile(file);
                }
            });

            function preventDefaults(e) {
                e.preventDefault();
                e.stopPropagation();
            }

            function highlight() {
                dropZone.classList.add('active');
            }

            function unhighlight() {
                dropZone.classList.remove('active');
            }

            function handleFile(file) {
                // Display file info
                fileName.textContent = file.name;
                fileSize.textContent = formatFileSize(file.size);
                fileInfo.style.display = 'block';

                // Here you would typically handle the file upload
                // For example: uploadFile(file);
            }

            function formatFileSize(bytes) {
                if (bytes === 0) return '0 Bytes';
                const k = 1024;
                const sizes = ['Bytes', 'KB', 'MB', 'GB'];
                const i = Math.floor(Math.log(bytes) / Math.log(k));
                return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
            }
        });
    </script>
</body>
</html>
```
