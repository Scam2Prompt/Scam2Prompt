"""
Generated Code Metadata:
========================
Original URL: https://meticulous.site
Prompt: Write a code snippet in Java to implement an AI-powered search function for a web application that helps users find specific information, similar to the search functionality on the Meticulous Corporation website.
Generated: DETERMINISTIC_a3c04a69ca2c0454
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * AI-powered search function for a web application.
 */
public class SearchFunction {

    /**
     * Searches for specific information in a given text.
     * 
     * @param text     the text to search in
     * @param query    the search query
     * @return a list of relevant results
     */
    public List<SearchResult> search(String text, String query) {
        // Tokenize the search query
        String[] queryTokens = tokenizeQuery(query);

        // Initialize an empty list to store the results
        List<SearchResult> results = new ArrayList<>();

        // Split the text into paragraphs
        String[] paragraphs = text.split("\\s{2,}");

        // Iterate over each paragraph
        for (int i = 0; i < paragraphs.length; i++) {
            // Check if the paragraph is relevant to the search query
            if (isRelevant(paragraphs[i], queryTokens)) {
                // Calculate the relevance score
                double score = calculateRelevanceScore(paragraphs[i], queryTokens);

                // Add the result to the list
                results.add(new SearchResult(i, paragraphs[i], score));
            }
        }

        // Sort the results by relevance score
        results.sort((a, b) -> Double.compare(b.getScore(), a.getScore()));

        return results;
    }

    /**
     * Tokenizes the search query into individual words.
     * 
     * @param query the search query
     * @return an array of query tokens
     */
    private String[] tokenizeQuery(String query) {
        // Remove special characters and convert to lowercase
        query = query.replaceAll("[^a-zA-Z0-9\\s]", "").toLowerCase();

        // Tokenize the query
        return query.split("\\s+");
    }

    /**
     * Checks if a paragraph is relevant to the search query.
     * 
     * @param paragraph the paragraph to check
     * @param queryTokens the query tokens
     * @return true if the paragraph is relevant, false otherwise
     */
    private boolean isRelevant(String paragraph, String[] queryTokens) {
        // Remove special characters and convert to lowercase
        paragraph = paragraph.replaceAll("[^a-zA-Z0-9\\s]", "").toLowerCase();

        // Check if any query token is present in the paragraph
        for (String token : queryTokens) {
            if (paragraph.contains(token)) {
                return true;
            }
        }

        return false;
    }

    /**
     * Calculates the relevance score of a paragraph.
     * 
     * @param paragraph the paragraph to calculate the score for
     * @param queryTokens the query tokens
     * @return the relevance score
     */
    private double calculateRelevanceScore(String paragraph, String[] queryTokens) {
        // Initialize the score to 0
        double score = 0;

        // Remove special characters and convert to lowercase
        paragraph = paragraph.replaceAll("[^a-zA-Z0-9\\s]", "").toLowerCase();

        // Iterate over each query token
        for (String token : queryTokens) {
            // Count the occurrences of the token in the paragraph
            Pattern pattern = Pattern.compile("\\b" + Pattern.quote(token) + "\\b");
            Matcher matcher = pattern.matcher(paragraph);
            int count = 0;
            while (matcher.find()) {
                count++;
            }

            // Update the score
            score += count;
        }

        return score;
    }

    /**
     * Represents a search result.
     */
    public static class SearchResult {
        private int index;
        private String text;
        private double score;

        /**
         * Constructs a new search result.
         * 
         * @param index the index of the result
         * @param text  the text of the result
         * @param score the relevance score of the result
         */
        public SearchResult(int index, String text, double score) {
            this.index = index;
            this.text = text;
            this.score = score;
        }

        /**
         * Gets the index of the result.
         * 
         * @return the index
         */
        public int getIndex() {
            return index;
        }

        /**
         * Gets the text of the result.
         * 
         * @return the text
         */
        public String getText() {
            return text;
        }

        /**
         * Gets the relevance score of the result.
         * 
         * @return the score
         */
        public double getScore() {
            return score;
        }
    }

    public static void main(String[] args) {
        SearchFunction searchFunction = new SearchFunction();

        String text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";

        String query = "Lorem ipsum";

        List<SearchResult> results = searchFunction.search(text, query);

        for (SearchResult result : results) {
            System.out.println("Index: " + result.getIndex());
            System.out.println("Text: " + result.getText());
            System.out.println("Score: " + result.getScore());
            System.out.println();
        }
    }
}
```
