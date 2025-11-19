"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ksaacademy-classera.classera.com
Prompt: Generate a code snippet that demonstrates how to implement a loading screen similar to the one described on Classera's KSA Academy webpage.
Generated: DETERMINISTIC_2ea5701e12a3fc5b
Batch ID: 20250612_160823
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
    <title>Loading Screen Example</title>
    <style>
        /* Basic reset and full-height style for body */
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #f0f0f0; /* Light background for contrast */
            font-family: Arial, sans-serif;
        }

        /* Loading screen container */
        .loading-screen {
            display: none; /* Initially hidden */
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent background */
            z-index: 9999; /* Ensure it covers other elements */
            justify-content: center;
            align-items: center;
        }

        /* Spinner styles */
        .spinner {
            border: 8px solid #ddd; /* Light border */
            border-top: 8px solid #3498db; /* Blue top border */
            border-radius: 50%;
            width: 60px; /* Width of the spinner */
            height: 60px; /* Height of the spinner */
            animation: spin 1s linear infinite; /* Animation for spinning */
        }

        /* Spinner rotation animation */
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <!-- Loading screen element -->
    <div class="loading-screen" id="loadingScreen">
        <div class="spinner"></div>
    </div>

    <div id="content" style="display: none;">
        <!-- Main content of the page goes here -->
        <h1>Welcome to KSA Academy</h1>
        <p>This is a sample application demonstrating a loading screen.</p>
    </div>

    <script>
        // Function to show the loading screen
        function showLoadingScreen() {
            const loadingScreen = document.getElementById('loadingScreen');
            loadingScreen.style.display = 'flex'; // Show loading screen
        }

        // Function to hide the loading screen
        function hideLoadingScreen() {
            const loadingScreen = document.getElementById('loadingScreen');
            loadingScreen.style.display = 'none'; // Hide loading screen
        }

        // Simulate content loading
        function loadContent() {
            showLoadingScreen(); // Display the loading screen

            // Simulating a network request with setTimeout
            setTimeout(() => {
                hideLoadingScreen(); // Hide loading screen after loading
                document.getElementById('content').style.display = 'block'; // Show content
            }, 3000); // 3 seconds delay
        }

        // Start loading the content when the page is fully loaded
        window.addEventListener('load', loadContent);
    </script>
</body>
</html>
```
