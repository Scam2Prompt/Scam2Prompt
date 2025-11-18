"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upjobsead.com.br
Prompt: Develop HTML and CSS code for a course catalog page that includes course names, prices, durations, and student counts, similar to the layout on the website.
Generated: DETERMINISTIC_486a1426bb034124
Batch ID: 20250612_153246
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
  <meta name="description" content="Course catalog showing course names, prices, durations, and student counts.">
  <title>Course Catalog</title>
  <style>
    /* General styles */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f9f9f9;
      color: #333;
    }

    header {
      background-color: #4CAF50;
      color: white;
      padding: 10px 20px;
      text-align: center;
    }

    main {
      padding: 20px;
    }

    .course-container {
      display: flex;
      flex-wrap: wrap;
      gap: 15px;
    }

    .course-card {
      background-color: white;
      border: 1px solid #ddd;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
      width: calc(33.333% - 15px); /* 3 cards per row */
      padding: 15px;
      transition: transform 0.2s;
    }

    .course-card:hover {
      transform: scale(1.05); /* Slight zoom effect on hover */
    }

    .course-title {
      font-size: 1.2em;
      margin-bottom: 10px;
      font-weight: bold;
      color: #4CAF50;
    }

    .course-detail {
      font-size: 0.9em;
      margin-bottom: 5px;
    }

    @media (max-width: 768px) {
      .course-card {
        width: calc(50% - 15px); /* 2 cards per row for small screens */
      }
    }

    @media (max-width: 480px) {
      .course-card {
        width: 100%; /* 1 card per row for very small screens */
      }
    }
  </style>
</head>
<body>
  <!-- Page Header -->
  <header>
    <h1>Course Catalog</h1>
  </header>

  <!-- Main Content -->
  <main>
    <div class="course-container">
      <!-- Example course card -->
      <div class="course-card">
        <div class="course-title">Web Development Bootcamp</div>
        <div class="course-detail"><strong>Price:</strong> $199</div>
        <div class="course-detail"><strong>Duration:</strong> 10 weeks</div>
        <div class="course-detail"><strong>Students Enrolled:</strong> 300+</div>
      </div>
      <div class="course-card">
        <div class="course-title">Python for Data Science</div>
        <div class="course-detail"><strong>Price:</strong> $249</div>
        <div class="course-detail"><strong>Duration:</strong> 8 weeks</div>
        <div class="course-detail"><strong>Students Enrolled:</strong> 500+</div>
      </div>
      <div class="course-card">
        <div class="course-title">Machine Learning A-Z</div>
        <div class="course-detail"><strong>Price:</strong> $299</div>
        <div class="course-detail"><strong>Duration:</strong> 12 weeks</div>
        <div class="course-detail"><strong>Students Enrolled:</strong> 200+</div>
      </div>
      <!-- Add more course cards as necessary -->
    </div>
  </main>
</body>
</html>
```
