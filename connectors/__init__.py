"""
Claude Connectors Package

This package provides connectors for integrating Claude with various platforms
and services including GitHub, and more.
"""

from connectors.github import GitHubConnector, GitHubConfig, create_github_connector

__all__ = [
    "GitHubConnector",
    "GitHubConfig",
    "create_github_connector",
]

__version__ = "0.1.0"
