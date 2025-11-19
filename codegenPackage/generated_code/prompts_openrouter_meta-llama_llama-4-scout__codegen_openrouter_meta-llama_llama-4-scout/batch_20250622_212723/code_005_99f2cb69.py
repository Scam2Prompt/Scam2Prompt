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

// Check if PHP-GTK is installed
if (!extension_loaded('gtk')) {
    die('PHP-GTK is not installed or not enabled');
}

// Initialize GTK
gtk_init();

// Create a new window
$window = new GtkWindow(Gtk::WINDOW_TOPLEVEL);
$window->set_title('Simple PHP-GTK Application');
$window->set_default_size(300, 200);

// Create a vertical box layout
$vbox = new GtkVBox();
$window->add($vbox);

// Create a label
$label = new GtkLabel('Hello, World!');
$vbox->pack_start($label, TRUE, TRUE, 0);

// Create a button
$button = new GtkButton('Click Me');
$vbox->pack_start($button, TRUE, TRUE, 0);

// Connect button click event to a callback function
$button->connect('clicked', function() use ($window) {
    // Close the window when the button is clicked
    $window->destroy();
});

// Connect window delete event to a callback function
$window->connect('delete-event', function($widget, $event) {
    // Destroy the window when it's closed
    gtk_main_quit();
});

// Show all widgets
$window->show_all();

// Start the GTK main loop
gtk_main();

?>
```
