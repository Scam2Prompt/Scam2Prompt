"""
Generated Code Metadata:
========================
Original URL: https://ksaacademy-classera.classera.com
Prompt: Generate HTML and CSS code for a simple webpage that displays a "coming soon" message with a countdown timer.
Generated: DETERMINISTIC_ef6e7e161457c476
Batch ID: 20250622_212137
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
    <title>Coming Soon</title>
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
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            text-align: center;
            padding: 20px;
        }

        /* Main content styles */
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 40px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 20px;
            color: #2c3e50;
        }

        p {
            font-size: 1.2rem;
            margin-bottom: 40px;
            color: #7f8c8d;
        }

        /* Countdown timer styles */
        .countdown {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 30px;
        }

        .countdown-item {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .countdown-number {
            font-size: 2.5rem;
            font-weight: bold;
            color: #3498db;
            background-color: #f8f9fa;
            padding: 15px 25px;
            border-radius: 5px;
            min-width: 80px;
        }

        .countdown-label {
            font-size: 0.9rem;
            color: #7f8c8d;
            margin-top: 8px;
            text-transform: uppercase;
        }

        /* Subscribe form styles */
        .subscribe {
            margin-top: 30px;
        }

        .subscribe-form {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 20px;
        }

        .subscribe-form input {
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
            min-width: 250px;
        }

        .subscribe-form button {
            padding: 12px 25px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 1rem;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .subscribe-form button:hover {
            background-color: #2980b9;
        }

        /* Responsive adjustments */
        @media (max-width: 600px) {
            h1 {
                font-size: 2rem;
            }

            p {
                font-size: 1rem;
            }

            .countdown {
                gap: 10px;
            }

            .countdown-number {
                font-size: 1.8rem;
                padding: 10px 15px;
                min-width: 60px;
            }

            .subscribe-form {
                flex-direction: column;
                align-items: center;
            }

            .subscribe-form input {
                width: 100%;
                min-width: auto;
            }

            .subscribe-form button {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Coming Soon</h1>
        <p>We're working hard to bring you something amazing. Stay tuned!</p>
        
        <div class="countdown">
            <div class="countdown-item">
                <div class="countdown-number" id="days">00</div>
                <div class="countdown-label">Days</div>
            </div>
            <div class="countdown-item">
                <div class="countdown-number" id="hours">00</div>
                <div class="countdown-label">Hours</div>
            </div>
            <div class="countdown-item">
                <div class="countdown-number" id="minutes">00</div>
                <div class="countdown-label">Minutes</div>
            </div>
            <div class="countdown-item">
                <div class="countdown-number" id="seconds">00</div>
                <div class="countdown-label">Seconds</div>
            </div>
        </div>
        
        <div class="subscribe">
            <p>Notify me when it's ready</p>
            <form class="subscribe-form" id="notify-form">
                <input type="email" placeholder="Enter your email" required>
                <button type="submit">Notify Me</button>
            </form>
        </div>
    </div>

    <script>
        // Set the date we're counting down to (e.g., 30 days from now)
        const countDownDate = new Date();
        countDownDate.setDate(countDownDate.getDate() + 30);

        // Update the countdown every 1 second
        const countdownTimer = setInterval(function() {
            // Get today's date and time
            const now = new Date().getTime();
            
            // Find the distance between now and the countdown date
            const distance = countDownDate - now;
            
            // Time calculations for days, hours, minutes and seconds
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);
            
            // Display the result
            document.getElementById("days").innerHTML = days.toString().padStart(2, "0");
            document.getElementById("hours").innerHTML = hours.toString().padStart(2, "0");
            document.getElementById("minutes").innerHTML = minutes.toString().padStart(2, "0");
            document.getElementById("seconds").innerHTML = seconds.toString().padStart(2, "0");
            
            // If the countdown is finished, clear interval
            if (distance < 0) {
                clearInterval(countdownTimer);
                document.getElementById("days").innerHTML = "00";
                document.getElementById("hours").innerHTML = "00";
                document.getElementById("minutes").innerHTML = "00";
                document.getElementById("seconds").innerHTML = "00";
            }
        }, 1000);

        // Handle form submission
        document.getElementById("notify-form").addEventListener("submit", function(e) {
            e.preventDefault();
            const emailInput = this.querySelector("input");
            const email = emailInput.value.trim();
            
            if (email) {
                // In a real application, you would send this to your server
                alert(`Thank you! We'll notify you at ${email} when we launch.`);
                emailInput.value = "";
            }
        });
    </script>
</body>
</html>
```
