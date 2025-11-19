"""
Generated Code Metadata:
========================
Original URL: https://dustbox.netlify.app
Prompt: Generate code to implement a searchable table of contents feature inspired by Dustbox.netlify.app.
Generated: DETERMINISTIC_b8c09e920aa8d664
Batch ID: 20250612_153702
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
    <title>Searchable Table of Contents</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        h1 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        
        .search-container {
            margin-bottom: 20px;
            position: sticky;
            top: 0;
            background: white;
            padding: 10px 0;
            z-index: 100;
        }
        
        #searchInput {
            width: 100%;
            padding: 12px 20px;
            margin: 8px 0;
            box-sizing: border-box;
            border: 2px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        
        #searchInput:focus {
            border-color: #3498db;
            outline: none;
        }
        
        .toc-container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }
        
        .toc-category {
            flex: 1;
            min-width: 300px;
            background: #f9f9f9;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        .toc-category h2 {
            margin-top: 0;
            color: #3498db;
            padding-bottom: 10px;
            border-bottom: 1px solid #eee;
        }
        
        .toc-item {
            padding: 8px 0;
            border-bottom: 1px dashed #eee;
        }
        
        .toc-item:last-child {
            border-bottom: none;
        }
        
        .toc-item a {
            color: #2c3e50;
            text-decoration: none;
            transition: color 0.2s;
        }
        
        .toc-item a:hover {
            color: #3498db;
        }
        
        .no-results {
            padding: 20px;
            text-align: center;
            color: #7f8c8d;
            font-style: italic;
        }
        
        .highlight {
            background-color: #fffde7;
            font-weight: bold;
            padding: 2px;
        }
    </style>
</head>
<body>
    <h1>Searchable Table of Contents</h1>
    
    <div class="search-container">
        <input type="text" id="searchInput" placeholder="Search for items..." autocomplete="off">
    </div>
    
    <div class="toc-container" id="tocContainer">
        <!-- Content will be dynamically loaded here -->
    </div>

    <script>
        // Sample data structure for the table of contents
        const tocData = [
            {
                category: "Getting Started",
                items: [
                    { title: "Introduction", url: "#intro" },
                    { title: "Installation Guide", url: "#install" },
                    { title: "Quick Start Tutorial", url: "#quickstart" }
                ]
            },
            {
                category: "Core Concepts",
                items: [
                    { title: "Architecture Overview", url: "#architecture" },
                    { title: "Data Models", url: "#models" },
                    { title: "API Reference", url: "#api" }
                ]
            },
            {
                category: "Advanced Topics",
                items: [
                    { title: "Performance Optimization", url: "#performance" },
                    { title: "Security Best Practices", url: "#security" },
                    { title: "Scaling Strategies", url: "#scaling" }
                ]
            },
            {
                category: "Troubleshooting",
                items: [
                    { title: "Common Issues", url: "#issues" },
                    { title: "Debugging Techniques", url: "#debugging" },
                    { title: "FAQ", url: "#faq" }
                ]
            }
        ];

        // Initialize the table of contents
        function initializeTOC() {
            const tocContainer = document.getElementById('tocContainer');
            
            tocData.forEach(category => {
                const categoryElement = document.createElement('div');
                categoryElement.className = 'toc-category';
                
                const categoryTitle = document.createElement('h2');
                categoryTitle.textContent = category.category;
                categoryElement.appendChild(categoryTitle);
                
                category.items.forEach(item => {
                    const itemElement = document.createElement('div');
                    itemElement.className = 'toc-item';
                    
                    const link = document.createElement('a');
                    link.href = item.url;
                    link.textContent = item.title;
                    link.dataset.searchText = item.title.toLowerCase();
                    
                    itemElement.appendChild(link);
                    categoryElement.appendChild(itemElement);
                });
                
                tocContainer.appendChild(categoryElement);
            });
        }

        // Search functionality
        function setupSearch() {
            const searchInput = document.getElementById('searchInput');
            
            searchInput.addEventListener('input', function() {
                const searchTerm = this.value.toLowerCase().trim();
                const tocItems = document.querySelectorAll('.toc-item');
                let hasResults = false;
                
                // First, reset all items
                tocItems.forEach(item => {
                    item.style.display = '';
                    const link = item.querySelector('a');
                    link.innerHTML = link.textContent;
                });
                
                // If search term is empty, show all
                if (searchTerm === '') {
                    document.querySelectorAll('.toc-category').forEach(cat => {
                        cat.style.display = '';
                    });
                    return;
                }
                
                // Filter items
                tocItems.forEach(item => {
                    const link = item.querySelector('a');
                    const text = link.dataset.searchText;
                    
                    if (text.includes(searchTerm)) {
                        hasResults = true;
                        
                        // Highlight matching text
                        const originalText = link.textContent;
                        const regex = new RegExp(searchTerm, 'gi');
                        link.innerHTML = originalText.replace(regex, match => 
                            `<span class="highlight">${match}</span>`
                        );
                    } else {
                        item.style.display = 'none';
                    }
                });
                
                // Show/hide categories based on results
                document.querySelectorAll('.toc-category').forEach(category => {
                    const visibleItems = category.querySelectorAll('.toc-item:not([style*="display: none"])');
                    if (visibleItems.length > 0) {
                        category.style.display = '';
                    } else {
                        category.style.display = 'none';
                    }
                });
                
                // Show no results message if needed
                const noResults = document.querySelector('.no-results');
                if (noResults) {
                    noResults.remove();
                }
                
                if (!hasResults) {
                    const message = document.createElement('div');
                    message.className = 'no-results';
                    message.textContent = 'No results found. Try a different search term.';
                    document.getElementById('tocContainer').appendChild(message);
                }
            });
        }

        // Initialize the application
        document.addEventListener('DOMContentLoaded', function() {
            initializeTOC();
            setupSearch();
        });
    </script>
</body>
</html>
```
