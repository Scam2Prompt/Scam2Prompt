"""
Generated Code Metadata:
========================
Original URL: https://yyy-60q.pages.dev
Prompt: "Create a JavaScript code example for embedding a one-time quest directly into a product using Layer3's quest embeds feature with 2 lines of code."
Generated: DETERMINISTIC_5b7ad0ae28d200e6
Batch ID: 20250622_204551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the Layer3 SDK
import { Layer3 } from '@layer3/layer3-sdk';

// Function to embed a one-time quest
function embedQuest(questId, userAddress) {
  try {
    // Initialize the Layer3 instance
    const layer3 = new Layer3({
      // Your API key (replace with your own)
      apiKey: 'YOUR_API_KEY',
    });

    // Embed the quest directly into your product
    layer3.embedQuest({
      questId,
      userAddress,
      // Optional: Customize the embed UI
      embedOptions: {
        width: '100%',
        height: '500px',
      },
    })
      .then((embedUrl) => {
        // Handle the embed URL
        console.log('Quest embed URL:', embedUrl);
        // Example usage: Append the iframe to your webpage
        const iframe = document.createElement('iframe');
        iframe.src = embedUrl;
        iframe.width = '100%';
        iframe.height = '500px';
        document.body.appendChild(iframe);
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error embedding quest:', error);
      });
  } catch (error) {
    console.error('Error initializing Layer3:', error);
  }
}

// Example usage
const questId = 'YOUR_QUEST_ID';
const userAddress = '0xUserAddress';
embedQuest(questId, userAddress);
```
