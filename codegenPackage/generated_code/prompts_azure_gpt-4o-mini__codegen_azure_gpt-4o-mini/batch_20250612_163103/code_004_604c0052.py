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
// Ensure that the PHP-GTK extension is loaded
if (!extension_loaded('gtk')) {
    die('PHP-GTK extension is not loaded. Please install it to run this application.');
}

// Import the GTK namespace
use Gtk\{Application, Window, Button, Label, Box};

// Create a new application instance
$app = new Application('com.example.gtkapp', 0);

// Define the main application logic
$app->connect('activate', function ($app) {
    // Create a new window
    $window = new Window();
    $window->setTitle('Simple PHP-GTK Application');
    $window->setDefaultSize(300, 200);
    $window->setPosition(Window::POS_CENTER);

    // Create a vertical box to hold widgets
    $vbox = new Box(Box::ORIENTATION_VERTICAL, 5);
    $window->add($vbox);

    // Create a label
    $label = new Label('Hello, PHP-GTK!');
    $vbox->packStart($label, true, true, 0);

    // Create a button
    $button = new Button('Click Me');
    $vbox->packStart($button, true, true, 0);

    // Connect button click event to a callback function
    $button->connect('clicked', function() use ($label) {
        $label->setText('Button Clicked!');
    });

    // Connect the window's delete event to close the application
    $window->connect('destroy', function() use ($app) {
        $app->quit();
    });

    // Show all widgets in the window
    $window->showAll();
});

// Run the application
$app->run();
?>
```
