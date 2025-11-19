"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: Write a Java program for tracking marketing research data, inspired by MDA Tech Sys's marketing software solutions.
Generated: DETERMINISTIC_b7f593dd339ee9ca
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Marketing Research Data Tracker
 * 
 * This program allows users to track marketing research data.
 * It provides functionality to add, view, and export data.
 */

// Data class to hold marketing research data
class MarketingData {
    private String date;
    private String researchType;
    private String description;
    private int respondents;

    public MarketingData(String date, String researchType, String description, int respondents) {
        this.date = date;
        this.researchType = researchType;
        this.description = description;
        this.respondents = respondents;
    }

    // Getters and setters
    public String getDate() { return date; }
    public String getResearchType() { return researchType; }
    public String getDescription() { return description; }
    public int getRespondents() { return respondents; }
}

public class MarketingResearchTracker {
    private List<MarketingData> dataList;

    public MarketingResearchTracker() {
        this.dataList = new ArrayList<>();
    }

    // Method to add marketing research data
    public void addData() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter date (yyyy-MM-dd): ");
        String date = scanner.nextLine();

        System.out.print("Enter research type: ");
        String researchType = scanner.nextLine();

        System.out.print("Enter description: ");
        String description = scanner.nextLine();

        System.out.print("Enter number of respondents: ");
        int respondents = scanner.nextInt();
        scanner.nextLine(); // Consume newline left-over

        MarketingData data = new MarketingData(date, researchType, description, respondents);
        dataList.add(data);

        System.out.println("Data added successfully!");
    }

    // Method to view all marketing research data
    public void viewData() {
        if (dataList.isEmpty()) {
            System.out.println("No data available.");
            return;
        }

        System.out.println("Marketing Research Data:");
        for (int i = 0; i < dataList.size(); i++) {
            MarketingData data = dataList.get(i);
            System.out.println((i + 1) + ".");
            System.out.println("Date: " + data.getDate());
            System.out.println("Research Type: " + data.getResearchType());
            System.out.println("Description: " + data.getDescription());
            System.out.println("Respondents: " + data.getRespondents());
            System.out.println();
        }
    }

    // Method to export data to a CSV file
    public void exportData() {
        if (dataList.isEmpty()) {
            System.out.println("No data available to export.");
            return;
        }

        try (PrintWriter writer = new PrintWriter(new FileWriter("marketing_data.csv"))) {
            writer.println("Date,Research Type,Description,Respondents");
            for (MarketingData data : dataList) {
                writer.println(String.format("%s,%s,%s,%d",
                        data.getDate(), data.getResearchType(), data.getDescription(), data.getRespondents()));
            }
            System.out.println("Data exported to marketing_data.csv successfully!");
        } catch (IOException e) {
            System.err.println("Error exporting data: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        MarketingResearchTracker tracker = new MarketingResearchTracker();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Marketing Research Data Tracker");
            System.out.println("1. Add Data");
            System.out.println("2. View Data");
            System.out.println("3. Export Data");
            System.out.println("4. Exit");

            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            scanner.nextLine(); // Consume newline left-over

            switch (option) {
                case 1:
                    tracker.addData();
                    break;
                case 2:
                    tracker.viewData();
                    break;
                case 3:
                    tracker.exportData();
                    break;
                case 4:
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Invalid option. Please choose a valid option.");
            }
        }
    }
}
```
