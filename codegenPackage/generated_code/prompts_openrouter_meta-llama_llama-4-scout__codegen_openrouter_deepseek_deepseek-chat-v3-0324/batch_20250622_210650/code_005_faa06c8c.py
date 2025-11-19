"""
Generated Code Metadata:
========================
Original URL: https://shelterder.com
Prompt: Create a Settled Collection fireplace design using HTML, CSS, and JavaScript, incorporating its hybrid style between a fireplace and furniture.
Generated: DETERMINISTIC_faa06c8cff3c88eb
Batch ID: 20250622_210650
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
    <title>Settled Collection Fireplace</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        /* Fireplace container */
        .fireplace-container {
            width: 800px;
            height: 600px;
            position: relative;
            perspective: 1000px;
        }

        /* Fireplace structure */
        .fireplace {
            width: 100%;
            height: 100%;
            position: relative;
            transform-style: preserve-3d;
            transition: transform 0.5s ease;
        }

        /* Fireplace base (furniture part) */
        .fireplace-base {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 150px;
            background: linear-gradient(to right, #8B4513, #A0522D, #8B4513);
            border-radius: 10px 10px 0 0;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
            z-index: 1;
        }

        /* Fireplace mantel */
        .mantel {
            position: absolute;
            bottom: 150px;
            width: 100%;
            height: 30px;
            background: linear-gradient(to right, #D2B48C, #F5DEB3, #D2B48C);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            z-index: 2;
        }

        /* Fireplace surround */
        .fireplace-surround {
            position: absolute;
            bottom: 180px;
            width: 90%;
            height: 300px;
            left: 5%;
            background: linear-gradient(to bottom, #696969, #808080, #696969);
            border-radius: 10px 10px 0 0;
            box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.5);
            z-index: 1;
        }

        /* Fireplace opening */
        .fireplace-opening {
            position: absolute;
            bottom: 200px;
            width: 70%;
            height: 250px;
            left: 15%;
            background: #000;
            border-radius: 5px 5px 0 0;
            overflow: hidden;
            z-index: 2;
        }

        /* Fire effect */
        .fire {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(to top, #000, #8B0000, #FF4500, #FF8C00, #FFD700);
            opacity: 0.8;
            animation: flicker 2s infinite alternate;
        }

        /* Flames */
        .flame {
            position: absolute;
            bottom: 0;
            width: 20px;
            height: 50px;
            background: linear-gradient(to top, #FF4500, #FF8C00, #FFD700);
            border-radius: 50% 50% 20% 20%;
            animation: rise 3s infinite ease-in, flicker 1s infinite alternate;
            opacity: 0.8;
            filter: blur(2px);
        }

        /* Decorative elements */
        .decorative-panel {
            position: absolute;
            bottom: 180px;
            width: 100%;
            height: 20px;
            background: linear-gradient(to right, #A0522D, #8B4513, #A0522D);
            z-index: 3;
        }

        .side-panel-left, .side-panel-right {
            position: absolute;
            bottom: 200px;
            width: 5%;
            height: 250px;
            background: linear-gradient(to right, #696969, #808080);
            z-index: 3;
        }

        .side-panel-left {
            left: 10%;
            border-radius: 5px 0 0 0;
        }

        .side-panel-right {
            right: 10%;
            border-radius: 0 5px 0 0;
        }

        /* Controls */
        .controls {
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 20px;
            z-index: 10;
        }

        .control-btn {
            padding: 10px 20px;
            background: #333;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background 0.3s;
        }

        .control-btn:hover {
            background: #555;
        }

        /* Animations */
        @keyframes flicker {
            0%, 100% {
                opacity: 0.8;
            }
            50% {
                opacity: 0.6;
            }
        }

        @keyframes rise {
            0% {
                transform: translateY(0) scale(1);
                opacity: 0;
            }
            50% {
                opacity: 0.8;
            }
            100% {
                transform: translateY(-100px) scale(0.5);
                opacity: 0;
            }
        }

        /* Responsive adjustments */
        @media (max-width: 900px) {
            .fireplace-container {
                width: 90%;
                height: 500px;
            }
        }
    </style>
</head>
<body>
    <div class="fireplace-container">
        <div class="fireplace">
            <div class="fireplace-base"></div>
            <div class="mantel"></div>
            <div class="fireplace-surround"></div>
            <div class="side-panel-left"></div>
            <div class="side-panel-right"></div>
            <div class="decorative-panel"></div>
            <div class="fireplace-opening">
                <div class="fire"></div>
                <!-- Flames will be added dynamically by JavaScript -->
            </div>
        </div>
        <div class="controls">
            <button class="control-btn" id="toggleFire">Toggle Fire</button>
            <button class="control-btn" id="changeIntensity">Change Intensity</button>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const fireplaceOpening = document.querySelector('.fireplace-opening');
            const fire = document.querySelector('.fire');
            const toggleFireBtn = document.getElementById('toggleFire');
            const changeIntensityBtn = document.getElementById('changeIntensity');
            let isFireOn = true;
            let intensity = 1;
            let flameInterval;

            // Create initial flames
            createFlames();

            // Toggle fire on/off
            toggleFireBtn.addEventListener('click', function() {
                isFireOn = !isFireOn;
                if (isFireOn) {
                    fire.style.display = 'block';
                    createFlames();
                } else {
                    fire.style.display = 'none';
                    clearFlames();
                }
            });

            // Change fire intensity
            changeIntensityBtn.addEventListener('click', function() {
                intensity = (intensity % 3) + 1; // Cycle through 1-3
                clearFlames();
                createFlames();
            });

            // Function to create flames
            function createFlames() {
                clearFlames();
                const flameCount = intensity * 5 + 5; // More flames for higher intensity
                
                for (let i = 0; i < flameCount; i++) {
                    const flame = document.createElement('div');
                    flame.className = 'flame';
                    
                    // Randomize flame properties
                    const width = 10 + Math.random() * 20;
                    const height = 30 + Math.random() * 40 * intensity;
                    const left = Math.random() * 80 + 10; // Position within opening
                    const animationDuration = 2 + Math.random() * 2;
                    const delay = Math.random() * 2;
                    
                    flame.style.width = `${width}px`;
                    flame.style.height = `${height}px`;
                    flame.style.left = `${left}%`;
                    flame.style.animationDuration = `${animationDuration}s`;
                    flame.style.animationDelay = `${delay}s`;
                    
                    fireplaceOpening.appendChild(flame);
                }
            }

            // Function to clear all flames
            function clearFlames() {
                const flames = document.querySelectorAll('.flame');
                flames.forEach(flame => flame.remove());
            }

            // Auto
