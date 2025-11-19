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

// Check if PHP-GTK is installed
if (!extension_loaded('gtk')) {
    die('PHP-GTK is not installed or not enabled');
}

// Create a new GTK window
$window = new GtkWindow();
$window->set_title('PHP-GTK Example');
$window->set_default_size(300, 200);

// Create a vertical box layout
$vbox = new GtkVBox();
$vbox->set_spacing(6);

// Create a label
$label = new GtkLabel('Hello, World!');
$vbox->pack_start($label, FALSE, TRUE, 0);

// Create a button
$button = new GtkButton('Click me!');
$vbox->pack_start($button, FALSE, TRUE, 0);

// Add the vertical box layout to the window
$window->add($vbox);

// Connect the button's clicked signal to a callback function
$button->connect('clicked', function($button) use ($label) {
    $label->set_text('Button clicked!');
});

// Connect the window's delete event to a callback function
$window->connect('delete-event', function($window, $event) {
    $window->destroy();
    return FALSE;
});

// Show all widgets
$window->show_all();

// Run the GTK main loop
Gtk::main();

?>
```
