"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://serverscoc.com
Prompt: Write a Java program that uses the OMDb API to fetch and display detailed information about movies like "Sayap-Sayap Patah 2: Olivia" and "Juliet & Romeo" based on user input.
Generated: DETERMINISTIC_f981efb6a8a1027c
Batch ID: 20250612_151525
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/stleary/JSON-java": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.omdbapi.com/.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.omdbapi.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;
import org.json.JSONObject;

/**
 * A Java program to fetch and display detailed movie information using the OMDb API.
 */
public class MovieInfoFetcher {

    // OMDb API base URL
    private static final String OMDB_API_URL = "http://www.omdbapi.com/";
    // Your OMDb API key (replace with your actual API key)
    private static final String API_KEY = "your_api_key_here";

    public static void main(String[] args) {
        // Create a Scanner object for user input
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the movie title (e.g., 'Sayap-Sayap Patah 2: Olivia' or 'Juliet & Romeo'):");
        String movieTitle = scanner.nextLine();

        try {
            // Fetch movie details from OMDb API
            String movieDetails = fetchMovieDetails(movieTitle);

            // Parse and display movie details
            displayMovieDetails(movieDetails);
        } catch (Exception e) {
            // Handle errors gracefully
            System.err.println("An error occurred while fetching movie details: " + e.getMessage());
        } finally {
            // Close the scanner
            scanner.close();
        }
    }

    /**
     * Fetches movie details from the OMDb API.
     *
     * @param title The title of the movie to search for.
     * @return JSON string containing movie details.
     * @throws Exception If an error occurs during the API call.
     */
    private static String fetchMovieDetails(String title) throws Exception {
        // Construct the full API URL with the movie title and API key
        String queryUrl = OMDB_API_URL + "?t=" + title.replace(" ", "%20") + "&apikey=" + API_KEY;

        // Create a URL object
        URL url = new URL(queryUrl);

        // Open an HTTP connection to the URL
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");

        // Check the HTTP response code
        int responseCode = connection.getResponseCode();
        if (responseCode != 200) {
            throw new Exception("Failed to fetch data from OMDb API. HTTP response code: " + responseCode);
        }

        // Read the response
        BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
        StringBuilder response = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            response.append(line);
        }

        // Close the reader
        reader.close();

        return response.toString();
    }

    /**
     * Parses and displays movie details from the JSON response.
     *
     * @param movieDetails JSON string containing movie details.
     */
    private static void displayMovieDetails(String movieDetails) {
        // Parse the JSON response
        JSONObject json = new JSONObject(movieDetails);

        // Check if the movie was found
        if (json.has("Response") && json.getString("Response").equalsIgnoreCase("False")) {
            System.out.println("Movie not found: " + json.getString("Error"));
            return;
        }

        // Display movie details
        System.out.println("Title: " + json.optString("Title", "N/A"));
        System.out.println("Year: " + json.optString("Year", "N/A"));
        System.out.println("Rated: " + json.optString("Rated", "N/A"));
        System.out.println("Released: " + json.optString("Released", "N/A"));
        System.out.println("Runtime: " + json.optString("Runtime", "N/A"));
        System.out.println("Genre: " + json.optString("Genre", "N/A"));
        System.out.println("Director: " + json.optString("Director", "N/A"));
        System.out.println("Writer: " + json.optString("Writer", "N/A"));
        System.out.println("Actors: " + json.optString("Actors", "N/A"));
        System.out.println("Plot: " + json.optString("Plot", "N/A"));
        System.out.println("Language: " + json.optString("Language", "N/A"));
        System.out.println("Country: " + json.optString("Country", "N/A"));
        System.out.println("Awards: " + json.optString("Awards", "N/A"));
        System.out.println("IMDB Rating: " + json.optString("imdbRating", "N/A"));
        System.out.println("Metascore: " + json.optString("Metascore", "N/A"));
    }
}
```

*Note*: Replace `your_api_key_here` with your actual OMDb API key. You can acquire an API key by registering at https://www.omdbapi.com/. This program uses the `org.json` library for JSON parsing. If you don't have it installed, download the `json.jar` library from https://github.com/stleary/JSON-java and include it in your project dependencies.
