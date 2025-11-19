"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oliveiragomesadv.com.br
Prompt: Write a Java function that can analyze legal documents related to labor law, inspired by the services offered by Oliveira Gomes Advogados in the field of Direito Trabalhista.
Generated: DETERMINISTIC_85ca97c9eaeb00c7
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

/**
 * This class provides methods to analyze legal documents related to labor law.
 */
public class LaborLawDocumentAnalyzer {

    private static final String[] KEY_TERMS = {
        "contract", "termination", "employee", "employer", "rights", 
        "obligations", "compensation", "dispute", "collective", "negotiation"
    };

    /**
     * Analyzes the content of a legal document and counts the occurrences of relevant key terms.
     *
     * @param filePath the path to the legal document file
     * @return a map containing key terms and their respective counts
     * @throws IOException if an error occurs while reading the file
     */
    public Map<String, Integer> analyzeDocument(String filePath) throws IOException {
        // Initialize a map to store the count of key terms
        Map<String, Integer> termCounts = new HashMap<>();

        // Initialize the term counts to zero
        for (String term : KEY_TERMS) {
            termCounts.put(term, 0);
        }

        // Read the document
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                // Process each line for key term occurrences
                countKeyTerms(line.toLowerCase(), termCounts);
            }
        } catch (IOException e) {
            // Log the error and rethrow it for handling by the caller
            System.err.println("Error reading the document: " + e.getMessage());
            throw e;
        }

        return termCounts;
    }

    /**
     * Counts occurrences of key terms in a given line of text.
     *
     * @param line the line of text to analyze
     * @param termCounts the map to update with term counts
     */
    private void countKeyTerms(String line, Map<String, Integer> termCounts) {
        // Iterate over each key term and count its occurrences in the line
        for (String term : KEY_TERMS) {
            int count = line.split("\\b" + term + "\\b", -1).length - 1; // Use word boundary to count
            termCounts.put(term, termCounts.get(term) + count);
        }
    }

    /**
     * Main method to execute the document analysis.
     *
     * @param args command-line arguments (first argument should be the path to the document)
     */
    public static void main(String[] args) {
        if (args.length < 1) {
            System.err.println("Please provide a path to the legal document.");
            return;
        }

        LaborLawDocumentAnalyzer analyzer = new LaborLawDocumentAnalyzer();
        try {
            Map<String, Integer> results = analyzer.analyzeDocument(args[0]);
            // Output the results
            results.forEach((term, count) -> 
                System.out.println("Term: \"" + term + "\", Count: " + count));
        } catch (IOException e) {
            System.err.println("An error occurred during document analysis: " + e.getMessage());
        }
    }
}
```
