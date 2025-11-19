"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Generate code using HTML and CSS to design a webpage section showcasing the unique features of the "Laguna Ride" horse riding tour, including swimming with horses and pristine nature.
Generated: DETERMINISTIC_2a8d72c52d6e7b5d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Laguna Ride</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <section class="laguna-ride">
        <h1>Laguna Ride: Unique Horse Riding Experience</h1>
        <div class="features">
            <div class="feature">
                <img src="horse-swimming.jpg" alt="Swimming with Horses">
                <h2>Swim with Your Horse</h2>
                <p>Experience the thrill of swimming with your horse in our pristine lagoon.</p>
            </div>
            <div class="feature">
                <img src="pristine-nature.jpg" alt="Pristine Nature">
                <h2>Pristine Nature</h2>
                <p>Immerse yourself in the breathtaking beauty of our natural surroundings.</p>
            </div>
            <div class="feature">
                <img src="horse-riding.jpg" alt="Horse Riding">
                <h2>Guided Horse Riding</h2>
                <p>Enjoy a guided horse riding tour through our scenic trails.</p>
            </div>
        </div>
        <button class="book-now">Book Now</button>
    </section>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

.laguna-ride {
    max-width: 1200px;
    margin: 40px auto;
    text-align: center;
}

.laguna-ride h1 {
    color: #333;
    margin-bottom: 20px;
}

.features {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.feature {
    margin: 20px;
    width: calc(33.33% - 40px);
    background-color: #f7f7f7;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.feature img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.feature h2 {
    color: #333;
    margin-top: 10px;
}

.feature p {
    color: #666;
    margin-bottom: 20px;
}

.book-now {
    background-color: #4CAF50;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-top: 20px;
}

.book-now:hover {
    background-color: #3e8e41;
}

@media only screen and (max-width: 768px) {
    .feature {
        width: calc(50% - 40px);
    }
}

@media only screen and (max-width: 480px) {
    .feature {
        width: 100%;
        margin: 20px 0;
    }
}
```
