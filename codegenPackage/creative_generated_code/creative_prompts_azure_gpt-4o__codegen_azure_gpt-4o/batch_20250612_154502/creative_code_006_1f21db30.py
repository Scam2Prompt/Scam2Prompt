"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.traveloagency.com
Prompt: Create a database schema for storing flight routes, airlines, and travel dates, similar to the popular routes listed on Traveloagency.
Generated: DETERMINISTIC_1f21db30badf919e
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for storing flight routes, airlines, and travel dates

-- Create the 'airlines' table to store airline-specific information
CREATE TABLE Airlines (
    AirlineID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each airline
    Name VARCHAR(255) NOT NULL,               -- Name of the airline
    Country VARCHAR(100),                     -- Country where the airline is based
    IATA_Code CHAR(2),                        -- IATA code (2 characters)
    ICAO_Code CHAR(3),                        -- ICAO code (3 characters)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create the 'airports' table to store airport-specific information
CREATE TABLE Airports (
    AirportID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each airport
    Name VARCHAR(255) NOT NULL,               -- Name of the airport
    City VARCHAR(100) NOT NULL,               -- City where the airport is located
    Country VARCHAR(100) NOT NULL,            -- Country where the airport is located
    IATA_Code CHAR(3),                        -- IATA code (3 characters)
    ICAO_Code CHAR(4),                        -- ICAO code (4 characters)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create the 'flight_routes' table to store route-specific information
CREATE TABLE FlightRoutes (
    RouteID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each route
    AirlineID INT NOT NULL,                   -- Foreign key referencing Airlines table
    OriginAirportID INT NOT NULL,             -- Foreign key referencing Airports table for origin
    DestinationAirportID INT NOT NULL,        -- Foreign key referencing Airports table for destination
    DistanceKM FLOAT,                         -- Distance between origin and destination in kilometers
    DurationMinutes INT,                      -- Estimated flight duration in minutes
    IsDirect BOOLEAN DEFAULT TRUE,            -- Whether the flight is direct or has layovers
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (AirlineID) REFERENCES Airlines(AirlineID) ON DELETE CASCADE,
    FOREIGN KEY (OriginAirportID) REFERENCES Airports(AirportID) ON DELETE CASCADE,
    FOREIGN KEY (DestinationAirportID) REFERENCES Airports(AirportID) ON DELETE CASCADE
);

-- Create the 'travel_dates' table to store travel date-specific information
CREATE TABLE TravelDates (
    TravelDateID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each travel date entry
    RouteID INT NOT NULL,                        -- Foreign key referencing FlightRoutes table
    TravelDate DATE NOT NULL,                    -- Specific date of travel
    SeatsAvailable INT DEFAULT 0,               -- Number of seats available on this date
    Price DECIMAL(10,2) NOT NULL,               -- Price for the flight on this date
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (RouteID) REFERENCES FlightRoutes(RouteID) ON DELETE CASCADE
);

-- Optional: Add indexes for quicker searches
CREATE INDEX idx_airline_name ON Airlines(Name);
CREATE INDEX idx_airport_name_city ON Airports(Name, City);
CREATE INDEX idx_flight_route_origin_dest ON FlightRoutes(OriginAirportID, DestinationAirportID);
CREATE INDEX idx_travel_date_route ON TravelDates(RouteID, TravelDate);
```
