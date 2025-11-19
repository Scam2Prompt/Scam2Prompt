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
import java.sql.*;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * A simple database for storing information about recyclable materials.
 */
public class RecyclableMaterialsDatabase {

    // Database connection properties
    private static final String DB_URL = "jdbc:sqlite:recyclable_materials.db";
    private static final String CREATE_TABLE_QUERY = """
            CREATE TABLE IF NOT EXISTS materials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                weight REAL NOT NULL,
                is_recyclable INTEGER NOT NULL
            );
            """;

    private Connection connection;

    /**
     * Establishes a connection to the database.
     *
     * @throws SQLException if a database access error occurs
     */
    public RecyclableMaterialsDatabase() throws SQLException {
        connection = DriverManager.getConnection(DB_URL);
        createTable();
    }

    /**
     * Creates the materials table if it does not exist.
     *
     * @throws SQLException if a database access error occurs
     */
    private void createTable() throws SQLException {
        try (Statement statement = connection.createStatement()) {
            statement.execute(CREATE_TABLE_QUERY);
        }
    }

    /**
     * Inserts a new recyclable material into the database.
     *
     * @param name           the name of the material
     * @param type           the type of the material
     * @param weight         the weight of the material
     * @param isRecyclable   whether the material is recyclable
     * @throws SQLException if a database access error occurs
     */
    public void insertMaterial(String name, String type, double weight, boolean isRecyclable) throws SQLException {
        String insertQuery = "INSERT INTO materials (name, type, weight, is_recyclable) VALUES (?, ?, ?, ?)";
        try (PreparedStatement statement = connection.prepareStatement(insertQuery)) {
            statement.setString(1, name);
            statement.setString(2, type);
            statement.setDouble(3, weight);
            statement.setInt(4, isRecyclable ? 1 : 0);
            statement.executeUpdate();
        }
    }

    /**
     * Retrieves all recyclable materials from the database.
     *
     * @return a result set containing all recyclable materials
     * @throws SQLException if a database access error occurs
     */
    public ResultSet getAllRecyclableMaterials() throws SQLException {
        String query = "SELECT * FROM materials WHERE is_recyclable = 1";
        try (Statement statement = connection.createStatement()) {
            return statement.executeQuery(query);
        }
    }

    /**
     * Retrieves all materials from the database.
     *
     * @return a result set containing all materials
     * @throws SQLException if a database access error occurs
     */
    public ResultSet getAllMaterials() throws SQLException {
        String query = "SELECT * FROM materials";
        try (Statement statement = connection.createStatement()) {
            return statement.executeQuery(query);
        }
    }

    /**
     * Closes the database connection.
     *
     * @throws SQLException if a database access error occurs
     */
    public void close() throws SQLException {
        connection.close();
    }

    public static void main(String[] args) {
        try (RecyclableMaterialsDatabase db = new RecyclableMaterialsDatabase()) {
            db.insertMaterial("Paper", "Cardboard", 0.5, true);
            db.insertMaterial("Glass", "Bottle", 1.0, true);
            db.insertMaterial("Plastic", "Bag", 0.2, false);

            try (ResultSet recyclableMaterials = db.getAllRecyclableMaterials()) {
                System.out.println("Recyclable Materials:");
                while (recyclableMaterials.next()) {
                    System.out.println(recyclableMaterials.getString("name") + " - " + recyclableMaterials.getString("type"));
                }
            }

            try (ResultSet allMaterials = db.getAllMaterials()) {
                System.out.println("\nAll Materials:");
                while (allMaterials.next()) {
                    System.out.println(allMaterials.getString("name") + " - " + allMaterials.getString("type"));
                }
            }
        } catch (SQLException ex) {
            Logger.getLogger(RecyclableMaterialsDatabase.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
```
