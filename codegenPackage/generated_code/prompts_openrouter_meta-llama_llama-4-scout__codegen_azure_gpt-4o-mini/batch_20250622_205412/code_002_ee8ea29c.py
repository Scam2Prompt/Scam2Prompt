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
import java.util.List;
import java.util.Optional;

// Document class to represent a shared document
class Document {
    private String title;
    private String content;
    private String owner;

    public Document(String title, String content, String owner) {
        this.title = title;
        this.content = content;
        this.owner = owner;
    }

    public String getTitle() {
        return title;
    }

    public String getContent() {
        return content;
    }

    public String getOwner() {
        return owner;
    }

    @Override
    public String toString() {
        return "Document{" +
                "title='" + title + '\'' +
                ", owner='" + owner + '\'' +
                '}';
    }
}

// CollaborativePlatform class to manage documents
class CollaborativePlatform {
    private List<Document> documents;

    public CollaborativePlatform() {
        this.documents = new ArrayList<>();
    }

    // Method to add a document to the platform
    public void addDocument(String title, String content, String owner) {
        if (title == null || title.isEmpty() || content == null || content.isEmpty() || owner == null || owner.isEmpty()) {
            throw new IllegalArgumentException("Title, content, and owner must not be empty.");
        }
        Document document = new Document(title, content, owner);
        documents.add(document);
        System.out.println("Document added: " + document);
    }

    // Method to retrieve a document by title
    public Optional<Document> getDocument(String title) {
        return documents.stream()
                .filter(doc -> doc.getTitle().equalsIgnoreCase(title))
                .findFirst();
    }

    // Method to validate a document's content
    public boolean validateDocument(String title) {
        Optional<Document> document = getDocument(title);
        if (document.isPresent()) {
            // Simple validation logic (can be expanded)
            return document.get().getContent().length() > 10; // Example: content must be longer than 10 characters
        }
        return false;
    }

    // Method to list all documents
    public void listDocuments() {
        if (documents.isEmpty()) {
            System.out.println("No documents available.");
        } else {
            documents.forEach(System.out::println);
        }
    }
}

// Main class to demonstrate the collaborative platform
public class Main {
    public static void main(String[] args) {
        CollaborativePlatform platform = new CollaborativePlatform();

        try {
            // Adding documents
            platform.addDocument("Safety Guidelines", "Ensure to follow all safety protocols.", "Alice");
            platform.addDocument("Health Protocols", "Regular health checks are mandatory.", "Bob");

            // Listing documents
            platform.listDocuments();

            // Validating a document
            String titleToValidate = "Safety Guidelines";
            boolean isValid = platform.validateDocument(titleToValidate);
            System.out.println("Is the document '" + titleToValidate + "' valid? " + isValid);

        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
        }
    }
}
```
