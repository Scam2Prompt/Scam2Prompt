"""
Generated Code Metadata:
========================
Original URL: https://x2make.com
Prompt: Generate JavaScript code to create a user-friendly interface for a Twitter video downloader tool, similar to x2make.com, that allows users to paste a Twitter video URL and download the video in their preferred format.
Generated: DETERMINISTIC_acc6ec084a8143e4
Batch ID: 20250622_204925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Twitter Video Downloader Tool
// This script creates a user-friendly interface for downloading Twitter videos.
// It uses modern JavaScript practices and includes error handling.

document.addEventListener("DOMContentLoaded", () => {
  // Create the main container
  const appContainer = document.createElement("div");
  appContainer.style.maxWidth = "600px";
  appContainer.style.margin = "50px auto";
  appContainer.style.padding = "20px";
  appContainer.style.border = "1px solid #ccc";
  appContainer.style.borderRadius = "8px";
  appContainer.style.boxShadow = "0 4px 8px rgba(0, 0, 0, 0.1)";
  appContainer.style.fontFamily = "Arial, sans-serif";

  // Create the title
  const title = document.createElement("h1");
  title.textContent = "Twitter Video Downloader";
  title.style.textAlign = "center";
  title.style.color = "#333";
  appContainer.appendChild(title);

  // Create the input field for the Twitter video URL
  const urlInput = document.createElement("input");
  urlInput.type = "text";
  urlInput.placeholder = "Paste Twitter video URL here...";
  urlInput.style.width = "100%";
  urlInput.style.padding = "10px";
  urlInput.style.marginBottom = "20px";
  urlInput.style.border = "1px solid #ccc";
  urlInput.style.borderRadius = "4px";
  appContainer.appendChild(urlInput);

  // Create the format selection dropdown
  const formatSelect = document.createElement("select");
  formatSelect.style.width = "100%";
  formatSelect.style.padding = "10px";
  formatSelect.style.marginBottom = "20px";
  formatSelect.style.border = "1px solid #ccc";
  formatSelect.style.borderRadius = "4px";

  const formats = ["MP4", "WEBM", "AVI"];
  formats.forEach((format) => {
    const option = document.createElement("option");
    option.value = format.toLowerCase();
    option.textContent = format;
    formatSelect.appendChild(option);
  });
  appContainer.appendChild(formatSelect);

  // Create the download button
  const downloadButton = document.createElement("button");
  downloadButton.textContent = "Download Video";
  downloadButton.style.width = "100%";
  downloadButton.style.padding = "10px";
  downloadButton.style.backgroundColor = "#007BFF";
  downloadButton.style.color = "#fff";
  downloadButton.style.border = "none";
  downloadButton.style.borderRadius = "4px";
  downloadButton.style.cursor = "pointer";
  downloadButton.style.fontSize = "16px";
  downloadButton.addEventListener("mouseover", () => {
    downloadButton.style.backgroundColor = "#0056b3";
  });
  downloadButton.addEventListener("mouseout", () => {
    downloadButton.style.backgroundColor = "#007BFF";
  });
  appContainer.appendChild(downloadButton);

  // Create a message container for feedback
  const messageContainer = document.createElement("p");
  messageContainer.style.marginTop = "20px";
  messageContainer.style.color = "#d9534f";
  messageContainer.style.textAlign = "center";
  appContainer.appendChild(messageContainer);

  // Append the app container to the body
  document.body.appendChild(appContainer);

  // Event listener for the download button
  downloadButton.addEventListener("click", async () => {
    const videoUrl = urlInput.value.trim();
    const format = formatSelect.value;

    // Validate the input
    if (!videoUrl) {
      messageContainer.textContent = "Please enter a valid Twitter video URL.";
      return;
    }

    try {
      // Simulate an API call to download the video
      messageContainer.textContent = "Downloading video...";
      const response = await fetch(`/api/download?url=${encodeURIComponent(videoUrl)}&format=${format}`);
      
      if (!response.ok) {
        throw new Error("Failed to download video. Please try again.");
      }

      const blob = await response.blob();
      const downloadLink = document.createElement("a");
      downloadLink.href = URL.createObjectURL(blob);
      downloadLink.download = `twitter_video.${format}`;
      downloadLink.click();

      messageContainer.textContent = "Video downloaded successfully!";
    } catch (error) {
      console.error(error);
      messageContainer.textContent = error.message || "An error occurred. Please try again.";
    }
  });
});
```
