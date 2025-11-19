"""
Generated Code Metadata:
========================
Original URL: https://sophon-farming.pro
Prompt: How can I implement a farm management system using PHP, similar to what is seen on sophon-farming.pro, focusing on integrating key data like crop rotation and soil health?
Generated: DETERMINISTIC_1c22e37aed6cd940
Batch ID: 20250622_211443
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
 * Farm Management System
 *
 * This system allows for the management of farm data, including crop rotation and soil health.
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'root',
    'db_password' => '',
    'db_name' => 'farm_management',
];

// Database Connection
try {
    $pdo = new PDO(
        'mysql:host=' . $config['db_host'] . ';dbname=' . $config['db_name'],
        $config['db_username'],
        $config['db_password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo 'Connection failed: ' . $e->getMessage();
    exit();
}

/**
 * Crop Class
 */
class Crop
{
    private $id;
    private $name;
    private $rotationPeriod;

    public function __construct($id, $name, $rotationPeriod)
    {
        $this->id = $id;
        $this->name = $name;
        $this->rotationPeriod = $rotationPeriod;
    }

    public function getId()
    {
        return $this->id;
    }

    public function getName()
    {
        return $this->name;
    }

    public function getRotationPeriod()
    {
        return $this->rotationPeriod;
    }
}

/**
 * Soil Class
 */
class Soil
{
    private $id;
    private $health;
    private $cropId;

    public function __construct($id, $health, $cropId)
    {
        $this->id = $id;
        $this->health = $health;
        $this->cropId = $cropId;
    }

    public function getId()
    {
        return $this->id;
    }

    public function getHealth()
    {
        return $this->health;
    }

    public function getCropId()
    {
        return $this->cropId;
    }
}

/**
 * Farm Class
 */
class Farm
{
    private $pdo;

    public function __construct($pdo)
    {
        $this->pdo = $pdo;
    }

    /**
     * Add Crop
     *
     * @param Crop $crop
     */
    public function addCrop(Crop $crop)
    {
        try {
            $stmt = $this->pdo->prepare('INSERT INTO crops (name, rotation_period) VALUES (:name, :rotationPeriod)');
            $stmt->bindParam(':name', $crop->getName());
            $stmt->bindParam(':rotationPeriod', $crop->getRotationPeriod());
            $stmt->execute();
        } catch (PDOException $e) {
            echo 'Error adding crop: ' . $e->getMessage();
        }
    }

    /**
     * Add Soil
     *
     * @param Soil $soil
     */
    public function addSoil(Soil $soil)
    {
        try {
            $stmt = $this->pdo->prepare('INSERT INTO soils (health, crop_id) VALUES (:health, :cropId)');
            $stmt->bindParam(':health', $soil->getHealth());
            $stmt->bindParam(':cropId', $soil->getCropId());
            $stmt->execute();
        } catch (PDOException $e) {
            echo 'Error adding soil: ' . $e->getMessage();
        }
    }

    /**
     * Get Crops
     *
     * @return array
     */
    public function getCrops()
    {
        try {
            $stmt = $this->pdo->prepare('SELECT * FROM crops');
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            echo 'Error getting crops: ' . $e->getMessage();
            return [];
        }
    }

    /**
     * Get Soil
     *
     * @param int $id
     * @return array
     */
    public function getSoil($id)
    {
        try {
            $stmt = $this->pdo->prepare('SELECT * FROM soils WHERE id = :id');
            $stmt->bindParam(':id', $id);
            $stmt->execute();
            return $stmt->fetch(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            echo 'Error getting soil: ' . $e->getMessage();
            return [];
        }
    }
}

// Create Farm
$farm = new Farm($pdo);

// Create Tables
try {
    $pdo->exec('
        CREATE TABLE IF NOT EXISTS crops (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            rotation_period INT NOT NULL
        )
    ');

    $pdo->exec('
        CREATE TABLE IF NOT EXISTS soils (
            id INT AUTO_INCREMENT PRIMARY KEY,
            health DECIMAL(3, 2) NOT NULL,
            crop_id INT NOT NULL,
            FOREIGN KEY (crop_id) REFERENCES crops(id)
        )
    ');
} catch (PDOException $e) {
    echo 'Error creating tables: ' . $e->getMessage();
}

// Example Usage
$crop = new Crop(null, 'Wheat', 3);
$farm->addCrop($crop);

$soil = new Soil(null, 80.00, 1);
$farm->addSoil($soil);

$crops = $farm->getCrops();
print_r($crops);

$soilData = $farm->getSoil(1);
print_r($soilData);

// Close Database Connection
$pdo = null;
```
