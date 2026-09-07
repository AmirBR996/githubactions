# GitHub Actions CI/CD Demo

This repository is focused on GitHub Actions and CI/CD workflows. It demonstrates a simple pipeline that validates changes on every push and pull request to `main`.

## Workflow

The main workflow is defined in [.github/workflows/python-app.yml](.github/workflows/python-app.yml).

It currently:

- triggers on `push` and `pull_request` events against `main`
- runs on `ubuntu-latest`
- sets up Python 3.11
- installs dependencies from [requirement.txt](requirement.txt)
- runs the test suite with `pytest`

## CI/CD purpose

The goal of this repo is to show how GitHub Actions can be used to:

- automate validation on every change
- keep the main branch protected by test runs
- provide a repeatable pipeline for continuous integration
- serve as a starting point for adding deployment steps later

## Repository layout

```text
.github/workflows/python-app.yml
README.md
requirement.txt
src/
tests/
```

## Extending the workflow

Typical next steps for a CI/CD pipeline include:

- adding linting or formatting checks
- running tests across multiple Python versions
- publishing build artifacts
- deploying to a hosting platform after successful validation

## Notes

- Keep workflow changes small and reviewable.
- Treat the workflow file as the source of truth for automation behavior.