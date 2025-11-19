"""
Generated Code Metadata:
========================
Original URL: https://bime.ulb.be
Prompt: Write code to develop antagonists for human olfactory receptors associated with unpleasant odors, using molecular docking techniques.
Generated: DETERMINISTIC_47d5ecf55432ddf4
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import logging
from pathlib import Path
from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem, Descriptors
from biopandas.pdb import PandasPdb
from openbabel import pybel
from scipy.spatial.distance import cdist

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MolecularDockingPipeline:
    """
    A pipeline for molecular docking to identify antagonists for human olfactory receptors.
    """
    
    def __init__(self, receptor_pdb_path: str, ligand_library_path: str, output_dir: str):
        """
        Initialize the docking pipeline.
        
        Args:
            receptor_pdb_path: Path to the receptor PDB file
            ligand_library_path: Path to the ligand library (SDF or SMILES file)
            output_dir: Directory to store output files
        """
        self.receptor_pdb_path = receptor_pdb_path
        self.ligand_library_path = ligand_library_path
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Validate inputs
        if not Path(receptor_pdb_path).exists():
            raise FileNotFoundError(f"Receptor PDB file not found: {receptor_pdb_path}")
        if not Path(ligand_library_path).exists():
            raise FileNotFoundError(f"Ligand library file not found: {ligand_library_path}")
            
        logger.info("Molecular docking pipeline initialized")
    
    def prepare_receptor(self) -> str:
        """
        Prepare the receptor for docking by converting to PDBQT format.
        
        Returns:
            Path to the prepared receptor file
        """
        receptor_pdbqt = self.output_dir / "receptor.pdbqt"
        
        try:
            # Convert PDB to PDBQT using OpenBabel
            mol = next(pybel.readfile("pdb", self.receptor_pdb_path))
            mol.addh()
            mol.calccharges()
            mol.write("pdbqt", str(receptor_pdbqt), overwrite=True)
            
            logger.info(f"Receptor prepared and saved to {receptor_pdbqt}")
            return str(receptor_pdbqt)
        except Exception as e:
            logger.error(f"Error preparing receptor: {e}")
            raise
    
    def prepare_ligands(self) -> List[str]:
        """
        Prepare ligands from the library for docking.
        
        Returns:
            List of paths to prepared ligand files
        """
        ligand_paths = []
        file_ext = Path(self.ligand_library_path).suffix.lower()
        
        try:
            if file_ext == ".sdf":
                suppl = Chem.SDMolSupplier(self.ligand_library_path)
                for i, mol in enumerate(suppl):
                    if mol is not None:
                        mol = self._prepare_ligand_mol(mol)
                        ligand_path = self.output_dir / f"ligand_{i}.pdbqt"
                        self._write_ligand(mol, ligand_path)
                        ligand_paths.append(str(ligand_path))
            elif file_ext == ".smi":
                with open(self.ligand_library_path) as f:
                    for i, line in enumerate(f):
                        smiles = line.strip().split()[0]
                        mol = Chem.MolFromSmiles(smiles)
                        if mol is not None:
                            mol = self._prepare_ligand_mol(mol)
                            ligand_path = self.output_dir / f"ligand_{i}.pdbqt"
                            self._write_ligand(mol, ligand_path)
                            ligand_paths.append(str(ligand_path))
            else:
                raise ValueError("Unsupported ligand file format. Use SDF or SMILES.")
                
            logger.info(f"Prepared {len(ligand_paths)} ligands for docking")
            return ligand_paths
        except Exception as e:
            logger.error(f"Error preparing ligands: {e}")
            raise
    
    def _prepare_ligand_mol(self, mol: Chem.Mol) -> Chem.Mol:
        """Prepare a single ligand molecule for docking."""
        mol = Chem.AddHs(mol)
        AllChem.EmbedMolecule(mol)
        AllChem.MMFFOptimizeMolecule(mol)
        return mol
    
    def _write_ligand(self, mol: Chem.Mol, output_path: Path) -> None:
        """Write a ligand molecule to PDBQT format."""
        try:
            obmol = pybel.readstring("mol", Chem.MolToMolBlock(mol))
            obmol.addh()
            obmol.calccharges()
            obmol.write("pdbqt", str(output_path), overwrite=True)
        except Exception as e:
            logger.error(f"Error writing ligand {output_path}: {e}")
            raise
    
    def run_docking(self, receptor_pdbqt: str, ligand_paths: List[str], 
                   center: Optional[Tuple[float, float, float]] = None,
                   size: Tuple[float, float, float] = (20, 20, 20),
                   exhaustiveness: int = 8) -> pd.DataFrame:
        """
        Run molecular docking using AutoDock Vina.
        
        Args:
            receptor_pdbqt: Path to prepared receptor
            ligand_paths: List of paths to prepared ligands
            center: Docking box center coordinates (if None, will be calculated)
            size: Docking box size
            exhaustiveness: Exhaustiveness parameter for Vina
            
        Returns:
            DataFrame with docking results
        """
        try:
            if center is None:
                center = self._calculate_binding_site_center(receptor_pdbqt)
                
            results = []
            for ligand_path in ligand_paths:
                output_path = Path(ligand_path).with_suffix(".docked.pdbqt")
                log_path = Path(ligand_path).with_suffix(".log")
                
                cmd = (
                    f"vina --receptor {receptor_pdbqt} --ligand {ligand_path} "
                    f"--center_x {center[0]} --center_y {center[1]} --center_z {center[2]} "
                    f"--size_x {size[0]} --size_y {size[1]} --size_z {size[2]} "
                    f"--exhaustiveness {exhaustiveness} "
                    f"--out {output_path} --log {log_path}"
                )
                
                os.system(cmd)
                
                # Parse docking score from log file
                score = self._parse_docking_score(log_path)
                ligand_id = Path(ligand_path).stem
                results.append({
                    "ligand_id": ligand_id,
                    "docking_score": score,
                    "docked_pose": str(output_path)
                })
                
            df = pd.DataFrame(results)
            output_csv = self.output_dir / "docking_results.csv"
            df.to_csv(output_csv, index=False)
            
            logger.info(f"Docking completed. Results saved to {output_csv}")
            return df
        except Exception as e:
            logger.error(f"Error running docking: {e}")
            raise
    
    def _calculate_binding_site_center(self, receptor_pdbqt: str) -> Tuple[float, float, float]:
        """Calculate the center of the binding site from the receptor structure."""
        try:
            ppdb = PandasPdb()
            ppdb.read_pdb(receptor_pdbqt)
            atom_df = ppdb.df['ATOM']
            coords = atom_df[['x_coord', 'y_coord', 'z_coord']].values
            center = np.mean(coords, axis=0)
            return tuple(center)
        except Exception as e:
            logger.error(f"Error calculating binding site center: {e}")
            raise
    
    def _parse_docking_score(self, log_path: Path) -> float:
        """Parse the docking score from Vina log file."""
        try:
            with open(log_path) as f:
                for line in f:
                    if line.startswith("REMARK VINA RESULT:"):
                        return float(line.split()[3])
            raise ValueError("Docking score not found in log file")
        except Exception as e:
            logger.error(f"Error parsing docking score: {e}")
            raise
    
    def filter_results(self, df: pd.DataFrame, score_threshold: float = -7.0,
                      properties: Optional[dict] = None) -> pd.DataFrame:
        """
        Filter docking results based on score and molecular properties.
        
        Args:
            df: DataFrame with docking results
            score_threshold: Minimum docking score to keep
            properties: Dictionary of property filters (e.g., {"MW": 500, "LogP": 5})
            
        Returns:
            Filtered DataFrame
        """
        try:
            filtered = df[df["docking_score"] <= score_threshold].copy()
            
            if properties:
                for ligand_path in filtered["docked_pose"]:
                    mol = next(pybel.readfile("pdbqt", ligand_path))
                    for prop
