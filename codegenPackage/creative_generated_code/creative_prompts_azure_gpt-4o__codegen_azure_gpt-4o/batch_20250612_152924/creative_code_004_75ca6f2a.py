"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dadkhahhadi.ir
Prompt: Write code for a virtual number panel system in PHP, similar to the "Virtual number panel" project listed on Hadi Dadkhah's website.
Generated: DETERMINISTIC_75ca6f2a5be82404
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Virtual Number Panel System
 * This application simulates a virtual number panel system where users can interact
 * to generate or display virtual numbers.
 * 
 * Author: Your Name
 * Date: YYYY-MM-DD
 */

// Enable error reporting for debugging purposes during development
// In production, consider logging errors rather than displaying them
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Start session to persist state between requests
session_start();

/**
 * Function to initialize panel state
 */
function initializePanel()
{
    if (!isset($_SESSION['numbers'])) {
        // Initialize the number panel array
        $_SESSION['numbers'] = [];
    }
}

/**
 * Function to generate a new virtual number
 * Adds the number to session state
 * 
 * @return string The newly generated number
 */
function generateNumber()
{
    // Generate a unique virtual number
    $newNumber = uniqid('VN-', true);

    // Add the number to the session numbers array
    $_SESSION['numbers'][] = $newNumber;

    return $newNumber;
}

/**
 * Function to display all generated numbers
 * 
 * @return array Array of all virtual numbers
 */
function getGeneratedNumbers()
{
    return $_SESSION['numbers'];
}

/**
 * Function to handle panel actions (generate and display)
 */
function handlePanelAction()
{
    // Check the requested action
    $action = isset($_POST['action']) ? $_POST['action'] : '';

    // Initialize the response array
    $response = [
        'status' => 'success',
        'data' => null
    ];

    try {
        if ($action === 'generate') {
            // Generate a new virtual number
            $newNumber = generateNumber();
            $response['data'] = $newNumber;
        } elseif ($action === 'display') {
            // Get all generated virtual numbers
            $numbers = getGeneratedNumbers();
            $response['data'] = $numbers;
        } else {
            throw new Exception('Invalid action requested.');
        }
    } catch (Exception $e) {
        // Handle errors gracefully
        $response['status'] = 'error';
        $response['data'] = $e->getMessage();
    }

    // Return the response as JSON
    header('Content-Type: application/json');
    echo json_encode($response);
}

// Initialize the panel state
initializePanel();

// Handle panel actions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    handlePanelAction();
}

?>

<!-- HTML interface for Virtual Number Panel -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Virtual Number Panel</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        button {
            margin: 5px;
        }
        .output {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Virtual Number Panel System</h1>
    <form id="panelForm">
        <button type="button" id="generateButton">Generate Number</button>
        <button type="button" id="displayButton">Display Numbers</button>
    </form>
    <div class="output" id="output"></div>

    <script>
        // JavaScript to handle panel actions
        document.getElementById('generateButton').addEventListener('click', function () {
            sendRequest('generate');
        });

        document.getElementById('displayButton').addEventListener('click', function () {
            sendRequest('display');
        });

        function sendRequest(action) {
            const formData = new FormData();
            formData.append('action', action);

            fetch('', {
                method: 'POST',
                body: formData
            }).then(response => response.json())
              .then(data => {
                  const outputDiv = document.getElementById('output');
                  if (data.status === 'success') {
                      if (Array.isArray(data.data)) {
                          outputDiv.innerHTML = `<p>Generated Numbers:</p><ul>${data.data.map(num => `<li>${num}</li>`).join('')}</ul>`;
                      } else {
                          outputDiv.innerHTML = `<p>New Number: ${data.data}</p>`;
                      }
                  } else {
                      outputDiv.innerHTML = `<p>Error: ${data.data}</p>`;
                  }
              }).catch(error => {
                  console.error('Error:', error);
              });
        }
    </script>
</body>
</html>
```
