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
/**
 * Simple PHP-GTK GUI Application Example
 * 
 * Demonstrates a basic window with a button that shows a message when clicked.
 */

// Check if PHP-GTK extension is loaded
if (!extension_loaded('gtk')) {
    die("PHP-GTK extension is not loaded. Please install and enable it to run this application.\n");
}

// Initialize GTK
if (!@gtk_init()) {
    die("Failed to initialize GTK.\n");
}

// Create the main window
$window = new GtkWindow();
$window->set_title('PHP-GTK Demo');
$window->set_default_size(300, 200);
$window->connect('destroy', function() {
    gtk::main_quit();
});

// Create a vertical box container
$vbox = new GtkVBox();
$window->add($vbox);

// Create a label
$label = new GtkLabel("Click the button below:");
$vbox->pack_start($label, false, false, 5);

// Create a button
$button = new GtkButton('Click Me');
$button->connect('clicked', function() {
    $dialog = new GtkMessageDialog(
        null,
        Gtk::DIALOG_MODAL,
        Gtk::MESSAGE_INFO,
        Gtk::BUTTONS_OK,
        "Hello from PHP-GTK!"
    );
    $dialog->run();
    $dialog->destroy();
});
$vbox->pack_start($button, false, false, 5);

// Show all widgets
$window->show_all();

// Start the GTK main loop
gtk::main();
```
