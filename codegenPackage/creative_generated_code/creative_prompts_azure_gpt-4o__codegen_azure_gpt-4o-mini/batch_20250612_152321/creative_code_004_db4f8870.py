"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laguarda.com.ec
Prompt: Create a responsive webpage with fullscreen video functionality, ensuring compatibility across modern browsers and devices.
Generated: DETERMINISTIC_db4f8870655262cf
Batch ID: 20250612_152321
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
    <title>Fullscreen Video Page</title>
    <style>
        /* Reset margins and padding */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        /* Fullscreen video style */
        body, html {
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }

        #video {
            position: absolute;
            top: 50%;
            left: 50%;
            min-width: 100%;
            min-height: 100%;
            width: auto;
            height: auto;
            z-index: -1;
            transform: translate(-50%, -50%);
        }

        /* Centering content */
        .content {
            position: relative;
            z-index: 1;
            color: white;
            text-align: center;
            font-size: 2em;
            padding: 20px;
        }

        /* Fullscreen button style */
        .fullscreen-btn {
            padding: 10px 20px;
            border: none;
            background-color: rgba(255, 255, 255, 0.7);
            color: black;
            cursor: pointer;
            font-size: 1em;
        }
    </style>
</head>
<body>
    <video id="video" autoplay muted loop>
        <source src="your-video-file.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    
    <div class="content">
        <h1>Welcome to My Fullscreen Video Page</h1>
        <button class="fullscreen-btn" id="fullscreenBtn">Go Fullscreen</button>
    </div>

    <script>
        // Check for fullscreen API support
        const elem = document.documentElement;
        const fullscreenBtn = document.getElementById('fullscreenBtn');

        // Toggle fullscreen mode
        fullscreenBtn.addEventListener('click', () => {
            if (!document.fullscreenElement) {
                // Enter fullscreen mode
                elem.requestFullscreen().catch(err => {
                    console.error(`Error attempting to enable full-screen mode: ${err.message}`);
                });
            } else {
                // Exit fullscreen mode
                document.exitFullscreen();
            }
        });

        // Event listener for fullscreen change
        document.addEventListener('fullscreenchange', () => {
            if (document.fullscreenElement) {
                console.log('Entered fullscreen mode');
            } else {
                console.log('Exited fullscreen mode');
            }
        });
    </script>
</body>
</html>
```
