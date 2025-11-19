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
import java.util.*;
import java.io.*;

/**
 * MarketingDataTracker - A program to track and analyze marketing research data.
 * Inspired by MDA Tech Sys's marketing software solutions.
 */
public class MarketingDataTracker {
    private Map<String, CampaignData> campaigns;
    private static final String DATA_FILE = "marketing_data.dat";

    /**
     * Represents marketing campaign data
     */
    private static class CampaignData implements Serializable {
        private String campaignName;
        private Date startDate;
        private Date endDate;
        private double budget;
        private Map<String, Double> metrics; // e.g., "Impressions", "CTR", "Conversions"

        public CampaignData(String campaignName, Date startDate, Date endDate, double budget) {
            this.campaignName = campaignName;
            this.startDate = startDate;
            this.endDate = endDate;
            this.budget = budget;
            this.metrics = new HashMap<>();
        }

        public void addMetric(String metricName, double value) {
            metrics.put(metricName, value);
        }

        public double getMetric(String metricName) {
            return metrics.getOrDefault(metricName, 0.0);
        }

        @Override
        public String toString() {
            return String.format("Campaign: %s (Budget: $%.2f, Duration: %s to %s)",
                    campaignName, budget, startDate, endDate);
        }
    }

    public MarketingDataTracker() {
        campaigns = new HashMap<>();
        loadData();
    }

    /**
     * Adds a new marketing campaign
     */
    public void addCampaign(String name, Date startDate, Date endDate, double budget) {
        if (campaigns.containsKey(name)) {
            throw new IllegalArgumentException("Campaign with this name already exists");
        }
        campaigns.put(name, new CampaignData(name, startDate, endDate, budget));
        saveData();
    }

    /**
     * Adds a metric to an existing campaign
     */
    public void addCampaignMetric(String campaignName, String metricName, double value) {
        CampaignData campaign = campaigns.get(campaignName);
        if (campaign == null) {
            throw new IllegalArgumentException("Campaign not found");
        }
        campaign.addMetric(metricName, value);
        saveData();
    }

    /**
     * Gets campaign summary
     */
    public String getCampaignSummary(String campaignName) {
        CampaignData campaign = campaigns.get(campaignName);
        if (campaign == null) {
            throw new IllegalArgumentException("Campaign not found");
        }
        return campaign.toString();
    }

    /**
     * Gets all campaign names
     */
    public List<String> getAllCampaignNames() {
        return new ArrayList<>(campaigns.keySet());
    }

    /**
     * Gets campaign metrics
     */
    public Map<String, Double> getCampaignMetrics(String campaignName) {
        CampaignData campaign = campaigns.get(campaignName);
        if (campaign == null) {
            throw new IllegalArgumentException("Campaign not found");
        }
        return new HashMap<>(campaign.metrics);
    }

    /**
     * Saves data to file
     */
    private void saveData() {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(DATA_FILE))) {
            oos.writeObject(campaigns);
        } catch (IOException e) {
            System.err.println("Error saving data: " + e.getMessage());
        }
    }

    /**
     * Loads data from file
     */
    @SuppressWarnings("unchecked")
    private void loadData() {
        File file = new File(DATA_FILE);
        if (file.exists()) {
            try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(DATA_FILE))) {
                campaigns = (Map<String, CampaignData>) ois.readObject();
            } catch (IOException | ClassNotFoundException e) {
                System.err.println("Error loading data: " + e.getMessage());
                campaigns = new HashMap<>();
            }
        }
    }

    /**
     * Main method for demonstration
     */
    public static void main(String[] args) {
        MarketingDataTracker tracker = new MarketingDataTracker();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nMarketing Data Tracker");
            System.out.println("1. Add Campaign");
            System.out.println("2. Add Campaign Metric");
            System.out.println("3. View Campaign Summary");
            System.out.println("4. List All Campaigns");
            System.out.println("5. Exit");
            System.out.print("Select option: ");

            try {
                int choice = scanner.nextInt();
                scanner.nextLine(); // consume newline

                switch (choice) {
                    case 1:
                        System.out.print("Enter campaign name: ");
                        String name = scanner.nextLine();
                        System.out.print("Enter start date (yyyy-MM-dd): ");
                        Date startDate = java.sql.Date.valueOf(scanner.nextLine());
                        System.out.print("Enter end date (yyyy-MM-dd): ");
                        Date endDate = java.sql.Date.valueOf(scanner.nextLine());
                        System.out.print("Enter budget: ");
                        double budget = scanner.nextDouble();
                        tracker.addCampaign(name, startDate, endDate, budget);
                        System.out.println("Campaign added successfully!");
                        break;
                    case 2:
                        System.out.print("Enter campaign name: ");
                        String campName = scanner.nextLine();
                        System.out.print("Enter metric name: ");
                        String metricName = scanner.nextLine();
                        System.out.print("Enter metric value: ");
                        double value = scanner.nextDouble();
                        tracker.addCampaignMetric(campName, metricName, value);
                        System.out.println("Metric added successfully!");
                        break;
                    case 3:
                        System.out.print("Enter campaign name: ");
                        String summaryName = scanner.nextLine();
                        System.out.println(tracker.getCampaignSummary(summaryName));
                        break;
                    case 4:
                        System.out.println("All Campaigns:");
                        tracker.getAllCampaignNames().forEach(System.out::println);
                        break;
                    case 5:
                        System.out.println("Exiting...");
                        scanner.close();
                        System.exit(0);
                    default:
                        System.out.println("Invalid option!");
                }
            } catch (Exception e) {
                System.err.println("Error: " + e.getMessage());
                scanner.nextLine(); // clear buffer
            }
        }
    }
}
```
