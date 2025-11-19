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
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * A simple campus tour guide application for SMKN 1 Kadipaten.
 * Highlights key facilities and activities such as Pelaksanaan PSAJ (Penilaian Sumatif Akhir Jenjang).
 */
public class CampusTourGuide {

    // Map to store facility names and their descriptions
    private static final Map<String, String> FACILITIES = new HashMap<>();

    static {
        // Initialize facilities with their descriptions
        FACILITIES.put("Classrooms", "Modern classrooms equipped with projectors and comfortable seating.");
        FACILITIES.put("Library", "A well-stocked library with a variety of books and digital resources.");
        FACILITIES.put("Computer Lab", "State-of-the-art computer lab with high-speed internet.");
        FACILITIES.put("PSAJ Area", "Area dedicated to Pelaksanaan PSAJ (Penilaian Sumatif Akhir Jenjang).");
        FACILITIES.put("Sports Field", "Large sports field for various athletic activities.");
        FACILITIES.put("Cafeteria", "Clean and spacious cafeteria serving healthy meals.");
    }

    /**
     * Displays the welcome message and available facilities.
     */
    private static void displayWelcomeMessage() {
        System.out.println("Welcome to SMKN 1 Kadipaten Campus Tour Guide!");
        System.out.println("Here are the key facilities you can explore:");
        
        for (String facility : FACILITIES.keySet()) {
            System.out.println("- " + facility);
        }
    }

    /**
     * Displays the description of a selected facility.
     * @param facilityName The name of the facility to describe.
     */
    private static void displayFacilityDescription(String facilityName) {
        String description = FACILITIES.get(facilityName);
        if (description != null) {
            System.out.println("\n" + facilityName + ":");
            System.out.println(description);
        } else {
            System.out.println("\nFacility not found. Please try again.");
        }
    }

    /**
     * Main method to run the campus tour guide application.
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        displayWelcomeMessage();
        
        while (true) {
            System.out.println("\nEnter the name of a facility to learn more (or type 'exit' to quit):");
            String input = scanner.nextLine().trim();
            
            if (input.equalsIgnoreCase("exit")) {
                System.out.println("Thank you for using the SMKN 1 Kadipaten Campus Tour Guide. Have a great day!");
                break;
            }
            
            displayFacilityDescription(input);
        }
        
        scanner.close();
    }
}
```
