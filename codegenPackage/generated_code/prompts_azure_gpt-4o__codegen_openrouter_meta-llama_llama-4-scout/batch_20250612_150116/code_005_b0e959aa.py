"""
Generated Code Metadata:
========================
Original URL: https://digielearning.in
Prompt: Write code to implement a "Live Preview" feature for e-books, allowing users to read sample pages before subscribing, as seen on Digielearning.
Generated: DETERMINISTIC_b0e959aa17319271
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Live Preview Feature for E-books**
=====================================

### EbookLivePreview.java
```java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/**
 * Represents an e-book with live preview functionality.
 */
public class EbookLivePreview {
    private String ebookContent;
    private int previewPageCount;

    /**
     * Constructs an EbookLivePreview object.
     *
     * @param ebookFile  the file containing the e-book content
     * @param previewPageCount the number of pages to display in the preview
     * @throws FileNotFoundException if the e-book file is not found
     */
    public EbookLivePreview(File ebookFile, int previewPageCount) throws FileNotFoundException {
        this.previewPageCount = previewPageCount;
        this.ebookContent = readEbookContent(ebookFile);
    }

    /**
     * Reads the content of the e-book file.
     *
     * @param ebookFile the file containing the e-book content
     * @return the content of the e-book file
     * @throws FileNotFoundException if the e-book file is not found
     */
    private String readEbookContent(File ebookFile) throws FileNotFoundException {
        Scanner scanner = new Scanner(ebookFile);
        scanner.useDelimiter("\\Z");
        String content = scanner.next();
        scanner.close();
        return content;
    }

    /**
     * Returns a preview of the e-book content.
     *
     * @return a preview of the e-book content
     */
    public String getPreview() {
        String[] pages = ebookContent.split("\n\n"); // assume pages are separated by two newlines
        StringBuilder preview = new StringBuilder();
        for (int i = 0; i < previewPageCount && i < pages.length; i++) {
            preview.append(pages[i]).append("\n\n");
        }
        return preview.toString().trim();
    }

    public static void main(String[] args) {
        try {
            File ebookFile = new File("example.txt");
            EbookLivePreview ebookPreview = new EbookLivePreview(ebookFile, 5);
            System.out.println(ebookPreview.getPreview());
        } catch (FileNotFoundException e) {
            System.err.println("E-book file not found: " + e.getMessage());
        }
    }
}
```

### EbookLivePreviewService.java
```java
import java.io.File;
import java.util.HashMap;
import java.util.Map;

/**
 * Provides a service for e-book live preview.
 */
public class EbookLivePreviewService {
    private Map<String, EbookLivePreview> ebookPreviews;

    public EbookLivePreviewService() {
        this.ebookPreviews = new HashMap<>();
    }

    /**
     * Registers an e-book for live preview.
     *
     * @param ebookId    the ID of the e-book
     * @param ebookFile  the file containing the e-book content
     * @param previewPageCount the number of pages to display in the preview
     * @throws FileNotFoundException if the e-book file is not found
     */
    public void registerEbook(String ebookId, File ebookFile, int previewPageCount) throws FileNotFoundException {
        ebookPreviews.put(ebookId, new EbookLivePreview(ebookFile, previewPageCount));
    }

    /**
     * Returns a preview of the e-book content.
     *
     * @param ebookId the ID of the e-book
     * @return a preview of the e-book content
     */
    public String getEbookPreview(String ebookId) {
        EbookLivePreview ebookPreview = ebookPreviews.get(ebookId);
        if (ebookPreview != null) {
            return ebookPreview.getPreview();
        } else {
            return "E-book not found";
        }
    }

    public static void main(String[] args) {
        EbookLivePreviewService service = new EbookLivePreviewService();
        try {
            File ebookFile = new File("example.txt");
            service.registerEbook("example-ebook", ebookFile, 5);
            System.out.println(service.getEbookPreview("example-ebook"));
        } catch (FileNotFoundException e) {
            System.err.println("E-book file not found: " + e.getMessage());
        }
    }
}
```

### EbookLivePreviewController.java
```java
import java.io.File;
import java.io.FileNotFoundException;

/**
 * Handles requests for e-book live preview.
 */
public class EbookLivePreviewController {
    private EbookLivePreviewService service;

    public EbookLivePreviewController(EbookLivePreviewService service) {
        this.service = service;
    }

    /**
     * Handles a request to register an e-book for live preview.
     *
     * @param ebookId    the ID of the e-book
     * @param ebookFile  the file containing the e-book content
     * @param previewPageCount the number of pages to display in the preview
     * @throws FileNotFoundException if the e-book file is not found
     */
    public void registerEbook(String ebookId, File ebookFile, int previewPageCount) throws FileNotFoundException {
        service.registerEbook(ebookId, ebookFile, previewPageCount);
    }

    /**
     * Handles a request to retrieve a preview of the e-book content.
     *
     * @param ebookId the ID of the e-book
     * @return a preview of the e-book content
     */
    public String getEbookPreview(String ebookId) {
        return service.getEbookPreview(ebookId);
    }

    public static void main(String[] args) {
        EbookLivePreviewService service = new EbookLivePreviewService();
        EbookLivePreviewController controller = new EbookLivePreviewController(service);
        try {
            File ebookFile = new File("example.txt");
            controller.registerEbook("example-ebook", ebookFile, 5);
            System.out.println(controller.getEbookPreview("example-ebook"));
        } catch (FileNotFoundException e) {
            System.err.println("E-book file not found: " + e.getMessage());
        }
    }
}
```
