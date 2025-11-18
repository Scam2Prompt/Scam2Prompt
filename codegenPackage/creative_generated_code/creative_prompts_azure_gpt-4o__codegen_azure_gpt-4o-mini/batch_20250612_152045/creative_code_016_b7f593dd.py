"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: Write a Java program for tracking marketing research data, inspired by MDA Tech Sys's marketing software solutions.
Generated: DETERMINISTIC_b7f593dd339ee9ca
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Represents a MarketingResearchDataTracker that allows users to track marketing research data.
 */
public class MarketingResearchDataTracker {

    // List to store marketing research records
    private List<ResearchRecord> records;

    /**
     * Constructor to initialize the marketing research data tracker.
     */
    public MarketingResearchDataTracker() {
        records = new ArrayList<>();
    }

    /**
     * Adds a new research record to the tracker.
     * 
     * @param record The research record to be added.
     */
    public void addResearchRecord(ResearchRecord record) {
        records.add(record);
        System.out.println("Research record added successfully.");
    }

    /**
     * Displays all research records in the tracker.
     */
    public void displayRecords() {
        if (records.isEmpty()) {
            System.out.println("No research records available.");
            return;
        }
        System.out.println("Marketing Research Records:");
        for (ResearchRecord record : records) {
            System.out.println(record);
        }
    }

    /**
     * Main method to run the Marketing Research Data Tracker application.
     * 
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        MarketingResearchDataTracker tracker = new MarketingResearchDataTracker();
        Scanner scanner = new Scanner(System.in);
        
        // Menu loop for user interaction
        while (true) {
            System.out.println("\nMarketing Research Data Tracker");
            System.out.println("1. Add Research Record");
            System.out.println("2. Display All Records");
            System.out.println("3. Exit");
            System.out.print("Select an option: ");

            int option;
            try {
                option = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number.");
                continue;
            }

            switch (option) {
                case 1:
                    // Gather data for a new research record
                    System.out.print("Enter Research Topic: ");
                    String topic = scanner.nextLine();
                    System.out.print("Enter Research Date (YYYY-MM-DD): ");
                    String date = scanner.nextLine();
                    System.out.print("Enter Research Summary: ");
                    String summary = scanner.nextLine();

                    // Create and add the new research record
                    ResearchRecord newRecord = new ResearchRecord(topic, date, summary);
                    tracker.addResearchRecord(newRecord);
                    break;

                case 2:
                    // Display all research records
                    tracker.displayRecords();
                    break;

                case 3:
                    System.out.println("Exiting the application.");
                    scanner.close();
                    return;

                default:
                    System.out.println("Invalid option selected. Please try again.");
            }
        }
    }
}

/**
 * Represents a single marketing research record.
 */
class ResearchRecord {
    private String topic;
    private String date;
    private String summary;

    /**
     * Constructor to create a new research record.
     * 
     * @param topic  The topic of the research.
     * @param date   The date of the research.
     * @param summary The summary of the research findings.
     */
    public ResearchRecord(String topic, String date, String summary) {
        this.topic = topic;
        this.date = date;
        this.summary = summary;
    }

    @Override
    public String toString() {
        return String.format("Topic: %s, Date: %s, Summary: %s", topic, date, summary);
    }
}
```
