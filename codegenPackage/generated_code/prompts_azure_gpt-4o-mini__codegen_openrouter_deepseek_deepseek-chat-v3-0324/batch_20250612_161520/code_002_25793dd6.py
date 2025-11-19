"""
Generated Code Metadata:
========================
Original URL: https://synerex-bo.com
Prompt: Write a JavaScript function that fetches and displays file information from a server directory, inspired by the synerex-bo.com index page.
Generated: DETERMINISTIC_25793dd6a5c96e57
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Fetches and displays file information from a server directory.
 * Inspired by synerex-bo.com index page functionality.
 * 
 * @param {string} directoryPath - The path to the directory to fetch files from
 * @param {HTMLElement} container - The DOM element to display the files in
 * @returns {Promise<void>} - Resolves when files are displayed
 */
async function fetchAndDisplayFiles(directoryPath, container) {
    try {
        // Validate inputs
        if (!directoryPath || typeof directoryPath !== 'string') {
            throw new Error('Invalid directory path provided');
        }
        
        if (!container || !(container instanceof HTMLElement)) {
            throw new Error('Invalid container element provided');
        }

        // Show loading state
        container.innerHTML = '<div class="loading">Loading files...</div>';

        // Fetch directory listing
        const response = await fetch(directoryPath, {
            headers: {
                'Accept': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`Server returned ${response.status}: ${response.statusText}`);
        }

        const files = await response.json();

        // Validate response
        if (!Array.isArray(files)) {
            throw new Error('Invalid server response - expected array of files');
        }

        // Clear loading state
        container.innerHTML = '';

        // Create and append file list
        const fileList = document.createElement('ul');
        fileList.className = 'file-list';

        files.forEach(file => {
            const listItem = document.createElement('li');
            listItem.className = 'file-item';

            const link = document.createElement('a');
            link.href = `${directoryPath}/${file.name}`;
            link.textContent = file.name;
            
            if (file.size) {
                const sizeSpan = document.createElement('span');
                sizeSpan.className = 'file-size';
                sizeSpan.textContent = formatFileSize(file.size);
                link.appendChild(document.createTextNode(' '));
                link.appendChild(sizeSpan);
            }

            if (file.modified) {
                const dateSpan = document.createElement('span');
                dateSpan.className = 'file-date';
                dateSpan.textContent = formatDate(file.modified);
                link.appendChild(document.createTextNode(' '));
                link.appendChild(dateSpan);
            }

            listItem.appendChild(link);
            fileList.appendChild(listItem);
        });

        container.appendChild(fileList);

    } catch (error) {
        console.error('Error fetching files:', error);
        container.innerHTML = `<div class="error">Error loading files: ${error.message}</div>`;
    }
}

/**
 * Formats file size in human-readable format
 * @param {number} bytes - File size in bytes
 * @returns {string} - Formatted size string
 */
function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

/**
 * Formats date in readable format
 * @param {string|Date} date - Date to format
 * @returns {string} - Formatted date string
 */
function formatDate(date) {
    const d = new Date(date);
    return d.toLocaleDateString() + ' ' + d.toLocaleTimeString();
}

// Example usage:
// fetchAndDisplayFiles('/files', document.getElementById('file-container'));
```
