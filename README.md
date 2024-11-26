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
import rasterio               # For raster operations
import geopandas as gpd       # For vector data
import numpy as np            # For numerical data
import pandas as pd           # For tabular data manipulation
```
