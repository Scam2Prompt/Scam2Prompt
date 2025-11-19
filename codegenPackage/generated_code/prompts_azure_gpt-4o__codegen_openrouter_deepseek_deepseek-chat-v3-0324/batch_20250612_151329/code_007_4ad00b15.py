"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Generate SQL queries to track and optimize revenue management in hotel operations, referencing the Hampton's Hotel Institute's Hotel Operations Management curriculum.
Generated: DETERMINISTIC_4ad00b15a02b144e
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Queries for Hotel Revenue Management Optimization
-- Based on Hampton's Hotel Institute's Hotel Operations Management Curriculum

-- 1. Create tables for hotel operations data
CREATE TABLE IF NOT EXISTS room_types (
    room_type_id INT PRIMARY KEY,
    room_type_name VARCHAR(50) NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    max_capacity INT NOT NULL,
    amenities TEXT
);

CREATE TABLE IF NOT EXISTS rooms (
    room_id INT PRIMARY KEY,
    room_type_id INT NOT NULL,
    floor_number INT NOT NULL,
    room_status VARCHAR(20) NOT NULL CHECK (room_status IN ('Available', 'Occupied', 'Maintenance', 'Reserved')),
    FOREIGN KEY (room_type_id) REFERENCES room_types(room_type_id)
);

CREATE TABLE IF NOT EXISTS reservations (
    reservation_id INT PRIMARY KEY,
    guest_id INT NOT NULL,
    room_id INT NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    booking_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total_price DECIMAL(10, 2) NOT NULL,
    payment_status VARCHAR(20) NOT NULL CHECK (payment_status IN ('Paid', 'Pending', 'Cancelled', 'Refunded')),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

CREATE TABLE IF NOT EXISTS revenue_streams (
    revenue_id INT PRIMARY KEY,
    stream_name VARCHAR(50) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    transaction_date DATE NOT NULL,
    description TEXT
);

-- 2. Key Performance Indicators (KPIs) for Revenue Management
-- Occupancy Rate
SELECT 
    COUNT(CASE WHEN room_status = 'Occupied' THEN 1 END) * 100.0 / COUNT(*) AS occupancy_rate
FROM rooms;

-- Average Daily Rate (ADR)
SELECT 
    AVG(total_price / DATEDIFF(check_out_date, check_in_date)) AS average_daily_rate
FROM reservations
WHERE payment_status = 'Paid' 
AND check_out_date >= CURRENT_DATE - INTERVAL 30 DAY;

-- Revenue Per Available Room (RevPAR)
SELECT 
    (SUM(total_price) / COUNT(DISTINCT room_id)) AS revpar
FROM reservations
WHERE payment_status = 'Paid'
AND check_in_date >= CURRENT_DATE - INTERVAL 30 DAY
AND check_out_date <= CURRENT_DATE;

-- 3. Revenue Optimization Queries
-- Room Type Performance Analysis
SELECT 
    rt.room_type_name,
    COUNT(r.reservation_id) AS bookings,
    AVG(r.total_price) AS avg_revenue,
    SUM(r.total_price) AS total_revenue,
    (COUNT(r.reservation_id) * 100.0 / (SELECT COUNT(*) FROM reservations)) AS market_share
FROM reservations r
JOIN rooms rm ON r.room_id = rm.room_id
JOIN room_types rt ON rm.room_type_id = rt.room_type_id
WHERE r.check_in_date >= CURRENT_DATE - INTERVAL 90 DAY
GROUP BY rt.room_type_name
ORDER BY total_revenue DESC;

-- Dynamic Pricing Analysis
SELECT 
    rt.room_type_name,
    DAYNAME(r.check_in_date) AS day_of_week,
    AVG(r.total_price / DATEDIFF(r.check_out_date, r.check_in_date)) AS avg_daily_rate,
    COUNT(r.reservation_id) AS booking_count
FROM reservations r
JOIN rooms rm ON r.room_id = rm.room_id
JOIN room_types rt ON rm.room_type_id = rt.room_type_id
WHERE r.check_in_date >= CURRENT_DATE - INTERVAL 180 DAY
GROUP BY rt.room_type_name, DAYNAME(r.check_in_date)
ORDER BY rt.room_type_name, booking_count DESC;

-- Revenue Forecast for Next 30 Days
SELECT 
    DATE(check_in_date) AS date,
    SUM(total_price) AS projected_revenue,
    COUNT(*) AS projected_bookings
FROM reservations
WHERE check_in_date BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL 30 DAY
AND payment_status IN ('Paid', 'Pending')
GROUP BY DATE(check_in_date)
ORDER BY date;

-- 4. Revenue Leakage Detection
-- Unpaid Reservations
SELECT 
    r.reservation_id,
    g.guest_name,
    r.total_price,
    DATEDIFF(CURRENT_DATE, r.booking_date) AS days_unpaid
FROM reservations r
JOIN guests g ON r.guest_id = g.guest_id
WHERE r.payment_status = 'Pending'
AND r.check_in_date <= CURRENT_DATE + INTERVAL 3 DAY
ORDER BY days_unpaid DESC;

-- Cancellation Analysis
SELECT 
    room_type_name,
    COUNT(*) AS cancellations,
    SUM(total_price) AS lost_revenue
FROM reservations r
JOIN rooms rm ON r.room_id = rm.room_id
JOIN room_types rt ON rm.room_type_id = rt.room_type_id
WHERE payment_status = 'Cancelled'
AND booking_date >= CURRENT_DATE - INTERVAL 90 DAY
GROUP BY room_type_name
ORDER BY lost_revenue DESC;

-- 5. Ancillary Revenue Tracking
SELECT 
    stream_name,
    SUM(amount) AS total_revenue,
    (SUM(amount) * 100.0 / (SELECT SUM(amount) FROM revenue_streams)) AS revenue_percentage
FROM revenue_streams
WHERE transaction_date >= CURRENT_DATE - INTERVAL 30 DAY
GROUP BY stream_name
ORDER BY total_revenue DESC;

-- 6. Optimal Room Allocation Query
SELECT 
    rt.room_type_name,
    COUNT(rm.room_id) AS total_rooms,
    COUNT(CASE WHEN rm.room_status = 'Occupied' THEN 1 END) AS occupied_rooms,
    COUNT(CASE WHEN rm.room_status = 'Available' THEN 1 END) AS available_rooms,
    (COUNT(CASE WHEN rm.room_status = 'Occupied' THEN 1 END) * 100.0 / COUNT(rm.room_id)) AS occupancy_rate
FROM rooms rm
JOIN room_types rt ON rm.room_type_id = rt.room_type_id
GROUP BY rt.room_type_name
ORDER BY occupancy_rate DESC;

-- 7. High-Value Guest Identification
SELECT 
    g.guest_id,
    g.guest_name,
    COUNT(r.reservation_id) AS total_stays,
    SUM(r.total_price) AS total_spend,
    AVG(r.total_price) AS avg_spend_per_stay,
    MAX(r.check_out_date) AS last_stay_date
FROM reservations r
JOIN guests g ON r.guest_id = g.guest_id
WHERE r.payment_status = 'Paid'
GROUP BY g.guest_id, g.guest_name
ORDER BY total_spend DESC
LIMIT 50;
```
