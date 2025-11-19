"""
Generated Code Metadata:
========================
Original URL: https://sensibleoptimism.com
Prompt: Generate HTML and CSS code for a basic webpage that announces a "Launching Soon" status for a blog or product named Sensible Optimism.
Generated: DETERMINISTIC_6f018da744cb0b68
Batch ID: 20250622_210145
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
    <title>Sensible Optimism - Coming Soon</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f7fa;
            color: #333;
            line-height: 1.6;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            text-align: center;
            padding: 20px;
        }

        .container {
            max-width: 800px;
            width: 100%;
            padding: 40px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 20px;
            color: #2c3e50;
        }

        .logo {
            font-weight: bold;
            color: #3498db;
        }

        p {
            font-size: 1.2rem;
            margin-bottom: 30px;
            color: #7f8c8d;
        }

        .countdown {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 40px;
        }

        .countdown-item {
            background-color: #3498db;
            color: white;
            padding: 15px 20px;
            border-radius: 5px;
            font-size: 1.5rem;
            font-weight: bold;
            min-width: 80px;
        }

        .countdown-label {
            display: block;
            font-size: 0.8rem;
            font-weight: normal;
            margin-top: 5px;
        }

        .notify-form {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }

        .notify-input {
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 5px 0 0 5px;
            font-size: 1rem;
            width: 300px;
            max-width: 100%;
        }

        .notify-button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 0 5px 5px 0;
            cursor: pointer;
            font-size: 1rem;
            transition: background-color 0.3s;
        }

        .notify-button:hover {
            background-color: #2980b9;
        }

        .social-links {
            margin-top: 40px;
            display: flex;
            justify-content: center;
            gap: 20px;
        }

        .social-link {
            color: #3498db;
            font-size: 1.5rem;
            transition: color 0.3s;
        }

        .social-link:hover {
            color: #2980b9;
        }

        @media (max-width: 600px) {
            .container {
                padding: 20px;
            }

            h1 {
                font-size: 2rem;
            }

            .countdown {
                flex-wrap: wrap;
            }

            .notify-form {
                flex-direction: column;
            }

            .notify-input {
                border-radius: 5px;
                margin-bottom: 10px;
                width: 100%;
            }

            .notify-button {
                border-radius: 5px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1><span class="logo">Sensible Optimism</span> is launching soon!</h1>
        <p>We're working hard to bring you something amazing. Stay tuned!</p>
        
        <div class="countdown">
            <div class="countdown-item">
                <span id="days">00</span>
                <span class="countdown-label">Days</span>
            </div>
            <div class="countdown-item">
                <span id="hours">00</span>
                <span class="countdown-label">Hours</span>
            </div>
            <div class="countdown-item">
                <span id="minutes">00</span>
                <span class="countdown-label">Minutes</span>
            </div>
            <div class="countdown-item">
                <span id="seconds">00</span>
                <span class="countdown-label">Seconds</span>
            </div>
        </div>

        <form class="notify-form" id="notifyForm">
            <input type="email" class="notify-input" placeholder="Enter your email for updates" required>
            <button type="submit" class="notify-button">Notify Me</button>
        </form>

        <div class="social-links">
            <a href="#" class="social-link">Twitter</a>
            <a href="#" class="social-link">Facebook</a>
            <a href="#" class="social-link">Instagram</a>
        </div>
    </div>

    <script>
        // Set the launch date (YYYY, MM-1, DD, HH, MM, SS)
        const launchDate = new Date(2023, 11, 31, 0, 0, 0).getTime();

        // Update countdown every second
        const countdown = setInterval(function() {
            const now = new Date().getTime();
            const distance = launchDate - now;

            // Calculate days, hours, minutes, seconds
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Display results
            document.getElementById("days").textContent = days.toString().padStart(2, '0');
            document.getElementById("hours").textContent = hours.toString().padStart(2, '0');
            document.getElementById("minutes").textContent = minutes.toString().padStart(2, '0');
            document.getElementById("seconds").textContent = seconds.toString().padStart(2, '0');

            // If countdown finished
            if (distance < 0) {
                clearInterval(countdown);
                document.querySelector("h1").textContent = "Sensible Optimism has launched!";
                document.querySelector("p").textContent = "Check out our new website!";
                document.querySelector(".countdown").style.display = "none";
            }
        }, 1000);

        // Handle form submission
        document.getElementById("notifyForm").addEventListener("submit", function(e) {
            e.preventDefault();
            const email = this.querySelector(".notify-input").value;
            // In a real app, you would send this to your backend
            alert(`Thanks! We'll notify you at ${email} when we launch.`);
            this.querySelector(".notify-input").value = "";
        });
    </script>
</body>
</html>
```
