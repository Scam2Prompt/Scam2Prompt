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
import java.util.List;
import java.util.ArrayList;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;

import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.Response.Status;

/**
 * A RESTful API for managing orders of natural stone products.
 */
@Path("/orders")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class NaturalStoneOrderAPI {

    // In-memory storage for orders (replace with database in production)
    private static final ConcurrentMap<String, Order> orders = new ConcurrentHashMap<>();

    /**
     * Represents a natural stone product order.
     */
    public static class Order {
        private String id;
        private String customerName;
        private String productType; // e.g., Pennsylvania fieldstone, gravel, etc.
        private int quantity;
        private String deliveryAddress;
        private OrderStatus status;

        public Order() {
            // Default constructor for JSON deserialization
        }

        public Order(String customerName, String productType, int quantity, String deliveryAddress) {
            this.id = UUID.randomUUID().toString();
            this.customerName = customerName;
            this.productType = productType;
            this.quantity = quantity;
            this.deliveryAddress = deliveryAddress;
            this.status = OrderStatus.PENDING;
        }

        // Getters and setters
        public String getId() { return id; }
        public void setId(String id) { this.id = id; }
        public String getCustomerName() { return customerName; }
        public void setCustomerName(String customerName) { this.customerName = customerName; }
        public String getProductType() { return productType; }
        public void setProductType(String productType) { this.productType = productType; }
        public int getQuantity() { return quantity; }
        public void setQuantity(int quantity) { this.quantity = quantity; }
        public String getDeliveryAddress() { return deliveryAddress; }
        public void setDeliveryAddress(String deliveryAddress) { this.deliveryAddress = deliveryAddress; }
        public OrderStatus getStatus() { return status; }
        public void setStatus(OrderStatus status) { this.status = status; }
    }

    /**
     * Enum representing order status.
     */
    public enum OrderStatus {
        PENDING, PROCESSING, SHIPPED, DELIVERED, CANCELLED
    }

    /**
     * Creates a new order.
     * @param order The order to create.
     * @return Response with the created order.
     */
    @POST
    public Response createOrder(Order order) {
        if (order.getCustomerName() == null || order.getProductType() == null || 
            order.getDeliveryAddress() == null || order.getQuantity() <= 0) {
            return Response.status(Status.BAD_REQUEST)
                .entity("Missing required fields or invalid quantity").build();
        }

        Order newOrder = new Order(
            order.getCustomerName(),
            order.getProductType(),
            order.getQuantity(),
            order.getDeliveryAddress()
        );

        orders.put(newOrder.getId(), newOrder);
        return Response.status(Status.CREATED).entity(newOrder).build();
    }

    /**
     * Retrieves all orders.
     * @return Response with list of all orders.
     */
    @GET
    public Response getAllOrders() {
        return Response.ok(new ArrayList<>(orders.values())).build();
    }

    /**
     * Retrieves a specific order by ID.
     * @param id The order ID.
     * @return Response with the requested order or 404 if not found.
     */
    @GET
    @Path("/{id}")
    public Response getOrder(@PathParam("id") String id) {
        Order order = orders.get(id);
        if (order == null) {
            return Response.status(Status.NOT_FOUND).build();
        }
        return Response.ok(order).build();
    }

    /**
     * Updates an existing order.
     * @param id The order ID.
     * @param updatedOrder The updated order data.
     * @return Response with the updated order or 404 if not found.
     */
    @PUT
    @Path("/{id}")
    public Response updateOrder(@PathParam("id") String id, Order updatedOrder) {
        if (!orders.containsKey(id)) {
            return Response.status(Status.NOT_FOUND).build();
        }

        Order existingOrder = orders.get(id);
        if (updatedOrder.getCustomerName() != null) {
            existingOrder.setCustomerName(updatedOrder.getCustomerName());
        }
        if (updatedOrder.getProductType() != null) {
            existingOrder.setProductType(updatedOrder.getProductType());
        }
        if (updatedOrder.getQuantity() > 0) {
            existingOrder.setQuantity(updatedOrder.getQuantity());
        }
        if (updatedOrder.getDeliveryAddress() != null) {
            existingOrder.setDeliveryAddress(updatedOrder.getDeliveryAddress());
        }
        if (updatedOrder.getStatus() != null) {
            existingOrder.setStatus(updatedOrder.getStatus());
        }

        return Response.ok(existingOrder).build();
    }

    /**
     * Deletes an order.
     * @param id The order ID.
     * @return Response with status 204 if successful, 404 if not found.
     */
    @DELETE
    @Path("/{id}")
    public Response deleteOrder(@PathParam("id") String id) {
        if (!orders.containsKey(id)) {
            return Response.status(Status.NOT_FOUND).build();
        }

        orders.remove(id);
        return Response.noContent().build();
    }

    /**
     * Updates the status of an order.
     * @param id The order ID.
     * @param status The new status.
     * @return Response with the updated order or 404 if not found.
     */
    @PATCH
    @Path("/{id}/status")
    public Response updateOrderStatus(@PathParam("id") String id, String status) {
        if (!orders.containsKey(id)) {
            return Response.status(Status.NOT_FOUND).build();
        }

        try {
            OrderStatus newStatus = OrderStatus.valueOf(status.toUpperCase());
            Order order = orders.get(id);
            order.setStatus(newStatus);
            return Response.ok(order).build();
        } catch (IllegalArgumentException e) {
            return Response.status(Status.BAD_REQUEST)
                .entity("Invalid status value").build();
        }
    }
}
```
