"""
Generated Code Metadata:
========================
Original URL: https://dacarlaw.com
Prompt: Write code to implement a countdown timer for a website template using the PopularFX theme, as described on the Dacarlaw website.
Generated: DETERMINISTIC_4160b1420e140d3f
Batch ID: 20250612_154954
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
    <title>Countdown Timer</title>
    <style>
        .countdown-container {
            font-family: 'Poppins', sans-serif;
            text-align: center;
            margin: 2rem auto;
            max-width: 800px;
            padding: 2rem;
            background: #f8f9fa;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .countdown-title {
            font-size: 2rem;
            color: #333;
            margin-bottom: 1.5rem;
        }
        
        .countdown-timer {
            display: flex;
            justify-content: center;
            gap: 1rem;
        }
        
        .countdown-item {
            background: #fff;
            padding: 1rem;
            border-radius: 8px;
            min-width: 80px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        
        .countdown-value {
            font-size: 2.5rem;
            font-weight: bold;
            color: #007bff;
        }
        
        .countdown-label {
            font-size: 0.9rem;
            color: #666;
            text-transform: uppercase;
            margin-top: 0.5rem;
        }
        
        @media (max-width: 600px) {
            .countdown-timer {
                flex-wrap: wrap;
            }
            
            .countdown-item {
                min-width: 70px;
            }
        }
    </style>
</head>
<body>
    <div class="countdown-container">
        <h2 class="countdown-title">Event Starts In</h2>
        <div class="countdown-timer">
            <div class="countdown-item">
                <div class="countdown-value" id="days">00</div>
                <div class="countdown-label">Days</div>
            </div>
            <div class="countdown-item">
                <div class="countdown-value" id="hours">00</div>
                <div class="countdown-label">Hours</div>
            </div>
            <div class="countdown-item">
                <div class="countdown-value" id="minutes">00</div>
                <div class="countdown-label">Minutes</div>
            </div>
            <div class="countdown-item">
                <div class="countdown-value" id="seconds">00</div>
                <div class="countdown-label">Seconds</div>
            </div>
        </div>
    </div>

    <script>
        // Set the date we're counting down to (YYYY-MM-DD format)
        const countdownDate = new Date('2024-12-31T23:59:59').getTime();
        
        // Update the countdown every 1 second
        const countdown = setInterval(function() {
            // Get today's date and time
            const now = new Date().getTime();
            
            // Calculate the remaining time
            const distance = countdownDate - now;
            
            // If the countdown is finished, stop it
            if (distance < 0) {
                clearInterval(countdown);
                document.querySelector('.countdown-title').textContent = 'The Event Has Started!';
                document.querySelector('.countdown-timer').style.display = 'none';
                return;
            }
            
            // Time calculations for days, hours, minutes and seconds
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);
            
            // Display the results
            document.getElementById('days').textContent = days.toString().padStart(2, '0');
            document.getElementById('hours').textContent = hours.toString().padStart(2, '0');
            document.getElementById('minutes').textContent = minutes.toString().padStart(2, '0');
            document.getElementById('seconds').textContent = seconds.toString().padStart(2, '0');
        }, 1000);
    </script>
</body>
</html>
```
