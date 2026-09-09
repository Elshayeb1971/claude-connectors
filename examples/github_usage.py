"""
Example usage of the GitHub connector
"""

from connectors import create_github_connector


def main():
    """Example demonstration of GitHub connector"""
    
    # Create connector from environment variables
    # Make sure GITHUB_TOKEN is set
    connector = create_github_connector()
    
    try:
        # Example 1: Get repository information
        print("Fetching repository information...")
        repo = connector.get_repository("Elshayeb1971", "claude-connectors")
        print(f"Repository: {repo['full_name']}")
        print(f"Description: {repo['description']}")
        print()
        
        # Example 2: Search repositories
        print("Searching for repositories...")
        results = connector.search_repositories("claude", per_page=5)
        for repo in results:
            print(f"  - {repo['full_name']}: {repo['description']}")
        print()
        
        # Example 3: Get issues
        print("Fetching open issues...")
        issues = connector.get_issues("Elshayeb1971", "claude-connectors", state="open")
        print(f"Found {len(issues)} open issues")
        for issue in issues:
            print(f"  - #{issue['number']}: {issue['title']}")
        print()
        
        # Example 4: Create an issue
        print("Creating a test issue...")
        new_issue = connector.create_issue(
            "Elshayeb1971",
            "claude-connectors",
            "Test issue from GitHub connector",
            "This is an automated test issue created by the connector."
        )
        print(f"Created issue #{new_issue['number']}: {new_issue['title']}")
        
    finally:
        connector.close()


if __name__ == "__main__":
    main()
