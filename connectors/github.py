"""
GitHub Connector for Claude

This module provides integration between Claude and GitHub,
enabling access to repositories, issues, pull requests, and more.
"""

import os
from typing import Optional, Dict, Any, List
import requests
from dataclasses import dataclass


@dataclass
class GitHubConfig:
    """Configuration for GitHub connector"""
    token: str
    base_url: str = "https://api.github.com"
    timeout: int = 30


class GitHubConnector:
    """
    A connector class for interacting with GitHub API.
    
    This connector allows Claude to:
    - Search repositories
    - Fetch repository information
    - List issues and pull requests
    - Create and update issues
    - Manage repository contents
    """
    
    def __init__(self, config: GitHubConfig):
        """
        Initialize the GitHub connector.
        
        Args:
            config: GitHubConfig object with authentication and settings
        """
        self.config = config
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"token {config.token}",
            "Accept": "application/vnd.github.v3+json"
        })
    
    def get_repository(self, owner: str, repo: str) -> Dict[str, Any]:
        """
        Fetch repository information.
        
        Args:
            owner: Repository owner username
            repo: Repository name
            
        Returns:
            Repository data dictionary
        """
        url = f"{self.config.base_url}/repos/{owner}/{repo}"
        response = self.session.get(url, timeout=self.config.timeout)
        response.raise_for_status()
        return response.json()
    
    def search_repositories(self, query: str, per_page: int = 10) -> List[Dict[str, Any]]:
        """
        Search for repositories on GitHub.
        
        Args:
            query: Search query
            per_page: Number of results per page
            
        Returns:
            List of repository data dictionaries
        """
        url = f"{self.config.base_url}/search/repositories"
        params = {"q": query, "per_page": per_page}
        response = self.session.get(url, params=params, timeout=self.config.timeout)
        response.raise_for_status()
        return response.json().get("items", [])
    
    def get_issues(self, owner: str, repo: str, state: str = "open") -> List[Dict[str, Any]]:
        """
        Fetch issues from a repository.
        
        Args:
            owner: Repository owner username
            repo: Repository name
            state: Issue state ('open', 'closed', 'all')
            
        Returns:
            List of issue data dictionaries
        """
        url = f"{self.config.base_url}/repos/{owner}/{repo}/issues"
        params = {"state": state}
        response = self.session.get(url, params=params, timeout=self.config.timeout)
        response.raise_for_status()
        return response.json()
    
    def get_pull_requests(self, owner: str, repo: str, state: str = "open") -> List[Dict[str, Any]]:
        """
        Fetch pull requests from a repository.
        
        Args:
            owner: Repository owner username
            repo: Repository name
            state: PR state ('open', 'closed', 'all')
            
        Returns:
            List of pull request data dictionaries
        """
        url = f"{self.config.base_url}/repos/{owner}/{repo}/pulls"
        params = {"state": state}
        response = self.session.get(url, params=params, timeout=self.config.timeout)
        response.raise_for_status()
        return response.json()
    
    def create_issue(self, owner: str, repo: str, title: str, body: Optional[str] = None) -> Dict[str, Any]:
        """
        Create an issue in a repository.
        
        Args:
            owner: Repository owner username
            repo: Repository name
            title: Issue title
            body: Issue description (optional)
            
        Returns:
            Created issue data dictionary
        """
        url = f"{self.config.base_url}/repos/{owner}/{repo}/issues"
        payload = {"title": title}
        if body:
            payload["body"] = body
        
        response = self.session.post(url, json=payload, timeout=self.config.timeout)
        response.raise_for_status()
        return response.json()
    
    def get_file_content(self, owner: str, repo: str, path: str) -> str:
        """
        Fetch file content from a repository.
        
        Args:
            owner: Repository owner username
            repo: Repository name
            path: File path in repository
            
        Returns:
            File content as string
        """
        url = f"{self.config.base_url}/repos/{owner}/{repo}/contents/{path}"
        response = self.session.get(url, timeout=self.config.timeout)
        response.raise_for_status()
        
        import base64
        data = response.json()
        if "content" in data:
            return base64.b64decode(data["content"]).decode("utf-8")
        return data.get("content", "")
    
    def close(self):
        """Close the connector session"""
        self.session.close()


def create_github_connector() -> GitHubConnector:
    """
    Factory function to create a GitHub connector from environment variables.
    
    Environment Variables:
        GITHUB_TOKEN: GitHub personal access token
        GITHUB_API_URL: Optional custom GitHub API URL (defaults to https://api.github.com)
    
    Returns:
        Initialized GitHubConnector instance
        
    Raises:
        ValueError: If GITHUB_TOKEN is not set
    """
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN environment variable is required")
    
    base_url = os.getenv("GITHUB_API_URL", "https://api.github.com")
    
    config = GitHubConfig(token=token, base_url=base_url)
    return GitHubConnector(config)
