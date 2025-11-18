"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoag.com
Prompt: Create a database schema to manage promotional offers for agricultural equipment, such as the "Unleash the Best Deals" campaign described on RhinoAg's website.
Generated: DETERMINISTIC_ae8e67d24b52d9e9
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema to manage promotional offers for agricultural equipment

-- Table to store information about promotional campaigns
CREATE TABLE PromotionalCampaigns (
    CampaignID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each campaign
    CampaignName VARCHAR(255) NOT NULL, -- Name of the promotional campaign
    Description TEXT, -- Detailed description of the campaign
    StartDate DATE NOT NULL, -- Start date of the campaign
    EndDate DATE NOT NULL, -- End date of the campaign
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the campaign was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the campaign was last updated
);

-- Table to store equipment details associated with promotional offers
CREATE TABLE Equipment (
    EquipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each equipment
    EquipmentName VARCHAR(255) NOT NULL, -- Name of the equipment
    EquipmentCategory VARCHAR(255), -- Category of the equipment (e.g., Tractors, Mowers, etc.)
    Price DECIMAL(10, 2) NOT NULL, -- Base price of the equipment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the equipment was added to the database
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the equipment details were last updated
);

-- Table to store promotional offers for specific equipment
CREATE TABLE PromotionalOffers (
    OfferID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each promotional offer
    CampaignID INT NOT NULL, -- Foreign key referencing PromotionalCampaigns
    EquipmentID INT NOT NULL, -- Foreign key referencing Equipment
    DiscountPercentage DECIMAL(5, 2) NOT NULL, -- Discount percentage applied to the equipment
    OfferPrice DECIMAL(10, 2) NOT NULL, -- Final price after applying the discount
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the offer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the offer was last updated
    CONSTRAINT FK_Campaign FOREIGN KEY (CampaignID) REFERENCES PromotionalCampaigns(CampaignID) ON DELETE CASCADE, -- Cascade delete on campaign removal
    CONSTRAINT FK_Equipment FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID) ON DELETE CASCADE -- Cascade delete on equipment removal
);

-- Table to track campaign analytics and activity
CREATE TABLE CampaignAnalytics (
    AnalyticsID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for campaign analytics
    CampaignID INT NOT NULL, -- Foreign key referencing PromotionalCampaigns
    TotalViews INT DEFAULT 0, -- Number of times the campaign has been viewed
    TotalClicks INT DEFAULT 0, -- Number of times the campaign has been clicked
    TotalPurchases INT DEFAULT 0, -- Number of purchases through the campaign
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    CONSTRAINT FK_Analytics_Campaign FOREIGN KEY (CampaignID) REFERENCES PromotionalCampaigns(CampaignID) ON DELETE CASCADE -- Cascade delete on campaign removal
);

-- Example indexes to optimize query performance
CREATE INDEX idx_campaign_startdate ON PromotionalCampaigns(StartDate); -- Index on campaign start date
CREATE INDEX idx_equipment_category ON Equipment(EquipmentCategory); -- Index on equipment category
CREATE INDEX idx_promotional_offer_price ON PromotionalOffers(OfferPrice); -- Index on offer price

-- Example triggers for additional consistency (optional, based on business logic)
DELIMITER $$

-- Trigger to automatically calculate OfferPrice based on DiscountPercentage
CREATE TRIGGER CalculateOfferPrice 
BEFORE INSERT ON PromotionalOffers
FOR EACH ROW
BEGIN
    SET NEW.OfferPrice = (SELECT Price FROM Equipment WHERE EquipmentID = NEW.EquipmentID) * (1 - NEW.DiscountPercentage / 100);
END$$

DELIMITER ;
```
