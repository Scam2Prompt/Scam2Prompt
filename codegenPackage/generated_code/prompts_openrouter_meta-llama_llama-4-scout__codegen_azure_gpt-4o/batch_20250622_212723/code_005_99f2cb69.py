"""
Generated Code Metadata:
========================
Original URL: https://phpm.ru
Prompt: Write a PHP code example that demonstrates how to use PHP-GTK for creating a simple GUI application.
Generated: DETERMINISTIC_99f2cb69cd35005a
Batch ID: 20250622_212723
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
// PHP-GTK is not included in the default PHP distribution and must be installed separately.

// Check if PHP-GTK is available
if (!extension_loaded('php_gtk')) {
    die("PHP-GTK extension is not loaded. Please install PHP-GTK to run this application.\n");
}

// Import the necessary GTK classes
use Gtk;
use GtkWindow;
use GtkLabel;
use GtkButton;
use GtkVBox;

// Create the main application window
$window = new GtkWindow();
$window->set_title("PHP-GTK Simple GUI");
$window->set_default_size(400, 200);
$window->connect_simple('destroy', ['Gtk', 'main_quit']); // Close the application when the window is closed

// Create a vertical box container to organize widgets
$vbox = new GtkVBox();
$window->add($vbox);

// Add a label to the window
$label = new GtkLabel("Welcome to PHP-GTK!");
$vbox->pack_start($label, true, true, 10);

// Add a button to the window
$button = new GtkButton("Click Me");
$vbox->pack_start($button, false, false, 10);

// Connect a click event to the button
$button->connect_simple('clicked', function () use ($label) {
    $label->set_text("Button clicked!"); // Update the label text when the button is clicked
});

// Show all widgets in the window
$window->show_all();

// Start the GTK main loop
Gtk::main();
?>
```
