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
// File: TravelItineraryLibrary.java
package travel;

import java.util.ArrayList;
import java.util.List;

// Class representing a destination
public class Destination {
    private String name;
    private String country;

    public Destination(String name, String country) {
        this.name = name;
        this.country = country;
    }

    public String getName() {
        return name;
    }

    public String getCountry() {
        return country;
    }

    @Override
    public String toString() {
        return name + ", " + country;
    }
}

// Class representing an activity at a destination
class Activity {
    private String name;
    private String description;
    private double cost;

    public Activity(String name, String description, double cost) {
        this.name = name;
        this.description = description;
        this.cost = cost;
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }

    public double getCost() {
        return cost;
    }

    @Override
    public String toString() {
        return name + " - " + description + " ($" + cost + ")";
    }
}

// Class representing an accommodation at a destination
class Accommodation {
    private String name;
    private String type; // e.g., Hotel, Hostel, Airbnb
    private double costPerNight;

    public Accommodation(String name, String type, double costPerNight) {
        this.name = name;
        this.type = type;
        this.costPerNight = costPerNight;
    }

    public String getName() {
        return name;
    }

    public String getType() {
        return type;
    }

    public double getCostPerNight() {
        return costPerNight;
    }

    @Override
    public String toString() {
        return name + " (" + type + ") - $" + costPerNight + "/night";
    }
}

// Class representing a travel itinerary
class Itinerary {
    private List<Destination> destinations;
    private List<Activity> activities;
    private List<Accommodation> accommodations;

    public Itinerary() {
        this.destinations = new ArrayList<>();
        this.activities = new ArrayList<>();
        this.accommodations = new ArrayList<>();
    }

    public void addDestination(Destination destination) {
        destinations.add(destination);
    }

    public void addActivity(Activity activity) {
        activities.add(activity);
    }

    public void addAccommodation(Accommodation accommodation) {
        accommodations.add(accommodation);
    }

    public List<Destination> getDestinations() {
        return destinations;
    }

    public List<Activity> getActivities() {
        return activities;
    }

    public List<Accommodation> getAccommodations() {
        return accommodations;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Travel Itinerary:\n");
        sb.append("Destinations:\n");
        for (Destination d : destinations) {
            sb.append("  - ").append(d).append("\n");
        }
        sb.append("Activities:\n");
        for (Activity a : activities) {
            sb.append("  - ").append(a).append("\n");
        }
        sb.append("Accommodations:\n");
        for (Accommodation ac : accommodations) {
            sb.append("  - ").append(ac).append("\n");
        }
        return sb.toString();
    }
}

// File: Main.java
package travel;

public class Main {
    public static void main(String[] args) {
        try {
            // Create a new itinerary
            Itinerary peruItinerary = new Itinerary();

            // Add destinations
            Destination lima = new Destination("Lima", "Peru");
            Destination cusco = new Destination("Cusco", "Peru");
            Destination machuPicchu = new Destination("Machu Picchu", "Peru");
            peruItinerary.addDestination(lima);
            peruItinerary.addDestination(cusco);
            peruItinerary.addDestination(machuPicchu);

            // Add activities
            Activity cityTour = new Activity("City Tour", "Explore the historic center of Lima", 50.0);
            Activity sacredValley = new Activity("Sacred Valley Tour", "Visit the Sacred Valley near Cusco", 100.0);
            Activity machuPicchuVisit = new Activity("Machu Picchu Visit", "Guided tour of Machu Picchu", 150.0);
            peruItinerary.addActivity(cityTour);
            peruItinerary.addActivity(sacredValley);
            peruItinerary.addActivity(machuPicchuVisit);

            // Add accommodations
            Accommodation limaHotel = new Accommodation("Lima Grand Hotel", "Hotel", 120.0);
            Accommodation cuscoHostel = new Accommodation("Cusco Backpackers", "Hostel", 30.0);
            Accommodation machuPicchuLodge = new Accommodation("Machu Picchu Lodge", "Lodge", 200.0);
            peruItinerary.addAccommodation(limaHotel);
            peruItinerary.addAccommodation(cuscoHostel);
            peruItinerary.addAccommodation(machuPicchuLodge);

            // Print the itinerary
            System.out.println(peruItinerary);
        } catch (Exception e) {
            // Handle any unexpected errors
            System.err.println("An error occurred while creating the itinerary: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
```
