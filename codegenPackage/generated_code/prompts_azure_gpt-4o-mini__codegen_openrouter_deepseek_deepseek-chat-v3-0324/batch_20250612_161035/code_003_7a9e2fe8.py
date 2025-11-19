"""
Generated Code Metadata:
========================
Original URL: https://prom-app.vercel.app
Prompt: Create a simple HTML layout for an event page that includes a countdown timer and a schedule, inspired by the design of Gabe and Adnan's Prom.
Generated: DETERMINISTIC_7a9e2fe891c50ed3
Batch ID: 20250612_161035
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
    <title>Gabe & Adnan's Prom - Event Page</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
            color: #333;
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            text-align: center;
            padding: 30px 0;
            background: linear-gradient(135deg, #6e48aa, #9d50bb);
            color: white;
            border-radius: 8px;
            margin-bottom: 30px;
        }
        
        h1 {
            margin: 0;
            font-size: 2.5em;
        }
        
        .subtitle {
            font-size: 1.2em;
            margin-top: 10px;
        }
        
        .countdown-container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin-bottom: 30px;
            text-align: center;
        }
        
        .countdown {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
        }
        
        .countdown-item {
            background-color: #6e48aa;
            color: white;
            padding: 15px;
            border-radius: 8px;
            min-width: 80px;
        }
        
        .countdown-number {
            font-size: 2em;
            font-weight: bold;
        }
        
        .countdown-label {
            font-size: 0.8em;
            text-transform: uppercase;
        }
        
        .schedule {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        .schedule h2 {
            color: #6e48aa;
            border-bottom: 2px solid #6e48aa;
            padding-bottom: 10px;
        }
        
        .schedule-item {
            display: flex;
            margin: 15px 0;
            padding-bottom: 15px;
            border-bottom: 1px solid #eee;
        }
        
        .schedule-time {
            font-weight: bold;
            min-width: 100px;
            color: #6e48aa;
        }
        
        .schedule-details {
            flex-grow: 1;
        }
        
        .schedule-title {
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        footer {
            text-align: center;
            margin-top: 30px;
            padding: 20px;
            color: #666;
            font-size: 0.9em;
        }
        
        @media (max-width: 600px) {
            .countdown {
                flex-wrap: wrap;
            }
            
            .schedule-item {
                flex-direction: column;
            }
            
            .schedule-time {
                margin-bottom: 5px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Gabe & Adnan's Prom</h1>
            <div class="subtitle">A Night to Remember</div>
        </header>
        
        <div class="countdown-container">
            <h2>Countdown to the Event</h2>
            <div class="countdown" id="countdown">
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
        </div>
        
        <div class="schedule">
            <h2>Event Schedule</h2>
            
            <div class="schedule-item">
                <div class="schedule-time">7:00 PM</div>
                <div class="schedule-details">
                    <div class="schedule-title">Grand Entrance</div>
                    <div class="schedule-description">Arrival of guests and welcome drinks</div>
                </div>
            </div>
            
            <div class="schedule-item">
                <div class="schedule-time">7:30 PM</div>
                <div class="schedule-details">
                    <div class="schedule-title">Opening Remarks</div>
                    <div class="schedule-description">Welcome speech by the hosts</div>
                </div>
            </div>
            
            <div class="schedule-item">
                <div class="schedule-time">8:00 PM</div>
                <div class="schedule-details">
                    <div class="schedule-title">Dinner Service</div>
                    <div class="schedule-description">Three-course gourmet meal</div>
                </div>
            </div>
            
            <div class="schedule-item">
                <div class="schedule-time">9:30 PM</div>
                <div class="schedule-details">
                    <div class="schedule-title">Dancing Begins</div>
                    <div class="schedule-description">Live DJ and dance floor opens</div>
                </div>
            </div>
            
            <div class="schedule-item">
                <div class="schedule-time">11:00 PM</div>
                <div class="schedule-details">
                    <div class="schedule-title">Special Performance</div>
                    <div class="schedule-description">Surprise musical guest</div>
                </div>
            </div>
            
            <div class="schedule-item">
                <div class="schedule-time">12:00 AM</div>
                <div class="schedule-details">
                    <div class="schedule-title">Final Dance</div>
                    <div class="schedule-description">Last song of the night</div>
                </div>
            </div>
        </div>
        
        <footer>
            <p>© 2023 Gabe & Adnan's Prom. All rights reserved.</p>
        </footer>
    </div>

    <script>
        // Set the date we're counting down to (YYYY-MM-DD format)
        const eventDate = new Date("2023-12-31T19:00:00").getTime();
        
        // Update the countdown every 1 second
        const countdown = setInterval(function() {
            // Get today's date and time
            const now = new Date().getTime();
            
            // Find the distance between now and the event date
            const distance = eventDate - now;
            
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
            
            // If the countdown is finished
            if (distance < 0) {
                clearInterval(countdown);
                document.getElementById("countdown").innerHTML = "<div style='font-size: 1.5em; color: #6e48aa;'>The event has started!</div>";
            }
        }, 1000);
    </script>
</body>
</html>
```
