"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gigzio.com
Prompt: Write code to display job categories (e.g., SEO Specialist, HR, DevOps) dynamically on a job board website, inspired by Gigzio's job browsing functionality.
Generated: DETERMINISTIC_6a9b0adc3005a85f
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// jobCategories.js

// Dummy data representing job categories
const jobCategories = [
    { id: 1, name: 'SEO Specialist' },
    { id: 2, name: 'HR' },
    { id: 3, name: 'DevOps' },
    { id: 4, name: 'Frontend Developer' },
    { id: 5, name: 'Backend Developer' },
    { id: 6, name: 'Data Scientist' }
];

// Function to create a category element
function createCategoryElement(category) {
    const categoryElement = document.createElement('div');
    categoryElement.className = 'job-category';
    categoryElement.textContent = category.name;

    // Adding a click event to filter jobs by category
    categoryElement.addEventListener('click', () => {
        filterJobsByCategory(category.id);
    });

    return categoryElement;
}

// Function to display job categories dynamically
function displayJobCategories(categories) {
    const container = document.getElementById('job-categories-container');
    
    // Check if container exists
    if (!container) {
        console.error('Job categories container not found');
        return;
    }

    // Clear existing categories
    container.innerHTML = '';

    try {
        // Create and append each category element to the container
        categories.forEach(category => {
            const categoryElement = createCategoryElement(category);
            container.appendChild(categoryElement);
        });
    } catch (error) {
        console.error('Error displaying job categories:', error);
    }
}

// Dummy function to simulate job filtering by category
function filterJobsByCategory(categoryId) {
    console.log(`Filtering jobs for category ID: ${categoryId}`);
    // Implement filtering logic here
}

// Initialization function to set up the job categories display
function init() {
    displayJobCategories(jobCategories);
}

// Call init on window load
window.onload = init;
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Board</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="job-categories-container"></div>

    <script src="jobCategories.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic styling for job categories */
#job-categories-container {
    display: flex;
    flex-wrap: wrap;
    margin: 20px;
}

.job-category {
    background-color: #f0f0f0;
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
    margin: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.job-category:hover {
    background-color: #e0e0e0;
}
```
