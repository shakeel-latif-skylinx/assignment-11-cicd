# CI/CD Reflection

**What does each stage protect against?**

The lint stage catches style and formatting issues (and some common bugs) before they enter the codebase, keeping the project consistent and readable. The test stage verifies that the API behaves correctly — endpoints return the right status codes, data is created and listed properly, and invalid input is rejected. The deploy stage simulates shipping code to production; in a real setup it would only run after quality checks pass, so broken code never reaches users.

**Why does the order matter?**

If deploy ran before test (or without waiting for test to succeed), broken or untested code could go live. A failing test or lint error would be ignored, and users would hit bugs that CI was meant to catch. Running lint and test first, then deploy only when both pass, ensures only verified code is released.

**One thing to add for production:**

I would add a test matrix across Python 3.10, 3.11, and 3.12, plus branch protection on `main` so pull requests cannot merge unless the CI workflow passes. Optionally, containerize with Docker and deploy to a real host (e.g., Render or Railway) using secrets for API keys instead of a simulated echo step.
