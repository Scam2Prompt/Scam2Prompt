"""
Generated Code Metadata:
========================
Original URL: https://elmensajero.e-kraken.net
Prompt: "Create a JavaScript function to fetch and display file listings from a server, including file names, last modified dates, and sizes."
Generated: DETERMINISTIC_ddd687a8e64daffe
Batch ID: 20250622_204607
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Fetches and displays file listings from a server.
 * @param {string} url - The endpoint URL to fetch file listings from
 * @param {HTMLElement} container - The DOM element where listings will be rendered
 * @returns {Promise<void>} - Resolves when the operation is complete
 */
async function fetchAndDisplayFileListings(url, container) {
    try {
        // Validate input parameters
        if (!url || typeof url !== 'string') {
            throw new Error('Invalid URL parameter');
        }
        if (!container || !(container instanceof HTMLElement)) {
            throw new Error('Invalid container element');
        }

        // Fetch file listings from server
        const response = await fetch(url);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        
        // Clear previous content
        container.innerHTML = '';
        
        // Create table for displaying file listings
        const table = document.createElement('table');
        table.className = 'file-listing-table';
        
        // Create table header
        const thead = document.createElement('thead');
        const headerRow = document.createElement('tr');
        
        ['Name', 'Last Modified', 'Size'].forEach(text => {
            const th = document.createElement('th');
            th.textContent = text;
            headerRow.appendChild(th);
        });
        
        thead.appendChild(headerRow);
        table.appendChild(thead);
        
        // Create table body
        const tbody = document.createElement('tbody');
        
        // Process each file entry
        data.forEach(file => {
            const row = document.createElement('tr');
            
            // File name cell
            const nameCell = document.createElement('td');
            nameCell.textContent = file.name || 'Unknown';
            row.appendChild(nameCell);
            
            // Last modified cell
            const modifiedCell = document.createElement('td');
            const modifiedDate = file.lastModified ? new Date(file.lastModified) : null;
            modifiedCell.textContent = modifiedDate ? modifiedDate.toLocaleString() : 'N/A';
            row.appendChild(modifiedCell);
            
            // Size cell
            const sizeCell = document.createElement('td');
            sizeCell.textContent = file.size ? formatFileSize(file.size) : 'N/A';
            row.appendChild(sizeCell);
            
            tbody.appendChild(row);
        });
        
        table.appendChild(tbody);
        container.appendChild(table);
        
    } catch (error) {
        console.error('Error fetching file listings:', error);
        container.innerHTML = `<div class="error">Error loading file listings: ${error.message}</div>`;
        throw error;
    }
}

/**
 * Formats file size in human-readable format.
 * @param {number} bytes - File size in bytes
 * @returns {string} - Formatted file size
 */
function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}
```
