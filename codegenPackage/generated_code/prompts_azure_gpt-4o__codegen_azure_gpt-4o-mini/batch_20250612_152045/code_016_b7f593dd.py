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
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Represents a marketing research data entry.
 */
class ResearchData {
    private String campaignName;
    private int leadsGenerated;
    private double conversionRate;

    public ResearchData(String campaignName, int leadsGenerated, double conversionRate) {
        this.campaignName = campaignName;
        this.leadsGenerated = leadsGenerated;
        this.conversionRate = conversionRate;
    }

    public String getCampaignName() {
        return campaignName;
    }

    public int getLeadsGenerated() {
        return leadsGenerated;
    }

    public double getConversionRate() {
        return conversionRate;
    }

    @Override
    public String toString() {
        return "Campaign: " + campaignName + ", Leads: " + leadsGenerated + ", Conversion Rate: " + conversionRate + "%";
    }
}

/**
 * Manages a collection of marketing research data.
 */
class ResearchDataManager {
    private List<ResearchData> researchDataList;

    public ResearchDataManager() {
        researchDataList = new ArrayList<>();
    }

    public void addResearchData(ResearchData data) {
        researchDataList.add(data);
    }

    public void displayAllData() {
        if (researchDataList.isEmpty()) {
            System.out.println("No research data available.");
            return;
        }
        for (ResearchData data : researchDataList) {
            System.out.println(data);
        }
    }
}

/**
 * Main class to run the marketing research data tracking application.
 */
public class MarketingResearchTracker {
    private static final Scanner scanner = new Scanner(System.in);
    private static final ResearchDataManager dataManager = new ResearchDataManager();

    public static void main(String[] args) {
        while (true) {
            System.out.println("Marketing Research Tracker");
            System.out.println("1. Add Research Data");
            System.out.println("2. Display All Research Data");
            System.out.println("3. Exit");
            System.out.print("Choose an option: ");

            int choice = getUserChoice();

            switch (choice) {
                case 1:
                    addResearchData();
                    break;
                case 2:
                    dataManager.displayAllData();
                    break;
                case 3:
                    System.out.println("Exiting the application.");
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    private static int getUserChoice() {
        while (true) {
            try {
                return Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number.");
            }
        }
    }

    private static void addResearchData() {
        System.out.print("Enter campaign name: ");
        String campaignName = scanner.nextLine();

        int leadsGenerated = getPositiveInteger("Enter leads generated: ");
        double conversionRate = getPositiveDouble("Enter conversion rate (in %): ");

        ResearchData data = new ResearchData(campaignName, leadsGenerated, conversionRate);
        dataManager.addResearchData(data);
        System.out.println("Research data added successfully.");
    }

    private static int getPositiveInteger(String prompt) {
        while (true) {
            System.out.print(prompt);
            try {
                int value = Integer.parseInt(scanner.nextLine());
                if (value < 0) {
                    throw new IllegalArgumentException("Value must be non-negative.");
                }
                return value;
            } catch (NumberFormatException | IllegalArgumentException e) {
                System.out.println("Invalid input. Please enter a non-negative integer.");
            }
        }
    }

    private static double getPositiveDouble(String prompt) {
        while (true) {
            System.out.print(prompt);
            try {
                double value = Double.parseDouble(scanner.nextLine());
                if (value < 0) {
                    throw new IllegalArgumentException("Value must be non-negative.");
                }
                return value;
            } catch (NumberFormatException | IllegalArgumentException e) {
                System.out.println("Invalid input. Please enter a non-negative number.");
            }
        }
    }
}
```
