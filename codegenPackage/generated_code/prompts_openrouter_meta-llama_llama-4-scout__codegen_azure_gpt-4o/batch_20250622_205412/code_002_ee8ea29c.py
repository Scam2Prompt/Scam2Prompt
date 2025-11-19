"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Generate a code snippet in Java to create a collaborative platform for AFCO regional members to share and validate documents and tools for safety and health coordination.
Generated: DETERMINISTIC_ee8ea29c44c92c68
Batch ID: 20250622_205412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * CollaborativePlatform class to manage document and tool sharing
 * for AFCO regional members with validation functionality.
 */
public class CollaborativePlatform {

    // Map to store documents and tools shared by members
    private Map<String, List<Document>> sharedResources;

    // Constructor to initialize the platform
    public CollaborativePlatform() {
        sharedResources = new HashMap<>();
    }

    /**
     * Method to share a document or tool.
     *
     * @param memberName Name of the member sharing the resource.
     * @param document   Document or tool to be shared.
     */
    public void shareResource(String memberName, Document document) {
        if (memberName == null || memberName.isEmpty() || document == null) {
            throw new IllegalArgumentException("Member name and document cannot be null or empty.");
        }

        sharedResources.putIfAbsent(memberName, new ArrayList<>());
        sharedResources.get(memberName).add(document);
        System.out.println("Resource shared successfully by " + memberName);
    }

    /**
     * Method to validate a document or tool.
     *
     * @param document Document or tool to be validated.
     * @return true if the document is valid, false otherwise.
     */
    public boolean validateResource(Document document) {
        if (document == null) {
            throw new IllegalArgumentException("Document cannot be null.");
        }

        // Example validation logic: Check if the document has a title and content
        boolean isValid = document.getTitle() != null && !document.getTitle().isEmpty()
                && document.getContent() != null && !document.getContent().isEmpty();

        if (isValid) {
            System.out.println("Document validated successfully.");
        } else {
            System.out.println("Document validation failed.");
        }

        return isValid;
    }

    /**
     * Method to display all shared resources.
     */
    public void displaySharedResources() {
        System.out.println("Shared Resources:");
        for (Map.Entry<String, List<Document>> entry : sharedResources.entrySet()) {
            System.out.println("Member: " + entry.getKey());
            for (Document doc : entry.getValue()) {
                System.out.println(" - " + doc);
            }
        }
    }

    /**
     * Main method to demonstrate the functionality of the platform.
     */
    public static void main(String[] args) {
        CollaborativePlatform platform = new CollaborativePlatform();

        // Create sample documents
        Document doc1 = new Document("Safety Guidelines", "Content of safety guidelines.");
        Document doc2 = new Document("Health Coordination Plan", "Content of health coordination plan.");

        // Share resources
        platform.shareResource("Alice", doc1);
        platform.shareResource("Bob", doc2);

        // Validate resources
        platform.validateResource(doc1);
        platform.validateResource(doc2);

        // Display shared resources
        platform.displaySharedResources();
    }
}

/**
 * Document class to represent a document or tool.
 */
class Document {
    private String title;
    private String content;

    // Constructor
    public Document(String title, String content) {
        this.title = title;
        this.content = content;
    }

    // Getters
    public String getTitle() {
        return title;
    }

    public String getContent() {
        return content;
    }

    // Override toString for better display
    @Override
    public String toString() {
        return "Document{title='" + title + "', content='" + content + "'}";
    }
}
```
