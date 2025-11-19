"""
Generated Code Metadata:
========================
Original URL: https://corfucoastalcollection.com
Prompt: Create a SQL database schema to store information about villas and plots for sale in Corfu, including fields for location, price, and features like sea view.
Generated: DETERMINISTIC_604192fcac96a24d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema to store information about villas and plots for sale in Corfu

-- Create a table to store general property information
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    PropertyType ENUM('Villa', 'Plot') NOT NULL, -- Type of property: Villa or Plot
    Location VARCHAR(255) NOT NULL, -- Location of the property
    Price DECIMAL(15, 2) NOT NULL, -- Price of the property
    SeaView BOOLEAN NOT NULL DEFAULT FALSE, -- Indicates if the property has a sea view
    Features TEXT, -- Additional features of the property (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the property was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Create a table to store villa-specific details
CREATE TABLE Villas (
    VillaID INT PRIMARY KEY, -- Unique identifier for the villa (matches PropertyID)
    Bedrooms INT NOT NULL, -- Number of bedrooms in the villa
    Bathrooms INT NOT NULL, -- Number of bathrooms in the villa
    Pool BOOLEAN NOT NULL DEFAULT FALSE, -- Indicates if the villa has a pool
    FOREIGN KEY (VillaID) REFERENCES Properties(PropertyID) ON DELETE CASCADE -- Foreign key linking to Properties table
);

-- Create a table to store plot-specific details
CREATE TABLE Plots (
    PlotID INT PRIMARY KEY, -- Unique identifier for the plot (matches PropertyID)
    AreaSqMeters DECIMAL(10, 2) NOT NULL, -- Area of the plot in square meters
    Buildable BOOLEAN NOT NULL DEFAULT FALSE, -- Indicates if the plot is buildable
    FOREIGN KEY (PlotID) REFERENCES Properties(PropertyID) ON DELETE CASCADE -- Foreign key linking to Properties table
);

-- Example indexes for performance optimization
CREATE INDEX idx_location ON Properties(Location); -- Index for faster location-based searches
CREATE INDEX idx_price ON Properties(Price); -- Index for faster price-based searches
CREATE INDEX idx_seaview ON Properties(SeaView); -- Index for faster sea view filtering
```
