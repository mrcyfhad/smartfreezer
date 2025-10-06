# 🧊 SmartFreezer Runbook

## 1. Overview
SmartFreezer monitors freezer temperature and handles offline data.  
This runbook describes how to deploy, rollback, and troubleshoot the application.

---

## 2. Deployment Steps

1. **Ensure all tests and lint checks pass locally:**

```bash
flake8 src/
coverage run -m pytest && coverage report -m


2.Build and tag the Docker image:

docker build -t smartfreezer:latest .
docker tag smartfreezer:latest ghcr.io/mercy korir/smartfreezer:latest

3.Push to GitHub:

git add .
git commit -m "Deploy version X.Y.Z"
git push

4.GitHub Actions will automatically:

run CI checks,
build the Docker image, and
optionally push it to the container registry.


3. Rollback Procedure

If deployment fails:

1.Identify the last stable commit:

git log --oneline

2.Revert to that commit:

git revert <commit-hash>
git push

3.Confirm CI passes and redeploy.


4. Observability Checks
Logs: View logs via
docker logs smartfreezer
Metrics: Check offline_handler.log() entries in the console or monitoring dashboard.
Alerts: If offline data grows too large, trigger an alert or auto-cleanup.


5. Troubleshooting
Issue	Cause	Fix
CI fails	Lint or coverage below 80%	Run flake8 and add tests
App crash on startup	Missing dependencies	Run pip install -r requirements.txt
Docker build error	Invalid CMD or missing file	Check Dockerfile paths


6. Rollback Verification
After rollback, confirm:
container restarts cleanly (docker ps)
previous version responds normally
no data loss in offline queue


7. Owner / Contact
Maintainer: mercy korir
Repo: https://github.com/mrcyfhad/smartfreezer


