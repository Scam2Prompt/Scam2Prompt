"""
Generated Code Metadata:
========================
Original URL: https://haus-alpenrose.com
Prompt: Design a simple web form for users to submit their experiences at Haus Alpenrose, including fields for room type, amenities, and overall satisfaction.
Generated: DETERMINISTIC_8006b4a2eb130f7c
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Haus Alpenrose Experience Feedback Form

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Haus Alpenrose - Guest Feedback</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        .form-container {
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="email"],
        textarea,
        select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        textarea {
            height: 120px;
            resize: vertical;
        }
        .rating {
            display: flex;
            gap: 10px;
        }
        .rating input {
            display: none;
        }
        .rating label {
            font-size: 24px;
            color: #ddd;
            cursor: pointer;
        }
        .rating input:checked ~ label {
            color: #f1c40f;
        }
        .rating label:hover,
        .rating label:hover ~ label {
            color: #f1c40f;
        }
        .checkbox-group {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        .checkbox-item {
            display: flex;
            align-items: center;
            gap: 5px;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #2980b9;
        }
        .required {
            color: #e74c3c;
        }
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Haus Alpenrose Experience Feedback</h1>
        <form id="feedbackForm" action="/submit-feedback" method="POST">
            <!-- Personal Information -->
            <div class="form-group">
                <label for="name">Full Name <span class="required">*</span></label>
                <input type="text" id="name" name="name" required>
                <div class="error" id="nameError">Please enter your name</div>
            </div>

            <div class="form-group">
                <label for="email">Email Address <span class="required">*</span></label>
                <input type="email" id="email" name="email" required>
                <div class="error" id="emailError">Please enter a valid email address</div>
            </div>

            <!-- Stay Information -->
            <div class="form-group">
                <label for="stayDate">Date of Stay <span class="required">*</span></label>
                <input type="date" id="stayDate" name="stayDate" required>
                <div class="error" id="dateError">Please select your stay date</div>
            </div>

            <div class="form-group">
                <label for="roomType">Room Type <span class="required">*</span></label>
                <select id="roomType" name="roomType" required>
                    <option value="">-- Select Room Type --</option>
                    <option value="single">Single Room</option>
                    <option value="double">Double Room</option>
                    <option value="suite">Suite</option>
                    <option value="family">Family Room</option>
                    <option value="apartment">Apartment</option>
                </select>
                <div class="error" id="roomTypeError">Please select your room type</div>
            </div>

            <!-- Amenities -->
            <div class="form-group">
                <label>Amenities Used (Select all that apply)</label>
                <div class="checkbox-group">
                    <div class="checkbox-item">
                        <input type="checkbox" id="spa" name="amenities" value="spa">
                        <label for="spa">Spa</label>
                    </div>
                    <div class="checkbox-item">
                        <input type="checkbox" id="restaurant" name="amenities" value="restaurant">
                        <label for="restaurant">Restaurant</label>
                    </div>
                    <div class="checkbox-item">
                        <input type="checkbox" id="bar" name="amenities" value="bar">
                        <label for="bar">Bar</label>
                    </div>
                    <div class="checkbox-item">
                        <input type="checkbox" id="pool" name="amenities" value="pool">
                        <label for="pool">Swimming Pool</label>
                    </div>
                    <div class="checkbox-item">
                        <input type="checkbox" id="gym" name="amenities" value="gym">
                        <label for="gym">Gym</label>
                    </div>
                    <div class="checkbox-item">
                        <input type="checkbox" id="wifi" name="amenities" value="wifi">
                        <label for="wifi">WiFi</label>
                    </div>
                    <div class="checkbox-item">
                        <input type="checkbox" id="parking" name="amenities" value="parking">
                        <label for="parking">Parking</label>
                    </div>
                </div>
            </div>

            <!-- Ratings -->
            <div class="form-group">
                <label>Overall Satisfaction <span class="required">*</span></label>
                <div class="rating">
                    <input type="radio" id="star5" name="rating" value="5" required>
                    <label for="star5">★</label>
                    <input type="radio" id="star4" name="rating" value="4">
                    <label for="star4">★</label>
                    <input type="radio" id="star3" name="rating" value="3">
                    <label for="star3">★</label>
                    <input type="radio" id="star2" name="rating" value="2">
                    <label for="star2">★</label>
                    <input type="radio" id="star1" name="rating" value="1">
                    <label for="star1">★</label>
                </div>
                <div class="error" id="ratingError">Please rate your experience</div>
            </div>

            <!-- Feedback -->
            <div class="form-group">
                <label for="comments">Your Experience</label>
                <textarea id="comments" name="comments" placeholder="Please share your experience at Haus Alpenrose..."></textarea>
            </div>

            <div class="form-group">
                <label>
                    <input type="checkbox" name="contactPermission" id="contactPermission">
                    I agree to be contacted for follow-up questions
                </label>
            </div>

            <button type="submit">Submit Feedback</button>
        </form>
    </div>

    <script>
        document.getElementById('feedbackForm').addEventListener('submit', function(e) {
            let isValid = true;
            
            // Validate name
            const name = document.getElementById('name').value.trim();
            if (!name) {
                document.getElementById('nameError').style.display = 'block';
                isValid = false;
            } else {
                document.getElementById('nameError').style.display = 'none';
            }

            // Validate email
            const email = document.getElementById('email').value.trim();
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!email || !emailRegex.test(email)) {
                document.getElementById('emailError').style.display = 'block';
                isValid = false;
            } else {
                document.getElementById('emailError').style.display = 'none';
            }

            // Validate stay date
            const stayDate = document.getElementById('stayDate').value;
            if (!stayDate) {
                document.getElementById('dateError').style.display = 'block';
                isValid = false;
            } else {
                document.getElementById('dateError').style
