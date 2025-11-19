"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a292d5c1.docs-62t.pages.dev
Prompt: Describe the steps to create a supply chain management system using Código's CIDL and its code generation features.
Generated: DETERMINISTIC_793a7449dd0b20b0
Batch ID: 20250612_163243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cidl
// CIDL definition for a simple Supply Chain Management System

// Define the main entities in the supply chain
entity Product {
    key id: Integer // Unique identifier for the product
    name: String // Name of the product
    description: String // Description of the product
    quantity: Integer // Current stock quantity
    price: Decimal // Price of the product
}

entity Supplier {
    key id: Integer // Unique identifier for the supplier
    name: String // Name of the supplier
    contactInfo: String // Contact information for the supplier
}

// Define the relationship between products and suppliers
relationship Supplies {
    source Supplier // Supplier providing the products
    target Product // Products supplied by the supplier
    quantity: Integer // Quantity supplied
}

// Define the main processes in the supply chain
process AddProduct {
    parameters: {
        name: String,
        description: String,
        quantity: Integer,
        price: Decimal
    }
    // Logic to add a product to the inventory
    result: Product // Return the created product
}

process UpdateProduct {
    parameters: {
        id: Integer, // ID of the product to update
        name: String,
        description: String,
        quantity: Integer,
        price: Decimal
    }
    // Logic to update the product details
    result: Product // Return the updated product
}

process DeleteProduct {
    parameters: {
        id: Integer // ID of the product to delete
    }
    // Logic to delete a product from the inventory
    result: Boolean // Return success status
}

process AddSupplier {
    parameters: {
        name: String,
        contactInfo: String
    }
    // Logic to add a new supplier
    result: Supplier // Return the created supplier
}

process LinkSupplierToProduct {
    parameters: {
        supplierId: Integer, // ID of the supplier
        productId: Integer, // ID of the product
        quantity: Integer // Quantity supplied
    }
    // Logic to link a supplier to a product
    result: Supplies // Return the created relationship
}

// Define error handling for processes
error InvalidProductId { // Error for invalid product ID
    message: String // Error message
}

error InvalidSupplierId { // Error for invalid supplier ID
    message: String // Error message
}

error ProductNotFound { // Error for product not found
    message: String // Error message
}

error SupplierNotFound { // Error for supplier not found
    message: String // Error message
}

// Define validations for inputs
validate ProductNameRequired {
    // Validate that the product name is provided
    condition: name != null && name != ""
    message: "Product name is required"
}

validate SupplierNameRequired {
    // Validate that the supplier name is provided
    condition: name != null && name != ""
    message: "Supplier name is required"
}

// The end of the CIDL definition for the Supply Chain Management System
```
