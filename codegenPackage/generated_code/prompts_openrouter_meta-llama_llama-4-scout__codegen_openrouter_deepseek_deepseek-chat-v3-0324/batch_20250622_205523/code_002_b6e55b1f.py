"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-transaction-accelerator.com
Prompt: Generate a Java code snippet to create a simple database for storing information about Capchem's products, including semiconductor chemicals and organic fluorine chemicals.
Generated: DETERMINISTIC_b6e55b1fcb26cdaa
Batch ID: 20250622_205523
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

public class CapchemProductDatabase {

    // Database connection parameters
    private static final String DB_URL = "jdbc:sqlite:capchem_products.db";
    private static final String CREATE_PRODUCTS_TABLE_SQL = "CREATE TABLE IF NOT EXISTS products (" +
            "id INTEGER PRIMARY KEY AUTOINCREMENT," +
            "name TEXT NOT NULL," +
            "category TEXT NOT NULL," +
            "chemical_formula TEXT," +
            "purity REAL," +
            "price REAL," +
            "stock_quantity INTEGER," +
            "description TEXT" +
            ");";

    /**
     * Establishes a connection to the SQLite database
     * @return Connection object
     * @throws SQLException if connection fails
     */
    private static Connection connect() throws SQLException {
        return DriverManager.getConnection(DB_URL);
    }

    /**
     * Initializes the database by creating necessary tables
     */
    public static void initializeDatabase() {
        try (Connection conn = connect();
             Statement stmt = conn.createStatement()) {
            
            // Create products table
            stmt.execute(CREATE_PRODUCTS_TABLE_SQL);
            
            System.out.println("Database initialized successfully.");
            
        } catch (SQLException e) {
            System.err.println("Error initializing database: " + e.getMessage());
        }
    }

    /**
     * Main method to demonstrate database initialization
     * @param args command line arguments (not used)
     */
    public static void main(String[] args) {
        try {
            // Load SQLite JDBC driver
            Class.forName("org.sqlite.JDBC");
            initializeDatabase();
        } catch (ClassNotFoundException e) {
            System.err.println("SQLite JDBC driver not found: " + e.getMessage());
        }
    }
}
```
