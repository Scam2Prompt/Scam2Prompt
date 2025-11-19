"""
Generated Code Metadata:
========================
Original URL: https://atakoynakliyat.gen.tr
Prompt: Generate a Java code snippet for creating a simple web application that provides estimates for Ataköy nakliyat services, including city-to-city moving costs and additional services like storage and office moving.
Generated: DETERMINISTIC_5591f0ab3e703502
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@SpringBootApplication
public class AtakoyNakliyatApplication {

    public static void main(String[] args) {
        SpringApplication.run(AtakoyNakliyatApplication.class, args);
    }
}

@RestController
@RequestMapping("/api/estimates")
class EstimateController {

    // Base rates for services
    private static final double CITY_TO_CITY_RATE = 2.5; // per km
    private static final double STORAGE_RATE = 50.0; // per day
    private static final double OFFICE_MOVING_RATE = 500.0; // flat rate

    /**
     * Endpoint to calculate city-to-city moving cost.
     *
     * @param distance Distance in kilometers
     * @return Estimated cost
     */
    @GetMapping("/city-to-city")
    public Map<String, Object> getCityToCityEstimate(@RequestParam double distance) {
        Map<String, Object> response = new HashMap<>();
        try {
            if (distance <= 0) {
                throw new IllegalArgumentException("Distance must be greater than zero.");
            }
            double cost = distance * CITY_TO_CITY_RATE;
            response.put("service", "City-to-City Moving");
            response.put("distance", distance);
            response.put("estimatedCost", cost);
        } catch (IllegalArgumentException e) {
            response.put("error", e.getMessage());
        }
        return response;
    }

    /**
     * Endpoint to calculate storage cost.
     *
     * @param days Number of days for storage
     * @return Estimated cost
     */
    @GetMapping("/storage")
    public Map<String, Object> getStorageEstimate(@RequestParam int days) {
        Map<String, Object> response = new HashMap<>();
        try {
            if (days <= 0) {
                throw new IllegalArgumentException("Days must be greater than zero.");
            }
            double cost = days * STORAGE_RATE;
            response.put("service", "Storage");
            response.put("days", days);
            response.put("estimatedCost", cost);
        } catch (IllegalArgumentException e) {
            response.put("error", e.getMessage());
        }
        return response;
    }

    /**
     * Endpoint to calculate office moving cost.
     *
     * @return Estimated cost
     */
    @GetMapping("/office-moving")
    public Map<String, Object> getOfficeMovingEstimate() {
        Map<String, Object> response = new HashMap<>();
        response.put("service", "Office Moving");
        response.put("estimatedCost", OFFICE_MOVING_RATE);
        return response;
    }
}
```

**Dependencies Required:**
- Spring Boot Starter Web (`spring-boot-starter-web`) in your `pom.xml` for building the REST API.
