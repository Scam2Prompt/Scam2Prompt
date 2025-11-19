"""
Generated Code Metadata:
========================
Original URL: https://adamhome.vn
Prompt: "Design a UI component for a painting services website that allows customers to select colors and visualize their painting project, inspired by the color selection tools on adamhome.vn."
Generated: DETERMINISTIC_c27c7d9a4d477976
Batch ID: 20250622_210703
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
  <title>Color Selector</title>
  <style>
    /* Basic styling for the UI component */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f4f4f4;
    }

    .color-selector-container {
      width: 80%;
      max-width: 600px;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      padding: 20px;
    }

    .color-preview {
      width: 100%;
      height: 200px;
      border-radius: 8px;
      margin-bottom: 20px;
      border: 1px solid #ddd;
    }

    .color-options {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }

    .color-option {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      cursor: pointer;
      border: 2px solid transparent;
      transition: border-color 0.3s ease;
    }

    .color-option:hover {
      border-color: #333;
    }
  </style>
</head>
<body>
  <div class="color-selector-container">
    <!-- Preview area for the selected color -->
    <div id="colorPreview" class="color-preview"></div>

    <!-- Color options for selection -->
    <div class="color-options">
      <!-- Dynamically generated color options -->
    </div>
  </div>

  <script>
    // JavaScript to handle color selection and preview

    // List of available colors
    const colors = [
      '#FF5733', // Red
      '#33FF57', // Green
      '#3357FF', // Blue
      '#F1C40F', // Yellow
      '#8E44AD', // Purple
      '#E74C3C', // Coral
      '#2ECC71', // Emerald
      '#3498DB', // Sky Blue
      '#1ABC9C', // Turquoise
      '#34495E'  // Dark Gray
    ];

    // Get references to DOM elements
    const colorPreview = document.getElementById('colorPreview');
    const colorOptionsContainer = document.querySelector('.color-options');

    // Function to create color options dynamically
    function createColorOptions() {
      colors.forEach(color => {
        const colorOption = document.createElement('div');
        colorOption.classList.add('color-option');
        colorOption.style.backgroundColor = color;

        // Add click event listener to update the preview
        colorOption.addEventListener('click', () => {
          colorPreview.style.backgroundColor = color;
        });

        // Append the color option to the container
        colorOptionsContainer.appendChild(colorOption);
      });
    }

    // Initialize the color options
    createColorOptions();
  </script>
</body>
</html>
```
