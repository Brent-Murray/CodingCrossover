# Geomatics Functions in R and Python: A Cheat Sheet
This repository provides a side-by-side comparison of how to perform common geomatics tasks in **R** and **Python**. It focuses on the libraries `terra` and `sf` in R, and `rasterio`, `numpy`, `pandas`, and `geopandas` in Python.

---

## Library Overview

### R Libraries
| **Library**   | **Description**                                                                                   |
|---------------|---------------------------------------------------------------------------------------------------|
| **`terra`**   | For spatial data manipulation, raster data processing, and geospatial analysis.                  |
| **`sf`**      | For handling vector spatial data, including shapefiles, GeoJSON, and other formats.              |

### Python Libraries
| **Library**        | **Description**                                                                                   |
|--------------------|---------------------------------------------------------------------------------------------------|
| **`rasterio`**     | For raster file I/O and processing.                                                              |
| **`numpy`**        | For numerical data manipulation, often used with raster data.                                    |
| **`pandas`**       | For tabular data manipulation.                                                                   |
| **`geopandas`**    | For handling vector spatial data, extending `pandas` to work with geospatial formats.            |

---

## Importing Libraries

### R
```R
# Import libraries
library(terra)   # For raster operations
library(sf)      # For vector operations
library(dplyr)   # For data manipulation
```

### Python
```python
# Import libraries
import rasterio                                                     # For raster operations
import geopandas as gpd                                             # For vector data
import numpy as np                                                  # For numerical data
import pandas as pd                                                 # For tabular data manipulation
from rasterio.features import rasterize                             # For rasterizing vector data
from rasterio.mask import mask                                      # For masking raster data
from rasterio.warp import calculate_default_transform, reproject    # For raster reprojection
from shapely.geometry import box                                    # For creating bounding box
```
## Cheat Sheet: Common Geomatics Functions

| **Functionality**            | **R (`terra`, `sf`)**                                                                                                                                   | **Python (`rasterio`, `geopandas`, etc.)**                                                                                                                      |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Read a shapefile**          | ```R shp <- sf::st_read("path/to/file.shp")```                                                                                                               | `shp = gpd.read_file("path/to/file.shp")`                                                                                                                      |
| **Write a shapefile**         | `sf::st_write(shp, "path/to/output.shp")`                                                                                                              | `shp.to_file("path/to/output.shp")`                                                                                                                            |
| **Read a raster**             | `raster <- terra::rast("path/to/file.tif")`                                                                                                            | `with rasterio.open("path/to/file.tif") as src:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`raster = src.read()`                                                              |
| **Write a raster**            | `terra::writeRaster(raster, "path/to/output.tif", overwrite=TRUE)`                                                                                     | `with rasterio.open("path/to/output.tif", "w", **kwargs) as dst:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`dst.write(raster)`                                               |
| **Calculate NDVI**            | `ndvi <- (nir - red) / (nir + red)` <br>*(assuming `nir` and `red` are `terra` raster objects)*                                                        | `ndvi = (nir - red) / (nir + red)` <br>*(assuming `nir` and `red` are `numpy` arrays)*                                                                         |
| **Clip a raster by extent**   | `clipped <- terra::crop(raster, extent)`                                                                                                               | `clipped, _ = mask(src, shapes, crop=True)`                                                                                |
| **Clip a vector by extent**   | `clipped <- sf::st_crop(vector, xmin = x1, ymin = y1, xmax = x2, ymax = y2)`                                                                            | `bbox = box(x1, y1, x2, y2)`<br>`clipped = vector.clip(bbox)`                                                            |
| **Reproject a shapefile**     | `reproj <- sf::st_transform(shp, crs = 4326)`                                                                                                          | `shp = shp.to_crs(epsg=4326)`                                                                                                                                 |
| **Reproject a raster**        | `reproj <- terra::project(raster, "EPSG:4326")`                                                                                                        | `reprojected_raster = reproject(src, transform)`                                        |
| **Calculate area of polygons**| `shp$area <- sf::st_area(shp)`                                                                                                                         | `shp["area"] = shp.geometry.area`                                                                                                                              |
| **Sort polygons by attribute**| `sorted <- shp[order(shp$attribute), ]`                                                                                                                | `sorted = shp.sort_values("attribute")`                                                                                                                        |
| **Extract raster values**     | `values <- terra::extract(raster, sf::st_coordinates(points))`                                                                                         | `values = [raster[row, col] for row, col in points]` *(requires array coordinates for `numpy`)*                                                                |
| **Buffer around features**    | `buffered <- sf::st_buffer(shp, dist = 500)`                                                                                                           | `buffered = shp.buffer(500)`                                                                                                                                  |
| **Rasterize a vector layer**  | `rasterized <- terra::rasterize(shp, raster)`                                                                                                          | `rasterized = rasterize([(geom, 1) for geom in shp.geometry], out_shape=shape, transform=transform)`             |
