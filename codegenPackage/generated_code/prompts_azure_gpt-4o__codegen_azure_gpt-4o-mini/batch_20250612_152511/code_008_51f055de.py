"""
Generated Code Metadata:
========================
Original URL: https://irgift.info
Prompt: Generate code for a countdown timer feature to display limited-time offers on an e-commerce site, similar to the "0 روز 00 ساعت 00 دقیقه 00 ثانیه" timer shown on "ای ار گیفت."
Generated: DETERMINISTIC_51f055de65e0b2be
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Countdown Timer</title>
    <style>
        /* Basic styling for the countdown timer */
        .countdown {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 2em;
            margin: 20px;
        }
        .time-unit {
            margin: 0 10px;
        }
    </style>
</head>
<body>

<div class="countdown" id="countdown">
    <div class="time-unit" id="days">0 روز</div>
    <div class="time-unit" id="hours">00 ساعت</div>
    <div class="time-unit" id="minutes">00 دقیقه</div>
    <div class="time-unit" id="seconds">00 ثانیه</div>
</div>

<script>
    // Set the date we're counting down to
    const countdownDate = new Date("2023-12-31T23:59:59").getTime();

    // Update the countdown every second
    const countdownFunction = setInterval(() => {
        // Get current date and time
        const now = new Date().getTime();

        // Calculate the remaining time
        const distance = countdownDate - now;

        // Time calculations for days, hours, minutes and seconds
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result in the respective elements
        document.getElementById("days").innerText = `${days} روز`;
        document.getElementById("hours").innerText = `${hours.toString().padStart(2, '0')} ساعت`;
        document.getElementById("minutes").innerText = `${minutes.toString().padStart(2, '0')} دقیقه`;
        document.getElementById("seconds").innerText = `${seconds.toString().padStart(2, '0')} ثانیه`;

        // If the countdown is over, display a message
        if (distance < 0) {
            clearInterval(countdownFunction);
            document.getElementById("countdown").innerHTML = "زمان پیشنهاد به پایان رسید!";
        }
    }, 1000);
</script>

</body>
</html>
```
