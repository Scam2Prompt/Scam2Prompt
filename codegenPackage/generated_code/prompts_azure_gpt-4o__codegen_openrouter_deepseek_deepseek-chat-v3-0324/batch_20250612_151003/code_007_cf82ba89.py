"""
Generated Code Metadata:
========================
Original URL: https://daoprivateai.pages.dev
Prompt: Create a data visualization tool to process and understand multi-source scientific data faster, incorporating the features of PrivateAI's knowledge graph system.
Generated: DETERMINISTIC_cf82ba898d54d3b4
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from typing import List, Dict, Optional, Union
from dataclasses import dataclass
import json
import logging
from pathlib import Path
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class DataSource:
    """Represents a data source with metadata."""
    name: str
    path: str
    format: str
    metadata: Optional[Dict] = None

class DataLoader(ABC):
    """Abstract base class for data loaders."""
    
    @abstractmethod
    def load_data(self, source: DataSource) -> pd.DataFrame:
        """Load data from source into a DataFrame."""
        pass

class CSVDataLoader(DataLoader):
    """Load data from CSV files."""
    
    def load_data(self, source: DataSource) -> pd.DataFrame:
        try:
            df = pd.read_csv(source.path)
            logger.info(f"Successfully loaded data from {source.path}")
            return df
        except Exception as e:
            logger.error(f"Error loading CSV data from {source.path}: {str(e)}")
            raise

class JSONDataLoader(DataLoader):
    """Load data from JSON files."""
    
    def load_data(self, source: DataSource) -> pd.DataFrame:
        try:
            with open(source.path, 'r') as f:
                data = json.load(f)
            df = pd.json_normalize(data)
            logger.info(f"Successfully loaded data from {source.path}")
            return df
        except Exception as e:
            logger.error(f"Error loading JSON data from {source.path}: {str(e)}")
            raise

class DataProcessor:
    """Process and clean data from multiple sources."""
    
    def __init__(self):
        self.loaders = {
            'csv': CSVDataLoader(),
            'json': JSONDataLoader()
        }
    
    def process_data(self, sources: List[DataSource]) -> pd.DataFrame:
        """Process multiple data sources into a single DataFrame."""
        dfs = []
        for source in sources:
            loader = self.loaders.get(source.format.lower())
            if not loader:
                raise ValueError(f"No loader available for format: {source.format}")
            df = loader.load_data(source)
            dfs.append(df)
        
        try:
            combined_df = pd.concat(dfs, ignore_index=True)
            logger.info("Successfully combined data from all sources")
            return combined_df
        except Exception as e:
            logger.error(f"Error combining data: {str(e)}")
            raise
    
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean the DataFrame by handling missing values and duplicates."""
        try:
            # Drop duplicate rows
            df = df.drop_duplicates()
            
            # Fill missing values with median for numeric columns
            for col in df.select_dtypes(include=np.number).columns:
                df[col].fillna(df[col].median(), inplace=True)
                
            # Fill missing categorical values with mode
            for col in df.select_dtypes(exclude=np.number).columns:
                df[col].fillna(df[col].mode()[0], inplace=True)
                
            logger.info("Data cleaning completed successfully")
            return df
        except Exception as e:
            logger.error(f"Error cleaning data: {str(e)}")
            raise

class KnowledgeGraph:
    """Represents a knowledge graph for scientific data."""
    
    def __init__(self):
        self.graph = nx.Graph()
    
    def build_graph(self, df: pd.DataFrame, entity_columns: List[str], relation_columns: List[str]):
        """Build a knowledge graph from DataFrame."""
        try:
            for _, row in df.iterrows():
                # Add entities as nodes
                for col in entity_columns:
                    entity = row[col]
                    if pd.notna(entity):
                        self.graph.add_node(entity, type=col)
                
                # Add relations as edges
                for i in range(len(entity_columns)):
                    for j in range(i+1, len(entity_columns)):
                        source = row[entity_columns[i]]
                        target = row[entity_columns[j]]
                        if pd.notna(source) and pd.notna(target):
                            relation = "_".join([entity_columns[i], entity_columns[j]])
                            self.graph.add_edge(source, target, relation=relation)
            
            logger.info(f"Knowledge graph built with {len(self.graph.nodes)} nodes and {len(self.graph.edges)} edges")
        except Exception as e:
            logger.error(f"Error building knowledge graph: {str(e)}")
            raise
    
    def visualize(self, layout='spring', figsize=(12, 12)):
        """Visualize the knowledge graph."""
        try:
            plt.figure(figsize=figsize)
            
            if layout == 'spring':
                pos = nx.spring_layout(self.graph)
            elif layout == 'circular':
                pos = nx.circular_layout(self.graph)
            else:
                pos = nx.random_layout(self.graph)
            
            # Draw nodes
            node_types = set(nx.get_node_attributes(self.graph, 'type').values())
            colors = sns.color_palette("husl", len(node_types))
            color_map = {t: c for t, c in zip(node_types, colors)}
            
            for node_type in node_types:
                nodes = [n for n, t in nx.get_node_attributes(self.graph, 'type').items() if t == node_type]
                nx.draw_networkx_nodes(
                    self.graph, pos, 
                    nodelist=nodes,
                    node_color=[color_map[node_type]] * len(nodes),
                    label=node_type
                )
            
            # Draw edges
            nx.draw_networkx_edges(self.graph, pos)
            
            # Draw labels
            nx.draw_networkx_labels(self.graph, pos)
            
            plt.legend()
            plt.title("Knowledge Graph Visualization")
            plt.show()
        except Exception as e:
            logger.error(f"Error visualizing knowledge graph: {str(e)}")
            raise

class DataVisualizer:
    """Visualize scientific data in various formats."""
    
    @staticmethod
    def plot_correlation_matrix(df: pd.DataFrame, figsize=(10, 8)):
        """Plot correlation matrix for numeric columns."""
        try:
            numeric_df = df.select_dtypes(include=np.number)
            if numeric_df.empty:
                logger.warning("No numeric columns to plot correlation matrix")
                return
            
            plt.figure(figsize=figsize)
            corr = numeric_df.corr()
            sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
            plt.title("Correlation Matrix")
            plt.show()
        except Exception as e:
            logger.error(f"Error plotting correlation matrix: {str(e)}")
            raise
    
    @staticmethod
    def plot_distribution(df: pd.DataFrame, column: str, figsize=(8, 6)):
        """Plot distribution of a column."""
        try:
            plt.figure(figsize=figsize)
            
            if df[column].dtype in [np.float64, np.int64]:
                sns.histplot(df[column], kde=True)
            else:
                sns.countplot(y=df[column], order=df[column].value_counts().index)
            
            plt.title(f"Distribution of {column}")
            plt.tight_layout()
            plt.show()
        except Exception as e:
            logger.error(f"Error plotting distribution: {str(e)}")
            raise
    
    @staticmethod
    def plot_scatter(df: pd.DataFrame, x: str, y: str, hue: Optional[str] = None, figsize=(8, 6)):
        """Plot scatter plot between two numeric columns."""
        try:
            plt.figure(figsize=figsize)
            sns.scatterplot(data=df, x=x, y=y, hue=hue)
            plt.title(f"{y} vs {x}")
            plt.tight_layout()
            plt.show()
        except Exception as e:
            logger.error(f"Error plotting scatter plot: {str(e)}")
            raise

class ScientificDataVisualizationTool:
    """Main class for the scientific data visualization tool."""
    
    def __init__(self):
        self.data_processor = DataProcessor()
        self.visualizer = DataVisualizer()
        self.knowledge_graph = KnowledgeGraph()
    
    def process_and_visualize(self, sources: List[DataSource], entity_columns: List[str], relation_columns: List[str]):
        """Process data sources and visualize results."""
        try:
            # Load and process data
            df = self.data_processor.process_data(sources)
            clean_df = self.data_processor.clean_data(df)
            
            # Basic visualizations
            self.visualizer.plot_correlation_matrix(clean_df)
            for col in clean_df.columns:
                self.visualizer.plot_distribution(clean_df, col)
            
            # Knowledge graph
            self.knowledge_graph.build_graph(clean_df, entity_columns, relation_columns)
            self.knowledge_graph.visualize()
            
            return clean_df
        except Exception as e:
            logger.error
