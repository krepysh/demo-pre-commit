## Pre-requirements
Install pre-commit with pip, pipx, or brew:
```bash
pip install pre-commit
```
## Step 1
Generate pre-commit config file:
```bash
pre-commit sample-config > .pre-commit-config.yaml
```
## Step 2
Try to run pre-commit:
```bash
pre-commit run --all-files
# or the same:
pre-commit run -a
```
## Step 3
Use example config file to add hooks to your project:
```bash
cp ./examples/.pre-commit-config.yaml ./
```

## Step 4
Fix files with pre-commit:
```bash
pre-commit run -a
```

## Step 5
Install hooks to your repo:
```bash
pre-commit install
```

## Step 6
Add pre-commit to your CI:
```bash
mkdir -p .github/workflows
cp ./examples/pre-commit.yml .github/workflows/
```

