"""
Generated Code Metadata:
========================
Original URL: https://aibanshee.com
Prompt: Generate HTML and CSS code for a "Split Slider Home" layout with responsive design, inspired by the unique solutions mentioned on the IMST Telehealth webpage.
Generated: DETERMINISTIC_808969cdaa96c1da
Batch ID: 20250612_150013
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
    <title>Split Slider Home</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            overflow-x: hidden;
        }

        /* Split slider container */
        .split-slider {
            display: flex;
            height: 100vh;
            position: relative;
        }

        /* Individual panels */
        .panel {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            transition: all 0.6s cubic-bezier(0.645, 0.045, 0.355, 1);
            position: relative;
            overflow: hidden;
            padding: 20px;
            color: white;
            text-align: center;
        }

        /* Panel content */
        .panel-content {
            max-width: 600px;
            padding: 20px;
            z-index: 2;
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.6s 0.3s;
        }

        .panel.active .panel-content {
            opacity: 1;
            transform: translateY(0);
        }

        /* Panel backgrounds */
        .panel::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-size: cover;
            background-position: center;
            z-index: 1;
            transition: all 0.6s cubic-bezier(0.645, 0.045, 0.355, 1);
        }

        /* Individual panel styling */
        .panel-1::before {
            background-color: #3498db;
            background-image: linear-gradient(rgba(52, 152, 219, 0.8), rgba(52, 152, 219, 0.8));
        }

        .panel-2::before {
            background-color: #e74c3c;
            background-image: linear-gradient(rgba(231, 76, 60, 0.8), rgba(231, 76, 60, 0.8));
        }

        /* Panel headings */
        .panel h2 {
            font-size: 2.5rem;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        .panel p {
            font-size: 1.1rem;
            line-height: 1.6;
            margin-bottom: 30px;
        }

        /* Panel buttons */
        .panel-btn {
            display: inline-block;
            padding: 12px 30px;
            background: transparent;
            border: 2px solid white;
            color: white;
            text-decoration: none;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.3s;
        }

        .panel-btn:hover {
            background: white;
            color: #333;
        }

        /* Navigation controls */
        .slider-controls {
            position: absolute;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            z-index: 10;
        }

        .control-btn {
            width: 12px;
            height: 12px;
            margin: 0 8px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.5);
            cursor: pointer;
            transition: all 0.3s;
        }

        .control-btn.active {
            background: white;
            transform: scale(1.2);
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .split-slider {
                flex-direction: column;
                height: auto;
            }

            .panel {
                min-height: 100vh;
            }

            .panel-content {
                opacity: 1;
                transform: translateY(0);
            }

            .slider-controls {
                display: none;
            }
        }

        @media (max-width: 480px) {
            .panel h2 {
                font-size: 1.8rem;
            }

            .panel p {
                font-size: 1rem;
            }
        }
    </style>
</head>
<body>
    <div class="split-slider">
        <!-- First Panel -->
        <div class="panel panel-1 active">
            <div class="panel-content">
                <h2>Innovative Solutions</h2>
                <p>Discover cutting-edge technology designed to transform your experience with seamless integration and intuitive design.</p>
                <a href="#" class="panel-btn">Learn More</a>
            </div>
        </div>

        <!-- Second Panel -->
        <div class="panel panel-2">
            <div class="panel-content">
                <h2>Telehealth Services</h2>
                <p>Access professional healthcare services from the comfort of your home with our secure and reliable platform.</p>
                <a href="#" class="panel-btn">Get Started</a>
            </div>
        </div>

        <!-- Navigation Controls -->
        <div class="slider-controls">
            <div class="control-btn active" data-index="0"></div>
            <div class="control-btn" data-index="1"></div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const panels = document.querySelectorAll('.panel');
            const controlBtns = document.querySelectorAll('.control-btn');
            let currentIndex = 0;

            // Function to update slider
            function updateSlider(index) {
                // Update panels
                panels.forEach((panel, i) => {
                    panel.classList.toggle('active', i === index);
                });

                // Update controls
                controlBtns.forEach((btn, i) => {
                    btn.classList.toggle('active', i === index);
                });

                currentIndex = index;
            }

            // Control button click events
            controlBtns.forEach(btn => {
                btn.addEventListener('click', function() {
                    const index = parseInt(this.getAttribute('data-index'));
                    updateSlider(index);
                });
            });

            // Auto-rotate slider (optional)
            let sliderInterval = setInterval(() => {
                const nextIndex = (currentIndex + 1) % panels.length;
                updateSlider(nextIndex);
            }, 5000);

            // Pause on hover
            const sliderContainer = document.querySelector('.split-slider');
            sliderContainer.addEventListener('mouseenter', () => {
                clearInterval(sliderInterval);
            });

            sliderContainer.addEventListener('mouseleave', () => {
                sliderInterval = setInterval(() => {
                    const nextIndex = (currentIndex + 1) % panels.length;
                    updateSlider(nextIndex);
                }, 5000);
            });

            // Touch support for mobile
            let touchStartX = 0;
            let touchEndX = 0;

            sliderContainer.addEventListener('touchstart', e => {
                touchStartX = e.changedTouches[0].screenX;
            }, {passive: true});

            sliderContainer.addEventListener('touchend', e => {
                touchEndX = e.changedTouches[0].screenX;
                handleSwipe();
            }, {passive: true});

            function handleSwipe() {
                if (touchEndX < touchStartX - 50) {
                    // Swipe left
                    const nextIndex = (currentIndex + 1) % panels.length;
                    updateSlider(nextIndex);
                } else if (touchEndX > touchStartX + 50) {
                    // Swipe right
                    const prevIndex = (currentIndex - 1 + panels.length) % panels.length;
                    updateSlider(prevIndex);
                }
            }
        });
    </script>
</body>
</html>
```
