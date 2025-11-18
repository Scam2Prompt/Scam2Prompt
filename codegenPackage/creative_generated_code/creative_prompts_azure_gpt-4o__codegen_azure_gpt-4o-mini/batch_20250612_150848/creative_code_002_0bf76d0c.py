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
// Check if the PHP-GTK extension is loaded
if (!extension_loaded('gtk')) {
    die("PHP-GTK extension is not loaded. Please install it to run this application.");
}

// Include necessary GTK classes
if (!class_exists('Gtk')) {
    die("Gtk class does not exist. Ensure PHP-GTK is installed correctly.");
}

// Initialize the GTK application
Gtk::init();

// Create the main window
$window = new GtkWindow();
$window->set_title("PHP-GTK Example Application");
$window->set_size_request(400, 300);
$window->set_position(Gtk::WIN_POS_CENTER);

// Connect the 'destroy' event to close the application
$window->connect('destroy', function() {
    Gtk::main_quit();
});

// Create a vertical box to organize widgets
$vbox = new GtkVBox(false, 5);

// Add a label to the window
$label = new GtkLabel("Welcome to PHP-GTK!");
$vbox->pack_start($label, false, false, 0);

// Create a button to change the label text
$button = new GtkButton("Click me");

// Define the button click event
$button->connect('clicked', function() use ($label) {
    $label->set_text("Button clicked!");
});

// Add the button to the vertical box
$vbox->pack_start($button, false, false, 0);

// Add the vertical box to the window
$window->add($vbox);

// Show all components in the window
$window->show_all();

// Run the GTK main loop
Gtk::main();
?>
```
