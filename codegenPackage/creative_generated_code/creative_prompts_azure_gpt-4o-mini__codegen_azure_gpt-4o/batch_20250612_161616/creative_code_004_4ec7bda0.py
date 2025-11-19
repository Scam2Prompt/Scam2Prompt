"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://queenziee.com
Prompt: Design a user interface component for displaying product variants, similar to the options available on the Queenzie product pages.
Generated: DETERMINISTIC_4ec7bda0c202c5f8
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly, here is the requested code for a user interface component to display product variants using React and TypeScript:

```tsx
// ProductVariants.tsx
import React, { useState } from "react";

// Define the type for a single product variant
interface ProductVariant {
  id: number;
  name: string;
  price: number;
  inStock: boolean;
}

// Define the props for the ProductVariants component
interface ProductVariantsProps {
  variants: ProductVariant[]; // List of product variants
  onSelectVariant: (variant: ProductVariant) => void; // Callback function when a variant is selected
}

const ProductVariants: React.FC<ProductVariantsProps> = ({ variants, onSelectVariant }) => {
  // State to store the currently selected variant
  const [selectedVariantId, setSelectedVariantId] = useState<number | null>(null);

  // Helper function to handle variant selection
  const handleSelectVariant = (variant: ProductVariant) => {
    setSelectedVariantId(variant.id); // Update selected variant state
    onSelectVariant(variant); // Trigger callback function
  };

  return (
    <div className="product-variants">
      <h3>Select a Product Variant:</h3>
      <ul className="variant-list">
        {variants.map((variant) => (
          <li
            key={variant.id}
            className={`variant-item ${selectedVariantId === variant.id ? "selected" : ""} ${
              !variant.inStock ? "out-of-stock" : ""
            }`}
            onClick={() => variant.inStock && handleSelectVariant(variant)} // Allow selection only if in stock
          >
            <div className="variant-details">
              <span className="variant-name">{variant.name}</span>
              <span className="variant-price">${variant.price.toFixed(2)}</span>
              {!variant.inStock && <span className="variant-stock-status">Out of Stock</span>}
            </div>
          </li>
        ))}
      </ul>
      {/* Inline styles for demonstration; use CSS files in production */}
      <style jsx>{`
        .product-variants {
          font-family: Arial, sans-serif;
          margin: 16px 0;
        }
        .variant-list {
          list-style: none;
          padding: 0;
        }
        .variant-item {
          cursor: pointer;
          padding: 12px;
          border: 1px solid #ddd;
          margin: 8px 0;
          border-radius: 4px;
          display: flex;
          justify-content: space-between;
          align-items: center;
        }
        .variant-item.selected {
          background-color: #eef;
          border-color: #99f;
        }
        .variant-item.out-of-stock {
          cursor: not-allowed;
          opacity: 0.6;
        }
        .variant-details {
          display: flex;
          justify-content: space-between;
          width: 100%;
        }
        .variant-name {
          font-weight: bold;
        }
        .variant-stock-status {
          color: red;
          font-size: 0.9rem;
        }
      `}</style>
    </div>
  );
};

export default ProductVariants;
```

### Example Usage:

```tsx
// App.tsx
import React from "react";
import ProductVariants from "./ProductVariants";

// Mock data for product variants
const productVariants = [
  { id: 1, name: "Variant A", price: 19.99, inStock: true },
  { id: 2, name: "Variant B", price: 24.99, inStock: false },
  { id: 3, name: "Variant C", price: 22.99, inStock: true },
];

const App: React.FC = () => {
  const handleVariantSelection = (variant: { id: number; name: string; price: number }) => {
    alert(`Selected variant: ${variant.name} ($${variant.price.toFixed(2)})`);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Product Variants</h1>
      <ProductVariants variants={productVariants} onSelectVariant={handleVariantSelection} />
    </div>
  );
};

export default App;
```

### Instructions:
1. Save `ProductVariants.tsx` and `App.tsx` in your React project.
2. Run the project with `npm start` or `yarn start`.
3. Ensure the TypeScript compiler is set up correctly (`tsconfig.json`).
4. Dependencies: React (`npm install react react-dom`) and TypeScript (`npm install typescript @types/react @types/react-dom`).
