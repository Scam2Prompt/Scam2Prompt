"""
Generated Code Metadata:
========================
Original URL: https://wallstreetespepe.net
Prompt: Write a JavaScript function that fetches and lists the contents of a server directory, inspired by the index page of wallstreetespepe.net.
Generated: DETERMINISTIC_e9ca0b8991b18053
Batch ID: 20250612_155752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Fetches and lists the contents of a server directory.
 * @param {string} directoryPath - The path to the directory to list.
 * @returns {Promise<Array<{name: string, type: string, size: number, modified: string}>>} - A promise that resolves to an array of directory entries.
 */
async function fetchDirectoryContents(directoryPath) {
    try {
        // Validate input
        if (!directoryPath || typeof directoryPath !== 'string') {
            throw new Error('Invalid directory path provided');
        }

        // Normalize the path to ensure it ends with a slash
        const normalizedPath = directoryPath.endsWith('/') ? directoryPath : `${directoryPath}/`;

        // Fetch the directory listing
        const response = await fetch(normalizedPath, {
            method: 'GET',
            headers: {
                'Accept': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`Server returned ${response.status}: ${response.statusText}`);
        }

        // Parse the response
        const contentType = response.headers.get('content-type');
        if (!contentType || !contentType.includes('application/json')) {
            throw new Error('Server did not return JSON data');
        }

        const data = await response.json();

        // Validate the response structure
        if (!Array.isArray(data)) {
            throw new Error('Invalid server response: expected an array of directory entries');
        }

        // Process each entry to ensure it has required fields
        return data.map(entry => {
            if (!entry.name || typeof entry.name !== 'string') {
                throw new Error('Invalid directory entry: missing or invalid name');
            }

            return {
                name: entry.name,
                type: entry.type || 'unknown',
                size: entry.size || 0,
                modified: entry.modified || ''
            };
        });

    } catch (error) {
        console.error('Error fetching directory contents:', error.message);
        throw error; // Re-throw to allow caller to handle
    }
}

/**
 * Renders directory contents to the DOM as an HTML list.
 * @param {Array<{name: string, type: string, size: number, modified: string}>} contents - The directory contents to render.
 * @param {HTMLElement} container - The DOM element to render into.
 */
function renderDirectoryContents(contents, container) {
    if (!container || !(container instanceof HTMLElement)) {
        throw new Error('Invalid container element provided');
    }

    // Clear existing content
    container.innerHTML = '';

    // Create a list element
    const list = document.createElement('ul');
    list.className = 'directory-listing';

    // Add each entry as a list item
    contents.forEach(entry => {
        const item = document.createElement('li');
        item.className = `entry ${entry.type}`;

        // Create link for files
        if (entry.type === 'file') {
            const link = document.createElement('a');
            link.href = entry.name;
            link.textContent = entry.name;
            item.appendChild(link);
        } else {
            item.textContent = entry.name;
        }

        // Add metadata
        const meta = document.createElement('span');
        meta.className = 'meta';
        meta.textContent = ` (${entry.type}, ${formatBytes(entry.size)}, ${entry.modified})`;
        item.appendChild(meta);

        list.appendChild(item);
    });

    container.appendChild(list);
}

/**
 * Helper function to format bytes into human-readable format.
 * @param {number} bytes - The size in bytes.
 * @returns {string} - Formatted size string.
 */
function formatBytes(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

// Example usage:
// (async () => {
//     try {
//         const contents = await fetchDirectoryContents('/path/to/directory/');
//         renderDirectoryContents(contents, document.getElementById('directory-container'));
//     } catch (error) {
//         console.error('Failed to load directory:', error);
//     }
// })();
```
