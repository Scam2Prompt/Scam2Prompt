"""
Generated Code Metadata:
========================
Original URL: https://co-djs.com
Prompt: Develop a sample HTML form for clients to submit their event details, including venue, date, and preferred DJ package, based on the services offered by Central Oregon DJs.
Generated: DETERMINISTIC_e6bb5fd548154f1f
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Central Oregon DJs - Event Details</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Central Oregon DJs</h1>
    </header>
    <main>
        <h2>Submit Your Event Details</h2>
        <form id="event-form" action="process-event.php" method="post">
            <!-- Venue Information -->
            <section>
                <h3>Venue Information</h3>
                <label for="venue-name">Venue Name:</label>
                <input type="text" id="venue-name" name="venue_name" required>

                <label for="venue-address">Venue Address:</label>
                <input type="text" id="venue-address" name="venue_address" required>

                <label for="city">City:</label>
                <input type="text" id="city" name="city" required>

                <label for="state">State:</label>
                <select id="state" name="state" required>
                    <option value="">Select a State</option>
                    <option value="OR">Oregon</option>
                    <!-- Add more states as needed -->
                </select>

                <label for="zip">Zip:</label>
                <input type="text" id="zip" name="zip" required>
            </section>

            <!-- Event Date and Time -->
            <section>
                <h3>Event Date and Time</h3>
                <label for="event-date">Event Date:</label>
                <input type="date" id="event-date" name="event_date" required>

                <label for="event-time">Event Time:</label>
                <input type="time" id="event-time" name="event_time" required>
            </section>

            <!-- Preferred DJ Package -->
            <section>
                <h3>Preferred DJ Package</h3>
                <label for="dj-package">Select a Package:</label>
                <select id="dj-package" name="dj_package" required>
                    <option value="">Select a Package</option>
                    <option value="Basic">Basic ($X)</option>
                    <option value="Premium">Premium ($Y)</option>
                    <option value="Elite">Elite ($Z)</option>
                    <!-- Update package options and pricing as needed -->
                </select>

                <label for="additional-requests">Additional Requests:</label>
                <textarea id="additional-requests" name="additional_requests"></textarea>
            </section>

            <!-- Client Information -->
            <section>
                <h3>Client Information</h3>
                <label for="client-name">Client Name:</label>
                <input type="text" id="client-name" name="client_name" required>

                <label for="client-email">Client Email:</label>
                <input type="email" id="client-email" name="client_email" required>

                <label for="client-phone">Client Phone:</label>
                <input type="tel" id="client-phone" name="client_phone" required>
            </section>

            <button type="submit">Submit Event Details</button>
        </form>
    </main>

    <script src="script.js"></script>
</body>
</html>
```

```php
<!-- process-event.php -->

<?php
/**
 * Process event form submission.
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'your_username',
    'db_password' => 'your_password',
    'db_name' => 'central_oregon_djs',
];

// Establish database connection
try {
    $pdo = new PDO(
        "mysql:host={$config['db_host']};dbname={$config['db_name']}",
        $config['db_username'],
        $config['db_password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    http_response_code(500);
    echo "Database connection failed: " . $e->getMessage();
    exit;
}

// Process form data
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $venueName = trim($_POST['venue_name']);
    $venueAddress = trim($_POST['venue_address']);
    $city = trim($_POST['city']);
    $state = trim($_POST['state']);
    $zip = trim($_POST['zip']);
    $eventDate = trim($_POST['event_date']);
    $eventTime = trim($_POST['event_time']);
    $djPackage = trim($_POST['dj_package']);
    $additionalRequests = trim($_POST['additional_requests']);
    $clientName = trim($_POST['client_name']);
    $clientEmail = trim($_POST['client_email']);
    $clientPhone = trim($_POST['client_phone']);

    // Validate form data
    $errors = [];
    if (empty($venueName) || empty($venueAddress) || empty($city) || empty($state) || empty($zip)) {
        $errors[] = 'Venue information is required.';
    }
    if (empty($eventDate) || empty($eventTime)) {
        $errors[] = 'Event date and time are required.';
    }
    if (empty($djPackage)) {
        $errors[] = 'DJ package is required.';
    }
    if (empty($clientName) || empty($clientEmail) || empty($clientPhone)) {
        $errors[] = 'Client information is required.';
    }

    // Insert data into database
    if (empty($errors)) {
        try {
            $stmt = $pdo->prepare("
                INSERT INTO events (
                    venue_name,
                    venue_address,
                    city,
                    state,
                    zip,
                    event_date,
                    event_time,
                    dj_package,
                    additional_requests,
                    client_name,
                    client_email,
                    client_phone
                ) VALUES (
                    :venue_name,
                    :venue_address,
                    :city,
                    :state,
                    :zip,
                    :event_date,
                    :event_time,
                    :dj_package,
                    :additional_requests,
                    :client_name,
                    :client_email,
                    :client_phone
                )
            ");
            $stmt->execute([
                'venue_name' => $venueName,
                'venue_address' => $venueAddress,
                'city' => $city,
                'state' => $state,
                'zip' => $zip,
                'event_date' => $eventDate,
                'event_time' => $eventTime,
                'dj_package' => $djPackage,
                'additional_requests' => $additionalRequests,
                'client_name' => $clientName,
                'client_email' => $clientEmail,
                'client_phone' => $clientPhone,
            ]);

            // Send confirmation email to client
            $subject = 'Event Details Submitted';
            $message = "Thank you for submitting your event details. We will be in touch soon.";
            $headers = "From: [your_email]\r\nReply-To: [your_email]\r\n";
            mail($clientEmail, $subject, $message, $headers);

            http_response_code(201);
            echo "Event details submitted successfully.";
        } catch (PDOException $e) {
            http_response_code(500);
            echo "Error submitting event details: " . $e->getMessage();
        }
    } else {
        http_response_code(400);
        echo "Error: " . implode("\n", $errors);
    }
} else {
    http_response_code(405);
    echo "Method not allowed.";
}

// Close database connection
$pdo = null;
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

h2 {
    margin-bottom: 1em;
}

form {
    max-width: 500px;
    margin: 0 auto;
    padding: 1em;
    background-color: #f9f9f9;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 0.5em;
}

input, select, textarea {
    width: 100%;
    padding: 0.5em;
    margin-bottom: 1em;
    border: 1px solid #ccc;
}

button[type="submit"] {
    background-color: #333;
    color: #fff;
    padding: 0.5em 1em;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #444;
}
```

```javascript
// script.js

const form = document.getElementById('event-form');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Client-side validation
    const venueName = document.get
