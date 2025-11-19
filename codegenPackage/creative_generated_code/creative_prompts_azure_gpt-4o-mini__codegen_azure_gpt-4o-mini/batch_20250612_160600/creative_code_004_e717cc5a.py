"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedarlake.org
Prompt: Write a sample HTML form for potential volunteers to sign up for opportunities at Cedar Lake Foundation, including fields for name, contact information, and areas of interest.
Generated: DETERMINISTIC_e717cc5a938ed2a7
Batch ID: 20250612_160600
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
    <title>Volunteer Sign-Up Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Cedar Lake Foundation Volunteer Sign-Up</h1>
    </header>
    <main>
        <form id="volunteerForm" action="/submit-volunteer" method="POST">
            <!-- Name field -->
            <div class="form-group">
                <label for="name">Full Name <span class="required">*</span></label>
                <input type="text" id="name" name="name" required aria-required="true" placeholder="John Doe" />
            </div>

            <!-- Email address field -->
            <div class="form-group">
                <label for="email">Email Address <span class="required">*</span></label>
                <input type="email" id="email" name="email" required aria-required="true" placeholder="example@domain.com" />
            </div>

            <!-- Phone number field -->
            <div class="form-group">
                <label for="phone">Phone Number <span class="required">*</span></label>
                <input type="tel" id="phone" name="phone" required aria-required="true" placeholder="(123) 456-7890" />
            </div>
            
            <!-- Areas of interest field -->
            <div class="form-group">
                <label for="interest">Areas of Interest <span class="required">*</span></label>
                <select id="interest" name="interest" required aria-required="true">
                    <option value="" disabled selected>Select an area</option>
                    <option value="community_service">Community Service</option>
                    <option value="environmental_efforts">Environmental Efforts</option>
                    <option value="education">Education</option>
                    <option value="fundraising">Fundraising</option>
                    <option value="administrative_support">Administrative Support</option>
                </select>
            </div>

            <!-- Comments or additional information -->
            <div class="form-group">
                <label for="comments">Additional Comments</label>
                <textarea id="comments" name="comments" rows="4" placeholder="Any additional information or comments"></textarea>
            </div>

            <!-- Submit button -->
            <div class="form-group">
                <button type="submit">Sign Up</button>
            </div>
        </form>
    </main>
    <footer>
        <p>&copy; 2023 Cedar Lake Foundation. All rights reserved.</p>
    </footer>

    <script>
        // Form submission handler
        document.getElementById('volunteerForm').addEventListener('submit', function(event) {
            // Perform client-side validation if necessary
            // Handle form submission here, possibly with AJAX if required
            // For example, prevent the default and show a confirmation message
            alert('Thank you for signing up as a volunteer!');
            // event.preventDefault(); // Uncomment if you don't want to submit the form immediately
        });
    </script>
</body>
</html>
```
