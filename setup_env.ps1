# Auto-Setup Script for Windows Users
Write-Host ">>> Starting Scientific Plotting Environment Setup..." -ForegroundColor Cyan

# Check if conda is installed
$condaCheck = Get-Command conda -ErrorAction SilentlyContinue
if (-not $condaCheck) {
    Write-Host "[!] Conda is not found in your PATH. Please install Miniconda or Anaconda first." -ForegroundColor Red
    exit 1
}

Write-Host ">>> Building environment from environment.yml..." -ForegroundColor Cyan
conda env create -f environment.yml

if ($LASTEXITCODE -eq 0) {
    Write-Host ">>> Setup Complete!" -ForegroundColor Green
    Write-Host "Please actiavte the environment by running: conda activate (env_name)" -ForegroundColor Yellow
} else {
    Write-Host ">>> Conda environment creation failed or environment already exists." -ForegroundColor Red
}
