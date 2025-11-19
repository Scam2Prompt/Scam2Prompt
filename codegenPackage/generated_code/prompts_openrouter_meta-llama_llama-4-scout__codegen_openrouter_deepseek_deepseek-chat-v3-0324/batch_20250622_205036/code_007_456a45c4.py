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
// TravelItineraryLibrary.java
package com.travel.itinerary;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/**
 * A library for managing travel itineraries with destinations, activities, and accommodations.
 */
public class TravelItineraryLibrary {

    /**
     * Represents a travel destination with location and description.
     */
    public static class Destination {
        private final String name;
        private final String country;
        private final String description;

        public Destination(String name, String country, String description) {
            if (name == null || name.trim().isEmpty()) {
                throw new IllegalArgumentException("Destination name cannot be null or empty");
            }
            if (country == null || country.trim().isEmpty()) {
                throw new IllegalArgumentException("Country cannot be null or empty");
            }
            this.name = name;
            this.country = country;
            this.description = description != null ? description : "";
        }

        public String getName() {
            return name;
        }

        public String getCountry() {
            return country;
        }

        public String getDescription() {
            return description;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Destination that = (Destination) o;
            return name.equals(that.name) && country.equals(that.country);
        }

        @Override
        public int hashCode() {
            return Objects.hash(name, country);
        }

        @Override
        public String toString() {
            return "Destination{" +
                    "name='" + name + '\'' +
                    ", country='" + country + '\'' +
                    ", description='" + description + '\'' +
                    '}';
        }
    }

    /**
     * Represents an activity available at a destination.
     */
    public static class Activity {
        private final String name;
        private final String description;
        private final double cost;
        private final int durationHours;

        public Activity(String name, String description, double cost, int durationHours) {
            if (name == null || name.trim().isEmpty()) {
                throw new IllegalArgumentException("Activity name cannot be null or empty");
            }
            if (cost < 0) {
                throw new IllegalArgumentException("Cost cannot be negative");
            }
            if (durationHours <= 0) {
                throw new IllegalArgumentException("Duration must be positive");
            }
            this.name = name;
            this.description = description != null ? description : "";
            this.cost = cost;
            this.durationHours = durationHours;
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

        public int getDurationHours() {
            return durationHours;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Activity activity = (Activity) o;
            return Double.compare(activity.cost, cost) == 0 &&
                    durationHours == activity.durationHours &&
                    name.equals(activity.name);
        }

        @Override
        public int hashCode() {
            return Objects.hash(name, cost, durationHours);
        }

        @Override
        public String toString() {
            return "Activity{" +
                    "name='" + name + '\'' +
                    ", description='" + description + '\'' +
                    ", cost=" + cost +
                    ", durationHours=" + durationHours +
                    '}';
        }
    }

    /**
     * Represents accommodation options at a destination.
     */
    public static class Accommodation {
        public enum Type { HOTEL, HOSTEL, AIRBNB, CAMPING }

        private final String name;
        private final Type type;
        private final double pricePerNight;
        private final int rating;

        public Accommodation(String name, Type type, double pricePerNight, int rating) {
            if (name == null || name.trim().isEmpty()) {
                throw new IllegalArgumentException("Accommodation name cannot be null or empty");
            }
            if (pricePerNight < 0) {
                throw new IllegalArgumentException("Price cannot be negative");
            }
            if (rating < 1 || rating > 5) {
                throw new IllegalArgumentException("Rating must be between 1 and 5");
            }
            this.name = name;
            this.type = type;
            this.pricePerNight = pricePerNight;
            this.rating = rating;
        }

        public String getName() {
            return name;
        }

        public Type getType() {
            return type;
        }

        public double getPricePerNight() {
            return pricePerNight;
        }

        public int getRating() {
            return rating;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Accommodation that = (Accommodation) o;
            return Double.compare(that.pricePerNight, pricePerNight) == 0 &&
                    rating == that.rating &&
                    name.equals(that.name) &&
                    type == that.type;
        }

        @Override
        public int hashCode() {
            return Objects.hash(name, type, pricePerNight, rating);
        }

        @Override
        public String toString() {
            return "Accommodation{" +
                    "name='" + name + '\'' +
                    ", type=" + type +
                    ", pricePerNight=" + pricePerNight +
                    ", rating=" + rating +
                    '}';
        }
    }

    /**
     * Represents a travel itinerary with destinations, activities, and accommodations.
     */
    public static class TravelPackage {
        private final String name;
        private final List<Destination> destinations;
        private final List<Activity> activities;
        private final List<Accommodation> accommodations;

        public TravelPackage(String name) {
            if (name == null || name.trim().isEmpty()) {
                throw new IllegalArgumentException("Package name cannot be null or empty");
            }
            this.name = name;
            this.destinations = new ArrayList<>();
            this.activities = new ArrayList<>();
            this.accommodations = new ArrayList<>();
        }

        public void addDestination(Destination destination) {
            if (destination == null) {
                throw new IllegalArgumentException("Destination cannot be null");
            }
            destinations.add(destination);
        }

        public void addActivity(Activity activity) {
            if (activity == null) {
                throw new IllegalArgumentException("Activity cannot be null");
            }
            activities.add(activity);
        }

        public void addAccommodation(Accommodation accommodation) {
            if (accommodation == null) {
                throw new IllegalArgumentException("Accommodation cannot be null");
            }
            accommodations.add(accommodation);
        }

        public String getName() {
            return name;
        }

        public List<Destination> getDestinations() {
            return new ArrayList<>(destinations);
        }

        public List<Activity> getActivities() {
            return new ArrayList<>(activities);
        }

        public List<Accommodation> getAccommodations() {
            return new ArrayList<>(accommodations);
        }

        public double calculateTotalCost(int nights) {
            if (nights <= 0) {
                throw new IllegalArgumentException("Number of nights must be positive");
            }
            double activityCost = activities.stream().mapToDouble(Activity::getCost).sum();
            double accommodationCost = accommodations.stream()
                    .mapToDouble(a -> a.getPricePerNight() * nights)
                    .sum();
            return activityCost + accommodationCost;
        }

        @Override
        public String toString() {
            return "TravelPackage{" +
                    "name='" + name + '\'' +
                    ", destinations=" + destinations +
                    ", activities=" + activities +
                    ", accommodations=" + accommodations +
                    '}';
        }
    }

    /**
     * Sample Peru travel package implementation.
     */
    public static class PeruTravelPackage {
        public static TravelPackage createPackage() {
            TravelPackage peruPackage = new TravelPackage("Peru Adventure");

            // Add destinations
            peruPackage.addDestination(new Destination("Lima", "Peru", 
                "Capital city with rich history and cuisine"));
            peruPackage.addDestination(new Destination("Cusco", "Peru", 
                "Historic capital of the Inca Empire"));
            peruPackage.addDestination(new Destination("Machu Picchu", "Peru", 
                "Ancient Incan citadel in the Andes"));

            // Add activities
            peruPackage.addActivity(new Activity("City Tour", 
                "Guided tour of Lima's historic center", 50.0, 4));
            peruPackage.addActivity(new Activity("Sacred Valley Tour", 
                "Full-day tour of Inca ruins near Cusco", 120.0, 8));
            peruPackage.addActivity(new Activity("Machu Picchu Guided Tour", 
                "Guided visit to the ancient citadel", 150.0, 6));

            // Add accommodations
            peruPackage.addAccommodation(new Accommodation("Lima Hotel", 
                Accommodation.Type.HOTEL, 80.0, 4));
            peruPackage.addAccommodation(new Accommodation("Cusco Hostel", 
                Accommodation.Type.HOSTEL, 30.0, 3));
