"""
Generated Code Metadata:
========================
Original URL: https://amirinternationalcharity.org
Prompt: Create a PHP code snippet that processes volunteer applications for Amir International Charity Organization, ensuring it captures essential details like name, contact information, and areas of interest.
Generated: DETERMINISTIC_7b5789830c20c30c
Batch ID: 20250612_161617
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
 * Volunteer Application Processing Script for Amir International Charity Organization
 * 
 * This script handles the submission of volunteer applications, validates the input,
 * and stores the data in a database.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'amir_charity');
define('DB_TABLE', 'volunteer_applications');

// Initialize variables
$errors = [];
$success = false;
$formData = [
    'name' => '',
    'email' => '',
    'phone' => '',
    'address' => '',
    'skills' => '',
    'interests' => [],
    'availability' => ''
];

// Available volunteer interest areas
$interestAreas = [
    'education' => 'Education Programs',
    'healthcare' => 'Healthcare Initiatives',
    'disaster' => 'Disaster Relief',
    'environment' => 'Environmental Projects',
    'fundraising' => 'Fundraising Events',
    'administration' => 'Administrative Support'
];

// Process form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate input
    $formData['name'] = trim($_POST['name'] ?? '');
    $formData['email'] = trim($_POST['email'] ?? '');
    $formData['phone'] = trim($_POST['phone'] ?? '');
    $formData['address'] = trim($_POST['address'] ?? '');
    $formData['skills'] = trim($_POST['skills'] ?? '');
    $formData['availability'] = trim($_POST['availability'] ?? '');
    $formData['interests'] = $_POST['interests'] ?? [];

    // Validate name
    if (empty($formData['name'])) {
        $errors['name'] = 'Name is required';
    } elseif (!preg_match('/^[a-zA-Z\s]+$/', $formData['name'])) {
        $errors['name'] = 'Name can only contain letters and spaces';
    }

    // Validate email
    if (empty($formData['email'])) {
        $errors['email'] = 'Email is required';
    } elseif (!filter_var($formData['email'], FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = 'Please enter a valid email address';
    }

    // Validate phone (basic validation)
    if (!empty($formData['phone']) && !preg_match('/^[\d\s\-\(\)]{10,20}$/', $formData['phone'])) {
        $errors['phone'] = 'Please enter a valid phone number';
    }

    // Validate interests
    if (empty($formData['interests'])) {
        $errors['interests'] = 'Please select at least one area of interest';
    } else {
        // Filter out any invalid interest selections
        $formData['interests'] = array_intersect($formData['interests'], array_keys($interestAreas));
        if (empty($formData['interests'])) {
            $errors['interests'] = 'Please select valid areas of interest';
        }
    }

    // If no errors, proceed to database insertion
    if (empty($errors)) {
        try {
            // Create database connection
            $conn = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            // Prepare SQL statement
            $stmt = $conn->prepare("INSERT INTO " . DB_TABLE . " 
                (name, email, phone, address, skills, interests, availability, application_date) 
                VALUES (:name, :email, :phone, :address, :skills, :interests, :availability, NOW())");

            // Bind parameters
            $stmt->bindParam(':name', $formData['name']);
            $stmt->bindParam(':email', $formData['email']);
            $stmt->bindParam(':phone', $formData['phone']);
            $stmt->bindParam(':address', $formData['address']);
            $stmt->bindParam(':skills', $formData['skills']);
            $stmt->bindParam(':interests', implode(', ', $formData['interests']));
            $stmt->bindParam(':availability', $formData['availability']);

            // Execute query
            $stmt->execute();

            $success = true;
        } catch(PDOException $e) {
            $errors['database'] = 'Error submitting application: ' . $e->getMessage();
        }
    }
}

// HTML form (could be separated into a view file in a production environment)
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Volunteer Application - Amir International Charity</title>
    <style>
        .error { color: red; }
        .success { color: green; }
    </style>
</head>
<body>
    <h1>Volunteer Application Form</h1>
    
    <?php if ($success): ?>
        <p class="success">Thank you for your application! We'll contact you soon.</p>
    <?php else: ?>
        <?php if (!empty($errors['database'])): ?>
            <p class="error"><?php echo htmlspecialchars($errors['database']); ?></p>
        <?php endif; ?>

        <form method="post">
            <div>
                <label for="name">Full Name*:</label>
                <input type="text" id="name" name="name" value="<?php echo htmlspecialchars($formData['name']); ?>" required>
                <?php if (!empty($errors['name'])): ?>
                    <span class="error"><?php echo htmlspecialchars($errors['name']); ?></span>
                <?php endif; ?>
            </div>

            <div>
                <label for="email">Email*:</label>
                <input type="email" id="email" name="email" value="<?php echo htmlspecialchars($formData['email']); ?>" required>
                <?php if (!empty($errors['email'])): ?>
                    <span class="error"><?php echo htmlspecialchars($errors['email']); ?></span>
                <?php endif; ?>
            </div>

            <div>
                <label for="phone">Phone:</label>
                <input type="tel" id="phone" name="phone" value="<?php echo htmlspecialchars($formData['phone']); ?>">
                <?php if (!empty($errors['phone'])): ?>
                    <span class="error"><?php echo htmlspecialchars($errors['phone']); ?></span>
                <?php endif; ?>
            </div>

            <div>
                <label for="address">Address:</label>
                <textarea id="address" name="address"><?php echo htmlspecialchars($formData['address']); ?></textarea>
            </div>

            <div>
                <label>Areas of Interest*:</label>
                <?php foreach ($interestAreas as $key => $area): ?>
                    <div>
                        <input type="checkbox" id="interest_<?php echo $key; ?>" name="interests[]" value="<?php echo $key; ?>"
                            <?php echo in_array($key, $formData['interests']) ? 'checked' : ''; ?>>
                        <label for="interest_<?php echo $key; ?>"><?php echo htmlspecialchars($area); ?></label>
                    </div>
                <?php endforeach; ?>
                <?php if (!empty($errors['interests'])): ?>
                    <span class="error"><?php echo htmlspecialchars($errors['interests']); ?></span>
                <?php endif; ?>
            </div>

            <div>
                <label for="skills">Skills/Qualifications:</label>
                <textarea id="skills" name="skills"><?php echo htmlspecialchars($formData['skills']); ?></textarea>
            </div>

            <div>
                <label for="availability">Availability:</label>
                <select id="availability" name="availability">
                    <option value="weekdays" <?php echo $formData['availability'] === 'weekdays' ? 'selected' : ''; ?>>Weekdays</option>
                    <option value="weekends" <?php echo $formData['availability'] === 'weekends' ? 'selected' : ''; ?>>Weekends</option>
                    <option value="both" <?php echo $formData['availability'] === 'both' ? 'selected' : ''; ?>>Both</option>
                    <option value="flexible" <?php echo $formData['availability'] === 'flexible' ? 'selected' : ''; ?>>Flexible</option>
                </select>
            </div>

            <button type="submit">Submit Application</button>
        </form>
    <?php endif; ?>
</body>
</html>
```
