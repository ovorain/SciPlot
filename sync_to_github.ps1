# GitHub Sync Script
# Usage: .\sync_to_github.ps1 "Commit message"

param (
    [string]$Message = "Update plotting framework"
)

$remote = git remote get-url origin 2>$null
if (-not $remote) {
    Write-Host "Warning: No GitHub remote URL configured." -ForegroundColor Yellow
    Write-Host "Please run: git remote add origin <URL>"
    exit 1
}

Write-Host "Staging changes..." -ForegroundColor Cyan
git add .

Write-Host "Committing changes: $Message" -ForegroundColor Cyan
git commit -m "$Message"

Write-Host "Pushing to GitHub..." -ForegroundColor Cyan
git push origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "Sync successful!" -ForegroundColor Green
} else {
    Write-Host "Sync failed. Check your network or permissions." -ForegroundColor Red
}
