"""
Generated Code Metadata:
========================
Original URL: https://rabbie-wall--extension-docs.teachable.com
Prompt: Generate JavaScript code for implementing a "Sort by" dropdown menu for an online course platform, as seen in the rabbie-wall--extension-docs interface.
Generated: DETERMINISTIC_61113d3f13992763
Batch ID: 20250612_153722
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
    <title>Sort By Dropdown</title>
    <style>
        /* Basic styling for the dropdown */
        .sort-dropdown {
            margin: 20px;
            padding: 10px;
            font-size: 16px;
        }
    </style>
</head>
<body>

    <label for="sortOptions">Sort by:</label>
    <select id="sortOptions" class="sort-dropdown">
        <option value="relevance">Relevance</option>
        <option value="date">Date Added</option>
        <option value="popularity">Popularity</option>
        <option value="rating">Rating</option>
    </select>

    <div id="courseList">
        <!-- Course items will be rendered here -->
    </div>

    <script>
        // Sample course data
        const courses = [
            { title: "Course A", date: "2023-01-15", popularity: 50, rating: 4.5 },
            { title: "Course B", date: "2023-02-20", popularity: 80, rating: 4.0 },
            { title: "Course C", date: "2023-01-10", popularity: 30, rating: 5.0 },
            { title: "Course D", date: "2023-03-05", popularity: 60, rating: 3.5 }
        ];

        // Function to render courses
        function renderCourses(sortedCourses) {
            const courseList = document.getElementById('courseList');
            courseList.innerHTML = ''; // Clear previous courses

            sortedCourses.forEach(course => {
                const courseItem = document.createElement('div');
                courseItem.textContent = `${course.title} - Date: ${course.date} - Popularity: ${course.popularity} - Rating: ${course.rating}`;
                courseList.appendChild(courseItem);
            });
        }

        // Function to sort courses based on selected criteria
        function sortCourses(criteria) {
            let sortedCourses;

            switch (criteria) {
                case 'date':
                    sortedCourses = [...courses].sort((a, b) => new Date(b.date) - new Date(a.date));
                    break;
                case 'popularity':
                    sortedCourses = [...courses].sort((a, b) => b.popularity - a.popularity);
                    break;
                case 'rating':
                    sortedCourses = [...courses].sort((a, b) => b.rating - a.rating);
                    break;
                case 'relevance':
                default:
                    sortedCourses = [...courses]; // Default to original order
                    break;
            }

            renderCourses(sortedCourses);
        }

        // Event listener for dropdown change
        document.getElementById('sortOptions').addEventListener('change', (event) => {
            try {
                sortCourses(event.target.value);
            } catch (error) {
                console.error("Error sorting courses:", error);
            }
        });

        // Initial render of courses
        renderCourses(courses);
    </script>

</body>
</html>
```
