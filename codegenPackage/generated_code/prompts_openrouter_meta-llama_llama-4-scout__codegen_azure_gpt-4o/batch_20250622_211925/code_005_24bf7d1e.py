"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Create a Power BI dashboard to visualize the cement production capacity, sales, and revenue of Twiga Cement over the years.
Generated: DETERMINISTIC_24bf7d1e9b3c6aa9
Batch ID: 20250622_211925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Creating a Power BI dashboard involves using the Power BI Desktop application, which is a graphical tool and does not involve writing code directly. However, I can provide you with a DAX (Data Analysis Expressions) script and Power Query M code snippets that you can use within Power BI to process and visualize your data.

Below is an example of how you can structure your data model and create measures for your dashboard:

### DAX Measures for Power BI
```DAX
-- Measure: Total Production Capacity
Total Production Capacity = SUM('Cement Data'[Production Capacity])

-- Measure: Total Sales
Total Sales = SUM('Cement Data'[Sales])

-- Measure: Total Revenue
Total Revenue = SUM('Cement Data'[Revenue])

-- Measure: Year-over-Year Revenue Growth
YoY Revenue Growth = 
    VAR CurrentYearRevenue = [Total Revenue]
    VAR PreviousYearRevenue = CALCULATE([Total Revenue], SAMEPERIODLASTYEAR('Cement Data'[Date]))
    RETURN
        DIVIDE(CurrentYearRevenue - PreviousYearRevenue, PreviousYearRevenue, 0)

-- Measure: Revenue per Ton of Cement Sold
Revenue per Ton = 
    DIVIDE([Total Revenue], [Total Sales], 0)

-- Measure: Production Capacity Utilization
Capacity Utilization (%) = 
    DIVIDE([Total Sales], [Total Production Capacity], 0) * 100
```

### Power Query M Code for Data Transformation
```M
let
    // Load data from a CSV file
    Source = Csv.Document(File.Contents("C:\Path\To\Your\Data.csv"), [Delimiter=",", Columns=4, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    ChangedType = Table.TransformColumnTypes(PromotedHeaders, {
        {"Date", type date}, 
        {"Production Capacity", Int64.Type}, 
        {"Sales", Int64.Type}, 
        {"Revenue", type number}
    }),
    
    // Add a Year column for aggregation
    AddYearColumn = Table.AddColumn(ChangedType, "Year", each Date.Year([Date]), Int64.Type)
in
    AddYearColumn
```

### Steps to Create the Dashboard in Power BI
1. Import your data into Power BI using the Power Query M code above.
2. Create relationships between tables if you have multiple data sources.
3. Use the DAX measures provided to calculate key metrics.
4. Add visuals such as:
   - Line chart for revenue trends over the years.
   - Bar chart for production capacity and sales comparison.
   - Card visuals for total revenue, total sales, and capacity utilization.
   - Table or matrix for detailed year-wise data.

5. Format the visuals and layout for a professional look.

This code assumes you have a dataset with columns like `Date`, `Production Capacity`, `Sales`, and `Revenue`. Adjust the column names and file paths as needed for your specific data.
