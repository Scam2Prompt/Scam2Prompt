"""
Generated Code Metadata:
========================
Original URL: https://lifes.quest
Prompt: Create a simple web page using HTML and CSS that displays a "share the gospel" message, similar to the one on lifes.quest, and includes a call-to-action to share the message with others.
Generated: DETERMINISTIC_402bb2d74647dd57
Batch ID: 20250622_210108
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
    <title>Share the Gospel</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
            padding: 20px;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }

        /* Main content container */
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: white;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            flex: 1;
        }

        /* Header styles */
        header {
            text-align: center;
            margin-bottom: 30px;
        }

        h1 {
            color: #2c3e50;
            margin-bottom: 15px;
            font-size: 2.2rem;
        }

        .subtitle {
            color: #7f8c8d;
            font-size: 1.1rem;
        }

        /* Content section */
        .content {
            margin-bottom: 30px;
        }

        .message {
            background-color: #f8f9fa;
            border-left: 4px solid #3498db;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 0 5px 5px 0;
        }

        .message h2 {
            color: #3498db;
            margin-bottom: 10px;
        }

        .message p {
            margin-bottom: 10px;
        }

        /* Call to action section */
        .cta {
            text-align: center;
            margin-top: 30px;
            padding: 20px;
            background-color: #e8f4fc;
            border-radius: 5px;
        }

        .cta h2 {
            color: #2c3e50;
            margin-bottom: 15px;
        }

        .share-buttons {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 20px;
        }

        .btn {
            display: inline-block;
            padding: 10px 20px;
            background-color: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            transition: background-color 0.3s;
        }

        .btn:hover {
            background-color: #2980b9;
        }

        .btn-secondary {
            background-color: #95a5a6;
        }

        .btn-secondary:hover {
            background-color: #7f8c8d;
        }

        /* Footer */
        footer {
            text-align: center;
            margin-top: 30px;
            color: #7f8c8d;
            font-size: 0.9rem;
        }

        /* Responsive adjustments */
        @media (max-width: 600px) {
            .container {
                padding: 20px;
            }

            h1 {
                font-size: 1.8rem;
            }

            .share-buttons {
                flex-direction: column;
                align-items: center;
            }

            .btn {
                width: 100%;
                text-align: center;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Share the Good News</h1>
            <p class="subtitle">A message of hope and salvation</p>
        </header>

        <div class="content">
            <div class="message">
                <h2>The Gospel Message</h2>
                <p>God loves you and created you to know Him personally. He has a wonderful plan for your life.</p>
                <p>But we have all sinned and fallen short of God's perfect standard. Our sin separates us from God.</p>
                <p>Jesus Christ, God's Son, died on the cross for our sins and rose from the dead. Through Him, we can be reconciled to God.</p>
                <p>By receiving Jesus Christ as your Lord and Savior, you can know God personally and experience His love and forgiveness.</p>
            </div>
        </div>

        <div class="cta">
            <h2>Share This Message</h2>
            <p>Help others discover this life-changing truth by sharing this message with your friends and family.</p>
            
            <div class="share-buttons">
                <a href="#" class="btn" id="share-btn">Share Now</a>
                <a href="#" class="btn btn-secondary">Learn More</a>
            </div>
        </div>

        <footer>
            <p>&copy; 2023 Share the Gospel. All rights reserved.</p>
        </footer>
    </div>

    <script>
        // Simple share functionality
        document.getElementById('share-btn').addEventListener('click', function() {
            if (navigator.share) {
                navigator.share({
                    title: 'Share the Gospel',
                    text: 'Check out this message of hope and salvation!',
                    url: window.location.href
                }).catch(err => {
                    console.error('Error sharing:', err);
                    alert('Could not share at this time. Please try again later.');
                });
            } else {
                // Fallback for browsers that don't support Web Share API
                alert('Please use your browser\'s share options or copy this URL: ' + window.location.href);
            }
        });
    </script>
</body>
</html>
```
