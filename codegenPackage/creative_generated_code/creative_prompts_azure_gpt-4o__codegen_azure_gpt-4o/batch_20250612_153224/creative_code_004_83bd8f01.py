"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webservicesindia.info
Prompt: Develop a Java-based application for managing banner design campaigns, using the creative banner design services outlined by WebServicesIndia.
Generated: DETERMINISTIC_83bd8f011e66d4c2
Batch ID: 20250612_153224
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

// Main application class
public class BannerCampaignManager {

    public static void main(String[] args) {
        BannerCampaignService campaignService = new BannerCampaignService();
        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        System.out.println("Welcome to the Banner Campaign Manager!");

        while (running) {
            System.out.println("\nMenu:");
            System.out.println("1. Create a new banner campaign");
            System.out.println("2. View all banner campaigns");
            System.out.println("3. Update a banner campaign");
            System.out.println("4. Delete a banner campaign");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");

            try {
                int choice = Integer.parseInt(scanner.nextLine());
                switch (choice) {
                    case 1:
                        System.out.print("Enter campaign name: ");
                        String name = scanner.nextLine();
                        System.out.print("Enter target audience: ");
                        String audience = scanner.nextLine();
                        System.out.print("Enter budget: ");
                        double budget = Double.parseDouble(scanner.nextLine());
                        campaignService.createCampaign(name, audience, budget);
                        System.out.println("Campaign created successfully.");
                        break;
                    case 2:
                        List<BannerCampaign> campaigns = campaignService.getAllCampaigns();
                        if (campaigns.isEmpty()) {
                            System.out.println("No campaigns found.");
                        } else {
                            System.out.println("List of campaigns:");
                            for (BannerCampaign campaign : campaigns) {
                                System.out.println(campaign);
                            }
                        }
                        break;
                    case 3:
                        System.out.print("Enter campaign ID to update: ");
                        int updateId = Integer.parseInt(scanner.nextLine());
                        System.out.print("Enter new campaign name: ");
                        String newName = scanner.nextLine();
                        System.out.print("Enter new target audience: ");
                        String newAudience = scanner.nextLine();
                        System.out.print("Enter new budget: ");
                        double newBudget = Double.parseDouble(scanner.nextLine());
                        if (campaignService.updateCampaign(updateId, newName, newAudience, newBudget)) {
                            System.out.println("Campaign updated successfully.");
                        } else {
                            System.out.println("Campaign ID not found.");
                        }
                        break;
                    case 4:
                        System.out.print("Enter campaign ID to delete: ");
                        int deleteId = Integer.parseInt(scanner.nextLine());
                        if (campaignService.deleteCampaign(deleteId)) {
                            System.out.println("Campaign deleted successfully.");
                        } else {
                            System.out.println("Campaign ID not found.");
                        }
                        break;
                    case 5:
                        running = false;
                        System.out.println("Exiting Banner Campaign Manager. Goodbye!");
                        break;
                    default:
                        System.out.println("Invalid option. Please try again.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a valid number.");
            } catch (Exception e) {
                System.out.println("An unexpected error occurred: " + e.getMessage());
            }
        }
        scanner.close();
    }
}

// Model class representing a banner campaign
class BannerCampaign {
    private static int idCounter = 1;

    private int id;
    private String name;
    private String targetAudience;
    private double budget;

    public BannerCampaign(String name, String targetAudience, double budget) {
        this.id = idCounter++;
        this.name = name;
        this.targetAudience = targetAudience;
        this.budget = budget;
    }

    public int getId() {
        return id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setTargetAudience(String targetAudience) {
        this.targetAudience = targetAudience;
    }

    public void setBudget(double budget) {
        this.budget = budget;
    }

    @Override
    public String toString() {
        return "Campaign ID: " + id + ", Name: " + name + ", Target Audience: " + targetAudience + ", Budget: $" + budget;
    }
}

// Service class for managing banner campaigns
class BannerCampaignService {
    private final List<BannerCampaign> campaigns = new ArrayList<>();

    // Create a new campaign
    public void createCampaign(String name, String targetAudience, double budget) {
        BannerCampaign campaign = new BannerCampaign(name, targetAudience, budget);
        campaigns.add(campaign);
    }

    // Retrieve all campaigns
    public List<BannerCampaign> getAllCampaigns() {
        return new ArrayList<>(campaigns);
    }

    // Update a campaign by ID
    public boolean updateCampaign(int campaignId, String newName, String newTargetAudience, double newBudget) {
        for (BannerCampaign campaign : campaigns) {
            if (campaign.getId() == campaignId) {
                campaign.setName(newName);
                campaign.setTargetAudience(newTargetAudience);
                campaign.setBudget(newBudget);
                return true;
            }
        }
        return false; // Campaign ID not found
    }

    // Delete a campaign by ID
    public boolean deleteCampaign(int campaignId) {
        return campaigns.removeIf(campaign -> campaign.getId() == campaignId);
    }
}
```
