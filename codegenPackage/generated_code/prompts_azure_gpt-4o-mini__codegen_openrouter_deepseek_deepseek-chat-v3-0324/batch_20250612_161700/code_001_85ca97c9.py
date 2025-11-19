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
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * A class for analyzing legal documents related to labor law.
 * Inspired by Oliveira Gomes Advogados' services in Direito Trabalhista.
 */
public class LaborLawAnalyzer {

    // Common labor law keywords and phrases in Portuguese
    private static final String[] LABOR_LAW_KEYWORDS = {
        "CLT", "Consolidação das Leis do Trabalho", "direitos trabalhistas",
        "rescisão", "demissão", "justa causa", "aviso prévio",
        "FGTS", "férias", "13º salário", "hora extra",
        "acordo coletivo", "convenção coletiva", "dissídio coletivo",
        "jornada de trabalho", "adicional noturno", "periculosidade",
        "insalubridade", "estabilidade", "danos morais"
    };

    /**
     * Analyzes a legal document for labor law content.
     * @param filePath Path to the document file
     * @return Map containing analysis results (keyword counts and statistics)
     * @throws IOException If there's an error reading the file
     */
    public static Map<String, Object> analyzeLaborDocument(String filePath) throws IOException {
        Map<String, Integer> keywordCounts = new HashMap<>();
        int totalKeywords = 0;
        int totalSections = 0;
        int totalArticles = 0;

        // Initialize keyword counts
        for (String keyword : LABOR_LAW_KEYWORDS) {
            keywordCounts.put(keyword, 0);
        }

        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                // Count keywords
                for (String keyword : LABOR_LAW_KEYWORDS) {
                    Pattern pattern = Pattern.compile("\\b" + Pattern.quote(keyword) + "\\b", Pattern.CASE_INSENSITIVE);
                    Matcher matcher = pattern.matcher(line);
                    while (matcher.find()) {
                        keywordCounts.put(keyword, keywordCounts.get(keyword) + 1);
                        totalKeywords++;
                    }
                }

                // Count legal sections (assuming standard formatting)
                if (line.matches("(?i)^(seção|capítulo)\\s+[IVXLCDM]+.*")) {
                    totalSections++;
                }

                // Count articles (common in Brazilian legal documents)
                if (line.matches("(?i)^art\\.?\\s+\\d+.*")) {
                    totalArticles++;
                }
            }
        }

        // Prepare results
        Map<String, Object> results = new HashMap<>();
        results.put("keywordCounts", keywordCounts);
        results.put("totalKeywords", totalKeywords);
        results.put("totalSections", totalSections);
        results.put("totalArticles", totalArticles);
        results.put("relevanceScore", calculateRelevanceScore(totalKeywords, totalSections, totalArticles));

        return results;
    }

    /**
     * Calculates a relevance score for labor law content.
     * @param keywords Total keyword occurrences
     * @param sections Number of sections
     * @param articles Number of articles
     * @return Calculated relevance score (0-100)
     */
    private static int calculateRelevanceScore(int keywords, int sections, int articles) {
        if (sections == 0 && articles == 0) return 0;
        
        double score = (keywords * 0.6) + (sections * 0.2) + (articles * 0.2);
        return (int) Math.min(100, score);
    }

    /**
     * Generates a summary report from the analysis results.
     * @param analysisResults Results from analyzeLaborDocument
     * @return Formatted summary string
     */
    public static String generateSummaryReport(Map<String, Object> analysisResults) {
        StringBuilder report = new StringBuilder();
        report.append("Labor Law Document Analysis Report\n");
        report.append("=================================\n\n");
        
        report.append(String.format("Total Labor Law Keywords Found: %d%n", 
            analysisResults.get("totalKeywords")));
        report.append(String.format("Document Sections: %d%n", 
            analysisResults.get("totalSections")));
        report.append(String.format("Legal Articles: %d%n", 
            analysisResults.get("totalArticles")));
        report.append(String.format("Labor Law Relevance Score: %d/100%n%n", 
            analysisResults.get("relevanceScore")));
        
        report.append("Keyword Frequency:\n");
        report.append("-----------------\n");
        
        @SuppressWarnings("unchecked")
        Map<String, Integer> keywordCounts = (Map<String, Integer>) analysisResults.get("keywordCounts");
        for (Map.Entry<String, Integer> entry : keywordCounts.entrySet()) {
            if (entry.getValue() > 0) {
                report.append(String.format("%-25s: %d%n", entry.getKey(), entry.getValue()));
            }
        }
        
        return report.toString();
    }
}
```
