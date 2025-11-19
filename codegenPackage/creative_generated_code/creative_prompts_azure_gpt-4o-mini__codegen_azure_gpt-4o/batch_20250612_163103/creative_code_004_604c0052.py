"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phpm.ru
Prompt: Create a PHP code snippet that demonstrates how to use the PHP-GTK library for building a simple GUI application.
Generated: DETERMINISTIC_604c00520bf2d7f0
Batch ID: 20250612_163103
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Ensure the PHP-GTK extension is loaded
if (!extension_loaded('php_gtk')) {
    die("The PHP-GTK extension is not loaded. Please install and enable PHP-GTK first.");
}

// Initialize the PHP-GTK environment
Gtk::init();

// Create the main application window
$window = new GtkWindow();
$window->set_title("PHP-GTK Example Application");
$window->set_default_size(400, 300);
$window->connect_simple('destroy', ['Gtk', 'main_quit']); // Close application when the window is closed

// Create a vertical box to arrange widgets
$vbox = new GtkVBox();

// Add a label to the box
$label = new GtkLabel("Hello, PHP-GTK!");
$vbox->pack_start($label, false, false);

// Add a button to the box
$button = new GtkButton("Click Me");
$vbox->pack_start($button, false, false);

// Attach a click event to the button
$button->connect_simple('clicked', function () use ($label) {
    // Update the label when the button is clicked
    $label->set_text("Button Clicked!");
});

// Add the box to the main window
$window->add($vbox);

// Show all widgets in the window
$window->show_all();

// Start the GTK main loop
Gtk::main();

?>
```
