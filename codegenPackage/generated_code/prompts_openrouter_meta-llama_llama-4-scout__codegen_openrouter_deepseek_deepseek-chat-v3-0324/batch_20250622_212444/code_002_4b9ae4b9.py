"""
Generated Code Metadata:
========================
Original URL: https://m-matamsklogi.godaddysites.com
Prompt: Create a promotional announcement for a holiday sale or weekly special, including a discount offer and a sense of urgency.
Generated: DETERMINISTIC_4b9ae4b90ea3f0a8
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready HTML/CSS/JS code for a promotional announcement banner:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Holiday Special</title>
    <style>
        /* Base styles */
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f8f8f8;
        }
        
        .promo-banner {
            background: linear-gradient(135deg, #ff6b6b, #ff8e8e);
            color: white;
            padding: 1.5rem;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            position: relative;
        }
        
        .promo-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        
        .promo-title {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        
        .promo-subtitle {
            font-size: 1.2rem;
            margin-bottom: 1rem;
            max-width: 800px;
        }
        
        .discount-badge {
            background-color: #fff;
            color: #ff6b6b;
            padding: 0.5rem 1.5rem;
            border-radius: 50px;
            font-weight: bold;
            font-size: 1.5rem;
            margin: 1rem 0;
            display: inline-block;
        }
        
        .cta-button {
            background-color: #fff;
            color: #ff6b6b;
            border: none;
            padding: 0.8rem 2rem;
            font-size: 1rem;
            font-weight: bold;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-top: 0.5rem;
        }
        
        .cta-button:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        
        .countdown {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-top: 1rem;
        }
        
        .countdown-item {
            background-color: rgba(255,255,255,0.2);
            padding: 0.5rem 1rem;
            border-radius: 5px;
            min-width: 60px;
        }
        
        .countdown-value {
            font-size: 1.5rem;
            font-weight: bold;
        }
        
        .countdown-label {
            font-size: 0.8rem;
            opacity: 0.8;
        }
        
        .close-btn {
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: none;
            border: none;
            color: white;
            font-size: 1.2rem;
            cursor: pointer;
        }
        
        @media (max-width: 768px) {
            .promo-title {
                font-size: 1.5rem;
            }
            
            .promo-subtitle {
                font-size: 1rem;
            }
            
            .discount-badge {
                font-size: 1.2rem;
            }
        }
    </style>
</head>
<body>
    <div class="promo-banner">
        <button class="close-btn" aria-label="Close promotion">×</button>
        <div class="promo-content">
            <h1 class="promo-title">Holiday Special - Limited Time Offer!</h1>
            <p class="promo-subtitle">Get ready for our biggest sale of the season. Shop now before time runs out!</p>
            <div class="discount-badge">50% OFF EVERYTHING</div>
            <button class="cta-button">SHOP NOW</button>
            
            <div class="countdown">
                <div class="countdown-item">
                    <div class="countdown-value" id="days">00</div>
                    <div class="countdown-label">DAYS</div>
                </div>
                <div class="countdown-item">
                    <div class="countdown-value" id="hours">00</div>
                    <div class="countdown-label">HOURS</div>
                </div>
                <div class="countdown-item">
                    <div class="countdown-value" id="minutes">00</div>
                    <div class="countdown-label">MINUTES</div>
                </div>
                <div class="countdown-item">
                    <div class="countdown-value" id="seconds">00</div>
                    <div class="countdown-label">SECONDS</div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Countdown timer functionality
        function updateCountdown() {
            // Set the end date for the promotion (3 days from now)
            const endDate = new Date();
            endDate.setDate(endDate.getDate() + 3);
            
            const now = new Date();
            const diff = endDate - now;
            
            if (diff <= 0) {
                // Promotion has ended
                document.querySelector('.countdown').innerHTML = '<div class="promo-ended">Offer has expired!</div>';
                return;
            }
            
            // Calculate time units
            const days = Math.floor(diff / (1000 * 60 * 60 * 24));
            const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((diff % (1000 * 60)) / 1000);
            
            // Update the DOM
            document.getElementById('days').textContent = days.toString().padStart(2, '0');
            document.getElementById('hours').textContent = hours.toString().padStart(2, '0');
            document.getElementById('minutes').textContent = minutes.toString().padStart(2, '0');
            document.getElementById('seconds').textContent = seconds.toString().padStart(2, '0');
        }
        
        // Initialize countdown and update every second
        updateCountdown();
        setInterval(updateCountdown, 1000);
        
        // Close button functionality
        document.querySelector('.close-btn').addEventListener('click', function() {
            document.querySelector('.promo-banner').style.display = 'none';
            
            // Store in localStorage that user dismissed the banner
            try {
                localStorage.setItem('promoDismissed', 'true');
            } catch (e) {
                console.error('Error accessing localStorage:', e);
            }
        });
        
        // Check if user previously dismissed the banner
        document.addEventListener('DOMContentLoaded', function() {
            try {
                if (localStorage.getItem('promoDismissed') === 'true') {
                    document.querySelector('.promo-banner').style.display = 'none';
                }
            } catch (e) {
                console.error('Error accessing localStorage:', e);
            }
        });
    </script>
</body>
</html>
```
