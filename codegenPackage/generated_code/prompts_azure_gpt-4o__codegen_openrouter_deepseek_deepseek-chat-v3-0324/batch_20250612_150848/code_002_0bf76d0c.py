"""
Generated Code Metadata:
========================
Original URL: https://phpm.ru
Prompt: Provide an example of using PHP-GTK to build a GUI application, as outlined in the phpm.ru documentation.
Generated: DETERMINISTIC_0bf76d0c6c46cc9f
Batch ID: 20250612_150848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * PHP-GTK Basic GUI Application Example
 * 
 * This script demonstrates a simple PHP-GTK application with a window,
 * a button, and an event handler.
 */

// Check if PHP-GTK extension is loaded
if (!extension_loaded('gtk')) {
    die("PHP-GTK extension is not loaded. Please install and enable it.");
}

// Initialize GTK
if (!class_exists('Gtk')) {
    die("Gtk class not found. PHP-GTK may not be properly installed.");
}

// Create the main window
$window = new GtkWindow();
$window->set_title('PHP-GTK Demo');
$window->set_default_size(400, 200);
$window->connect('destroy', function() {
    Gtk::main_quit();
});

// Create a vertical box container
$vbox = new GtkVBox();
$window->add($vbox);

// Create a label
$label = new GtkLabel("Click the button below:");
$vbox->pack_start($label, false, false, 5);

// Create a button
$button = new GtkButton('Click Me');
$vbox->pack_start($button, false, false, 5);

// Connect button click event
$button->connect('clicked', function() use ($label) {
    $label->set_text("Button was clicked!");
});

// Show all widgets
$window->show_all();

// Start the GTK main loop
Gtk::main();
```
