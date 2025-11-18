"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.swellnetwork.tv
Prompt: Develop code to create a portfolio display similar to Swell Creative Management's "View fullsize" feature, showcasing creative projects dynamically.
Generated: DETERMINISTIC_aa0e882bb087a08a
Batch ID: 20250612_154842
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
    <title>Portfolio Display</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <div class="portfolio-container">
        <!-- Dynamic portfolio items will be injected here -->
    </div>

    <!-- Fullsize modal for displaying selected project -->
    <div id="modal" class="modal">
        <span class="close" id="closeModal">&times;</span>
        <div class="modal-content">
            <img id="modalImage" src="" alt="Project Image">
            <div id="modalDescription"></div>
        </div>
    </div>

    <script>
        // Sample data for portfolio projects
        const projects = [
            {
                title: "Project One",
                image: "images/project1.jpg",
                description: "Description for project one."
            },
            {
                title: "Project Two",
                image: "images/project2.jpg",
                description: "Description for project two."
            },
            {
                title: "Project Three",
                image: "images/project3.jpg",
                description: "Description for project three."
            }
        ];

        // Function to create portfolio items dynamically
        function createPortfolioItems(projects) {
            const portfolioContainer = document.querySelector('.portfolio-container');
            projects.forEach(project => {
                const portfolioItem = document.createElement('div');
                portfolioItem.className = 'portfolio-item';
                
                const img = document.createElement('img');
                img.src = project.image;
                img.alt = project.title;
                img.className = 'portfolio-image';

                // Event listener to show fullsize project on click
                img.addEventListener('click', () => {
                    showModal(project);
                });

                portfolioItem.appendChild(img);
                portfolioContainer.appendChild(portfolioItem);
            });
        }

        // Function to show modal with fullsize image and description
        function showModal(project) {
            document.getElementById('modalImage').src = project.image;
            document.getElementById('modalDescription').innerText = project.description;
            document.getElementById('modal').style.display = "block";
        }

        // Function to close modal
        function closeModal() {
            document.getElementById('modal').style.display = "none";
        }

        // Event listener for closing modal
        document.getElementById('closeModal').addEventListener('click', closeModal);
        window.addEventListener('click', (event) => {
            if (event.target === document.getElementById('modal')) {
                closeModal();
            }
        });

        // Initialize portfolio on page load
        window.onload = () => {
            createPortfolioItems(projects);
        };
    </script>

</body>
</html>

<style>
    /* Basic styles for the portfolio display */
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }

    .portfolio-container {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        padding: 20px;
    }

    .portfolio-item {
        cursor: pointer;
    }

    .portfolio-image {
        width: 200px;
        height: 150px;
        object-fit: cover;
        border-radius: 8px;
        transition: transform 0.2s;
    }

    .portfolio-image:hover {
        transform: scale(1.05);
    }

    /* Styles for modal */
    .modal {
        display: none;
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0,0,0,0.8);
    }

    .modal-content {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin: 15% auto;
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        max-width: 500px;
    }

    #modalImage {
        max-width: 100%;
        border-radius: 8px;
    }

    .close {
        color: #aaa;
        float: right;
        font-size: 28px;
        font-weight: bold;
    }

    .close:hover,
    .close:focus {
        color: black;
        text-decoration: none;
        cursor: pointer;
    }
</style>
```
