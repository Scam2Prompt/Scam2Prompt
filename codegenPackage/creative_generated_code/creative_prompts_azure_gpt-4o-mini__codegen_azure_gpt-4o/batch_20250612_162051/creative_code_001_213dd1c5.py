"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.getaconsulenze.it
Prompt: Write a Java program that integrates with the Geta Consulenze API to retrieve information about available courses in Sicurezza sul lavoro (work safety).
Generated: DETERMINISTIC_213dd1c5d6b6efaf
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.getaconsulenze.com": {
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
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import org.json.JSONArray;
import org.json.JSONObject;

/**
 * A program to retrieve information about available courses in work safety
 * from the Geta Consulenze API.
 */
public class WorkSafetyCoursesApp {

    // Base URL for the Geta Consulenze API
    private static final String API_BASE_URL = "https://api.getaconsulenze.com";

    // Endpoint for retrieving course information
    private static final String COURSES_ENDPOINT = "/courses";

    // API Key for authentication (replace with your actual API key)
    private static final String API_KEY = "your_api_key_here";

    public static void main(String[] args) {
        try {
            // Retrieve available courses from the API
            JSONArray courses = fetchWorkSafetyCourses();

            // Print the retrieved courses to the console
            System.out.println("Available Work Safety Courses:");
            for (int i = 0; i < courses.length(); i++) {
                JSONObject course = courses.getJSONObject(i);
                System.out.println("- " + course.getString("name") + " (Duration: " + course.getInt("duration") + " hours)");
            }
        } catch (Exception e) {
            // Handle any exceptions that occur during the API call
            System.err.println("Error occurred while retrieving courses: " + e.getMessage());
            e.printStackTrace();
        }
    }

    /**
     * Fetches available work safety courses from the Geta Consulenze API.
     *
     * @return A JSONArray containing the details of the courses.
     * @throws Exception If an error occurs during the API call.
     */
    private static JSONArray fetchWorkSafetyCourses() throws Exception {
        // Construct the full URL for the API request
        URL url = new URL(API_BASE_URL + COURSES_ENDPOINT + "?category=Sicurezza sul lavoro");

        // Create an HTTP connection to the API
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");
        connection.setRequestProperty("Authorization", "Bearer " + API_KEY);
        connection.setRequestProperty("Content-Type", "application/json");

        // Check the HTTP response code
        int responseCode = connection.getResponseCode();
        if (responseCode != HttpURLConnection.HTTP_OK) {
            throw new Exception("API request failed with response code: " + responseCode);
        }

        // Read the response from the API
        BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
        StringBuilder responseBuilder = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            responseBuilder.append(line);
        }
        reader.close();

        // Parse the response JSON and return the courses array
        JSONObject responseJson = new JSONObject(responseBuilder.toString());
        return responseJson.getJSONArray("courses");
    }
}
```

### Notes on running the code:
- Replace `your_api_key_here` with a valid API key for the Geta Consulenze API.
- Make sure the API's URL and expected JSON structure are correct and up-to-date.
- You might need to include `org.json` library in your project for JSON parsing. You can add it using Maven:
```xml
<dependency>
    <groupId>org.json</groupId>
    <artifactId>json</artifactId>
    <version>20210307</version>
</dependency>
```
