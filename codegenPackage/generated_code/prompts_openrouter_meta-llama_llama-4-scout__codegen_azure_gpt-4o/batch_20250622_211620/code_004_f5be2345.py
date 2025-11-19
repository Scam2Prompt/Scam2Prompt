"""
Generated Code Metadata:
========================
Original URL: https://www.pavainc.com
Prompt: Create a RESTful API library in Java for managing orders of natural stone products, such as Pennsylvania fieldstone, gravel, and decorative natural stone products.
Generated: DETERMINISTIC_f5be234570bf50ca
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
package com.naturalstone.api;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@SpringBootApplication
public class NaturalStoneApiApplication {
    public static void main(String[] args) {
        SpringApplication.run(NaturalStoneApiApplication.class, args);
    }
}

// Order model class
class Order {
    private Long id;
    private String productName;
    private int quantity;
    private double price;

    // Constructors
    public Order() {}

    public Order(Long id, String productName, int quantity, double price) {
        this.id = id;
        this.productName = productName;
        this.quantity = quantity;
        this.price = price;
    }

    // Getters and setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getProductName() {
        return productName;
    }

    public void setProductName(String productName) {
        this.productName = productName;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }
}

// REST Controller for managing orders
@RestController
@RequestMapping("/api/orders")
class OrderController {

    private final List<Order> orders = new ArrayList<>();
    private Long nextId = 1L;

    // Create a new order
    @PostMapping
    public ResponseEntity<Order> createOrder(@RequestBody Order order) {
        try {
            order.setId(nextId++);
            orders.add(order);
            return new ResponseEntity<>(order, HttpStatus.CREATED);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    // Get all orders
    @GetMapping
    public ResponseEntity<List<Order>> getAllOrders() {
        return new ResponseEntity<>(orders, HttpStatus.OK);
    }

    // Get a specific order by ID
    @GetMapping("/{id}")
    public ResponseEntity<Order> getOrderById(@PathVariable Long id) {
        Optional<Order> order = orders.stream().filter(o -> o.getId().equals(id)).findFirst();
        if (order.isPresent()) {
            return new ResponseEntity<>(order.get(), HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }

    // Update an existing order
    @PutMapping("/{id}")
    public ResponseEntity<Order> updateOrder(@PathVariable Long id, @RequestBody Order updatedOrder) {
        Optional<Order> existingOrder = orders.stream().filter(o -> o.getId().equals(id)).findFirst();
        if (existingOrder.isPresent()) {
            Order order = existingOrder.get();
            order.setProductName(updatedOrder.getProductName());
            order.setQuantity(updatedOrder.getQuantity());
            order.setPrice(updatedOrder.getPrice());
            return new ResponseEntity<>(order, HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }

    // Delete an order
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteOrder(@PathVariable Long id) {
        boolean removed = orders.removeIf(order -> order.getId().equals(id));
        if (removed) {
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }
}
```

This code provides a RESTful API for managing orders of natural stone products. It uses Spring Boot and includes endpoints for creating, retrieving, updating, and deleting orders. Each endpoint is properly documented with comments, and error handling is implemented where appropriate.
