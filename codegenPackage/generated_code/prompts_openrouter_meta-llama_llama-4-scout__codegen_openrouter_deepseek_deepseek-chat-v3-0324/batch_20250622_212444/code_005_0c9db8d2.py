"""
Generated Code Metadata:
========================
Original URL: https://m-matamsklogi.godaddysites.com
Prompt: Design a webpage section that showcases a big sale or on-site event, including details about the event and a call-to-action.
Generated: DETERMINISTIC_0c9db8d2366c1868
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready HTML and CSS implementation for a sale/event showcase section:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Big Summer Sale Event</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        }

        /* Event banner container */
        .event-banner {
            background: linear-gradient(135deg, #ff6b6b, #ff8e53);
            color: white;
            padding: 3rem 2rem;
            border-radius: 8px;
            max-width: 1200px;
            margin: 2rem auto;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            position: relative;
            overflow: hidden;
        }

        /* Decorative elements */
        .event-banner::before {
            content: '';
            position: absolute;
            top: -50px;
            right: -50px;
            width: 200px;
            height: 200px;
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
        }

        .event-banner::after {
            content: '';
            position: absolute;
            bottom: -30px;
            left: -30px;
            width: 100px;
            height: 100px;
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
        }

        /* Content layout */
        .event-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            position: relative;
            z-index: 1;
        }

        /* Event title */
        .event-title {
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 1rem;
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
        }

        /* Event subtitle */
        .event-subtitle {
            font-size: 1.25rem;
            font-weight: 500;
            margin-bottom: 1.5rem;
            max-width: 700px;
        }

        /* Event details */
        .event-details {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 2rem;
            margin-bottom: 2rem;
        }

        .detail-item {
            background-color: rgba(255, 255, 255, 0.2);
            padding: 1rem 1.5rem;
            border-radius: 6px;
            font-weight: 600;
        }

        /* Countdown timer */
        .countdown {
            display: flex;
            gap: 1rem;
            margin-bottom: 2rem;
        }

        .countdown-item {
            background-color: white;
            color: #ff6b6b;
            padding: 0.75rem 1rem;
            border-radius: 6px;
            font-weight: 700;
            min-width: 70px;
        }

        .countdown-label {
            font-size: 0.75rem;
            opacity: 0.8;
        }

        /* Call-to-action button */
        .cta-button {
            background-color: white;
            color: #ff6b6b;
            border: none;
            padding: 1rem 2.5rem;
            font-size: 1.1rem;
            font-weight: 700;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
        }

        .cta-button:active {
            transform: translateY(0);
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .event-title {
                font-size: 2rem;
            }
            
            .event-subtitle {
                font-size: 1rem;
            }
            
            .detail-item {
                padding: 0.75rem 1rem;
                font-size: 0.9rem;
            }
            
            .countdown {
                gap: 0.5rem;
            }
            
            .countdown-item {
                min-width: 60px;
                padding: 0.5rem 0.75rem;
            }
        }
    </style>
</head>
<body>
    <section class="event-banner">
        <div class="event-content">
            <h1 class="event-title">SUMMER SALE EXTRAVAGANZA</h1>
            <p class="event-subtitle">Huge discounts on all products - up to 70% off! Limited time offer ends soon.</p>
            
            <div class="event-details">
                <div class="detail-item">📍 Downtown Showroom</div>
                <div class="detail-item">📅 June 15-20, 2023</div>
                <div class="detail-item">⏰ 9AM - 9PM Daily</div>
            </div>
            
            <div class="countdown">
                <div class="countdown-item">
                    <div id="days">05</div>
                    <div class="countdown-label">DAYS</div>
                </div>
                <div class="countdown-item">
                    <div id="hours">12</div>
                    <div class="countdown-label">HOURS</div>
                </div>
                <div class="countdown-item">
                    <div id="minutes">45</div>
                    <div class="countdown-label">MIN</div>
                </div>
                <div class="countdown-item">
                    <div id="seconds">30</div>
                    <div class="countdown-label">SEC</div>
                </div>
            </div>
            
            <button class="cta-button">SHOP THE SALE NOW</button>
        </div>
    </section>

    <script>
        // Countdown timer functionality
        function updateCountdown() {
            const eventDate = new Date('June 20, 2023 23:59:59').getTime();
            const now = new Date().getTime();
            const distance = eventDate - now;

            // Calculate days, hours, minutes, seconds
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Update the DOM
            document.getElementById('days').textContent = days.toString().padStart(2, '0');
            document.getElementById('hours').textContent = hours.toString().padStart(2, '0');
            document.getElementById('minutes').textContent = minutes.toString().padStart(2, '0');
            document.getElementById('seconds').textContent = seconds.toString().padStart(2, '0');

            // If the countdown is finished
            if (distance < 0) {
                clearInterval(countdownTimer);
                document.querySelector('.countdown').innerHTML = '<div class="detail-item">The sale has ended!</div>';
            }
        }

        // Initialize and update countdown every second
        updateCountdown();
        const countdownTimer = setInterval(updateCountdown, 1000);

        // CTA button event listener
        document.querySelector('.cta-button').addEventListener('click', function() {
            // In a real implementation, this would redirect to the sale page
            console.log('Redirecting to sale page...');
            // window.location.href = '/sale';
        });
    </script>
</body>
</html>
```
