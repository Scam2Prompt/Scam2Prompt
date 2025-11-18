"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phpm.ru
Prompt: Provide an example of using PHP-GTK to build a GUI application, as outlined in the phpm.ru documentation.
Generated: DETERMINISTIC_0bf76d0c6c46cc9f
Batch ID: 20250612_150848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Ensure the PHP-GTK extension is enabled before running this script.
// PHP-GTK must be installed and properly configured.
// This script demonstrates creating a simple PHP-GTK GUI application.

if (!extension_loaded('php_gtk')) {
    die("The PHP-GTK extension is not loaded. Please enable it to run this application.\n");
}

// Include PHP-GTK
require_once 'phpgtk/gtk.php';

// Create the main window
$window = new GtkWindow();
$window->set_title("PHP-GTK GUI Example");
$window->set_default_size(400, 300);

// Set up the close event for the window
$window->connect_simple('destroy', ['Gtk', 'main_quit']);

// Create a vertical box container to organize widgets
$vbox = new GtkVBox();
$window->add($vbox);

// Create a label and add it to the vbox
$label = new GtkLabel("Welcome to PHP-GTK!");
$vbox->pack_start($label, false, false);

// Create an entry widget (text box) and add it to the vbox
$entry = new GtkEntry();
$entry->set_placeholder_text("Type something here...");
$vbox->pack_start($entry, false, false);

// Create a button and add it to the vbox
$button = new GtkButton("Click Me!");
$vbox->pack_start($button, false, false);

// Button click event: Display an alert with the entry text
$button->connect_simple('clicked', function() use ($entry) {
    $text = $entry->get_text();
    $dialog = new GtkMessageDialog(null, Gtk::DIALOG_MODAL, Gtk::MESSAGE_INFO, Gtk::BUTTONS_OK, "You entered: $text");
    $dialog->run();
    $dialog->destroy();
});

// Show all widgets and the window
$window->show_all();

// Start the PHP-GTK main loop
Gtk::main();
```
