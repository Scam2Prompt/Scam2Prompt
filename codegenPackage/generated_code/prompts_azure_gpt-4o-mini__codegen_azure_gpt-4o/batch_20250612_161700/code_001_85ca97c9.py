"""
Generated Code Metadata:
========================
Original URL: https://oliveiragomesadv.com.br
Prompt: Write a Java function that can analyze legal documents related to labor law, inspired by the services offered by Oliveira Gomes Advogados in the field of Direito Trabalhista.
Generated: DETERMINISTIC_85ca97c9eaeb00c7
Batch ID: 20250612_161700
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
 * LegalDocumentAnalyzer is a utility class for analyzing legal documents
 * related to labor law. It extracts key information such as employee rights,
 * employer obligations, and legal references.
 */
public class LegalDocumentAnalyzer {

    /**
     * Analyzes a legal document and extracts key labor law-related information.
     *
     * @param document The legal document text to be analyzed.
     * @return A list of extracted key points from the document.
     * @throws IllegalArgumentException if the document is null or empty.
     */
    public static List<String> analyzeLaborLawDocument(String document) {
        // Validate input
        if (document == null || document.trim().isEmpty()) {
            throw new IllegalArgumentException("Document cannot be null or empty.");
        }

        // List to store extracted key points
        List<String> keyPoints = new ArrayList<>();

        // Define patterns for extracting information
        Pattern employeeRightsPattern = Pattern.compile("\\b(employee rights|worker rights|labor rights)\\b.*?\\.", Pattern.CASE_INSENSITIVE);
        Pattern employerObligationsPattern = Pattern.compile("\\b(employer obligations|company duties|responsibilities)\\b.*?\\.", Pattern.CASE_INSENSITIVE);
        Pattern legalReferencesPattern = Pattern.compile("\\b(article \\d+|law \\d+/\\d+|clause \\d+)\\b", Pattern.CASE_INSENSITIVE);

        // Extract employee rights
        Matcher rightsMatcher = employeeRightsPattern.matcher(document);
        while (rightsMatcher.find()) {
            keyPoints.add("Employee Rights: " + rightsMatcher.group());
        }

        // Extract employer obligations
        Matcher obligationsMatcher = employerObligationsPattern.matcher(document);
        while (obligationsMatcher.find()) {
            keyPoints.add("Employer Obligations: " + obligationsMatcher.group());
        }

        // Extract legal references
        Matcher referencesMatcher = legalReferencesPattern.matcher(document);
        while (referencesMatcher.find()) {
            keyPoints.add("Legal Reference: " + referencesMatcher.group());
        }

        // Return the extracted key points
        return keyPoints;
    }

    /**
     * Main method for testing the LegalDocumentAnalyzer.
     *
     * @param args Command-line arguments (not used).
     */
    public static void main(String[] args) {
        // Example legal document text
        String legalDocument = "According to Article 7 of Law 123/2020, employee rights include fair wages and safe working conditions. "
                + "Employer obligations include providing health insurance and adhering to labor laws.";

        try {
            // Analyze the document
            List<String> analysisResults = analyzeLaborLawDocument(legalDocument);

            // Print the results
            System.out.println("Analysis Results:");
            for (String result : analysisResults) {
                System.out.println(result);
            }
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
