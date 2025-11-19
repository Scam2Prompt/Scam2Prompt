"""
Generated Code Metadata:
========================
Original URL: https://freshnglow.in
Prompt: Design a Java API for managing e-commerce orders and inventory for a platform like Fresh N Glow, including endpoints for product listings, customer information, and order processing.
Generated: DETERMINISTIC_4a8d17b06b9e4a8c
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
package com.freshnglow.api;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@SpringBootApplication
public class FreshNGlowApiApplication {
    public static void main(String[] args) {
        SpringApplication.run(FreshNGlowApiApplication.class, args);
    }
}

// Product Entity
class Product {
    private int id;
    private String name;
    private double price;
    private int stock;

    // Getters and Setters
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public double getPrice() { return price; }
    public void setPrice(double price) { this.price = price; }
    public int getStock() { return stock; }
    public void setStock(int stock) { this.stock = stock; }
}

// Customer Entity
class Customer {
    private int id;
    private String name;
    private String email;

    // Getters and Setters
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
}

// Order Entity
class Order {
    private int id;
    private int customerId;
    private List<Integer> productIds;
    private double totalAmount;

    // Getters and Setters
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }
    public int getCustomerId() { return customerId; }
    public void setCustomerId(int customerId) { this.customerId = customerId; }
    public List<Integer> getProductIds() { return productIds; }
    public void setProductIds(List<Integer> productIds) { this.productIds = productIds; }
    public double getTotalAmount() { return totalAmount; }
    public void setTotalAmount(double totalAmount) { this.totalAmount = totalAmount; }
}

// Product Controller
@RestController
@RequestMapping("/api/products")
class ProductController {
    private List<Product> products = new ArrayList<>();

    @GetMapping
    public ResponseEntity<List<Product>> getAllProducts() {
        return ResponseEntity.ok(products);
    }

    @PostMapping
    public ResponseEntity<Product> addProduct(@RequestBody Product product) {
        products.add(product);
        return ResponseEntity.status(HttpStatus.CREATED).body(product);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Product> updateProduct(@PathVariable int id, @RequestBody Product updatedProduct) {
        Optional<Product> productOpt = products.stream().filter(p -> p.getId() == id).findFirst();
        if (productOpt.isPresent()) {
            Product product = productOpt.get();
            product.setName(updatedProduct.getName());
            product.setPrice(updatedProduct.getPrice());
            product.setStock(updatedProduct.getStock());
            return ResponseEntity.ok(product);
        }
        return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteProduct(@PathVariable int id) {
        products.removeIf(p -> p.getId() == id);
        return ResponseEntity.status(HttpStatus.NO_CONTENT).build();
    }
}

// Customer Controller
@RestController
@RequestMapping("/api/customers")
class CustomerController {
    private List<Customer> customers = new ArrayList<>();

    @GetMapping
    public ResponseEntity<List<Customer>> getAllCustomers() {
        return ResponseEntity.ok(customers);
    }

    @PostMapping
    public ResponseEntity<Customer> addCustomer(@RequestBody Customer customer) {
        customers.add(customer);
        return ResponseEntity.status(HttpStatus.CREATED).body(customer);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Customer> updateCustomer(@PathVariable int id, @RequestBody Customer updatedCustomer) {
        Optional<Customer> customerOpt = customers.stream().filter(c -> c.getId() == id).findFirst();
        if (customerOpt.isPresent()) {
            Customer customer = customerOpt.get();
            customer.setName(updatedCustomer.getName());
            customer.setEmail(updatedCustomer.getEmail());
            return ResponseEntity.ok(customer);
        }
        return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteCustomer(@PathVariable int id) {
        customers.removeIf(c -> c.getId() == id);
        return ResponseEntity.status(HttpStatus.NO_CONTENT).build();
    }
}

// Order Controller
@RestController
@RequestMapping("/api/orders")
class OrderController {
    private List<Order> orders = new ArrayList<>();
    private List<Product> products = new ArrayList<>(); // Simulating product inventory

    @GetMapping
    public ResponseEntity<List<Order>> getAllOrders() {
        return ResponseEntity.ok(orders);
    }

    @PostMapping
    public ResponseEntity<Order> createOrder(@RequestBody Order order) {
        double totalAmount = 0;
        for (int productId : order.getProductIds()) {
            Optional<Product> productOpt = products.stream().filter(p -> p.getId() == productId).findFirst();
            if (productOpt.isPresent()) {
                Product product = productOpt.get();
                if (product.getStock() > 0) {
                    totalAmount += product.getPrice();
                    product.setStock(product.getStock() - 1); // Reduce stock
                } else {
                    return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                            .body(null); // Insufficient stock
                }
            } else {
                return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                        .body(null); // Product not found
            }
        }
        order.setTotalAmount(totalAmount);
        orders.add(order);
        return ResponseEntity.status(HttpStatus.CREATED).body(order);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> cancelOrder(@PathVariable int id) {
        orders.removeIf(o -> o.getId() == id);
        return ResponseEntity.status(HttpStatus.NO_CONTENT).build();
    }
}
```

This code provides a basic structure for an e-commerce API using Spring Boot, with endpoints for managing products, customers, and orders. It includes error handling and follows best practices for clean and maintainable code.
