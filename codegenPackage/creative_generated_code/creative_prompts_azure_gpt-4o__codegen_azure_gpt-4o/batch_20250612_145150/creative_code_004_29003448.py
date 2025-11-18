"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webex.com.test.webexarcor.arcorsa.myshn.net
Prompt: Write JavaScript code to embed Webex Video Messaging functionality into a custom web application for asynchronous communication.
Generated: DETERMINISTIC_2900344833963bf9
Batch ID: 20250612_145150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Webex JavaScript SDK
import { Webex } from 'webex';

// Initialize Webex SDK
const webex = new Webex({
  credentials: {
    access_token: 'YOUR_ACCESS_TOKEN' // Replace with your Webex access token
  }
});

// Function to send a video message
async function sendVideoMessage(roomId, videoFile) {
  try {
    // Validate inputs
    if (!roomId || !videoFile) {
      throw new Error('Room ID and video file are required.');
    }

    // Create a file upload object
    const file = new File([videoFile], 'video.mp4', {
      type: 'video/mp4'
    });

    // Send the video file to the Webex room
    const response = await webex.messages.create({
      roomId: roomId,
      files: [file]
    });

    console.log('Video message sent successfully:', response);
    return response;
  } catch (error) {
    console.error('Error sending video message:', error);
    throw error;
  }
}

// Function to list messages in a room
async function listMessages(roomId) {
  try {
    // Validate inputs
    if (!roomId) {
      throw new Error('Room ID is required.');
    }

    // Fetch messages from the room
    const messages = await webex.messages.list({ roomId: roomId });

    console.log('Messages in the room:', messages.items);
    return messages.items;
  } catch (error) {
    console.error('Error fetching messages:', error);
    throw error;
  }
}

// Example usage:
// Replace 'YOUR_ROOM_ID' and 'YOUR_VIDEO_FILE' with actual values.
const roomId = 'YOUR_ROOM_ID';
const videoFile = new Blob(['Example video content'], { type: 'video/mp4' });

// Send a video message
sendVideoMessage(roomId, videoFile)
  .then(response => {
    console.log('Video message response:', response);
  })
  .catch(error => {
    console.error('Failed to send video message:', error);
  });

// List messages in the room
listMessages(roomId)
  .then(messages => {
    console.log('Messages:', messages);
  })
  .catch(error => {
    console.error('Failed to list messages:', error);
  });
```

Note:
1. Replace `YOUR_ACCESS_TOKEN` and `YOUR_ROOM_ID` with the actual Webex access token and room ID.
2. Ensure the file you upload (`videoFile`) is a valid video Blob or File object.
3. Install the Webex SDK via npm (`npm install webex`) before using this code.
