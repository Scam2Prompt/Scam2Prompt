"""
Generated Code Metadata:
========================
Original URL: https://webservicesindia.info
Prompt: Develop a Java-based application for managing banner design campaigns, using the creative banner design services outlined by WebServicesIndia.
Generated: DETERMINISTIC_83bd8f011e66d4c2
Batch ID: 20250612_153224
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
 * Represents a banner design campaign.
 */
class BannerDesignCampaign {
    private String campaignName;
    private String clientName;
    private List<String> designs;

    public BannerDesignCampaign(String campaignName, String clientName) {
        this.campaignName = campaignName;
        this.clientName = clientName;
        this.designs = new ArrayList<>();
    }

    public String getCampaignName() {
        return campaignName;
    }

    public String getClientName() {
        return clientName;
    }

    public void addDesign(String design) {
        designs.add(design);
    }

    public List<String> getDesigns() {
        return designs;
    }

    @Override
    public String toString() {
        return "Campaign: " + campaignName + ", Client: " + clientName + ", Designs: " + designs;
    }
}

/**
 * Manages multiple banner design campaigns.
 */
class CampaignManager {
    private List<BannerDesignCampaign> campaigns;

    public CampaignManager() {
        campaigns = new ArrayList<>();
    }

    public void addCampaign(BannerDesignCampaign campaign) {
        campaigns.add(campaign);
    }

    public List<BannerDesignCampaign> getCampaigns() {
        return campaigns;
    }

    public void displayCampaigns() {
        if (campaigns.isEmpty()) {
            System.out.println("No campaigns available.");
        } else {
            for (BannerDesignCampaign campaign : campaigns) {
                System.out.println(campaign);
            }
        }
    }
}

/**
 * Main application class for managing banner design campaigns.
 */
public class BannerDesignApp {
    private static final Scanner scanner = new Scanner(System.in);
    private static final CampaignManager campaignManager = new CampaignManager();

    public static void main(String[] args) {
        while (true) {
            System.out.println("Banner Design Campaign Manager");
            System.out.println("1. Add Campaign");
            System.out.println("2. Display Campaigns");
            System.out.println("3. Exit");
            System.out.print("Choose an option: ");

            int choice = getUserInput();

            switch (choice) {
                case 1:
                    addCampaign();
                    break;
                case 2:
                    campaignManager.displayCampaigns();
                    break;
                case 3:
                    System.out.println("Exiting the application.");
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    private static void addCampaign() {
        System.out.print("Enter campaign name: ");
        String campaignName = scanner.nextLine();

        System.out.print("Enter client name: ");
        String clientName = scanner.nextLine();

        BannerDesignCampaign campaign = new BannerDesignCampaign(campaignName, clientName);
        campaignManager.addCampaign(campaign);

        System.out.println("Campaign added successfully.");
        addDesignsToCampaign(campaign);
    }

    private static void addDesignsToCampaign(BannerDesignCampaign campaign) {
        while (true) {
            System.out.print("Enter design name to add (or type 'done' to finish): ");
            String design = scanner.nextLine();

            if (design.equalsIgnoreCase("done")) {
                break;
            }

            campaign.addDesign(design);
            System.out.println("Design added.");
        }
    }

    private static int getUserInput() {
        while (true) {
            try {
                return Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number.");
            }
        }
    }
}
```
