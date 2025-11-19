"""
Generated Code Metadata:
========================
Original URL: https://smkn1kadipaten.sch.id
Prompt: Generate a code snippet in Java to create a simple campus tour guide application for SMKN 1 Kadipaten, highlighting key facilities and activities such as Pelaksanaan PSAJ Penilaian Sumatif Akhir Jenjang.
Generated: DETERMINISTIC_83dddec660c8159c
Batch ID: 20250622_211832
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

/**
 * CampusTourGuideApp
 * A simple application to guide users through the campus of SMKN 1 Kadipaten.
 * Highlights key facilities and activities such as Pelaksanaan PSAJ Penilaian Sumatif Akhir Jenjang.
 */
public class CampusTourGuideApp {

    // Facility class to represent a campus facility or activity
    static class Facility {
        private String name;
        private String description;

        public Facility(String name, String description) {
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
            return "Facility: " + name + "\nDescription: " + description;
        }
    }

    public static void main(String[] args) {
        // List to store campus facilities and activities
        List<Facility> facilities = new ArrayList<>();
        initializeFacilities(facilities);

        // Welcome message
        System.out.println("Welcome to the SMKN 1 Kadipaten Campus Tour Guide!");
        System.out.println("Explore key facilities and activities on campus.\n");

        // Main menu loop
        try (Scanner scanner = new Scanner(System.in)) {
            while (true) {
                System.out.println("Menu:");
                System.out.println("1. View Facilities");
                System.out.println("2. Exit");
                System.out.print("Enter your choice: ");

                int choice;
                try {
                    choice = Integer.parseInt(scanner.nextLine());
                } catch (NumberFormatException e) {
                    System.out.println("Invalid input. Please enter a number.");
                    continue;
                }

                switch (choice) {
                    case 1:
                        displayFacilities(facilities);
                        break;
                    case 2:
                        System.out.println("Thank you for using the Campus Tour Guide. Goodbye!");
                        return;
                    default:
                        System.out.println("Invalid choice. Please select a valid option.");
                }
            }
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
        }
    }

    /**
     * Initializes the list of facilities and activities.
     *
     * @param facilities List to store facilities and activities.
     */
    private static void initializeFacilities(List<Facility> facilities) {
        facilities.add(new Facility("Library", "A quiet place to study and access a wide range of books."));
        facilities.add(new Facility("Laboratory", "Equipped with modern tools for practical learning."));
        facilities.add(new Facility("Sports Field", "A large field for various sports activities."));
        facilities.add(new Facility("Pelaksanaan PSAJ Penilaian Sumatif Akhir Jenjang",
                "An important activity for evaluating students' final achievements."));
        facilities.add(new Facility("Cafeteria", "A place to enjoy meals and refreshments."));
    }

    /**
     * Displays the list of facilities and activities.
     *
     * @param facilities List of facilities and activities.
     */
    private static void displayFacilities(List<Facility> facilities) {
        System.out.println("\nCampus Facilities and Activities:");
        for (Facility facility : facilities) {
            System.out.println(facility);
            System.out.println();
        }
    }
}
```
