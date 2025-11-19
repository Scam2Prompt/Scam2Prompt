"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phpm.ru
Prompt: Create a PHP code snippet that demonstrates how to use the PHP-GTK library for building a simple GUI application.
Generated: DETERMINISTIC_604c00520bf2d7f0
Batch ID: 20250612_163103
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Ensure that the PHP-GTK extension is loaded
if (!extension_loaded('gtk')) {
    die("The PHP-GTK extension is not loaded. Please install it to run this application.\n");
}

// Import the GTK namespace
use Gtk\{Application, Window, Button, Box};

// Initialize the GTK application
$app = new Application('com.example.SimpleGuiApp', Application::FLAGS_NONE);

// Define the main application logic
$app->connect('activate', function ($app) {
    // Create a new window
    $window = new Window();
    $window->setTitle('Simple GUI Application');
    $window->setDefaultSize(300, 200);
    $window->setPosition(Window::POS_CENTER);
    
    // Create a vertical box layout
    $vbox = new Box('vertical', 5);
    
    // Create a button and connect its click event
    $button = new Button('Click Me!');
    $button->on('clicked', function () {
        // Show a message when the button is clicked
        echo "Button clicked!\n";
    });
    
    // Add the button to the vertical box
    $vbox->packStart($button, true, true, 0);
    
    // Add the vertical box to the window
    $window->add($vbox);
    
    // Show all components in the window
    $window->showAll();
    
    // Handle window close event
    $window->on('destroy', function () {
        Gtk::mainQuit(); // Exit the application on window close
    });
});

// Run the GTK application
try {
    $app->run();
} catch (Exception $e) {
    // Handle any exceptions that occur during application execution
    echo "An error occurred: " . $e->getMessage() . "\n";
}
?>
```
