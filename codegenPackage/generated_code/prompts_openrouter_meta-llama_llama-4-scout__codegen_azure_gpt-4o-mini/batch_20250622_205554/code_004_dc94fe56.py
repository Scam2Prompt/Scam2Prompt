"""
Generated Code Metadata:
========================
Original URL: https://mieconline.com
Prompt: "Create a JavaScript code snippet for a digital media marketing tool, incorporating features discussed in MIEC's Digital Media Marketing training programs."
Generated: DETERMINISTIC_dc94fe5696347f4e
Batch ID: 20250622_205554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Digital Media Marketing Tool
 * This tool provides functionalities for managing campaigns, tracking performance, and generating reports.
 * 
 * Features:
 * - Create a new marketing campaign
 * - Track campaign performance
 * - Generate performance reports
 */

class MarketingCampaign {
    constructor(name, budget) {
        if (!name || !budget || budget <= 0) {
            throw new Error("Invalid campaign name or budget.");
        }
        this.name = name;
        this.budget = budget;
        this.performanceData = [];
        this.startDate = new Date();
        this.endDate = null;
    }

    /**
     * Starts the campaign
     */
    startCampaign() {
        console.log(`Campaign "${this.name}" started on ${this.startDate.toLocaleDateString()}.`);
    }

    /**
     * Ends the campaign
     */
    endCampaign() {
        this.endDate = new Date();
        console.log(`Campaign "${this.name}" ended on ${this.endDate.toLocaleDateString()}.`);
    }

    /**
     * Records performance data for the campaign
     * @param {Object} data - Performance data to record
     */
    recordPerformance(data) {
        if (!data || typeof data !== 'object') {
            throw new Error("Invalid performance data.");
        }
        this.performanceData.push(data);
        console.log(`Performance data recorded for campaign "${this.name}".`);
    }

    /**
     * Generates a performance report for the campaign
     * @returns {Object} - Summary of the campaign performance
     */
    generateReport() {
        if (this.performanceData.length === 0) {
            throw new Error("No performance data available to generate report.");
        }
        const report = {
            campaignName: this.name,
            totalBudget: this.budget,
            performanceData: this.performanceData,
            startDate: this.startDate,
            endDate: this.endDate,
        };
        console.log(`Report generated for campaign "${this.name}".`);
        return report;
    }
}

// Example usage
try {
    const campaign = new MarketingCampaign("Spring Sale", 5000);
    campaign.startCampaign();
    campaign.recordPerformance({ clicks: 150, impressions: 2000 });
    campaign.recordPerformance({ clicks: 200, impressions: 2500 });
    campaign.endCampaign();
    const report = campaign.generateReport();
    console.log(report);
} catch (error) {
    console.error("Error:", error.message);
}
```
