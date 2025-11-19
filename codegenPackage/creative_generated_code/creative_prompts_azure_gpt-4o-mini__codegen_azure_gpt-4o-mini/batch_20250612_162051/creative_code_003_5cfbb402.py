"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ezway.com.br
Prompt: Develop a PHP script that integrates with the EZ Way English Center's TOEIC® test preparation resources and provides users with study material recommendations.
Generated: DETERMINISTIC_5cfbb402b5638240
Batch ID: 20250612_162051
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
 * EZ Way English Center TOEIC Test Preparation Recommendations
 * 
 * A simple PHP script that provides study material recommendations for TOEIC test preparation.
 * This script pulls data from a hypothetical database of study materials and returns relevant recommendations
 * based on user input (e.g., user proficiency level).
 */

// Database configuration - adjust to your environment
define('DB_HOST', 'localhost');
define('DB_NAME', 'ez_way_english');
define('DB_USER', 'root');
define('DB_PASS', 'password');

/**
 * Establishes a connection to the database.
 *
 * @return PDO|null Returns a PDO instance or null on failure.
 */
function getDatabaseConnection() {
    try {
        $connection = new PDO("mysql:host=".DB_HOST.";dbname=".DB_NAME, DB_USER, DB_PASS);
        $connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $connection;
    } catch (PDOException $e) {
        error_log("Database connection error: " . $e->getMessage());
        return null;
    }
}

/**
 * Fetches study material recommendations based on user proficiency level.
 *
 * @param string $level The proficiency level of the user (e.g., 'beginner', 'intermediate', 'advanced').
 * @return array|false Returns an array of recommended materials or false on failure.
 */
function getStudyMaterialRecommendations($level) {
    $db = getDatabaseConnection();
    if ($db === null) {
        return false; // Error already logged in getDatabaseConnection
    }

    // Prepare and execute the SQL query
    $query = "SELECT title, description, link FROM study_materials WHERE proficiency_level = :level";
    $stmt = $db->prepare($query);
    $stmt->bindParam(':level', $level, PDO::PARAM_STR);

    try {
        $stmt->execute();
        $materials = $stmt->fetchAll(PDO::FETCH_ASSOC);
        return $materials;
    } catch (PDOException $e) {
        error_log("Query error: " . $e->getMessage());
        return false; // Error logging done
    }
}

// Main execution flow
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Expecting a POST request with 'level' parameter
    $userLevel = isset($_POST['level']) ? trim($_POST['level']) : '';

    if (!empty($userLevel)) {
        $recommendations = getStudyMaterialRecommendations($userLevel);

        if ($recommendations !== false) {
            // Return recommendations as a JSON response
            header('Content-Type: application/json');
            echo json_encode([
                'success' => true,
                'recommendations' => $recommendations
            ]);
        } else {
            // Return error response
            header('Content-Type: application/json', true, 500);
            echo json_encode([
                'success' => false,
                'message' => 'Failed to fetch recommendations.'
            ]);
        }
    } else {
        // Return validation error response
        header('Content-Type: application/json', true, 400);
        echo json_encode([
            'success' => false,
            'message' => 'Invalid proficiency level provided.'
        ]);
    }
} else {
    // Handle requests that are not POST
    header('Content-Type: application/json', true, 405);
    echo json_encode([
        'success' => false,
        'message' => 'Method not allowed. Please use POST.'
    ]);
}
?>
```
