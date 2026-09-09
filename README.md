# Claude Connectors

A collection of connectors for integrating Claude with various platforms and services.

## Features

- **GitHub Connector**: Full integration with GitHub API for repositories, issues, pull requests, and more

## Installation

```bash
pip install -r requirements.txt
```

## Getting Started

### GitHub Connector

The GitHub connector enables Claude to interact with GitHub repositories, issues, and pull requests.

#### Setup

1. Create a GitHub Personal Access Token:
   - Go to GitHub Settings → Developer settings → Personal access tokens
   - Create a new token with appropriate scopes (repo, read:user, etc.)

2. Set the environment variable:
   ```bash
   export GITHUB_TOKEN="your_token_here"
   ```

#### Usage

```python
from connectors import create_github_connector

# Create connector
connector = create_github_connector()

# Get repository information
repo = connector.get_repository("owner", "repo")

# Search repositories
repos = connector.search_repositories("python")

# Get issues
issues = connector.get_issues("owner", "repo", state="open")

# Get pull requests
prs = connector.get_pull_requests("owner", "repo")

# Create an issue
issue = connector.create_issue("owner", "repo", "Issue Title", "Issue description")

# Get file content
content = connector.get_file_content("owner", "repo", "path/to/file.txt")

# Close connector
connector.close()
```

## API Reference

### GitHubConnector

#### Methods

- `get_repository(owner: str, repo: str) -> Dict[str, Any]`
  - Fetch repository information

- `search_repositories(query: str, per_page: int = 10) -> List[Dict[str, Any]]`
  - Search for repositories

- `get_issues(owner: str, repo: str, state: str = "open") -> List[Dict[str, Any]]`
  - Fetch issues from a repository

- `get_pull_requests(owner: str, repo: str, state: str = "open") -> List[Dict[str, Any]]`
  - Fetch pull requests from a repository

- `create_issue(owner: str, repo: str, title: str, body: Optional[str] = None) -> Dict[str, Any]`
  - Create a new issue

- `get_file_content(owner: str, repo: str, path: str) -> str`
  - Fetch file content from a repository

- `close()`
  - Close the connector session

## Examples

See the `examples/` directory for more detailed usage examples.

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
