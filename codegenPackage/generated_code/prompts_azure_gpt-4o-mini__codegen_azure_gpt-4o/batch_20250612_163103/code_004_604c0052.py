"""
Generated Code Metadata:
========================
Original URL: https://phpm.ru
Prompt: Create a PHP code snippet that demonstrates how to use the PHP-GTK library for building a simple GUI application.
Generated: DETERMINISTIC_604c00520bf2d7f0
Batch ID: 20250612_163103
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Ensure PHP-GTK is installed and enabled before running this script.
// PHP-GTK is not included in standard PHP distributions and must be installed separately.

// Check if PHP-GTK is available
if (!extension_loaded('php_gtk')) {
    die("PHP-GTK extension is not loaded. Please install and enable PHP-GTK to run this application.\n");
}

// Import necessary PHP-GTK classes
use GtkWindow;
use GtkLabel;
use GtkButton;
use GtkVBox;

// Create the main application window
$window = new GtkWindow();
$window->set_title("PHP-GTK Simple GUI Application");
$window->set_default_size(400, 200);
$window->connect_simple('destroy', ['Gtk', 'main_quit']); // Close the application when the window is closed

// Create a vertical box container to hold widgets
$vbox = new GtkVBox();
$window->add($vbox);

// Add a label to the window
$label = new GtkLabel("Welcome to PHP-GTK!");
$vbox->pack_start($label, false, false, 5);

// Add a button to the window
$button = new GtkButton("Click Me");
$vbox->pack_start($button, false, false, 5);

// Connect a callback function to the button's 'clicked' signal
$button->connect_simple('clicked', function () use ($label) {
    // Update the label text when the button is clicked
    $label->set_text("Button clicked!");
});

// Show all widgets in the window
$window->show_all();

// Start the GTK main loop
Gtk::main();
```
