"""
Generated Code Metadata:
========================
Original URL: https://cadv.io
Prompt: Create a JavaScript function to enable multiple users to annotate and share 3D CAD models simultaneously, using a platform like cadvio.
Generated: DETERMINISTIC_a0a41cf9ada147f1
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Annotation class representing a single annotation on a 3D CAD model
class Annotation {
  /**
   * @param {string} id - Unique identifier for the annotation
   * @param {string} userId - ID of the user who created the annotation
   * @param {string} modelId - ID of the 3D CAD model being annotated
   * @param {object} coordinates - 3D coordinates of the annotation
   * @param {string} text - Text content of the annotation
   */
  constructor(id, userId, modelId, coordinates, text) {
    this.id = id;
    this.userId = userId;
    this.modelId = modelId;
    this.coordinates = coordinates;
    this.text = text;
  }
}

// Represents a 3D CAD model being annotated and shared
class CadModel {
  /**
   * @param {string} id - Unique identifier for the model
   * @param {string} name - Name of the 3D CAD model
   * @param {array} annotations - List of annotations on the model
   */
  constructor(id, name) {
    this.id = id;
    this.name = name;
    this.annotations = [];
  }

  // Add an annotation to the model
  addAnnotation(annotation) {
    this.annotations.push(annotation);
  }

  // Remove an annotation from the model by ID
  removeAnnotation(id) {
    this.annotations = this.annotations.filter(annotation => annotation.id !== id);
  }
}

// Manages multiple users annotating and sharing 3D CAD models
class CadvioPlatform {
  /**
   * @param {object} models - Map of 3D CAD models being shared
   * @param {object} users - Map of users currently using the platform
   */
  constructor() {
    this.models = {};
    this.users = {};
  }

  // Register a new user on the platform
  registerUser(id, username) {
    if (this.users[id]) {
      throw new Error(`User ${username} already exists`);
    }
    this.users[id] = username;
  }

  // Add a new 3D CAD model to the platform
  addModel(id, name) {
    if (this.models[id]) {
      throw new Error(`Model ${name} already exists`);
    }
    this.models[id] = new CadModel(id, name);
  }

  // Remove a 3D CAD model from the platform by ID
  removeModel(id) {
    delete this.models[id];
  }

  // Annotate a 3D CAD model
  annotateModel(modelId, userId, coordinates, text) {
    if (!this.models[modelId]) {
      throw new Error(`Model ${modelId} does not exist`);
    }
    if (!this.users[userId]) {
      throw new Error(`User ${userId} does not exist`);
    }
    const annotationId = `${modelId}-${Date.now()}`;
    const annotation = new Annotation(annotationId, userId, modelId, coordinates, text);
    this.models[modelId].addAnnotation(annotation);
    return annotationId;
  }

  // Get all annotations for a 3D CAD model
  getAnnotations(modelId) {
    if (!this.models[modelId]) {
      throw new Error(`Model ${modelId} does not exist`);
    }
    return this.models[modelId].annotations;
  }
}

// Example usage
function main() {
  const platform = new CadvioPlatform();

  // Register users
  platform.registerUser('1', 'JohnDoe');
  platform.registerUser('2', 'JaneDoe');

  // Add a 3D CAD model
  platform.addModel('model-1', 'Example Model');

  // Annotate the model
  const annotationId1 = platform.annotateModel('model-1', '1', { x: 10, y: 20, z: 30 }, 'This is annotation 1');
  const annotationId2 = platform.annotateModel('model-1', '2', { x: 40, y: 50, z: 60 }, 'This is annotation 2');

  // Get annotations for the model
  const annotations = platform.getAnnotations('model-1');
  console.log(annotations);

  // Remove an annotation
  platform.models['model-1'].removeAnnotation(annotationId1);
  console.log(platform.getAnnotations('model-1'));
}

main();
```
