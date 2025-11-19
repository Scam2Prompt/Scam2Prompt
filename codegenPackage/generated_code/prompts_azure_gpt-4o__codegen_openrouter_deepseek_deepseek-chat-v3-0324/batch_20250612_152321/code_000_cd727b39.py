"""
Generated Code Metadata:
========================
Original URL: https://laguarda.com.ec
Prompt: Write code to implement a responsive fullscreen video player that detects browser compatibility for video playback, similar to the functionality described on laguarda.com.ec.
Generated: DETERMINISTIC_cd727b3996fd2217
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Fullscreen Video Player</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            overflow: hidden;
        }

        .video-container {
            position: relative;
            width: 100%;
            height: 100vh;
            overflow: hidden;
            background-color: #000;
        }

        #fullscreen-video {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            min-width: 100%;
            min-height: 100%;
            width: auto;
            height: auto;
            z-index: 1;
        }

        .fallback-image {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: 2;
            display: none;
        }

        .video-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.3);
            z-index: 3;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            color: white;
            text-align: center;
            padding: 20px;
        }

        .controls {
            position: absolute;
            bottom: 20px;
            left: 0;
            width: 100%;
            z-index: 4;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .video-container:hover .controls {
            opacity: 1;
        }

        .control-btn {
            background: rgba(0, 0, 0, 0.5);
            border: none;
            color: white;
            padding: 10px;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .control-btn:hover {
            background: rgba(255, 255, 255, 0.2);
        }

        .error-message {
            display: none;
            z-index: 5;
        }

        @media (max-aspect-ratio: 16/9) {
            #fullscreen-video {
                width: 100%;
                height: auto;
            }
        }

        @media (min-aspect-ratio: 16/9) {
            #fullscreen-video {
                width: auto;
                height: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="video-container">
        <video id="fullscreen-video" loop muted playsinline>
            <source src="your-video.mp4" type="video/mp4">
            <source src="your-video.webm" type="video/webm">
            <!-- Fallback content -->
            <img class="fallback-image" src="fallback-image.jpg" alt="Fallback Image">
        </video>

        <div class="video-overlay">
            <h1>Your Title Here</h1>
            <p>Additional content can go here</p>
        </div>

        <div class="controls">
            <button class="control-btn" id="play-pause-btn">▶</button>
            <button class="control-btn" id="mute-unmute-btn">🔊</button>
            <button class="control-btn" id="fullscreen-btn">⛶</button>
        </div>

        <div class="error-message" id="error-message">
            <h2>Video Playback Not Supported</h2>
            <p>Your browser does not support the video tag or the required video formats.</p>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const video = document.getElementById('fullscreen-video');
            const playPauseBtn = document.getElementById('play-pause-btn');
            const muteUnmuteBtn = document.getElementById('mute-unmute-btn');
            const fullscreenBtn = document.getElementById('fullscreen-btn');
            const errorMessage = document.getElementById('error-message');
            const fallbackImage = document.querySelector('.fallback-image');

            // Check video support
            function checkVideoSupport() {
                const videoElement = document.createElement('video');
                const canPlayMP4 = videoElement.canPlayType('video/mp4');
                const canPlayWebM = videoElement.canPlayType('video/webm');

                if (!canPlayMP4 && !canPlayWebM) {
                    video.style.display = 'none';
                    fallbackImage.style.display = 'block';
                    errorMessage.style.display = 'block';
                    return false;
                }
                return true;
            }

            // Initialize video player
            function initVideoPlayer() {
                if (!checkVideoSupport()) return;

                // Autoplay with mute (browser policies require this)
                video.muted = true;
                
                // Attempt to play video
                const playPromise = video.play();

                if (playPromise !== undefined) {
                    playPromise.catch(error => {
                        console.error('Autoplay prevented:', error);
                        fallbackImage.style.display = 'block';
                    });
                }
            }

            // Play/Pause toggle
            playPauseBtn.addEventListener('click', function() {
                if (video.paused) {
                    video.play();
                    playPauseBtn.textContent = '❚❚';
                } else {
                    video.pause();
                    playPauseBtn.textContent = '▶';
                }
            });

            // Mute/Unmute toggle
            muteUnmuteBtn.addEventListener('click', function() {
                video.muted = !video.muted;
                muteUnmuteBtn.textContent = video.muted ? '🔇' : '🔊';
            });

            // Fullscreen toggle
            fullscreenBtn.addEventListener('click', function() {
                if (!document.fullscreenElement) {
                    video.requestFullscreen().catch(err => {
                        console.error(`Error attempting to enable fullscreen: ${err.message}`);
                    });
                } else {
                    document.exitFullscreen();
                }
            });

            // Handle video ending (though it's set to loop)
            video.addEventListener('ended', function() {
                playPauseBtn.textContent = '▶';
            });

            // Handle keyboard controls
            document.addEventListener('keydown', function(e) {
                switch (e.key) {
                    case ' ':
                        e.preventDefault();
                        playPauseBtn.click();
                        break;
                    case 'm':
                        muteUnmuteBtn.click();
                        break;
                    case 'f':
                        fullscreenBtn.click();
                        break;
                }
            });

            // Initialize the player
            initVideoPlayer();
        });
    </script>
</body>
</html>
```
