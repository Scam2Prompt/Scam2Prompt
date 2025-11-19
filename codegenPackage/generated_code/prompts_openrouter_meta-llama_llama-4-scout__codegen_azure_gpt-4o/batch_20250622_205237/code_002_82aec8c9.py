"""
Generated Code Metadata:
========================
Original URL: https://pooledeth.us
Prompt: Generate Java code for creating a simple Taobao-like shopping cart system.
Generated: DETERMINISTIC_82aec8c9a690d9f5
Batch ID: 20250622_205237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// Class representing a product in the shopping cart
class Product {
    private int id;
    private String name;
    private double price;

    // Constructor
    public Product(int id, String name, double price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }

    // Getters
    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    @Override
    public String toString() {
        return "Product ID: " + id + ", Name: " + name + ", Price: $" + price;
    }
}

// Class representing the shopping cart
class ShoppingCart {
    private List<Product> cartItems;

    // Constructor
    public ShoppingCart() {
        this.cartItems = new ArrayList<>();
    }

    // Add a product to the cart
    public void addProduct(Product product) {
        cartItems.add(product);
        System.out.println(product.getName() + " has been added to the cart.");
    }

    // Remove a product from the cart by ID
    public void removeProduct(int productId) {
        boolean removed = cartItems.removeIf(product -> product.getId() == productId);
        if (removed) {
            System.out.println("Product with ID " + productId + " has been removed from the cart.");
        } else {
            System.out.println("Product with ID " + productId + " not found in the cart.");
        }
    }

    // Display all items in the cart
    public void displayCart() {
        if (cartItems.isEmpty()) {
            System.out.println("Your cart is empty.");
        } else {
            System.out.println("Items in your cart:");
            for (Product product : cartItems) {
                System.out.println(product);
            }
        }
    }

    // Calculate the total price of items in the cart
    public double calculateTotal() {
        double total = 0;
        for (Product product : cartItems) {
            total += product.getPrice();
        }
        return total;
    }
}

// Main class to run the shopping cart system
public class ShoppingCartSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ShoppingCart cart = new ShoppingCart();

        // Sample products
        Product product1 = new Product(1, "Laptop", 999.99);
        Product product2 = new Product(2, "Smartphone", 499.99);
        Product product3 = new Product(3, "Headphones", 79.99);

        // Menu-driven system
        while (true) {
            System.out.println("\n--- Shopping Cart Menu ---");
            System.out.println("1. Add Product to Cart");
            System.out.println("2. Remove Product from Cart");
            System.out.println("3. View Cart");
            System.out.println("4. Calculate Total");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");

            try {
                int choice = Integer.parseInt(scanner.nextLine());

                switch (choice) {
                    case 1:
                        System.out.println("Available Products:");
                        System.out.println(product1);
                        System.out.println(product2);
                        System.out.println(product3);
                        System.out.print("Enter Product ID to add: ");
                        int addId = Integer.parseInt(scanner.nextLine());
                        if (addId == 1) {
                            cart.addProduct(product1);
                        } else if (addId == 2) {
                            cart.addProduct(product2);
                        } else if (addId == 3) {
                            cart.addProduct(product3);
                        } else {
                            System.out.println("Invalid Product ID.");
                        }
                        break;

                    case 2:
                        System.out.print("Enter Product ID to remove: ");
                        int removeId = Integer.parseInt(scanner.nextLine());
                        cart.removeProduct(removeId);
                        break;

                    case 3:
                        cart.displayCart();
                        break;

                    case 4:
                        System.out.println("Total Price: $" + cart.calculateTotal());
                        break;

                    case 5:
                        System.out.println("Exiting the system. Thank you!");
                        scanner.close();
                        return;

                    default:
                        System.out.println("Invalid choice. Please try again.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number.");
            }
        }
    }
}
```
