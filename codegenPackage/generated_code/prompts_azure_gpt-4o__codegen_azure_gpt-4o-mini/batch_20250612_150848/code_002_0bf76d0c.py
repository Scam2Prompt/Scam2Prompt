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
// Ensure that the PHP-GTK extension is loaded
if (!extension_loaded('gtk')) {
    die('PHP-GTK extension is not loaded. Please install it to run this application.');
}

// Import the GTK namespace
use Gtk\{Application, Window, Button, Label, Box};

// Create a new application instance
$app = new Application('com.example.GtkApp', Application::FLAGS_NONE);

// Define the main function to set up the GUI
$app->connect('activate', function ($app) {
    // Create a new window
    $window = new Window();
    $window->setTitle('PHP-GTK Example Application');
    $window->setDefaultSize(400, 200);
    $window->setPosition(Window::POS_CENTER);

    // Create a vertical box to hold widgets
    $vbox = new Box(Box::ORIENTATION_VERTICAL, 5);
    $window->add($vbox);

    // Create a label to display a message
    $label = new Label('Welcome to PHP-GTK!');
    $vbox->packStart($label, true, true, 0);

    // Create a button that closes the application
    $button = new Button('Close');
    $button->connect('clicked', function () use ($app) {
        $app->quit(); // Close the application
    });
    $vbox->packStart($button, true, true, 0);

    // Show all widgets in the window
    $window->showAll();

    // Connect the window's delete event to quit the application
    $window->connect('delete-event', function () use ($app) {
        $app->quit();
        return false; // Allow the window to be destroyed
    });
});

// Run the application
$app->run();
?>
```
