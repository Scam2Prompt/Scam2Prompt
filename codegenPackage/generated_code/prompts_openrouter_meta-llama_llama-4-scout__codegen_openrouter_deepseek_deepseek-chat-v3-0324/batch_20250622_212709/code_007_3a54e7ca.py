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
import java.util.HashMap;
import java.util.Map;
import java.util.Random;

/**
 * A simple performance analytics system for marketing investments.
 * Tracks ROI (Return on Investment) and other metrics for different marketing channels.
 */
public class MarketingPerformanceAnalytics {

    private final Map<String, MarketingChannel> channels;
    private final Random random;

    public MarketingPerformanceAnalytics() {
        this.channels = new HashMap<>();
        this.random = new Random();
    }

    /**
     * Adds a new marketing channel to track.
     * @param channelName Name of the marketing channel
     * @param initialInvestment Initial investment amount
     */
    public void addChannel(String channelName, double initialInvestment) {
        if (channelName == null || channelName.trim().isEmpty()) {
            throw new IllegalArgumentException("Channel name cannot be null or empty");
        }
        if (initialInvestment < 0) {
            throw new IllegalArgumentException("Initial investment cannot be negative");
        }
        channels.put(channelName, new MarketingChannel(channelName, initialInvestment));
    }

    /**
     * Simulates a day's performance for all channels.
     */
    public void simulateDay() {
        for (MarketingChannel channel : channels.values()) {
            double dailyRevenue = random.nextDouble() * 1000;
            double dailyCost = random.nextDouble() * 200;
            channel.updatePerformance(dailyRevenue, dailyCost);
        }
    }

    /**
     * Gets the current ROI for a specific channel.
     * @param channelName Name of the channel
     * @return ROI percentage
     */
    public double getChannelROI(String channelName) {
        if (!channels.containsKey(channelName)) {
            throw new IllegalArgumentException("Channel not found: " + channelName);
        }
        return channels.get(channelName).calculateROI();
    }

    /**
     * Generates a performance report for all channels.
     * @return Formatted report string
     */
    public String generatePerformanceReport() {
        StringBuilder report = new StringBuilder();
        report.append("Marketing Performance Report\n");
        report.append("--------------------------------\n");
        
        for (MarketingChannel channel : channels.values()) {
            report.append(String.format("Channel: %s\n", channel.getName()));
            report.append(String.format("  Total Investment: $%.2f\n", channel.getTotalInvestment()));
            report.append(String.format("  Total Revenue: $%.2f\n", channel.getTotalRevenue()));
            report.append(String.format("  Total Cost: $%.2f\n", channel.getTotalCost()));
            report.append(String.format("  ROI: %.2f%%\n", channel.calculateROI()));
            report.append("--------------------------------\n");
        }
        
        return report.toString();
    }

    private static class MarketingChannel {
        private final String name;
        private double totalInvestment;
        private double totalRevenue;
        private double totalCost;

        public MarketingChannel(String name, double initialInvestment) {
            this.name = name;
            this.totalInvestment = initialInvestment;
            this.totalRevenue = 0;
            this.totalCost = 0;
        }

        public void updatePerformance(double revenue, double cost) {
            this.totalRevenue += revenue;
            this.totalCost += cost;
        }

        public double calculateROI() {
            if (totalInvestment == 0) return 0;
            return ((totalRevenue - totalCost) / totalInvestment) * 100;
        }

        public String getName() {
            return name;
        }

        public double getTotalInvestment() {
            return totalInvestment;
        }

        public double getTotalRevenue() {
            return totalRevenue;
        }

        public double getTotalCost() {
            return totalCost;
        }
    }

    public static void main(String[] args) {
        MarketingPerformanceAnalytics analytics = new MarketingPerformanceAnalytics();
        
        // Add some marketing channels
        analytics.addChannel("Google Ads", 5000);
        analytics.addChannel("Facebook Ads", 3000);
        analytics.addChannel("Email Marketing", 1000);
        
        // Simulate 30 days of performance
        for (int i = 0; i < 30; i++) {
            analytics.simulateDay();
        }
        
        // Generate and print report
        System.out.println(analytics.generatePerformanceReport());
    }
}
```
