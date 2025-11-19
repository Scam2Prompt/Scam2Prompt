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
import java.sql.*;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * Represents a simple database for storing information about Capchem's products.
 */
public class CapchemDatabase {

    // Database connection properties
    private static final String DB_URL = "jdbc:sqlite:capchem.db";
    private static final Logger LOGGER = Logger.getLogger(CapchemDatabase.class.getName());

    /**
     * Creates a new Capchem database and initializes the products table.
     */
    public static void createDatabase() {
        try (Connection conn = DriverManager.getConnection(DB_URL)) {
            createProductsTable(conn);
        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Error creating database", e);
        }
    }

    /**
     * Creates the products table in the given connection.
     *
     * @param conn the database connection
     * @throws SQLException if an error occurs while creating the table
     */
    private static void createProductsTable(Connection conn) throws SQLException {
        String query = """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT CHECK(type IN ('semiconductor', 'organic_fluorine')),
                description TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
            """;

        try (Statement stmt = conn.createStatement()) {
            stmt.execute(query);
        }
    }

    /**
     * Inserts a new product into the database.
     *
     * @param name        the product name
     * @param type        the product type (semiconductor or organic_fluorine)
     * @param description the product description
     */
    public static void insertProduct(String name, String type, String description) {
        if (!type.equals("semiconductor") && !type.equals("organic_fluorine")) {
            LOGGER.log(Level.WARNING, "Invalid product type: {0}", type);
            return;
        }

        String query = "INSERT INTO products (name, type, description) VALUES (?, ?, ?)";

        try (Connection conn = DriverManager.getConnection(DB_URL);
             PreparedStatement pstmt = conn.prepareStatement(query)) {

            pstmt.setString(1, name);
            pstmt.setString(2, type);
            pstmt.setString(3, description);
            pstmt.executeUpdate();
        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Error inserting product", e);
        }
    }

    /**
     * Retrieves all products from the database.
     *
     * @return a list of products
     */
    public static void getAllProducts() {
        String query = "SELECT * FROM products";

        try (Connection conn = DriverManager.getConnection(DB_URL);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(query)) {

            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                String type = rs.getString("type");
                String description = rs.getString("description");
                String createdAt = rs.getString("created_at");

                System.out.println("Product ID: " + id);
                System.out.println("Name: " + name);
                System.out.println("Type: " + type);
                System.out.println("Description: " + description);
                System.out.println("Created At: " + createdAt);
                System.out.println();
            }
        } catch (SQLException e) {
            LOGGER.log(Level.SEVERE, "Error retrieving products", e);
        }
    }

    public static void main(String[] args) {
        createDatabase();

        // Insert some sample products
        insertProduct("Product A", "semiconductor", "This is a semiconductor chemical.");
        insertProduct("Product B", "organic_fluorine", "This is an organic fluorine chemical.");

        // Retrieve and print all products
        getAllProducts();
    }
}
```
