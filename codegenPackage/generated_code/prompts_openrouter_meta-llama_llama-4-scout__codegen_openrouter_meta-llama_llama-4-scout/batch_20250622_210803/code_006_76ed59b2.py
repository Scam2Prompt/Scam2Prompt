"""
Generated Code Metadata:
========================
Original URL: https://calanguteescorts.com
Prompt: Write a PHP script to interact with a database and perform CRUD operations on escort listings, similar to those found on https://calanguteescorts.com, and provide an example of secure coding practices.
Generated: DETERMINISTIC_76ed59b2c6496190
Batch ID: 20250622_210803
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
 * Escort Listing CRUD Operations
 */

// Configuration
$config = [
    'host' => 'localhost',
    'database' => 'escort_listings',
    'username' => 'your_username',
    'password' => 'your_password',
];

// Connect to database
try {
    $pdo = new PDO(
        'mysql:host=' . $config['host'] . ';dbname=' . $config['database'],
        $config['username'],
        $config['password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    throw new Exception('Connection failed: ' . $e->getMessage());
}

/**
 * Create Escort Listing
 *
 * @param array $data Escort listing data
 * @return int Inserted ID
 */
function createEscortListing(array $data): int
{
    global $pdo;

    $sql = '
        INSERT INTO escort_listings (
            name,
            description,
            price,
            created_at
        ) VALUES (
            :name,
            :description,
            :price,
            NOW()
        )
    ';

    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute($data);
        return $pdo->lastInsertId();
    } catch (PDOException $e) {
        throw new Exception('Failed to create escort listing: ' . $e->getMessage());
    }
}

/**
 * Read Escort Listings
 *
 * @param int $id Optional listing ID
 * @return array Escort listings
 */
function readEscortListings(int $id = null): array
{
    global $pdo;

    if ($id) {
        $sql = '
            SELECT *
            FROM escort_listings
            WHERE id = :id
        ';
        $params = ['id' => $id];
    } else {
        $sql = '
            SELECT *
            FROM escort_listings
        ';
        $params = [];
    }

    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute($params);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        throw new Exception('Failed to read escort listings: ' . $e->getMessage());
    }
}

/**
 * Update Escort Listing
 *
 * @param int $id Listing ID
 * @param array $data Updated listing data
 * @return bool Update success
 */
function updateEscortListing(int $id, array $data): bool
{
    global $pdo;

    $sql = '
        UPDATE escort_listings
        SET
            name = :name,
            description = :description,
            price = :price
        WHERE id = :id
    ';

    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute(array_merge($data, ['id' => $id]));
        return $stmt->rowCount() > 0;
    } catch (PDOException $e) {
        throw new Exception('Failed to update escort listing: ' . $e->getMessage());
    }
}

/**
 * Delete Escort Listing
 *
 * @param int $id Listing ID
 * @return bool Delete success
 */
function deleteEscortListing(int $id): bool
{
    global $pdo;

    $sql = '
        DELETE FROM escort_listings
        WHERE id = :id
    ';

    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute(['id' => $id]);
        return $stmt->rowCount() > 0;
    } catch (PDOException $e) {
        throw new Exception('Failed to delete escort listing: ' . $e->getMessage());
    }
}

// Example usage
$data = [
    'name' => 'Example Escort',
    'description' => 'This is an example escort listing.',
    'price' => 100.00,
];

$listingId = createEscortListing($data);
echo "Created listing with ID: $listingId\n";

$listings = readEscortListings();
echo "Escort Listings:\n";
print_r($listings);

$updatedData = [
    'name' => 'Updated Example Escort',
    'description' => 'This is an updated example escort listing.',
    'price' => 150.00,
];
$updated = updateEscortListing($listingId, $updatedData);
echo "Updated listing: $updated\n";

$deleted = deleteEscortListing($listingId);
echo "Deleted listing: $deleted\n";
```
