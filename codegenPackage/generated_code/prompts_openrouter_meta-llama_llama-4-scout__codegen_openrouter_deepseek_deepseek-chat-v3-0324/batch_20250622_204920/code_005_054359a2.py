"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Develop a Java program to manage bookings and scheduling for armourer services, uniform hire, and prop rentals for a film production company.
Generated: DETERMINISTIC_054359a2514a22d5
Batch ID: 20250622_204920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

/**
 * A program to manage bookings and scheduling for armourer services,
 * uniform hire, and prop rentals for a film production company.
 */
public class ProductionBookingSystem {

    public enum ServiceType {
        ARMOURER,
        UNIFORM_HIRE,
        PROP_RENTAL
    }

    public enum BookingStatus {
        PENDING,
        CONFIRMED,
        CANCELLED,
        COMPLETED
    }

    /**
     * Represents a booking for a production service.
     */
    public static class Booking {
        private final String bookingId;
        private final String clientName;
        private final ServiceType serviceType;
        private final LocalDateTime startDateTime;
        private final LocalDateTime endDateTime;
        private BookingStatus status;
        private final Map<String, Integer> items; // item name to quantity
        private final String notes;

        public Booking(String clientName, ServiceType serviceType, 
                      LocalDateTime startDateTime, LocalDateTime endDateTime,
                      Map<String, Integer> items, String notes) {
            this.bookingId = UUID.randomUUID().toString();
            this.clientName = clientName;
            this.serviceType = serviceType;
            this.startDateTime = startDateTime;
            this.endDateTime = endDateTime;
            this.status = BookingStatus.PENDING;
            this.items = new HashMap<>(items);
            this.notes = notes;
        }

        // Getters
        public String getBookingId() { return bookingId; }
        public String getClientName() { return clientName; }
        public ServiceType getServiceType() { return serviceType; }
        public LocalDateTime getStartDateTime() { return startDateTime; }
        public LocalDateTime getEndDateTime() { return endDateTime; }
        public BookingStatus getStatus() { return status; }
        public Map<String, Integer> getItems() { return new HashMap<>(items); }
        public String getNotes() { return notes; }

        // Setters
        public void setStatus(BookingStatus status) {
            this.status = status;
        }

        @Override
        public String toString() {
            return "Booking{" +
                    "bookingId='" + bookingId + '\'' +
                    ", clientName='" + clientName + '\'' +
                    ", serviceType=" + serviceType +
                    ", startDateTime=" + startDateTime +
                    ", endDateTime=" + endDateTime +
                    ", status=" + status +
                    ", items=" + items +
                    ", notes='" + notes + '\'' +
                    '}';
        }
    }

    /**
     * Manages all bookings and provides scheduling functionality.
     */
    public static class BookingManager {
        private final List<Booking> bookings;
        private final Map<ServiceType, Map<String, Integer>> inventory; // service type to item name to quantity

        public BookingManager() {
            this.bookings = new ArrayList<>();
            this.inventory = new HashMap<>();
            initializeInventory();
        }

        private void initializeInventory() {
            // Initialize with sample inventory
            Map<String, Integer> armourerItems = new HashMap<>();
            armourerItems.put("Sword", 10);
            armourerItems.put("Shield", 8);
            armourerItems.put("Armor Set", 5);

            Map<String, Integer> uniformItems = new HashMap<>();
            uniformItems.put("Medieval Costume", 20);
            uniformItems.put("Military Uniform", 15);
            uniformItems.put("Fantasy Outfit", 12);

            Map<String, Integer> propItems = new HashMap<>();
            propItems.put("Furniture Set", 5);
            propItems.put("Weapon Rack", 3);
            propItems.put("Special Effects Prop", 8);

            inventory.put(ServiceType.ARMOURER, armourerItems);
            inventory.put(ServiceType.UNIFORM_HIRE, uniformItems);
            inventory.put(ServiceType.PROP_RENTAL, propItems);
        }

        /**
         * Creates a new booking if the items are available and there's no schedule conflict.
         */
        public Booking createBooking(String clientName, ServiceType serviceType,
                                   LocalDateTime startDateTime, LocalDateTime endDateTime,
                                   Map<String, Integer> requestedItems, String notes) 
                                   throws BookingException {
            // Validate dates
            if (endDateTime.isBefore(startDateTime)) {
                throw new BookingException("End date must be after start date");
            }

            if (startDateTime.isBefore(LocalDateTime.now())) {
                throw new BookingException("Cannot book in the past");
            }

            // Check item availability
            Map<String, Integer> availableItems = inventory.get(serviceType);
            if (availableItems == null) {
                throw new BookingException("Invalid service type");
            }

            for (Map.Entry<String, Integer> entry : requestedItems.entrySet()) {
                String item = entry.getKey();
                int requestedQty = entry.getValue();
                int availableQty = availableItems.getOrDefault(item, 0);

                if (requestedQty > availableQty) {
                    throw new BookingException("Not enough quantity available for item: " + item);
                }
            }

            // Check for schedule conflicts
            for (Booking existingBooking : bookings) {
                if (existingBooking.getServiceType() == serviceType &&
                    existingBooking.getStatus() != BookingStatus.CANCELLED &&
                    existingBooking.getStatus() != BookingStatus.COMPLETED) {
                    
                    if (startDateTime.isBefore(existingBooking.getEndDateTime()) &&
                        endDateTime.isAfter(existingBooking.getStartDateTime())) {
                        throw new BookingException("Schedule conflict with existing booking: " + 
                                                  existingBooking.getBookingId());
                    }
                }
            }

            // Create the booking
            Booking newBooking = new Booking(clientName, serviceType, startDateTime, 
                                           endDateTime, requestedItems, notes);
            bookings.add(newBooking);
            return newBooking;
        }

        /**
         * Updates the status of a booking.
         */
        public void updateBookingStatus(String bookingId, BookingStatus newStatus) 
                                      throws BookingException {
            Booking booking = findBookingById(bookingId);
            if (booking == null) {
                throw new BookingException("Booking not found");
            }
            booking.setStatus(newStatus);
        }

        /**
         * Returns all bookings for a given date range.
         */
        public List<Booking> getBookings(LocalDate startDate, LocalDate endDate) {
            List<Booking> result = new ArrayList<>();
            for (Booking booking : bookings) {
                LocalDate bookingDate = booking.getStartDateTime().toLocalDate();
                if (!bookingDate.isBefore(startDate) && !bookingDate.isAfter(endDate)) {
                    result.add(booking);
                }
            }
            return result;
        }

        /**
         * Returns all bookings for a specific service type.
         */
        public List<Booking> getBookingsByService(ServiceType serviceType) {
            List<Booking> result = new ArrayList<>();
            for (Booking booking : bookings) {
                if (booking.getServiceType() == serviceType) {
                    result.add(booking);
                }
            }
            return result;
        }

        /**
         * Returns the current inventory for a service type.
         */
        public Map<String, Integer> getInventory(ServiceType serviceType) {
            return new HashMap<>(inventory.getOrDefault(serviceType, new HashMap<>()));
        }

        /**
         * Updates inventory for a service type.
         */
        public void updateInventory(ServiceType serviceType, String itemName, int quantity) {
            Map<String, Integer> serviceInventory = inventory.computeIfAbsent(
                serviceType, k -> new HashMap<>());
            serviceInventory.put(itemName, quantity);
        }

        private Booking findBookingById(String bookingId) {
            for (Booking booking : bookings) {
                if (booking.getBookingId().equals(bookingId)) {
                    return booking;
                }
            }
            return null;
        }
    }

    /**
     * Custom exception for booking-related errors.
     */
    public static class BookingException extends Exception {
        public BookingException(String message) {
            super(message);
        }
    }

    // Example usage
    public static void main(String[] args) {
        try {
            BookingManager manager = new BookingManager();

            // Create a sample booking
            Map<String, Integer> requestedItems = new HashMap<>();
            requestedItems.put("Sword", 2);
            requestedItems.put("Armor Set", 1);

            LocalDateTime start = LocalDateTime.now().plusDays(1);
            LocalDateTime end = start.plusDays(3);

            Booking booking = manager.createBooking(
                "Fantasy Productions", 
                ServiceType.ARMOURER, 
                start, 
                end, 
                requestedItems, 
                "Need for medieval battle scene"
            );

            System.out.println("Created booking: " + booking);

            // Update booking status
            manager.updateBookingStatus(booking.getBookingId(), BookingStatus.CONFIRMED);
            System.out.println("Updated booking status to CONFIRMED");

            // Get bookings for today
            List<Booking> todayBookings = manager.getBookings(
                LocalDate.now(), 
                LocalDate.now()
            );
            System.out.println("Today's bookings: " + todayBookings.size());

        } catch (BookingException e) {
            System.err.println("Booking error: " + e.getMessage());
        }
    }
