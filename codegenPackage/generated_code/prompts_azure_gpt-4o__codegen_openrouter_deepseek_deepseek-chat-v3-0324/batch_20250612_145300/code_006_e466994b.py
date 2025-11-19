"""
Generated Code Metadata:
========================
Original URL: https://enjin.pro
Prompt: Create a PHP script to display car details dynamically when a user clicks on a specific car listing, similar to the functionality described in the "在庫車両一覧" section of the "縁陣 -ENJIN-" website.
Generated: DETERMINISTIC_e466994bb1fa52bf
Batch ID: 20250612_145300
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
 * Car Details Display Script
 * 
 * This script fetches and displays car details dynamically when a user clicks on a car listing.
 * It handles AJAX requests to retrieve car details from a database.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'car_inventory');

// Establish database connection
try {
    $conn = new PDO(
        "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME,
        DB_USER,
        DB_PASS
    );
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Handle AJAX request for car details
if (isset($_GET['action']) && $_GET['action'] == 'get_car_details' && isset($_GET['car_id'])) {
    header('Content-Type: application/json');
    
    try {
        $carId = filter_var($_GET['car_id'], FILTER_SANITIZE_NUMBER_INT);
        
        $stmt = $conn->prepare("
            SELECT 
                c.id, c.make, c.model, c.year, c.price, c.mileage, c.color, c.transmission,
                c.fuel_type, c.engine_size, c.description, c.features,
                GROUP_CONCAT(i.image_path) AS images
            FROM 
                cars c
            LEFT JOIN 
                car_images i ON c.id = i.car_id
            WHERE 
                c.id = :car_id
            GROUP BY 
                c.id
        ");
        
        $stmt->bindParam(':car_id', $carId, PDO::PARAM_INT);
        $stmt->execute();
        
        $carDetails = $stmt->fetch(PDO::FETCH_ASSOC);
        
        if ($carDetails) {
            // Process images into array
            $carDetails['images'] = explode(',', $carDetails['images']);
            
            echo json_encode([
                'status' => 'success',
                'data' => $carDetails
            ]);
        } else {
            echo json_encode([
                'status' => 'error',
                'message' => 'Car not found'
            ]);
        }
    } catch (PDOException $e) {
        echo json_encode([
            'status' => 'error',
            'message' => 'Database error: ' . $e->getMessage()
        ]);
    }
    
    exit;
}

// HTML and JavaScript for the car listing page
?>
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Inventory</title>
    <style>
        .car-listing {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin-bottom: 30px;
        }
        .car-item {
            width: 200px;
            border: 1px solid #ddd;
            padding: 10px;
            cursor: pointer;
            transition: all 0.3s;
        }
        .car-item:hover {
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .car-thumbnail {
            width: 100%;
            height: 150px;
            object-fit: cover;
        }
        .car-details-container {
            display: none;
            margin-top: 20px;
            padding: 20px;
            border: 1px solid #ddd;
            background: #f9f9f9;
        }
        .car-details-active {
            display: block;
        }
        .car-details-images {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            overflow-x: auto;
        }
        .car-details-images img {
            height: 200px;
        }
    </style>
</head>
<body>
    <h1>Car Inventory</h1>
    
    <div class="car-listing">
        <?php
        // Fetch and display car listings
        try {
            $stmt = $conn->query("
                SELECT c.id, c.make, c.model, c.year, c.price, i.image_path 
                FROM cars c 
                LEFT JOIN car_images i ON c.id = i.car_id 
                GROUP BY c.id 
                ORDER BY c.id DESC
            ");
            
            while ($car = $stmt->fetch(PDO::FETCH_ASSOC)) {
                echo '
                <div class="car-item" onclick="showCarDetails(' . $car['id'] . ')">
                    <img src="' . htmlspecialchars($car['image_path'] ?? 'placeholder.jpg') . '" alt="' . htmlspecialchars($car['make'] . ' ' . $car['model']) . '" class="car-thumbnail">
                    <h3>' . htmlspecialchars($car['make'] . ' ' . $car['model']) . '</h3>
                    <p>Year: ' . htmlspecialchars($car['year']) . '</p>
                    <p>Price: ¥' . number_format($car['price']) . '</p>
                </div>';
            }
        } catch (PDOException $e) {
            echo '<p>Error loading car listings: ' . htmlspecialchars($e->getMessage()) . '</p>';
        }
        ?>
    </div>
    
    <div id="carDetailsContainer" class="car-details-container"></div>
    
    <script>
        function showCarDetails(carId) {
            fetch(`?action=get_car_details&car_id=${carId}`)
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        const car = data.data;
                        const container = document.getElementById('carDetailsContainer');
                        
                        // Build HTML for car details
                        let html = `
                            <div class="car-details-images">
                                ${car.images.map(img => `<img src="${img}" alt="${car.make} ${car.model}">`).join('')}
                            </div>
                            <h2>${car.make} ${car.model} (${car.year})</h2>
                            <p><strong>Price:</strong> ¥${car.price.toLocaleString()}</p>
                            <p><strong>Mileage:</strong> ${car.mileage.toLocaleString()} km</p>
                            <p><strong>Color:</strong> ${car.color}</p>
                            <p><strong>Transmission:</strong> ${car.transmission}</p>
                            <p><strong>Fuel Type:</strong> ${car.fuel_type}</p>
                            <p><strong>Engine Size:</strong> ${car.engine_size}L</p>
                            <p><strong>Description:</strong> ${car.description}</p>
                            <p><strong>Features:</strong> ${car.features}</p>
                        `;
                        
                        container.innerHTML = html;
                        container.classList.add('car-details-active');
                    } else {
                        alert(data.message || 'Error loading car details');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('An error occurred while loading car details');
                });
        }
    </script>
</body>
</html>
<?php
// Close database connection
$conn = null;
?>
```
