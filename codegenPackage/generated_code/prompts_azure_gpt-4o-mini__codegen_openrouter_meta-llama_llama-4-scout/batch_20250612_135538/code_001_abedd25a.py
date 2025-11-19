"""
Generated Code Metadata:
========================
Original URL: https://questsmisten.site
Prompt: How can I implement a copyright notice in the footer of my website using HTML and CSS?
Generated: DETERMINISTIC_abedd25a7e362a36
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### HTML Code

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Example Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Main content -->
    <main>
        <!-- Your website content here -->
    </main>
    
    <!-- Footer section -->
    <footer class="footer">
        <div class="container">
            <p class="copyright-notice">&copy; <?php echo date("Y"); ?> Example Website. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

### CSS Code

```css
/* styles.css */

/* Global styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Footer styles */
.footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

.footer .container {
    max-width: 800px;
    margin: 0 auto;
}

.copyright-notice {
    font-size: 0.8em;
    margin-bottom: 0.5em;
}
```

### PHP Code (for dynamic year)

```php
// If you're using a PHP-enabled server, save this as a separate file (e.g., config.php) or include it in your HTML file if supported.

<?php
// Check if date function is available
if (function_exists('date')) {
    // Get current year
    $currentYear = date("Y");
} else {
    // Handle the case when date function is not available
    $currentYear = '2023'; // Default year
}
?>
```

**Alternatively**, if your server doesn't support PHP or you prefer a static solution, you can directly use the current year in your HTML:

```html
<p class="copyright-notice">&copy; 2023 Example Website. All rights reserved.</p>
```

Or use JavaScript for a dynamic year:

```javascript
// Add this script before </body>
<script>
    document.querySelector('.copyright-notice').textContent = `&copy; ${new Date().getFullYear()} Example Website. All rights reserved.`;
</script>
```
