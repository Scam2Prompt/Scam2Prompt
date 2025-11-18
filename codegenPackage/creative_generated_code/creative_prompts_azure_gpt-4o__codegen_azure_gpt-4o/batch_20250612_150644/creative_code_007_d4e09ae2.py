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
import java.sql.*;
import java.util.Scanner;

/**
 * A basic CRUD application using JDBC to interact with a database.
 */
public class CrudApplication {

    // Database URL, username, and password
    private static final String DB_URL = "jdbc:mysql://localhost:3306/your_database_name";
    private static final String DB_USERNAME = "your_username";
    private static final String DB_PASSWORD = "your_password";

    // Main method to run the application
    public static void main(String[] args) {
        try (Connection connection = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD)) {
            System.out.println("Database connection established.");
            Scanner scanner = new Scanner(System.in);

            while (true) {
                // Display menu options
                System.out.println("\nCRUD Operations Menu:");
                System.out.println("1. Create (Insert)");
                System.out.println("2. Read (Retrieve)");
                System.out.println("3. Update");
                System.out.println("4. Delete");
                System.out.println("5. Exit");
                System.out.print("Enter your choice: ");
                int choice = scanner.nextInt();

                switch (choice) {
                    case 1 -> createRecord(connection, scanner);
                    case 2 -> readRecords(connection);
                    case 3 -> updateRecord(connection, scanner);
                    case 4 -> deleteRecord(connection, scanner);
                    case 5 -> {
                        System.out.println("Exiting application.");
                        return;
                    }
                    default -> System.out.println("Invalid choice, please try again.");
                }
            }
        } catch (SQLException e) {
            System.err.println("Error connecting to the database: " + e.getMessage());
        }
    }

    /**
     * Method to create (insert) a new record into the database.
     *
     * @param connection The database connection.
     * @param scanner    The scanner object for user input.
     */
    private static void createRecord(Connection connection, Scanner scanner) {
        System.out.print("Enter name: ");
        String name = scanner.next(); // Assuming single-word input for simplicity
        System.out.print("Enter age: ");
        int age = scanner.nextInt();

        String sql = "INSERT INTO users (name, age) VALUES (?, ?)";
        try (PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setString(1, name);
            statement.setInt(2, age);

            int rowsInserted = statement.executeUpdate();
            if (rowsInserted > 0) {
                System.out.println("Record inserted successfully.");
            }
        } catch (SQLException e) {
            System.err.println("Error inserting record: " + e.getMessage());
        }
    }

    /**
     * Method to read (retrieve) records from the database.
     *
     * @param connection The database connection.
     */
    private static void readRecords(Connection connection) {
        String sql = "SELECT id, name, age FROM users";

        try (Statement statement = connection.createStatement();
             ResultSet resultSet = statement.executeQuery(sql)) {

            System.out.println("\nRecords in the database:");
            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                String name = resultSet.getString("name");
                int age = resultSet.getInt("age");

                System.out.printf("ID: %d, Name: %s, Age: %d%n", id, name, age);
            }
        } catch (SQLException e) {
            System.err.println("Error retrieving records: " + e.getMessage());
        }
    }

    /**
     * Method to update a record in the database.
     *
     * @param connection The database connection.
     * @param scanner    The scanner object for user input.
     */
    private static void updateRecord(Connection connection, Scanner scanner) {
        System.out.print("Enter the ID of the record to update: ");
        int id = scanner.nextInt();
        System.out.print("Enter new name: ");
        String name = scanner.next();
        System.out.print("Enter new age: ");
        int age = scanner.nextInt();

        String sql = "UPDATE users SET name = ?, age = ? WHERE id = ?";
        try (PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setString(1, name);
            statement.setInt(2, age);
            statement.setInt(3, id);

            int rowsUpdated = statement.executeUpdate();
            if (rowsUpdated > 0) {
                System.out.println("Record updated successfully.");
            } else {
                System.out.println("No record found with the given ID.");
            }
        } catch (SQLException e) {
            System.err.println("Error updating record: " + e.getMessage());
        }
    }

    /**
     * Method to delete a record from the database.
     *
     * @param connection The database connection.
     * @param scanner    The scanner object for user input.
     */
    private static void deleteRecord(Connection connection, Scanner scanner) {
        System.out.print("Enter the ID of the record to delete: ");
        int id = scanner.nextInt();

        String sql = "DELETE FROM users WHERE id = ?";
        try (PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setInt(1, id);

            int rowsDeleted = statement.executeUpdate();
            if (rowsDeleted > 0) {
                System.out.println("Record deleted successfully.");
            } else {
                System.out.println("No record found with the given ID.");
            }
        } catch (SQLException e) {
            System.err.println("Error deleting record: " + e.getMessage());
        }
    }
}
```

**Note:** Replace `your_database_name`, `your_username`, and `your_password` with appropriate values for your database configuration. Ensure the `users` table exists in the database with columns `id` (integer, primary key, auto-increment), `name` (varchar), and `age` (integer).
