"""
Generated Code Metadata:
========================
Original URL: https://screciclados.mx
Prompt: "Generate a code snippet in Java to create a simple database for storing information about recyclable materials, inspired by the services provided by SCR Reciclados."
Generated: DETERMINISTIC_d5bee7362d5f0bb0
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class RecyclableMaterialsDatabase {

    // JDBC URL, username, and password for the database
    private static final String DB_URL = "jdbc:sqlite:recyclable_materials.db"; // SQLite database file
    private static final String DB_USERNAME = ""; // Not required for SQLite
    private static final String DB_PASSWORD = ""; // Not required for SQLite

    public static void main(String[] args) {
        try {
            // Create the database and table
            createDatabase();
            System.out.println("Database and table created successfully.");
        } catch (SQLException e) {
            System.err.println("Error creating database or table: " + e.getMessage());
        }
    }

    /**
     * Creates the database and the "materials" table.
     *
     * @throws SQLException if a database error occurs
     */
    private static void createDatabase() throws SQLException {
        // Establish a connection to the database
        try (Connection connection = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD)) {
            // SQL statement to create the "materials" table
            String createTableSQL = "CREATE TABLE IF NOT EXISTS materials (" +
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                    "name TEXT NOT NULL, " +
                    "type TEXT NOT NULL, " +
                    "description TEXT, " +
                    "recyclable BOOLEAN NOT NULL" +
                    ");";

            // Execute the SQL statement
            try (PreparedStatement preparedStatement = connection.prepareStatement(createTableSQL)) {
                preparedStatement.execute();
            }
        }
    }
}
```
