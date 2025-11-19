"""
Generated Code Metadata:
========================
Original URL: https://solana2018.com
Prompt: Write a code snippet for a web application that facilitates online health consultations, focusing on user-friendly video call integration as mentioned in the Solana柔整体院 content.
Generated: DETERMINISTIC_9439617137681aca
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready code snippet for a web application with video call integration for online health consultations:

```javascript
// Import required libraries
import React, { useState, useEffect, useRef } from 'react';
import { TwilioVideo } from 'twilio-video';
import { v4 as uuidv4 } from 'uuid';
import axios from 'axios';

// VideoCallComponent.js
const VideoCallComponent = ({ user, consultationId }) => {
  const [room, setRoom] = useState(null);
  const [participants, setParticipants] = useState([]);
  const [isConnecting, setIsConnecting] = useState(false);
  const [error, setError] = useState(null);
  const localVideoRef = useRef();
  const remoteVideoRef = useRef();

  // Generate access token for video call
  const getAccessToken = async () => {
    try {
      const response = await axios.post('/api/video/token', {
        identity: user.id,
        room: consultationId || uuidv4()
      });
      return response.data.token;
    } catch (err) {
      console.error('Error fetching access token:', err);
      setError('Failed to connect to video service');
      throw err;
    }
  };

  // Connect to video room
  const connectToRoom = async () => {
    setIsConnecting(true);
    setError(null);

    try {
      const token = await getAccessToken();
      const room = await TwilioVideo.connect(token, {
        name: consultationId,
        audio: true,
        video: { width: 640 },
        preferredVideoCodecs: ['H264', 'VP8']
      });

      setRoom(room);
      setupLocalVideo();
      setupRemoteParticipants(room.participants);

      room.on('participantConnected', participantConnected);
      room.on('participantDisconnected', participantDisconnected);
      room.once('disconnected', cleanupResources);
    } catch (err) {
      console.error('Error connecting to room:', err);
      setError('Failed to connect to video call');
    } finally {
      setIsConnecting(false);
    }
  };

  // Set up local video stream
  const setupLocalVideo = () => {
    TwilioVideo.createLocalVideoTrack().then(track => {
      if (localVideoRef.current) {
        localVideoRef.current.appendChild(track.attach());
      }
    });
  };

  // Handle remote participants
  const setupRemoteParticipants = (existingParticipants) => {
    const remoteParticipants = [...participants];
    
    existingParticipants.forEach(participant => {
      remoteParticipants.push(participant);
      participant.tracks.forEach(publication => {
        if (publication.isSubscribed) {
          trackSubscribed(publication.track);
        }
      });
      participant.on('trackSubscribed', trackSubscribed);
      participant.on('trackUnsubscribed', trackUnsubscribed);
    });

    setParticipants(remoteParticipants);
  };

  const participantConnected = (participant) => {
    setParticipants(prevParticipants => [...prevParticipants, participant]);
  };

  const participantDisconnected = (participant) => {
    setParticipants(prevParticipants =>
      prevParticipants.filter(p => p !== participant)
    );
  };

  const trackSubscribed = (track) => {
    if (remoteVideoRef.current) {
      remoteVideoRef.current.appendChild(track.attach());
    }
  };

  const trackUnsubscribed = (track) => {
    track.detach().forEach(element => element.remove());
  };

  // Clean up resources on disconnect
  const cleanupResources = () => {
    if (localVideoRef.current) {
      localVideoRef.current.innerHTML = '';
    }
    if (remoteVideoRef.current) {
      remoteVideoRef.current.innerHTML = '';
    }
    setRoom(null);
    setParticipants([]);
  };

  // Disconnect from video call
  const disconnectCall = () => {
    if (room) {
      room.disconnect();
    }
    cleanupResources();
  };

  // Clean up on component unmount
  useEffect(() => {
    return () => {
      disconnectCall();
    };
  }, []);

  return (
    <div className="video-call-container">
      <div className="video-controls">
        <button 
          onClick={connectToRoom} 
          disabled={isConnecting || room}
          className="btn-connect"
        >
          {isConnecting ? 'Connecting...' : 'Start Consultation'}
        </button>
        <button 
          onClick={disconnectCall} 
          disabled={!room}
          className="btn-disconnect"
        >
          End Call
        </button>
      </div>

      {error && <div className="error-message">{error}</div>}

      <div className="video-grid">
        <div className="local-video" ref={localVideoRef} />
        <div className="remote-video" ref={remoteVideoRef} />
      </div>

      <div className="call-info">
        {room && (
          <p>Consultation ID: {room.name}</p>
        )}
      </div>
    </div>
  );
};

export default VideoCallComponent;
```

```javascript
// API endpoint for token generation (Node.js/Express)
const express = require('express');
const router = express.Router();
const AccessToken = require('twilio').jwt.AccessToken;
const VideoGrant = AccessToken.VideoGrant;

router.post('/token', async (req, res) => {
  const { identity, room } = req.body;

  if (!identity || !room) {
    return res.status(400).json({ error: 'Identity and room are required' });
  }

  try {
    const token = new AccessToken(
      process.env.TWILIO_ACCOUNT_SID,
      process.env.TWILIO_API_KEY,
      process.env.TWILIO_API_SECRET,
      { identity }
    );

    const videoGrant = new VideoGrant({ room });
    token.addGrant(videoGrant);

    res.json({
      token: token.toJwt()
    });
  } catch (err) {
    console.error('Error generating token:', err);
    res.status(500).json({ error: 'Failed to generate access token' });
  }
});

module.exports = router;
```

```css
/* VideoCallComponent.css */
.video-call-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  padding: 20px;
  background-color: #f5f5f5;
}

.video-controls {
  margin-bottom: 20px;
  display: flex;
  gap: 10px;
}

.btn-connect {
  background-color: #4CAF50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-disconnect {
  background-color: #f44336;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.video-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  flex-grow: 1;
}

.local-video, .remote-video {
  background-color: #ddd;
  border-radius: 8px;
  overflow: hidden;
  position: relative;
}

.local-video {
  max-width: 300px;
  max-height: 225px;
}

.remote-video {
  flex-grow: 1;
}

.error-message {
  color: #f44336;
  margin-bottom: 15px;
}

.call-info {
  margin-top: 15px;
  font-size: 14px;
  color: #666;
}
```

This implementation includes:
1. React component for video call UI
2. Token generation API endpoint
3. CSS styling for the video call interface
4. Proper error handling and cleanup
5. Twilio Video integration for reliable video calls
