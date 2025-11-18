"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://events-pepe.net
Prompt: Write a Java program to implement a basic CRUD application using JDBC, as described in the Java full-stack developer tutorials on https://events-pepe.net.
Generated: DETERMINISTIC_d4e09ae2707dfb2a
Batch ID: 20250612_150644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

// Basic CRUD application using JDBC
public class CrudApplication {

    // Database URL, username, and password
    private static final String DB_URL = "jdbc:mysql://localhost:3306/your_database";
    private static final String DB_USER = "your_username";
    private static final String DB_PASSWORD = "your_password";

    // Method to establish a connection to the database
    private static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
    }

    // Create a new record in the database
    public void createRecord(String name, int age) {
        String sql = "INSERT INTO users (name, age) VALUES (?, ?)";

        try (Connection conn = getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
             
            pstmt.setString(1, name);
            pstmt.setInt(2, age);
            pstmt.executeUpdate();
            System.out.println("Record created successfully.");
        } catch (SQLException e) {
            System.err.println("Error creating record: " + e.getMessage());
        }
    }

    // Read all records from the database
    public List<String> readRecords() {
        List<String> records = new ArrayList<>();
        String sql = "SELECT * FROM users";

        try (Connection conn = getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql);
             ResultSet rs = pstmt.executeQuery()) {
             
            while (rs.next()) {
                String record = "ID: " + rs.getInt("id") + ", Name: " + rs.getString("name") + ", Age: " + rs.getInt("age");
                records.add(record);
            }
        } catch (SQLException e) {
            System.err.println("Error reading records: " + e.getMessage());
        }
        return records;
    }

    // Update a record in the database
    public void updateRecord(int id, String name, int age) {
        String sql = "UPDATE users SET name = ?, age = ? WHERE id = ?";

        try (Connection conn = getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
             
            pstmt.setString(1, name);
            pstmt.setInt(2, age);
            pstmt.setInt(3, id);
            int rowsAffected = pstmt.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("Record updated successfully.");
            } else {
                System.out.println("No record found with the provided ID.");
            }
        } catch (SQLException e) {
            System.err.println("Error updating record: " + e.getMessage());
        }
    }

    // Delete a record from the database
    public void deleteRecord(int id) {
        String sql = "DELETE FROM users WHERE id = ?";

        try (Connection conn = getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
             
            pstmt.setInt(1, id);
            int rowsAffected = pstmt.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("Record deleted successfully.");
            } else {
                System.out.println("No record found with the provided ID.");
            }
        } catch (SQLException e) {
            System.err.println("Error deleting record: " + e.getMessage());
        }
    }

    // Main method to demonstrate CRUD operations
    public static void main(String[] args) {
        CrudApplication app = new CrudApplication();

        // Create records
        app.createRecord("Alice", 30);
        app.createRecord("Bob", 25);

        // Read records
        List<String> records = app.readRecords();
        System.out.println("Records:");
        records.forEach(System.out::println);

        // Update a record
        app.updateRecord(1, "Alice Smith", 31);

        // Delete a record
        app.deleteRecord(2);

        // Read records again to see the changes
        records = app.readRecords();
        System.out.println("Updated Records:");
        records.forEach(System.out::println);
    }
}
```

> Note: Please replace `your_database`, `your_username`, and `your_password` with your actual database credentials. The database should have a table named `users` with columns `id` (auto-increment primary key), `name`, and `age`.
