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

// Check if PHP-GTK is installed
if (!extension_loaded('gtk')) {
    die('PHP-GTK is not installed or not enabled');
}

// Import the GTK library
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

// Connect the button's clicked signal to a callback
$button->connect('clicked', function() use ($label) {
    $label->set_text('Button clicked!');
});

// Connect the window's delete event to a callback
$window->connect('delete-event', function($widget, $event) {
    gtk_main_quit();
    return FALSE;
});

// Show all widgets
$window->show_all();

// Start the GTK main loop
gtk_main();

?>
```
