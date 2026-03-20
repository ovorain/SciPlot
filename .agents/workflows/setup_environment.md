---
description: Create and configure the Conda environment for scientific plotting
---

# Deploy Scientific Plotting Environment

This workflow executes an automated pipeline to install all necessary Python plotting libraries (Matplotlib, Numpy, etc.) through the provided Conda configuration mapping.

// turbo-all

1. Verify that Conda is installed and accessible:

```powershell
conda --version
```

2. Create the environment unconditionally from the YAML definition:

```powershell
conda env create -f environment.yml
```

3. If requested by the user or as a sanity check, list the packages inside the newly built environment:

```powershell
conda list -f matplotlib
```
