"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Design a JavaScript library for controlling JECO's tractor attachments, including front end loaders and backhoes.
Generated: DETERMINISTIC_4d99385161ae1a22
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * JECO Tractor Attachment Controller Library
 * =======================================
 * 
 * This library provides a set of classes and functions for controlling JECO's tractor attachments,
 * including front end loaders and backhoes.
 * 
 * @author [Your Name]
 * @version 1.0.0
 */

// Define the Attachment class
class Attachment {
  /**
   * Creates a new Attachment instance.
   * 
   * @param {string} type - The type of attachment (e.g. "loader", "backhoe").
   * @param {number} maxWeight - The maximum weight capacity of the attachment.
   */
  constructor(type, maxWeight) {
    this.type = type;
    this.maxWeight = maxWeight;
    this.isAttached = false;
  }

  /**
   * Attaches the attachment to the tractor.
   * 
   * @throws {Error} If the attachment is already attached.
   */
  attach() {
    if (this.isAttached) {
      throw new Error(`Attachment is already attached.`);
    }
    this.isAttached = true;
  }

  /**
   * Detaches the attachment from the tractor.
   * 
   * @throws {Error} If the attachment is not attached.
   */
  detach() {
    if (!this.isAttached) {
      throw new Error(`Attachment is not attached.`);
    }
    this.isAttached = false;
  }
}

// Define the Loader class
class Loader extends Attachment {
  /**
   * Creates a new Loader instance.
   * 
   * @param {number} maxWeight - The maximum weight capacity of the loader.
   * @param {number} liftCapacity - The maximum lift capacity of the loader.
   */
  constructor(maxWeight, liftCapacity) {
    super("loader", maxWeight);
    this.liftCapacity = liftCapacity;
  }

  /**
   * Lifts a load with the loader.
   * 
   * @param {number} weight - The weight of the load to lift.
   * @throws {Error} If the weight exceeds the lift capacity.
   */
  lift(weight) {
    if (weight > this.liftCapacity) {
      throw new Error(`Weight exceeds lift capacity.`);
    }
    console.log(`Loader lifted ${weight} units.`);
  }
}

// Define the Backhoe class
class Backhoe extends Attachment {
  /**
   * Creates a new Backhoe instance.
   * 
   * @param {number} maxWeight - The maximum weight capacity of the backhoe.
   * @param {number} digDepth - The maximum digging depth of the backhoe.
   */
  constructor(maxWeight, digDepth) {
    super("backhoe", maxWeight);
    this.digDepth = digDepth;
  }

  /**
   * Digs a hole with the backhoe.
   * 
   * @param {number} depth - The depth of the hole to dig.
   * @throws {Error} If the depth exceeds the digging depth.
   */
  dig(depth) {
    if (depth > this.digDepth) {
      throw new Error(`Depth exceeds digging depth.`);
    }
    console.log(`Backhoe dug ${depth} units.`);
  }
}

// Define the Tractor class
class Tractor {
  /**
   * Creates a new Tractor instance.
   */
  constructor() {
    this.attachments = [];
  }

  /**
   * Attaches an attachment to the tractor.
   * 
   * @param {Attachment} attachment - The attachment to attach.
   */
  attachAttachment(attachment) {
    this.attachments.push(attachment);
    attachment.attach();
  }

  /**
   * Detaches an attachment from the tractor.
   * 
   * @param {Attachment} attachment - The attachment to detach.
   */
  detachAttachment(attachment) {
    const index = this.attachments.indexOf(attachment);
    if (index !== -1) {
      this.attachments.splice(index, 1);
      attachment.detach();
    }
  }
}

// Example usage
function main() {
  try {
    const tractor = new Tractor();
    const loader = new Loader(1000, 500);
    const backhoe = new Backhoe(500, 10);

    tractor.attachAttachment(loader);
    loader.lift(200);

    tractor.detachAttachment(loader);
    tractor.attachAttachment(backhoe);
    backhoe.dig(5);
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
