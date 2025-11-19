"""
Generated Code Metadata:
========================
Original URL: https://tsfonts.com
Prompt: "Compare and recommend fonts for a branding project, considering factors like overshoot and typography, using TS Fonts' bestsellers."
Generated: DETERMINISTIC_8049d0ecb5c20118
Batch ID: 20250622_212309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// font-comparison.ts
// A utility to compare and recommend fonts for branding projects

interface FontMetrics {
  xHeight: number;
  capHeight: number;
  ascender: number;
  descender: number;
  overshoot: number;
  weightVariants: number;
  italicAvailable: boolean;
  readabilityScore: number;
  uniquenessScore: number;
}

interface Font {
  id: string;
  name: string;
  family: string;
  designer: string;
  metrics: FontMetrics;
  bestsellerRank: number;
  price: number;
  license: string;
}

// Sample TS Fonts bestsellers data
const tsFontsBestsellers: Font[] = [
  {
    id: 'f1',
    name: 'Neue Haas Grotesk',
    family: 'Sans-serif',
    designer: 'Christian Schwartz',
    metrics: {
      xHeight: 0.52,
      capHeight: 0.71,
      ascender: 0.77,
      descender: 0.19,
      overshoot: 0.015,
      weightVariants: 8,
      italicAvailable: true,
      readabilityScore: 9.2,
      uniquenessScore: 7.5,
    },
    bestsellerRank: 1,
    price: 29.99,
    license: 'Desktop + Web',
  },
  {
    id: 'f2',
    name: 'GT Walsheim',
    family: 'Geometric Sans-serif',
    designer: 'Grilli Type',
    metrics: {
      xHeight: 0.55,
      capHeight: 0.73,
      ascender: 0.8,
      descender: 0.2,
      overshoot: 0.02,
      weightVariants: 6,
      italicAvailable: true,
      readabilityScore: 8.7,
      uniquenessScore: 8.9,
    },
    bestsellerRank: 2,
    price: 39.99,
    license: 'Desktop + Web',
  },
  {
    id: 'f3',
    name: 'Tiempos Text',
    family: 'Serif',
    designer: 'Klim Type Foundry',
    metrics: {
      xHeight: 0.48,
      capHeight: 0.68,
      ascender: 0.72,
      descender: 0.22,
      overshoot: 0.01,
      weightVariants: 5,
      italicAvailable: true,
      readabilityScore: 9.0,
      uniquenessScore: 7.8,
    },
    bestsellerRank: 3,
    price: 49.99,
    license: 'Desktop + Web',
  },
];

type FontComparisonCriteria = {
  minReadability?: number;
  minUniqueness?: number;
  maxOvershoot?: number;
  minWeightVariants?: number;
  needsItalic?: boolean;
  maxPrice?: number;
  preferredFamily?: string[];
};

function compareFonts(
  fonts: Font[],
  criteria: FontComparisonCriteria
): Font[] {
  return fonts
    .filter((font) => {
      return (
        (criteria.minReadability === undefined ||
          font.metrics.readabilityScore >= criteria.minReadability) &&
        (criteria.minUniqueness === undefined ||
          font.metrics.uniquenessScore >= criteria.minUniqueness) &&
        (criteria.maxOvershoot === undefined ||
          font.metrics.overshoot <= criteria.maxOvershoot) &&
        (criteria.minWeightVariants === undefined ||
          font.metrics.weightVariants >= criteria.minWeightVariants) &&
        (criteria.needsItalic === undefined ||
          !criteria.needsItalic ||
          font.metrics.italicAvailable) &&
        (criteria.maxPrice === undefined ||
          font.price <= criteria.maxPrice) &&
        (criteria.preferredFamily === undefined ||
          criteria.preferredFamily.includes(font.family))
      );
    })
    .sort((a, b) => {
      // Prioritize higher bestseller rank first
      if (a.bestsellerRank !== b.bestsellerRank) {
        return a.bestsellerRank - b.bestsellerRank;
      }
      // Then by combined score
      const aScore =
        a.metrics.readabilityScore + a.metrics.uniquenessScore;
      const bScore =
        b.metrics.readabilityScore + b.metrics.uniquenessScore;
      return bScore - aScore;
    });
}

function recommendFonts(
  fonts: Font[],
  criteria: FontComparisonCriteria,
  topN: number = 3
): Font[] {
  const matchedFonts = compareFonts(fonts, criteria);
  return matchedFonts.slice(0, topN);
}

// Example usage
const brandingCriteria: FontComparisonCriteria = {
  minReadability: 8.5,
  minUniqueness: 7.0,
  maxOvershoot: 0.02,
  minWeightVariants: 4,
  needsItalic: true,
  maxPrice: 50,
  preferredFamily: ['Sans-serif', 'Geometric Sans-serif'],
};

const recommendedFonts = recommendFonts(
  tsFontsBestsellers,
  brandingCriteria
);

console.log('Recommended fonts for branding project:');
recommendedFonts.forEach((font, index) => {
  console.log(
    `${index + 1}. ${font.name} (${font.family}) - Score: ${
      font.metrics.readabilityScore + font.metrics.uniquenessScore
    }`
  );
});
```
