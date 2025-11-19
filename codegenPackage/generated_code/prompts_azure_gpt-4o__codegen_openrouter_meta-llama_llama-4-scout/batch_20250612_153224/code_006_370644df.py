"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Write code in PHP to display a list of horse riding tours offered by Chile Horse Riding, with detailed descriptions such as "swim with your horse" and "authentic lifestyle of Chilean Arrieros."
Generated: DETERMINISTIC_370644df5a2d80e5
Batch ID: 20250612_153224
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
 * Chile Horse Riding Tour Class
 */
class ChileHorseRidingTour {
    private $id;
    private $name;
    private $description;
    private $duration;
    private $price;

    /**
     * Constructor
     *
     * @param int    $id          Tour ID
     * @param string $name        Tour Name
     * @param string $description Tour Description
     * @param string $duration    Tour Duration
     * @param float  $price       Tour Price
     */
    public function __construct($id, $name, $description, $duration, $price) {
        $this->id = $id;
        $this->name = $name;
        $this->description = $description;
        $this->duration = $duration;
        $this->price = $price;
    }

    /**
     * Get Tour Details
     *
     * @return array
     */
    public function getTourDetails() {
        return [
            'id'          => $this->id,
            'name'        => $this->name,
            'description' => $this->description,
            'duration'    => $this->duration,
            'price'       => $this->price,
        ];
    }
}

/**
 * Chile Horse Riding Tour Service Class
 */
class ChileHorseRidingTourService {
    private $tours;

    /**
     * Constructor
     */
    public function __construct() {
        $this->tours = [];
    }

    /**
     * Add Tour
     *
     * @param ChileHorseRidingTour $tour Tour Object
     */
    public function addTour(ChileHorseRidingTour $tour) {
        $this->tours[] = $tour;
    }

    /**
     * Get All Tours
     *
     * @return ChileHorseRidingTour[]
     */
    public function getAllTours() {
        return $this->tours;
    }

    /**
     * Display Tours
     */
    public function displayTours() {
        try {
            if (empty($this->tours)) {
                throw new Exception('No tours available');
            }

            foreach ($this->tours as $tour) {
                $tourDetails = $tour->getTourDetails();
                echo "Tour ID: {$tourDetails['id']}\n";
                echo "Tour Name: {$tourDetails['name']}\n";
                echo "Tour Description: {$tourDetails['description']}\n";
                echo "Tour Duration: {$tourDetails['duration']}\n";
                echo "Tour Price: {$tourDetails['price']}\n";
                echo "------------------------\n";
            }
        } catch (Exception $e) {
            echo 'Error: ' . $e->getMessage() . "\n";
        }
    }
}

// Create Tour Service
$tourService = new ChileHorseRidingTourService();

// Create Tours
$tour1 = new ChileHorseRidingTour(1, 'Swim with Your Horse', 'Experience the thrill of swimming with your horse in a serene lake', '3 days', 500.00);
$tour2 = new ChileHorseRidingTour(2, 'Authentic Lifestyle of Chilean Arrieros', 'Immerse yourself in the authentic lifestyle of Chilean Arrieros', '5 days', 800.00);
$tour3 = new ChileHorseRidingTour(3, 'Horse Riding in the Andes', 'Explore the breathtaking Andes mountains on horseback', '7 days', 1200.00);

// Add Tours to Service
$tourService->addTour($tour1);
$tourService->addTour($tour2);
$tourService->addTour($tour3);

// Display Tours
$tourService->displayTours();

?>
```
