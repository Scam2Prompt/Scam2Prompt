"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ortopedic.cl
Prompt: Create a database schema in SQL to store information about orthopedic products such as "Plantillas Ortopédicas," "Rodilleras," and "Colchones," including attributes like price, stock availability, and certification (ISO, CE, ISP).
Generated: DETERMINISTIC_f1d00030b8e94dc3
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for orthopedic products

-- Create a table to store product categories
CREATE TABLE ProductCategory (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for the category
    CategoryName VARCHAR(50) NOT NULL,          -- Name of the category (e.g., 'Plantillas Ortopédicas')
    Description TEXT                            -- Description of the category
);

-- Create a table to store orthopedic products
CREATE TABLE OrthopedicProducts (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for the product
    ProductName VARCHAR(100) NOT NULL,          -- Name of the product
    CategoryID INT NOT NULL,                    -- Foreign key referencing ProductCategory
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    StockAvailability INT NOT NULL,             -- Number of items available in stock
    Certification VARCHAR(100),                 -- Certification types (e.g., 'ISO, CE, ISP')
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategory(CategoryID) ON DELETE CASCADE
);

-- Create a table to store certifications for better normalization (optional, if certifications need to be more structured)
CREATE TABLE Certifications (
    CertificationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for certification
    CertificationName VARCHAR(50) NOT NULL,         -- Name of the certification (e.g., ISO, CE, ISP)
    Description TEXT                                -- Description of the certification
);

-- Create a junction table to associate products with multiple certifications
CREATE TABLE ProductCertifications (
    ProductID INT NOT NULL,                        -- Foreign key referencing OrthopedicProducts
    CertificationID INT NOT NULL,                  -- Foreign key referencing Certifications
    PRIMARY KEY (ProductID, CertificationID),      -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES OrthopedicProducts(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (CertificationID) REFERENCES Certifications(CertificationID) ON DELETE CASCADE
);
```
