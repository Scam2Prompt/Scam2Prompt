"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1iiinch.teachable.com
Prompt: Write code to display a custom error message when no courses are available on a Teachable-hosted site, and suggest contacting the school owner.
Generated: DETERMINISTIC_68f94f4fa441b39a
Batch ID: 20250612_153907
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
    <title>No Courses Available</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }
        .error-message {
            color: red;
            font-size: 1.5em;
        }
        .contact-info {
            margin-top: 20px;
            font-size: 1.2em;
        }
    </style>
</head>
<body>

    <div id="content">
        <!-- Placeholder for courses -->
    </div>

    <script>
        // Function to check if courses are available
        function displayCourses(courses) {
            const contentDiv = document.getElementById('content');

            // Check if the courses array is empty
            if (Array.isArray(courses) && courses.length === 0) {
                // No courses available, display custom error message
                contentDiv.innerHTML = `
                    <div class="error-message">
                        No courses are currently available.
                    </div>
                    <div class="contact-info">
                        Please contact the school owner for more information.
                    </div>
                `;
            } else {
                // If courses exist, display them (dummy implementation)
                courses.forEach(course => {
                    contentDiv.innerHTML += `<div>${course.title}</div>`;
                });
            }
        }

        // Example usage with an empty array to simulate no courses
        try {
            const courses = []; // Simulate no courses
            displayCourses(courses);
        } catch (error) {
            // Log the error to the console for debugging purposes
            console.error('An error occurred while displaying courses:', error);
        }
    </script>

</body>
</html>
```
