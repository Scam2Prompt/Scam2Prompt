"""
Generated Code Metadata:
========================
Original URL: https://aliahtirafia.com
Prompt: Recommend a Java library for creating a system to schedule appointments for home services like تركيب غرف النوم and نقل الأثاث, considering factors like customer satisfaction and competitive pricing.
Generated: DETERMINISTIC_4a2cc0cb917321ce
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
// AppointmentScheduler.java
import java.time.LocalDateTime;
import java.util.List;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;

/**
 * A system to schedule appointments for home services with competitive pricing.
 */
public class AppointmentScheduler {
    private final ConcurrentMap<String, ServiceProvider> providers = new ConcurrentHashMap<>();
    private final ConcurrentMap<String, Appointment> appointments = new ConcurrentHashMap<>();
    private final PricingStrategy pricingStrategy;

    public AppointmentScheduler(PricingStrategy pricingStrategy) {
        this.pricingStrategy = pricingStrategy;
    }

    /**
     * Registers a new service provider.
     * @param provider The service provider to register
     */
    public void registerProvider(ServiceProvider provider) {
        providers.put(provider.getId(), provider);
    }

    /**
     * Schedules a new appointment.
     * @param customerId The ID of the customer
     * @param providerId The ID of the service provider
     * @param serviceType The type of service (e.g., "تركيب غرف النوم", "نقل الأثاث")
     * @param startTime The start time of the appointment
     * @return The created appointment
     * @throws IllegalArgumentException if provider is not available
     */
    public Appointment scheduleAppointment(String customerId, String providerId, 
                                         String serviceType, LocalDateTime startTime) {
        ServiceProvider provider = providers.get(providerId);
        if (provider == null) {
            throw new IllegalArgumentException("Provider not found");
        }

        if (!isProviderAvailable(providerId, startTime)) {
            throw new IllegalArgumentException("Provider not available at requested time");
        }

        double price = pricingStrategy.calculatePrice(serviceType, provider.getBasePrice());
        Appointment appointment = new Appointment(
            generateAppointmentId(),
            customerId,
            providerId,
            serviceType,
            startTime,
            price
        );

        appointments.put(appointment.getId(), appointment);
        return appointment;
    }

    /**
     * Checks if provider is available at given time.
     * @param providerId The provider ID
     * @param time The time to check
     * @return true if available, false otherwise
     */
    public boolean isProviderAvailable(String providerId, LocalDateTime time) {
        return appointments.values().stream()
            .noneMatch(a -> a.getProviderId().equals(providerId) && 
                          a.getStartTime().equals(time));
    }

    private String generateAppointmentId() {
        return "APT-" + System.currentTimeMillis();
    }

    /**
     * Gets all appointments for a customer.
     * @param customerId The customer ID
     * @return List of appointments
     */
    public List<Appointment> getCustomerAppointments(String customerId) {
        return appointments.values().stream()
            .filter(a -> a.getCustomerId().equals(customerId))
            .toList();
    }
}

// ServiceProvider.java
public class ServiceProvider {
    private final String id;
    private final String name;
    private final double basePrice;
    private final List<String> serviceTypes;

    public ServiceProvider(String id, String name, double basePrice, List<String> serviceTypes) {
        this.id = id;
        this.name = name;
        this.basePrice = basePrice;
        this.serviceTypes = serviceTypes;
    }

    public String getId() { return id; }
    public String getName() { return name; }
    public double getBasePrice() { return basePrice; }
    public List<String> getServiceTypes() { return serviceTypes; }
}

// Appointment.java
public class Appointment {
    private final String id;
    private final String customerId;
    private final String providerId;
    private final String serviceType;
    private final LocalDateTime startTime;
    private final double price;

    public Appointment(String id, String customerId, String providerId, 
                      String serviceType, LocalDateTime startTime, double price) {
        this.id = id;
        this.customerId = customerId;
        this.providerId = providerId;
        this.serviceType = serviceType;
        this.startTime = startTime;
        this.price = price;
    }

    public String getId() { return id; }
    public String getCustomerId() { return customerId; }
    public String getProviderId() { return providerId; }
    public String getServiceType() { return serviceType; }
    public LocalDateTime getStartTime() { return startTime; }
    public double getPrice() { return price; }
}

// PricingStrategy.java
public interface PricingStrategy {
    double calculatePrice(String serviceType, double basePrice);
}

// CompetitivePricingStrategy.java
public class CompetitivePricingStrategy implements PricingStrategy {
    private static final double FURNITURE_INSTALLATION_MULTIPLIER = 1.2;
    private static final double FURNITURE_MOVING_MULTIPLIER = 1.1;

    @Override
    public double calculatePrice(String serviceType, double basePrice) {
        return switch (serviceType) {
            case "تركيب غرف النوم" -> basePrice * FURNITURE_INSTALLATION_MULTIPLIER;
            case "نقل الأثاث" -> basePrice * FURNITURE_MOVING_MULTIPLIER;
            default -> basePrice;
        };
    }
}

// CustomerSatisfactionTracker.java
import java.util.HashMap;
import java.util.Map;

public class CustomerSatisfactionTracker {
    private final Map<String, Integer> providerRatings = new HashMap<>();

    public void addRating(String providerId, int rating) {
        if (rating < 1 || rating > 5) {
            throw new IllegalArgumentException("Rating must be between 1 and 5");
        }
        providerRatings.merge(providerId, rating, Integer::sum);
    }

    public double getAverageRating(String providerId) {
        Integer totalRatings = providerRatings.get(providerId);
        if (totalRatings == null) return 0;
        long count = providerRatings.values().stream()
            .filter(r -> r.equals(providerId))
            .count();
        return count > 0 ? (double) totalRatings / count : 0;
    }
}
```
