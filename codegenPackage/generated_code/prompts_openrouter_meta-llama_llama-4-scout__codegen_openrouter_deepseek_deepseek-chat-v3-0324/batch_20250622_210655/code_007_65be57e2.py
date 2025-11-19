"""
Generated Code Metadata:
========================
Original URL: https://churchproweb.com
Prompt: Create a Church Banner Design Concept using Adobe Creative Suite, inspired by ChurchProWeb's banner design services.
Generated: DETERMINISTIC_65be57e2e2efd695
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Adobe Illustrator Script for Church Banner Design Concept
// Inspired by ChurchProWeb's banner design services

// Main function to create the banner design
function createChurchBanner() {
    try {
        // Create a new document
        var doc = app.documents.add(DocumentColorSpace.RGB, 36, 24); // 36x24 inches
        
        // Set up layers for organization
        var backgroundLayer = doc.layers.add();
        backgroundLayer.name = "Background";
        var textLayer = doc.layers.add();
        textLayer.name = "Text";
        var graphicsLayer = doc.layers.add();
        graphicsLayer.name = "Graphics";
        
        // Create background gradient
        backgroundLayer.activate();
        var backgroundRect = doc.pathItems.rectangle(0, 0, doc.width, doc.height);
        var gradient = backgroundRect.fillColor = new Gradient();
        gradient.type = GradientType.LINEAR;
        var gradientStops = gradient.gradientStops;
        
        // Add gradient stops (gold to white)
        gradientStops.add(0, new RGBColor(), new RGBColor(255, 215, 0)); // Gold
        gradientStops.add(100, new RGBColor(), new RGBColor(255, 255, 255)); // White
        
        // Add church name text
        textLayer.activate();
        var churchName = doc.textFrames.add();
        churchName.contents = "FAITH COMMUNITY CHURCH";
        churchName.textRange.characterAttributes.size = 72; // 72pt font
        churchName.textRange.characterAttributes.font = "Times New Roman Bold";
        churchName.textRange.characterAttributes.fillColor = new RGBColor(0, 0, 0); // Black
        churchName.top = doc.height - 4; // Position 4 inches from top
        churchName.left = doc.width / 2;
        churchName.textRange.paragraphAttributes.justification = Justification.CENTER;
        
        // Add verse text
        var verseText = doc.textFrames.add();
        verseText.contents = "\"For where two or three gather in my name, there am I with them.\" - Matthew 18:20";
        verseText.textRange.characterAttributes.size = 36; // 36pt font
        verseText.textRange.characterAttributes.font = "Times New Roman";
        verseText.textRange.characterAttributes.fillColor = new RGBColor(0, 0, 0); // Black
        verseText.top = doc.height - 8; // Position 8 inches from top
        verseText.left = doc.width / 2;
        verseText.textRange.paragraphAttributes.justification = Justification.CENTER;
        
        // Add cross graphic
        graphicsLayer.activate();
        var cross = createCross(doc, doc.width / 2, doc.height / 2, 8, 12);
        cross.fillColor = new RGBColor(139, 0, 0); // Dark red
        
        // Add decorative elements
        addDecorativeElements(doc, graphicsLayer);
        
        return "Church banner design created successfully!";
    } catch (e) {
        return "Error creating banner: " + e.message;
    }
}

// Helper function to create a cross symbol
function createCross(doc, x, y, width, height) {
    var vertical = doc.pathItems.rectangle(x - width/4, y - height/2, width/2, height);
    var horizontal = doc.pathItems.rectangle(x - width/2, y - height/4, width, height/2);
    
    var cross = doc.groupItems.add();
    cross.addToGroup(vertical);
    cross.addToGroup(horizontal);
    
    return cross;
}

// Helper function to add decorative elements
function addDecorativeElements(doc, layer) {
    layer.activate();
    
    // Add vine pattern border
    var borderWidth = 2; // inches
    var borderRect = doc.pathItems.rectangle(borderWidth, borderWidth, 
                                            doc.width - borderWidth*2, 
                                            doc.height - borderWidth*2);
    borderRect.stroked = true;
    borderRect.strokeWidth = 3;
    borderRect.strokeColor = new RGBColor(139, 0, 0); // Dark red
    borderRect.filled = false;
    
    // Add corner flourishes
    var flourishSize = 3; // inches
    for (var i = 0; i < 4; i++) {
        var angle = i * 90;
        var x = (i % 2) ? doc.width - flourishSize : 0;
        var y = (i < 2) ? doc.height - flourishSize : 0;
        
        var flourish = doc.pathItems.add();
        // Simplified flourish path (would be more complex in production)
        flourish.setEntirePath([
            [x, y + flourishSize/2],
            [x + flourishSize/2, y],
            [x + flourishSize, y + flourishSize/2],
            [x + flourishSize/2, y + flourishSize]
        ]);
        flourish.stroked = true;
        flourish.strokeWidth = 2;
        flourish.strokeColor = new RGBColor(139, 0, 0); // Dark red
        flourish.filled = false;
    }
}

// Execute the main function
createChurchBanner();
```
