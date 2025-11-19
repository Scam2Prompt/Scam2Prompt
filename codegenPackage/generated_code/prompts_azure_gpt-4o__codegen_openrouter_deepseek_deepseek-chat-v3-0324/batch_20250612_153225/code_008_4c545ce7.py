"""
Generated Code Metadata:
========================
Original URL: https://nucleicinsights.com
Prompt: Write code in JavaScript to implement a dynamic CV download button on a portfolio website, similar to the one featured on Umama Shahid's webpage.
Generated: DETERMINISTIC_4c545ce7961b55df
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Dynamic CV Download Button Implementation
 * 
 * This script creates a dynamic CV download button that:
 * - Changes appearance on hover
 * - Shows download progress
 * - Handles download completion
 * - Works across modern browsers
 */

class CVDownloadButton {
  constructor(buttonId, cvUrl) {
    this.button = document.getElementById(buttonId);
    this.cvUrl = cvUrl;
    this.init();
  }

  init() {
    if (!this.button) {
      console.error('Button element not found');
      return;
    }

    this.setupStyles();
    this.setupEventListeners();
  }

  setupStyles() {
    // Add base styles if not already present
    const style = document.createElement('style');
    style.textContent = `
      .cv-download-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 12px 24px;
        border-radius: 4px;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        text-decoration: none;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        position: relative;
        overflow: hidden;
      }
      
      .cv-download-btn:hover {
        background-color: #45a049;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      }
      
      .cv-download-btn:active {
        transform: translateY(0);
      }
      
      .cv-download-btn .progress {
        position: absolute;
        bottom: 0;
        left: 0;
        height: 4px;
        background-color: rgba(255, 255, 255, 0.5);
        width: 0%;
        transition: width 0.3s ease;
      }
      
      .cv-download-btn .icon {
        margin-right: 8px;
      }
    `;
    document.head.appendChild(style);

    // Add button classes
    this.button.classList.add('cv-download-btn');
    
    // Add icon if not present
    if (!this.button.querySelector('.icon')) {
      const icon = document.createElement('span');
      icon.className = 'icon';
      icon.innerHTML = '📄';
      this.button.prepend(icon);
    }
    
    // Add progress bar if not present
    if (!this.button.querySelector('.progress')) {
      const progress = document.createElement('div');
      progress.className = 'progress';
      this.button.appendChild(progress);
    }
  }

  setupEventListeners() {
    this.button.addEventListener('click', (e) => {
      e.preventDefault();
      this.downloadCV();
    });
  }

  async downloadCV() {
    try {
      // Show downloading state
      this.button.disabled = true;
      this.button.querySelector('.icon').innerHTML = '⏳';
      
      // Simulate progress (in a real scenario, you'd track actual download progress)
      const progressBar = this.button.querySelector('.progress');
      let progress = 0;
      const interval = setInterval(() => {
        progress += 10;
        progressBar.style.width = `${progress}%`;
        if (progress >= 100) clearInterval(interval);
      }, 100);
      
      // Fetch the CV file
      const response = await fetch(this.cvUrl);
      if (!response.ok) throw new Error('Failed to download CV');
      
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      
      // Create download link
      const a = document.createElement('a');
      a.href = url;
      a.download = this.cvUrl.split('/').pop() || 'cv.pdf';
      document.body.appendChild(a);
      a.click();
      
      // Cleanup
      window.URL.revokeObjectURL(url);
      document.body.removeChild(a);
      
      // Reset button state
      setTimeout(() => {
        this.button.disabled = false;
        this.button.querySelector('.icon').innerHTML = '📄';
        progressBar.style.width = '0%';
      }, 1000);
      
    } catch (error) {
      console.error('Download error:', error);
      this.button.querySelector('.icon').innerHTML = '❌';
      this.button.disabled = false;
      
      // Show error message
      const originalText = this.button.textContent;
      this.button.textContent = 'Download Failed!';
      
      setTimeout(() => {
        this.button.innerHTML = `<span class="icon">📄</span>${originalText}`;
      }, 2000);
    }
  }
}

// Usage example:
// document.addEventListener('DOMContentLoaded', () => {
//   new CVDownloadButton('cv-download-btn', '/path/to/cv.pdf');
// });
```
