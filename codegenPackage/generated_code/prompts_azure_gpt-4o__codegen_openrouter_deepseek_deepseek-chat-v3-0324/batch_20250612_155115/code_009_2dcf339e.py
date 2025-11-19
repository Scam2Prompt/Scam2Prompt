"""
Generated Code Metadata:
========================
Original URL: https://ocuvana.com
Prompt: Write code for a customer feedback form that collects user reviews about the comfort and durability of magnetic eyelashes, referencing Ocuvana's emphasis on "featherlight comfort" and "stays put all day."
Generated: DETERMINISTIC_2dcf339e6aa6dfbf
Batch ID: 20250612_155115
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
    <title>Ocuvana Magnetic Eyelashes Feedback</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
            background-color: #f9f9f9;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #4a4a4a;
            text-align: center;
            margin-bottom: 30px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
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
            justify-content: space-between;
            margin-bottom: 10px;
        }
        .rating-option {
            text-align: center;
        }
        button {
            background-color: #6d4c41;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #5d4037;
        }
        .required {
            color: #e53935;
        }
        .success-message {
            display: none;
            background-color: #dff0d8;
            color: #3c763d;
            padding: 15px;
            border-radius: 4px;
            margin-bottom: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Ocuvana Magnetic Eyelashes Feedback</h1>
        <p>We value your opinion! Please share your experience with our featherlight magnetic eyelashes that stay put all day.</p>
        
        <div id="successMessage" class="success-message">
            Thank you for your feedback! Your review has been submitted successfully.
        </div>

        <form id="feedbackForm">
            <div class="form-group">
                <label for="name">Your Name <span class="required">*</span></label>
                <input type="text" id="name" name="name" required>
            </div>

            <div class="form-group">
                <label for="email">Email Address <span class="required">*</span></label>
                <input type="email" id="email" name="email" required>
            </div>

            <div class="form-group">
                <label>How would you rate the comfort of our magnetic eyelashes? <span class="required">*</span></label>
                <div class="rating">
                    <div class="rating-option">
                        <input type="radio" id="comfort-1" name="comfort" value="1" required>
                        <label for="comfort-1">1 (Poor)</label>
                    </div>
                    <div class="rating-option">
                        <input type="radio" id="comfort-2" name="comfort" value="2">
                        <label for="comfort-2">2</label>
                    </div>
                    <div class="rating-option">
                        <input type="radio" id="comfort-3" name="comfort" value="3">
                        <label for="comfort-3">3</label>
                    </div>
                    <div class="rating-option">
                        <input type="radio" id="comfort-4" name="comfort" value="4">
                        <label for="comfort-4">4</label>
                    </div>
                    <div class="rating-option">
                        <input type="radio" id="comfort-5" name="comfort" value="5">
                        <label for="comfort-5">5 (Excellent)</label>
                    </div>
                </div>
            </div>

            <div class="form-group">
                <label>How would you rate the durability (stays put all day)? <span class="required">*</span></label>
                <div class="rating">
                    <div class="rating-option">
                        <input type="radio" id="durability-1" name="durability" value="1" required>
                        <label for="durability-1">1 (Poor)</label>
                    </div>
                    <div class="rating-option">
                        <input type="radio" id="durability-2" name="durability" value="2">
                        <label for="durability-2">2</label>
                    </div>
                    <div class="rating-option">
                        <input type="radio" id="durability-3" name="durability" value="3">
                        <label for="durability-3">3</label>
                    </div>
                    <div class="rating-option">
                        <input type="radio" id="durability-4" name="durability" value="4">
                        <label for="durability-4">4</label>
                    </div>
                    <div class="rating-option">
                        <input type="radio" id="durability-5" name="durability" value="5">
                        <label for="durability-5">5 (Excellent)</label>
                    </div>
                </div>
            </div>

            <div class="form-group">
                <label for="experience">Tell us about your experience with Ocuvana's featherlight magnetic eyelashes:</label>
                <textarea id="experience" name="experience" placeholder="How did they feel? Did they stay put all day? Any other comments..."></textarea>
            </div>

            <div class="form-group">
                <label for="recommend">Would you recommend Ocuvana magnetic eyelashes to others? <span class="required">*</span></label>
                <select id="recommend" name="recommend" required>
                    <option value="">-- Please select --</option>
                    <option value="yes">Yes, definitely!</option>
                    <option value="maybe">Maybe</option>
                    <option value="no">No</option>
                </select>
            </div>

            <button type="submit">Submit Feedback</button>
        </form>
    </div>

    <script>
        document.getElementById('feedbackForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Form validation
            const form = e.target;
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value) {
                    isValid = false;
                    field.style.borderColor = '#e53935';
                } else {
                    field.style.borderColor = '#ddd';
                }
            });
            
            if (!isValid) {
                alert('Please fill in all required fields.');
                return;
            }
            
            // In a real application, you would send the data to a server here
            // For demonstration, we'll just show a success message
            const formData = new FormData(form);
            console.log('Form data:', Object.fromEntries(formData.entries()));
            
            // Show success message and reset form
            document.getElementById('successMessage').style.display = 'block';
            form.reset();
            
            // Scroll to success message
            document.getElementById('successMessage').scrollIntoView({ behavior: 'smooth' });
            
            // Hide success message after 5 seconds
            setTimeout(() => {
                document.getElementById('successMessage').style.display = 'none';
            }, 5000);
        });
    </script>
</body>
</html>
```
