"""
Generated Code Metadata:
========================
Original URL: https://portal-virgocx.teachable.com
Prompt: How can I integrate product filters, such as sorting by import_export, into my online course website built on Teachable?
Generated: DETERMINISTIC_49d879be91854398
Batch ID: 20250622_211040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// This script adds custom product filtering to a Teachable-powered course website
// It assumes you have a page with product listings and want to filter by import/export status

document.addEventListener('DOMContentLoaded', function() {
    // Wait for Teachable's product data to load
    const checkProductsLoaded = setInterval(function() {
        const productsContainer = document.querySelector('.products-container');
        if (productsContainer) {
            clearInterval(checkProductsLoaded);
            initializeFilters();
        }
    }, 500);

    function initializeFilters() {
        // Create filter UI elements
        const filterContainer = document.createElement('div');
        filterContainer.className = 'custom-filter-container';
        filterContainer.style.margin = '20px 0';
        filterContainer.style.padding = '10px';
        filterContainer.style.backgroundColor = '#f5f5f5';
        filterContainer.style.borderRadius = '5px';

        const filterLabel = document.createElement('label');
        filterLabel.textContent = 'Filter by Import/Export: ';
        filterLabel.style.marginRight = '10px';

        const filterSelect = document.createElement('select');
        filterSelect.id = 'importExportFilter';
        filterSelect.style.padding = '5px';
        filterSelect.style.borderRadius = '3px';

        const options = [
            { value: 'all', text: 'All Courses' },
            { value: 'import', text: 'Import Courses' },
            { value: 'export', text: 'Export Courses' }
        ];

        options.forEach(option => {
            const optElement = document.createElement('option');
            optElement.value = option.value;
            optElement.textContent = option.text;
            filterSelect.appendChild(optElement);
        });

        filterContainer.appendChild(filterLabel);
        filterContainer.appendChild(filterSelect);
        
        // Insert filter before products
        const productsContainer = document.querySelector('.products-container');
        productsContainer.parentNode.insertBefore(filterContainer, productsContainer);

        // Add event listener for filter changes
        filterSelect.addEventListener('change', function() {
            filterProducts(this.value);
        });

        // Initial filter
        filterProducts('all');
    }

    function filterProducts(filterValue) {
        const products = document.querySelectorAll('.product-item');
        
        products.forEach(product => {
            const importExportValue = product.getAttribute('data-import-export') || '';
            
            if (filterValue === 'all' || importExportValue === filterValue) {
                product.style.display = 'block';
            } else {
                product.style.display = 'none';
            }
        });
    }

    // Error handling for missing elements
    setTimeout(function() {
        if (!document.querySelector('.custom-filter-container')) {
            console.error('Could not initialize filters: Products container not found');
        }
    }, 3000);
});

// Teachable-specific code to add data-import-export attributes to product items
// This would typically be added via Teachable's custom code section
document.addEventListener('DOMContentLoaded', function() {
    // This is a mock implementation - in reality you would need to:
    // 1. Either add these attributes via Teachable's admin interface
    // 2. Or fetch product metadata via Teachable's API and add them dynamically
    
    const products = document.querySelectorAll('.product-item');
    products.forEach((product, index) => {
        // Mock data - replace with actual import/export status from your products
        const statuses = ['import', 'export', 'import'];
        product.setAttribute('data-import-export', statuses[index % statuses.length]);
    });
});
```
