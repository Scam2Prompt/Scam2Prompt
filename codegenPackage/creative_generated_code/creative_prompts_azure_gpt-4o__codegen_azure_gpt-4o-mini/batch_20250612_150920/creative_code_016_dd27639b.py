"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edukacija.net
Prompt: Develop a Java program for database connectivity using Oracle 11g, referencing the training content available on edukacija.net.
Generated: DETERMINISTIC_dd27639b289d468c
Batch ID: 20250612_150920
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

/**
 * DatabaseConnector is a utility class for connecting to an Oracle 11g database.
 * It provides methods to establish a connection and execute queries.
 */
public class DatabaseConnector {

    // JDBC URL, username, and password for connecting to the database
    private static final String DB_URL = "jdbc:oracle:thin:@localhost:1521:orcl"; // Update with your DB URL
    private static final String USER = "your_username"; // Update with your DB username
    private static final String PASSWORD = "your_password"; // Update with your DB password

    /**
     * Establishes a connection to the Oracle database.
     * 
     * @return Connection object if successful, null if failed
     */
    public static Connection connect() {
        Connection connection = null;
        try {
            // Load Oracle JDBC Driver
            Class.forName("oracle.jdbc.driver.OracleDriver");
            // Establish connection to the database
            connection = DriverManager.getConnection(DB_URL, USER, PASSWORD);
            System.out.println("Connection to the database established successfully.");
        } catch (ClassNotFoundException e) {
            System.err.println("Oracle JDBC Driver not found. Include it in your library path.");
            e.printStackTrace();
        } catch (SQLException e) {
            System.err.println("Connection to the database failed. Check your database URL, username, and password.");
            e.printStackTrace();
        }
        return connection;
    }

    /**
     * Executes a SELECT query and prints the results.
     * 
     * @param query The SQL query to execute
     */
    public static void executeQuery(String query) {
        try (Connection connection = connect();
             PreparedStatement preparedStatement = connection.prepareStatement(query);
             ResultSet resultSet = preparedStatement.executeQuery()) {

            // Process the result set
            while (resultSet.next()) {
                // Assuming the first column is a string for demonstration
                String result = resultSet.getString(1);
                System.out.println("Query Result: " + result);
            }

        } catch (SQLException e) {
            System.err.println("Error executing query: " + e.getMessage());
            e.printStackTrace();
        }
    }

    /**
     * Main method to demonstrate database connectivity.
     * 
     * @param args Command line arguments
     */
    public static void main(String[] args) {
        // Example query to retrieve data from a table named 'employees'
        String query = "SELECT first_name FROM employees"; // Update with your actual query
        executeQuery(query);
    }
}
```

Make sure to replace `your_username`, `your_password`, and the database URL in the `DB_URL` constant with the actual credentials and connection string for your Oracle 11g database. Also, ensure that the Oracle JDBC driver is included in your project's classpath.
