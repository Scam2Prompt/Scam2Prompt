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
import java.sql.SQLException;
import java.sql.Statement;

/**
 * A simple database setup for storing information about recyclable materials.
 * Inspired by SCR Reciclados services.
 */
public class RecyclableMaterialsDatabase {

    // Database connection parameters
    private static final String DB_URL = "jdbc:sqlite:recyclable_materials.db";
    
    /**
     * Establishes a connection to the SQLite database.
     * @return Connection object
     * @throws SQLException if connection fails
     */
    private static Connection connect() throws SQLException {
        return DriverManager.getConnection(DB_URL);
    }

    /**
     * Creates the database tables for storing recyclable materials information.
     */
    public static void createDatabase() {
        // SQL statement for creating materials table
        String sqlCreateMaterialsTable = "CREATE TABLE IF NOT EXISTS materials (\n"
                + " id INTEGER PRIMARY KEY AUTOINCREMENT,\n"
                + " name TEXT NOT NULL,\n"
                + " category TEXT NOT NULL,\n"
                + " price_per_kg REAL,\n"
                + " description TEXT,\n"
                + " collection_center TEXT\n"
                + ");";

        // SQL statement for creating transactions table
        String sqlCreateTransactionsTable = "CREATE TABLE IF NOT EXISTS transactions (\n"
                + " id INTEGER PRIMARY KEY AUTOINCREMENT,\n"
                + " material_id INTEGER,\n"
                + " quantity REAL,\n"
                + " transaction_date TEXT,\n"
                + " client_id INTEGER,\n"
                + " FOREIGN KEY (material_id) REFERENCES materials(id)\n"
                + ");";

        try (Connection conn = connect();
             Statement stmt = conn.createStatement()) {
            
            // Create tables
            stmt.execute(sqlCreateMaterialsTable);
            stmt.execute(sqlCreateTransactionsTable);
            
            System.out.println("Database tables created successfully.");
            
        } catch (SQLException e) {
            System.err.println("Error creating database tables: " + e.getMessage());
        }
    }

    /**
     * Main method to demonstrate database creation.
     * @param args command line arguments (not used)
     */
    public static void main(String[] args) {
        createDatabase();
    }
}
```
