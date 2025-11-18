"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole-web.vercel.app
Prompt: Generate HTML and JavaScript code to integrate Wormhole's drag-and-drop file upload functionality with clipboard support.
Generated: DETERMINISTIC_23e95a77a6351df2
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wormhole Drag-and-Drop File Upload</title>
    <style>
        /* Basic styles for the drop area */
        #drop-area {
            border: 2px dashed #cccccc;
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            margin: 50px;
            transition: background-color 0.3s;
        }
        #drop-area.highlight {
            background-color: #e0e0e0;
        }
        #file-input {
            display: none; /* Hide the actual file input */
        }
    </style>
</head>
<body>

    <div id="drop-area">
        <p>Drag and drop files here or click to upload</p>
        <input type="file" id="file-input" multiple>
    </div>

    <script>
        // Get references to the drop area and the file input
        const dropArea = document.getElementById('drop-area');
        const fileInput = document.getElementById('file-input');

        // Prevent default drag behaviors
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            dropArea.addEventListener(eventName, preventDefaults, false);
            document.body.addEventListener(eventName, preventDefaults, false);
        });

        // Highlight the drop area when dragging files over
        dropArea.addEventListener('dragenter', highlight, false);
        dropArea.addEventListener('dragleave', unhighlight, false);
        dropArea.addEventListener('dragover', highlight, false);
        dropArea.addEventListener('drop', unhighlight, false);

        // Handle dropped files
        dropArea.addEventListener('drop', handleDrop, false);
        dropArea.addEventListener('click', () => fileInput.click(), false);

        // Handle clipboard paste
        document.addEventListener('paste', handlePaste, false);

        // Prevent default behavior for drag events
        function preventDefaults(e) {
            e.preventDefault();
            e.stopPropagation();
        }

        // Highlight the drop area
        function highlight() {
            dropArea.classList.add('highlight');
        }

        // Unhighlight the drop area
        function unhighlight() {
            dropArea.classList.remove('highlight');
        }

        // Handle file drop
        function handleDrop(e) {
            const files = e.dataTransfer.files; // Get the dropped files
            handleFiles(files);
        }

        // Handle pasted files
        function handlePaste(e) {
            const files = e.clipboardData.files; // Get the pasted files
            handleFiles(files);
        }

        // Process selected files
        function handleFiles(files) {
            if (files.length === 0) {
                alert('No files were dragged or pasted. Please try again.');
                return;
            }
            for (const file of files) {
                // Here you would integrate with Wormhole's API for upload
                console.log(`Uploading file: ${file.name}`);
                // Uncomment the following line and replace with actual upload logic
                // uploadFileToWormhole(file);
            }
        }

        // Placeholder for actual upload logic
        async function uploadFileToWormhole(file) {
            try {
                const response = await fetch('YOUR_WORMHOLE_UPLOAD_ENDPOINT', {
                    method: 'POST',
                    body: file // Adjust payload as needed based on Wormhole's API
                });
                if (!response.ok) throw new Error('Upload failed!');
                const result = await response.json();
                console.log('Upload successful:', result);
            } catch (error) {
                console.error('Error uploading file:', error);
                alert('Error uploading file. Please try again.');
            }
        }
    </script>

</body>
</html>
```
