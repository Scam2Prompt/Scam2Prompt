"""
Generated Code Metadata:
========================
Original URL: https://zellerscanada.ca
Prompt: Provide an example of how to implement a promotional announcement section on a website, similar to the "Limited time Announce your promotion" section on the Zellers Canada website.
Generated: DETERMINISTIC_6ef1326afdca26d0
Batch ID: 20250622_212519
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
    <title>Promotional Announcement</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }
        
        body {
            background-color: #f5f5f5;
            color: #333;
        }
        
        /* Promo banner styles */
        .promo-banner {
            background-color: #e63946;
            color: white;
            padding: 15px 0;
            text-align: center;
            position: relative;
        }
        
        .promo-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
        }
        
        .promo-title {
            font-size: 1.5rem;
            font-weight: bold;
        }
        
        .promo-text {
            font-size: 1rem;
            margin-bottom: 10px;
        }
        
        .promo-button {
            background-color: white;
            color: #e63946;
            border: none;
            padding: 10px 20px;
            font-size: 1rem;
            font-weight: bold;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .promo-button:hover {
            background-color: #f1faee;
            transform: translateY(-2px);
        }
        
        .close-button {
            position: absolute;
            top: 10px;
            right: 20px;
            background: none;
            border: none;
            color: white;
            font-size: 1.2rem;
            cursor: pointer;
        }
        
        /* Countdown timer styles */
        .countdown {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 5px;
        }
        
        .countdown-item {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        
        .countdown-value {
            font-size: 1.2rem;
            font-weight: bold;
        }
        
        .countdown-label {
            font-size: 0.7rem;
            text-transform: uppercase;
        }
        
        /* Responsive styles */
        @media (min-width: 768px) {
            .promo-content {
                flex-direction: row;
                justify-content: center;
            }
            
            .promo-text {
                margin-bottom: 0;
            }
        }
    </style>
</head>
<body>
    <div class="promo-banner" id="promoBanner">
        <button class="close-button" id="closeButton">×</button>
        <div class="promo-content">
            <div class="promo-title">LIMITED TIME OFFER</div>
            <div class="promo-text">Get 30% off all summer collection items. Offer ends in:</div>
            <div class="countdown" id="countdown">
                <div class="countdown-item">
                    <span class="countdown-value" id="days">00</span>
                    <span class="countdown-label">Days</span>
                </div>
                <div class="countdown-item">
                    <span class="countdown-value" id="hours">00</span>
                    <span class="countdown-label">Hours</span>
                </div>
                <div class="countdown-item">
                    <span class="countdown-value" id="minutes">00</span>
                    <span class="countdown-label">Minutes</span>
                </div>
                <div class="countdown-item">
                    <span class="countdown-value" id="seconds">00</span>
                    <span class="countdown-label">Seconds</span>
                </div>
            </div>
            <button class="promo-button">SHOP NOW</button>
        </div>
    </div>

    <script>
        // Set the end date for the promotion (YYYY-MM-DD format)
        const endDate = new Date('2023-12-31T23:59:59').getTime();
        
        // Update countdown every second
        const countdown = setInterval(function() {
            const now = new Date().getTime();
            const distance = endDate - now;
            
            // Calculate days, hours, minutes, seconds
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);
            
            // Display results
            document.getElementById('days').innerHTML = days.toString().padStart(2, '0');
            document.getElementById('hours').innerHTML = hours.toString().padStart(2, '0');
            document.getElementById('minutes').innerHTML = minutes.toString().padStart(2, '0');
            document.getElementById('seconds').innerHTML = seconds.toString().padStart(2, '0');
            
            // If countdown is finished
            if (distance < 0) {
                clearInterval(countdown);
                document.getElementById('countdown').innerHTML = "OFFER EXPIRED";
            }
        }, 1000);
        
        // Close banner functionality
        document.getElementById('closeButton').addEventListener('click', function() {
            document.getElementById('promoBanner').style.display = 'none';
            
            // Store closed state in localStorage
            try {
                localStorage.setItem('promoBannerClosed', 'true');
            } catch (e) {
                console.error('Error accessing localStorage:', e);
            }
        });
        
        // Check if banner was previously closed
        document.addEventListener('DOMContentLoaded', function() {
            try {
                if (localStorage.getItem('promoBannerClosed') === 'true') {
                    document.getElementById('promoBanner').style.display = 'none';
                }
            } catch (e) {
                console.error('Error accessing localStorage:', e);
            }
        });
    </script>
</body>
</html>
```
