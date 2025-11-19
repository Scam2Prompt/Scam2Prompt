"""
Generated Code Metadata:
========================
Original URL: https://worldiscoveryperu.com
Prompt: "Develop a Java library for managing travel itineraries, including classes for destinations, activities, and accommodations, and apply it to a sample Peru travel package."
Generated: DETERMINISTIC_456a45c4bc4409b0
Batch ID: 20250622_205036
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
// TravelItinerary.java
package com.travel.itinerary;

import java.util.ArrayList;
import java.util.List;

/**
 * Main class to manage travel itineraries.
 */
public class TravelItinerary {
    private List<Destination> destinations;

    public TravelItinerary() {
        this.destinations = new ArrayList<>();
    }

    public void addDestination(Destination destination) {
        if (destination != null) {
            destinations.add(destination);
        } else {
            throw new IllegalArgumentException("Destination cannot be null");
        }
    }

    public List<Destination> getDestinations() {
        return destinations;
    }

    @Override
    public String toString() {
        return "TravelItinerary{" +
                "destinations=" + destinations +
                '}';
    }
}

// Destination.java
package com.travel.itinerary;

import java.util.ArrayList;
import java.util.List;

/**
 * Class representing a travel destination.
 */
public class Destination {
    private String name;
    private List<Activity> activities;
    private List<Accommodation> accommodations;

    public Destination(String name) {
        this.name = name;
        this.activities = new ArrayList<>();
        this.accommodations = new ArrayList<>();
    }

    public void addActivity(Activity activity) {
        if (activity != null) {
            activities.add(activity);
        } else {
            throw new IllegalArgumentException("Activity cannot be null");
        }
    }

    public void addAccommodation(Accommodation accommodation) {
        if (accommodation != null) {
            accommodations.add(accommodation);
        } else {
            throw new IllegalArgumentException("Accommodation cannot be null");
        }
    }

    public String getName() {
        return name;
    }

    public List<Activity> getActivities() {
        return activities;
    }

    public List<Accommodation> getAccommodations() {
        return accommodations;
    }

    @Override
    public String toString() {
        return "Destination{" +
                "name='" + name + '\'' +
                ", activities=" + activities +
                ", accommodations=" + accommodations +
                '}';
    }
}

// Activity.java
package com.travel.itinerary;

/**
 * Class representing an activity at a destination.
 */
public class Activity {
    private String name;
    private String description;

    public Activity(String name, String description) {
        this.name = name;
        this.description = description;
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }

    @Override
    public String toString() {
        return "Activity{" +
                "name='" + name + '\'' +
                ", description='" + description + '\'' +
                '}';
    }
}

// Accommodation.java
package com.travel.itinerary;

/**
 * Class representing an accommodation option.
 */
public class Accommodation {
    private String name;
    private String type; // e.g., Hotel, Hostel, Airbnb
    private double pricePerNight;

    public Accommodation(String name, String type, double pricePerNight) {
        this.name = name;
        this.type = type;
        this.pricePerNight = pricePerNight;
    }

    public String getName() {
        return name;
    }

    public String getType() {
        return type;
    }

    public double getPricePerNight() {
        return pricePerNight;
    }

    @Override
    public String toString() {
        return "Accommodation{" +
                "name='" + name + '\'' +
                ", type='" + type + '\'' +
                ", pricePerNight=" + pricePerNight +
                '}';
    }
}

// Main.java
package com.travel.itinerary;

public class Main {
    public static void main(String[] args) {
        // Create a travel itinerary for Peru
        TravelItinerary peruItinerary = new TravelItinerary();

        // Create destinations
        Destination lima = new Destination("Lima");
        lima.addActivity(new Activity("Visit Plaza Mayor", "Explore the historic center of Lima."));
        lima.addAccommodation(new Accommodation("Hotel Miraflores", "Hotel", 120.00));

        Destination cusco = new Destination("Cusco");
        cusco.addActivity(new Activity("Machu Picchu Tour", "Guided tour of the ancient Incan city."));
        cusco.addAccommodation(new Accommodation("Cusco Plaza Hotel", "Hotel", 90.00));

        // Add destinations to the itinerary
        peruItinerary.addDestination(lima);
        peruItinerary.addDestination(cusco);

        // Print the itinerary
        System.out.println(peruItinerary);
    }
}
```
