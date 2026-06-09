# Contributing Guide

## Branch Strategy

* main → Production branch
* feature-login → Login feature
* feature-dashboard → Dashboard feature
* feature-a → Conflict simulation
* feature-b → Conflict simulation

## Workflow

1. Create feature branch from main.
2. Develop feature.
3. Commit changes.
4. Push branch to GitHub.
5. Open Pull Request.
6. Review code.
7. Resolve conflicts if any.
8. Merge to main.
9. Create release tag.

## Pull Request Rules

* Use descriptive commit messages.
* One feature per branch.
* Resolve merge conflicts before merge.
* All changes must go through PR review.

## Release Process

After successful testing:

git tag -a v1.0 -m "Release"

Push tag:

git push origin v1.0
