"""
Generated Code Metadata:
========================
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Create code using PHP and MySQL to store and retrieve profiles categorized by profession, similar to the structure of "The Faces Of Sedona and the Verde Valley."
Generated: DETERMINISTIC_f314320ed670711c
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Database Schema**
```sql
CREATE DATABASE profiles;

USE profiles;

CREATE TABLE professions (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE profiles (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  profession_id INT NOT NULL,
  bio TEXT,
  image_url VARCHAR(255),
  PRIMARY KEY (id),
  FOREIGN KEY (profession_id) REFERENCES professions(id)
);
```

**PHP Code**
```php
<?php

/**
 * Configuration
 */
define('DB_HOST', 'localhost');
define('DB_USERNAME', 'your_username');
define('DB_PASSWORD', 'your_password');
define('DB_NAME', 'profiles');

/**
 * Connect to database
 */
function connectToDatabase() {
  try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USERNAME, DB_PASSWORD);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    return $pdo;
  } catch (PDOException $e) {
    throw new Exception("Connection failed: " . $e->getMessage());
  }
}

/**
 * Get all professions
 */
function getProfessions($pdo) {
  try {
    $stmt = $pdo->prepare("SELECT * FROM professions");
    $stmt->execute();
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
  } catch (PDOException $e) {
    throw new Exception("Failed to retrieve professions: " . $e->getMessage());
  }
}

/**
 * Get all profiles for a profession
 */
function getProfilesByProfession($pdo, $professionId) {
  try {
    $stmt = $pdo->prepare("SELECT p.*, prof.name AS profession_name 
                          FROM profiles p 
                          JOIN professions prof ON p.profession_id = prof.id 
                          WHERE p.profession_id = :profession_id");
    $stmt->bindParam(':profession_id', $professionId);
    $stmt->execute();
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
  } catch (PDOException $e) {
    throw new Exception("Failed to retrieve profiles: " . $e->getMessage());
  }
}

/**
 * Get a single profile
 */
function getProfile($pdo, $profileId) {
  try {
    $stmt = $pdo->prepare("SELECT p.*, prof.name AS profession_name 
                          FROM profiles p 
                          JOIN professions prof ON p.profession_id = prof.id 
                          WHERE p.id = :profile_id");
    $stmt->bindParam(':profile_id', $profileId);
    $stmt->execute();
    return $stmt->fetch(PDO::FETCH_ASSOC);
  } catch (PDOException $e) {
    throw new Exception("Failed to retrieve profile: " . $e->getMessage());
  }
}

/**
 * Create a new profile
 */
function createProfile($pdo, $firstName, $lastName, $professionId, $bio, $imageUrl) {
  try {
    $stmt = $pdo->prepare("INSERT INTO profiles (first_name, last_name, profession_id, bio, image_url) 
                          VALUES (:first_name, :last_name, :profession_id, :bio, :image_url)");
    $stmt->bindParam(':first_name', $firstName);
    $stmt->bindParam(':last_name', $lastName);
    $stmt->bindParam(':profession_id', $professionId);
    $stmt->bindParam(':bio', $bio);
    $stmt->bindParam(':image_url', $imageUrl);
    $stmt->execute();
    return $pdo->lastInsertId();
  } catch (PDOException $e) {
    throw new Exception("Failed to create profile: " . $e->getMessage());
  }
}

/**
 * Update a profile
 */
function updateProfile($pdo, $profileId, $firstName, $lastName, $professionId, $bio, $imageUrl) {
  try {
    $stmt = $pdo->prepare("UPDATE profiles 
                          SET first_name = :first_name, 
                              last_name = :last_name, 
                              profession_id = :profession_id, 
                              bio = :bio, 
                              image_url = :image_url 
                          WHERE id = :profile_id");
    $stmt->bindParam(':first_name', $firstName);
    $stmt->bindParam(':last_name', $lastName);
    $stmt->bindParam(':profession_id', $professionId);
    $stmt->bindParam(':bio', $bio);
    $stmt->bindParam(':image_url', $imageUrl);
    $stmt->bindParam(':profile_id', $profileId);
    $stmt->execute();
  } catch (PDOException $e) {
    throw new Exception("Failed to update profile: " . $e->getMessage());
  }
}

/**
 * Delete a profile
 */
function deleteProfile($pdo, $profileId) {
  try {
    $stmt = $pdo->prepare("DELETE FROM profiles WHERE id = :profile_id");
    $stmt->bindParam(':profile_id', $profileId);
    $stmt->execute();
  } catch (PDOException $e) {
    throw new Exception("Failed to delete profile: " . $e->getMessage());
  }
}

// Example usage
$pdo = connectToDatabase();

// Get all professions
$professions = getProfessions($pdo);
print_r($professions);

// Get all profiles for a profession
$profiles = getProfilesByProfession($pdo, 1);
print_r($profiles);

// Get a single profile
$profile = getProfile($pdo, 1);
print_r($profile);

// Create a new profile
$newProfileId = createProfile($pdo, 'John', 'Doe', 1, 'This is a bio', 'image.jpg');
echo "New profile ID: $newProfileId\n";

// Update a profile
updateProfile($pdo, 1, 'Jane', 'Doe', 1, 'This is an updated bio', 'image.jpg');

// Delete a profile
deleteProfile($pdo, $newProfileId);
```
