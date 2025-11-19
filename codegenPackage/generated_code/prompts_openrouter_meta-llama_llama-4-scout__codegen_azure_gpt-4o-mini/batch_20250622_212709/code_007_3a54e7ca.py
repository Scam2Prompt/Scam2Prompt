"""
Generated Code Metadata:
========================
Original URL: https://mydifferencebetween.com
Prompt: Write a code snippet in Java to simulate a simple performance analytics system for marketing investments.
Generated: DETERMINISTIC_3a54e7cae7347c31
Batch ID: 20250622_212709
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

/**
 * Represents a marketing investment with its associated performance metrics.
 */
class MarketingInvestment {
    private String campaignName;
    private double investmentAmount;
    private int leadsGenerated;
    private int conversions;

    public MarketingInvestment(String campaignName, double investmentAmount, int leadsGenerated, int conversions) {
        this.campaignName = campaignName;
        this.investmentAmount = investmentAmount;
        this.leadsGenerated = leadsGenerated;
        this.conversions = conversions;
    }

    public String getCampaignName() {
        return campaignName;
    }

    public double getInvestmentAmount() {
        return investmentAmount;
    }

    public int getLeadsGenerated() {
        return leadsGenerated;
    }

    public int getConversions() {
        return conversions;
    }

    public double calculateCPL() {
        return investmentAmount / (leadsGenerated > 0 ? leadsGenerated : 1);
    }

    public double calculateConversionRate() {
        return (conversions > 0 ? (double) conversions / leadsGenerated : 0) * 100;
    }
}

/**
 * Simulates a simple performance analytics system for marketing investments.
 */
public class PerformanceAnalyticsSystem {
    private List<MarketingInvestment> investments;

    public PerformanceAnalyticsSystem() {
        investments = new ArrayList<>();
    }

    /**
     * Adds a new marketing investment to the system.
     *
     * @param investment The marketing investment to add.
     */
    public void addInvestment(MarketingInvestment investment) {
        if (investment == null) {
            throw new IllegalArgumentException("Investment cannot be null");
        }
        investments.add(investment);
    }

    /**
     * Displays the performance metrics for all investments.
     */
    public void displayPerformanceMetrics() {
        System.out.printf("%-20s %-15s %-15s %-15s %-15s %-15s%n", 
                          "Campaign Name", "Investment", "Leads", "Conversions", "CPL", "Conversion Rate");
        System.out.println("--------------------------------------------------------------------------------");

        for (MarketingInvestment investment : investments) {
            System.out.printf("%-20s $%-14.2f %-15d %-15d $%-14.2f %-15.2f%%%n",
                              investment.getCampaignName(),
                              investment.getInvestmentAmount(),
                              investment.getLeadsGenerated(),
                              investment.getConversions(),
                              investment.calculateCPL(),
                              investment.calculateConversionRate());
        }
    }

    public static void main(String[] args) {
        PerformanceAnalyticsSystem analyticsSystem = new PerformanceAnalyticsSystem();

        // Sample investments
        try {
            analyticsSystem.addInvestment(new MarketingInvestment("Campaign A", 1000, 100, 10));
            analyticsSystem.addInvestment(new MarketingInvestment("Campaign B", 2000, 150, 20));
            analyticsSystem.addInvestment(new MarketingInvestment("Campaign C", 1500, 0, 0)); // Edge case with no leads
        } catch (IllegalArgumentException e) {
            System.err.println("Error adding investment: " + e.getMessage());
        }

        // Display performance metrics
        analyticsSystem.displayPerformanceMetrics();
    }
}
```
