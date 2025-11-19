"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Write a Python code snippet to process and generate products cartográficos using Georreferenciadas images acquired from RPA sensores remotos.
Generated: DETERMINISTIC_d35b9a16dd4f24d7
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import numpy as np
from osgeo import gdal, osr
from PIL import Image

def georreferenciar_imagem(image_path, output_path, 
                           rpc_path=None, dem_path=None):
    """
    Georreferencia uma imagem utilizando dados RPC e DEM.

    Parameters:
    image_path (str): Caminho para a imagem a ser georreferenciada.
    output_path (str): Caminho para a imagem georreferenciada saída.
    rpc_path (str, optional): Caminho para o arquivo RPC. Defaults to None.
    dem_path (str, optional): Caminho para o arquivo DEM. Defaults to None.

    Returns:
    None
    """

    try:
        # Abrir a imagem
        img = gdal.Open(image_path)

        # Verificar se o arquivo RPC foi fornecido
        if rpc_path:
            # Ler o arquivo RPC
            rpc = gdal.RPCFile(rpc_path)

            # Obter as coordenadas do canto da imagem
            ulx, uly, lrx, lry = rpc.GetGeoTransform()

        else:
            print("Arquivo RPC não fornecido. Utilizando coordenadas default.")
            ulx, uly, lrx, lry = img.GetGeoTransform()

        # Verificar se o arquivo DEM foi fornecido
        if dem_path:
            # Ler o arquivo DEM
            dem = gdal.Open(dem_path)

            # Obter as bandas do DEM
            dem_bands = dem.RasterCount

            if dem_bands != 1:
                raise ValueError("O arquivo DEM deve ter apenas uma banda.")

        else:
            print("Arquivo DEM não fornecido. Utilizando valores default.")

        # Criar o sistema de coordenadas
        srs = osr.SpatialReference()
        srs.ImportFromEPSG(4326)  # SIRGAS2000

        # Criar a imagem georreferenciada
        driver = gdal.GetDriverByName("GTiff")
        dst_dataset = driver.Create(output_path, 
                                    img.RasterXSize, 
                                    img.RasterYSize, 
                                    img.RasterCount, 
                                    gdal.GDT_Float32)

        # Definir a transformação geográfica
        dst_dataset.SetGeoTransform((ulx, 
                                      img.RasterXSize * 1.0 / img.RasterXSize, 
                                      0.0, 
                                      uly, 
                                      0.0, 
                                      -img.RasterYSize * 1.0 / img.RasterYSize))

        # Definir o sistema de coordenadas
        dst_dataset.SetProjection(srs.ExportToWkt())

        # Copiar as bandas da imagem
        for i in range(img.RasterCount):
            src_band = img.GetRasterBand(i + 1)
            dst_band = dst_dataset.GetRasterBand(i + 1)
            dst_band.WriteArray(src_band.ReadAsArray())

        # Liberar recursos
        del img
        del dst_dataset

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

def main():
    image_path = "path/to/image.tif"
    output_path = "path/to/output.tif"
    rpc_path = "path/to/rpc.txt"
    dem_path = "path/to/dem.tif"

    georreferenciar_imagem(image_path, output_path, rpc_path, dem_path)

if __name__ == "__main__":
    main()
```
