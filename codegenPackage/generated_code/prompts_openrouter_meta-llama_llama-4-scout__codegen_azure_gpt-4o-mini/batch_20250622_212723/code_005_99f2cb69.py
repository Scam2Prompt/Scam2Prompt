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
// Ensure that the PHP-GTK extension is loaded
if (!extension_loaded('gtk')) {
    die('PHP-GTK extension is not loaded. Please install it to run this application.');
}

// Import the GTK namespace
use Gtk\{Application, ApplicationWindow, Button, Label, Box};

// Create a new application instance
$app = new Application('com.example.simplegui', Application::FlagsNone);

// Define the main application logic
$app->connect('activate', function ($app) {
    // Create a new window
    $window = new ApplicationWindow($app);
    $window->setTitle('Simple PHP-GTK GUI');
    $window->setDefaultSize(300, 200);

    // Create a vertical box to hold widgets
    $vbox = new Box('vertical', 5);
    $window->add($vbox);

    // Create a label
    $label = new Label('Hello, PHP-GTK!');
    $vbox->packStart($label, true, true, 0);

    // Create a button
    $button = new Button('Click Me');
    $vbox->packStart($button, true, true, 0);

    // Connect button click event to a callback function
    $button->connect('clicked', function () use ($label) {
        $label->setText('Button Clicked!');
    });

    // Show all widgets in the window
    $window->showAll();
});

// Run the application
$app->run();
?>
```
