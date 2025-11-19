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
/**
 * Simple PHP-GTK GUI Application Example
 * 
 * This script demonstrates how to create a basic window with a button using PHP-GTK.
 * When the button is clicked, it shows a dialog message.
 */

// Check if PHP-GTK extension is available
if (!extension_loaded('gtk')) {
    die("PHP-GTK extension is not loaded. Please install and enable it to run this application.\n");
}

// Initialize GTK
if (!class_exists('Gtk')) {
    die("Gtk class not found. PHP-GTK may not be properly installed.\n");
}

// Create the main window
$window = new GtkWindow();
$window->set_title('PHP-GTK Demo');
$window->set_default_size(300, 200);
$window->set_position(Gtk::WIN_POS_CENTER);

// Connect the 'destroy' signal to exit the application
$window->connect('destroy', function() {
    Gtk::main_quit();
});

// Create a button
$button = new GtkButton('Click Me!');

// Connect the 'clicked' signal to show a message dialog
$button->connect('clicked', function() use ($window) {
    $dialog = new GtkMessageDialog(
        $window,
        Gtk::DIALOG_MODAL,
        Gtk::MESSAGE_INFO,
        Gtk::BUTTONS_OK,
        "Hello from PHP-GTK!"
    );
    $dialog->run();
    $dialog->destroy();
});

// Add the button to the window
$window->add($button);

// Show all widgets
$window->show_all();

// Start the GTK main loop
Gtk::main();
?>
```
