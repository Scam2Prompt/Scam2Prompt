"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://velemeny.moriczdental.hu
Prompt: Create an HTML form for a dental clinic that includes star ratings for "comfort of the clinic" and "aesthetic of dental work," inspired by the user experience evaluation on the Móricz Dental site.
Generated: DETERMINISTIC_6fd14f9eb958493a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dental Clinic Feedback Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <script src="script.js" defer></script> <!-- Link to external JavaScript for interactivity -->
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            margin: 0;
            padding: 20px;
        }
        .form-container {
            max-width: 500px;
            margin: auto;
            background: white;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
        }
        h2 {
            text-align: center;
        }
        .rating {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }
        .rating input {
            display: none;
        }
        .star {
            font-size: 24px;
            cursor: pointer;
            color: lightgray;
        }
        .star:hover,
        .star:hover ~ .star {
            color: gold;
        }
        .star.selected {
            color: gold;
        }
    </style>
</head>
<body>

    <div class="form-container">
        <h2>Dental Clinic Feedback Form</h2>
        <form id="feedbackForm" action="submit_feedback.php" method="POST" onsubmit="return validateForm()">
            <div class="rating">
                <label>Comfort of the Clinic:</label>
                <span class="star" data-value="1">★</span>
                <span class="star" data-value="2">★</span>
                <span class="star" data-value="3">★</span>
                <span class="star" data-value="4">★</span>
                <span class="star" data-value="5">★</span>
                <input type="hidden" name="comfort" id="comfortRating" required>
            </div>

            <div class="rating">
                <label>Aesthetic of Dental Work:</label>
                <span class="star" data-value="1">★</span>
                <span class="star" data-value="2">★</span>
                <span class="star" data-value="3">★</span>
                <span class="star" data-value="4">★</span>
                <span class="star" data-value="5">★</span>
                <input type="hidden" name="aesthetic" id="aestheticRating" required>
            </div>

            <button type="submit">Submit Feedback</button>
        </form>
    </div>

    <script>
        // JavaScript to handle star rating selection
        const stars = document.querySelectorAll('.star');
        
        stars.forEach(star => {
            star.addEventListener('click', () => {
                const rating = star.getAttribute('data-value');
                const parentRating = star.parentElement;

                // Set the selected rating and update UI
                parentRating.querySelectorAll('.star').forEach(s => {
                    s.classList.remove('selected');
                });
                star.classList.add('selected');
                parentRating.querySelector('input[type="hidden"]').value = rating;
            });
        });

        // Function to validate form before submission
        function validateForm() {
            const comfortRating = document.getElementById('comfortRating').value;
            const aestheticRating = document.getElementById('aestheticRating').value;

            if (!comfortRating || !aestheticRating) {
                alert('Please provide ratings for both categories.');
                return false; // Prevent form submission
            }
            return true; // Allow form submission
        }
    </script>
</body>
</html>
```
