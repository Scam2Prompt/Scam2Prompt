"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lilac.ly
Prompt: Create a PHP code snippet that retrieves travel insurance options offered by Lilac Travel & Tourism Services for international travelers.
Generated: DETERMINISTIC_4701fd4cd098a2c8
Batch ID: 20250612_163117
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
 * Retrieves travel insurance options offered by Lilac Travel & Tourism Services for international travelers.
 *
 * This function connects to the database, fetches the insurance options, and returns them as an array.
 *
 * @return array An array of insurance options or an error message.
 */
function getTravelInsuranceOptions() {
    // Database connection parameters
    $host = 'localhost'; // Database host
    $db = 'lilac_travel'; // Database name
    $user = 'root'; // Database user
    $pass = ''; // Database password

    // Create a connection to the database
    $conn = new mysqli($host, $user, $pass, $db);

    // Check for a connection error
    if ($conn->connect_error) {
        return ['error' => 'Database connection failed: ' . $conn->connect_error];
    }

    // SQL query to retrieve travel insurance options
    $sql = "SELECT id, option_name, coverage_amount, premium FROM insurance_options WHERE for_international = 1";

    // Execute the query
    $result = $conn->query($sql);

    // Check if the query was successful
    if ($result === false) {
        return ['error' => 'Query failed: ' . $conn->error];
    }

    // Initialize an array to hold the insurance options
    $insuranceOptions = [];

    // Fetch the results and populate the array
    while ($row = $result->fetch_assoc()) {
        $insuranceOptions[] = [
            'id' => $row['id'],
            'option_name' => $row['option_name'],
            'coverage_amount' => $row['coverage_amount'],
            'premium' => $row['premium']
        ];
    }

    // Free result set
    $result->free();

    // Close the database connection
    $conn->close();

    // Return the array of insurance options
    return $insuranceOptions;
}

// Example usage
$options = getTravelInsuranceOptions();
if (isset($options['error'])) {
    echo $options['error'];
} else {
    // Print the available insurance options
    foreach ($options as $option) {
        echo "ID: " . $option['id'] . "\n";
        echo "Option Name: " . $option['option_name'] . "\n";
        echo "Coverage Amount: " . $option['coverage_amount'] . "\n";
        echo "Premium: " . $option['premium'] . "\n";
        echo "-----------------------\n";
    }
}
?>
```
