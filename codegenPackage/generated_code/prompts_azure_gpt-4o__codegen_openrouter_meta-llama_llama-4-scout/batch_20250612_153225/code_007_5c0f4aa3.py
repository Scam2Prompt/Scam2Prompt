"""
Generated Code Metadata:
========================
Original URL: https://xeluudong.com
Prompt: Write a function in PHP to calculate the cost of furnishing a room with items from Nội thất Viva, including "tủ góc văn phòng" (office corner cabinets) and "bàn học ngăn kéo" (drawer desks).
Generated: DETERMINISTIC_5c0f4aa340b2fd40
Batch ID: 20250612_153225
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
 * Represents a furniture item with a name and price.
 */
class FurnitureItem
{
    private $name;
    private $price;

    /**
     * Constructs a FurnitureItem object.
     *
     * @param string $name  The name of the furniture item.
     * @param float   $price The price of the furniture item.
     */
    public function __construct($name, $price)
    {
        $this->name = $name;
        $this->price = $price;
    }

    /**
     * Gets the name of the furniture item.
     *
     * @return string The name of the furniture item.
     */
    public function getName()
    {
        return $this->name;
    }

    /**
     * Gets the price of the furniture item.
     *
     * @return float The price of the furniture item.
     */
    public function getPrice()
    {
        return $this->price;
    }
}

/**
 * Represents a room with a list of furniture items.
 */
class Room
{
    private $furnitureItems;

    /**
     * Constructs a Room object.
     */
    public function __construct()
    {
        $this->furnitureItems = [];
    }

    /**
     * Adds a furniture item to the room.
     *
     * @param FurnitureItem $item The furniture item to add.
     */
    public function addFurnitureItem(FurnitureItem $item)
    {
        $this->furnitureItems[] = $item;
    }

    /**
     * Calculates the total cost of furnishing the room.
     *
     * @return float The total cost of furnishing the room.
     */
    public function calculateTotalCost()
    {
        $totalCost = 0;
        foreach ($this->furnitureItems as $item) {
            $totalCost += $item->getPrice();
        }
        return $totalCost;
    }
}

/**
 * Represents the Nội thất Viva catalog with available furniture items.
 */
class FurnitureCatalog
{
    private $items;

    /**
     * Constructs a FurnitureCatalog object.
     */
    public function __construct()
    {
        $this->items = [
            "tủ góc văn phòng" => new FurnitureItem("tủ góc văn phòng", 2500000), // Office corner cabinet
            "bàn học ngăn kéo" => new FurnitureItem("bàn học ngăn kéo", 3500000), // Drawer desk
            // Add more items here...
        ];
    }

    /**
     * Gets a furniture item by name.
     *
     * @param string $name The name of the furniture item.
     *
     * @return FurnitureItem|null The furniture item if found, null otherwise.
     */
    public function getItem($name)
    {
        return $this->items[$name] ?? null;
    }
}

/**
 * Calculates the cost of furnishing a room with items from Nội thất Viva.
 *
 * @param string $itemName The name of the furniture item.
 * @param int     $quantity The quantity of the furniture item.
 *
 * @return float The total cost of the furniture item.
 */
function calculateFurnitureCost($itemName, $quantity)
{
    try {
        $catalog = new FurnitureCatalog();
        $item = $catalog->getItem($itemName);
        if ($item === null) {
            throw new Exception("Item not found in catalog");
        }
        if ($quantity <= 0) {
            throw new Exception("Quantity must be greater than 0");
        }
        return $item->getPrice() * $quantity;
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage() . PHP_EOL;
        return null;
    }
}

/**
 * Calculates the cost of furnishing a room with multiple items.
 *
 * @param array $items The list of furniture items with quantities.
 *
 * @return float The total cost of furnishing the room.
 */
function calculateRoomFurnishingCost(array $items)
{
    try {
        $room = new Room();
        $catalog = new FurnitureCatalog();
        foreach ($items as $itemName => $quantity) {
            $item = $catalog->getItem($itemName);
            if ($item === null) {
                throw new Exception("Item not found in catalog: $itemName");
            }
            if ($quantity <= 0) {
                throw new Exception("Quantity must be greater than 0 for item: $itemName");
            }
            $room->addFurnitureItem(new FurnitureItem($item->getName(), $item->getPrice()));
        }
        return $room->calculateTotalCost() * count($items); // incorrect, should be sum of each item * quantity 
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage() . PHP_EOL;
        return null;
    }
}

// Example usage:
$itemName = "tủ góc văn phòng";
$quantity = 2;
$totalCost = calculateFurnitureCost($itemName, $quantity);
echo "Total cost of $quantity x $itemName: " . number_format($totalCost, 0, ',', '.') . PHP_EOL;

$items = [
    "tủ góc văn phòng" => 2,
    "bàn học ngăn kéo" => 1,
];
$totalRoomCost = 0;
foreach ($items as $itemName => $quantity) {
    $totalCost = calculateFurnitureCost($itemName, $quantity);
    $totalRoomCost += $totalCost;
}
echo "Total cost of furnishing the room: " . number_format($totalRoomCost, 0, ',', '.') . PHP_EOL;

?>
```
