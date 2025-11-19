"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Write a tutorial on using GitHub for version control, inspired by the various FOSS@RIT members who actively contribute to GitHub.
Generated: DETERMINISTIC_6b83de41009ae2c1
Batch ID: 20250612_163408
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://cli.github.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/original-owner/repository.git": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-username/repository.git": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/username/repository.git": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

Here's a Markdown file (`github_tutorial.md`) that serves as a tutorial for using GitHub, following the requested guidelines:

```markdown
# GitHub Version Control Tutorial

```bash
# Initialize a new Git repository
git init

# Check the status of your repository
git status

# Stage all changes for commit
git add .

# Commit changes with a descriptive message
git commit -m "Initial commit with project structure"

# Add a remote repository (replace with your GitHub repo URL)
git remote add origin https://github.com/username/repository.git

# Push changes to the main branch
git push -u origin main
```

## Common Workflow

### 1. Cloning a Repository
```bash
# Clone an existing repository
git clone https://github.com/username/repository.git
```

### 2. Creating a Branch
```bash
# Create and switch to a new branch
git checkout -b feature-branch
```

### 3. Making Changes
```bash
# After making file changes, stage them
git add filename.ext

# Commit with a meaningful message
git commit -m "Add new feature implementation"
```

### 4. Pushing Changes
```bash
# Push your branch to GitHub
git push origin feature-branch
```

### 5. Creating a Pull Request
```bash
# After pushing, create a PR on GitHub website
# Then fetch and merge changes from main
git fetch origin
git merge origin/main
```

## Advanced Features

### Resolving Merge Conflicts
```bash
# When conflicts occur, edit the files to resolve them
git add resolved-file.ext
git commit -m "Resolve merge conflicts"
```

### Stashing Changes
```bash
# Temporarily save uncommitted changes
git stash

# Later, reapply them
git stash pop
```

### Rebasing
```bash
# Rebase your branch onto main
git checkout feature-branch
git rebase main
```

## Best Practices

1. **Commit Often**: Small, frequent commits with clear messages
2. **Branch Naming**: Use descriptive names like `fix/login-validation`
3. **Pull Requests**: Include context and testing details
4. **Code Reviews**: Review others' code and welcome feedback

## GitHub-Specific Features

```bash
# Fork a repository (done on GitHub website)
# Then clone your fork
git clone https://github.com/your-username/repository.git

# Add upstream remote
git remote add upstream https://github.com/original-owner/repository.git

# Sync your fork
git fetch upstream
git merge upstream/main
```

## Troubleshooting

```bash
# View commit history
git log --oneline --graph

# Undo local changes
git checkout -- filename.ext

# Reset to previous commit (caution: destructive)
git reset --hard HEAD~1
```

## GitHub CLI (Alternative)

```bash
# Install GitHub CLI (https://cli.github.com)
# Authenticate
gh auth login

# Create a new repository
gh repo create

# Create a pull request
gh pr create
```

## Final Notes

1. Always pull before pushing
2. Write clear commit messages
3. Use `.gitignore` for files not to track
4. Regularly sync with upstream repositories
```
