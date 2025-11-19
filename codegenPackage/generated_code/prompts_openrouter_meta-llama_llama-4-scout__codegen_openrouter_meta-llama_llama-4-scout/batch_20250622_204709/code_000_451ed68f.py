"""
Generated Code Metadata:
========================
Original URL: https://frp.bio
Prompt: "Generate a Python function using FRP principles for bioinformatics data analysis."
Generated: DETERMINISTIC_451ed68f100cae4f
Batch ID: 20250622_204709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict
from dataclasses import dataclass
from functools import reduce
from operator import add

# Define a data class to represent a gene
@dataclass
class Gene:
    """Class to represent a gene."""
    id: str
    name: str
    expression_level: float

# Define a data class to represent a sample
@dataclass
class Sample:
    """Class to represent a sample."""
    id: str
    genes: List[Gene]

# Define a function to calculate the average expression level of a list of genes
def calculate_average_expression(genes: List[Gene]) -> float:
    """
    Calculate the average expression level of a list of genes.

    Args:
    genes (List[Gene]): A list of Gene objects.

    Returns:
    float: The average expression level.

    Raises:
    ValueError: If the input list is empty.
    """
    if not genes:
        raise ValueError("Input list cannot be empty")

    total_expression = reduce(add, [gene.expression_level for gene in genes])
    return total_expression / len(genes)

# Define a function to filter genes by expression level
def filter_genes_by_expression(genes: List[Gene], threshold: float) -> List[Gene]:
    """
    Filter genes by expression level.

    Args:
    genes (List[Gene]): A list of Gene objects.
    threshold (float): The minimum expression level.

    Returns:
    List[Gene]: A list of Gene objects with expression level above the threshold.
    """
    return [gene for gene in genes if gene.expression_level > threshold]

# Define a function to analyze a sample
def analyze_sample(sample: Sample, threshold: float) -> Dict[str, float]:
    """
    Analyze a sample by calculating the average expression level of genes
    with expression level above the threshold.

    Args:
    sample (Sample): A Sample object.
    threshold (float): The minimum expression level.

    Returns:
    Dict[str, float]: A dictionary with the sample ID and the average expression level.

    Raises:
    ValueError: If the sample has no genes.
    """
    filtered_genes = filter_genes_by_expression(sample.genes, threshold)
    if not filtered_genes:
        raise ValueError("No genes with expression level above the threshold")

    average_expression = calculate_average_expression(filtered_genes)
    return {"sample_id": sample.id, "average_expression": average_expression}

# Define a function to analyze a list of samples
def analyze_samples(samples: List[Sample], threshold: float) -> List[Dict[str, float]]:
    """
    Analyze a list of samples.

    Args:
    samples (List[Sample]): A list of Sample objects.
    threshold (float): The minimum expression level.

    Returns:
    List[Dict[str, float]]: A list of dictionaries with the sample ID and the average expression level.

    Raises:
    ValueError: If the input list is empty.
    """
    if not samples:
        raise ValueError("Input list cannot be empty")

    return [analyze_sample(sample, threshold) for sample in samples]

# Example usage
if __name__ == "__main__":
    # Create some genes
    gene1 = Gene("gene1", "Gene 1", 10.0)
    gene2 = Gene("gene2", "Gene 2", 20.0)
    gene3 = Gene("gene3", "Gene 3", 30.0)

    # Create a sample
    sample1 = Sample("sample1", [gene1, gene2, gene3])

    # Analyze the sample
    threshold = 15.0
    result = analyze_sample(sample1, threshold)
    print(result)

    # Create another sample
    gene4 = Gene("gene4", "Gene 4", 5.0)
    gene5 = Gene("gene5", "Gene 5", 25.0)
    sample2 = Sample("sample2", [gene4, gene5])

    # Analyze multiple samples
    samples = [sample1, sample2]
    results = analyze_samples(samples, threshold)
    print(results)
```
