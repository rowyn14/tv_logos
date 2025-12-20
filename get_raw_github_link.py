"""
Convert GitHub browser URLs to raw GitHub links.

This module provides functionality to transform GitHub web interface URLs
into raw.githubusercontent.com URLs for direct file access.
"""

import re
import sys
from typing import Optional
from urllib.parse import urlparse


class GitHubLinkConverter:
    """Convert GitHub browser URLs to raw GitHub content URLs."""

    # Supported GitHub URL patterns
    GITHUB_URL_PATTERN = re.compile(
        r'https?://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+)/'
        r'(blob|raw)/(?P<branch>[^/]+)/(?P<path>.+)$'
    )
    RAW_GITHUB_URL_TEMPLATE = (
        'https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}'
    )

    @staticmethod
    def is_valid_github_url(url: str) -> bool:
        """
        Check if the provided URL is a valid GitHub URL.

        Args:
            url: The URL to validate

        Returns:
            True if the URL matches GitHub format, False otherwise
        """
        return bool(GitHubLinkConverter.GITHUB_URL_PATTERN.match(url))

    @staticmethod
    def sanitize_url(url: str) -> str:
        """
        Sanitize the input URL by stripping whitespace.

        Args:
            url: The URL to sanitize

        Returns:
            The sanitized URL
        """
        return url.strip()

    @staticmethod
    def convert_to_raw(url: str) -> Optional[str]:
        """
        Convert a GitHub browser URL to a raw GitHub URL.

        Handles URLs in the following formats:
        - https://github.com/owner/repo/blob/branch/path/to/file
        - https://github.com/owner/repo/raw/branch/path/to/file

        Args:
            url: The GitHub URL to convert

        Returns:
            The raw GitHub URL if conversion is successful, None otherwise
        """
        sanitized_url = GitHubLinkConverter.sanitize_url(url)

        match = GitHubLinkConverter.GITHUB_URL_PATTERN.match(sanitized_url)
        if not match:
            return None

        groups = match.groupdict()
        raw_url = GitHubLinkConverter.RAW_GITHUB_URL_TEMPLATE.format(**groups)
        return raw_url


def main() -> None:
    """Main entry point for the script."""
    print("GitHub Link Converter")
    print("=" * 50)
    print("Enter a GitHub browser URL to convert it to a raw link.")
    print("Type 'quit' or 'exit' to exit.\n")

    while True:
        try:
            user_input = input("Paste GitHub URL: ").strip()

            if user_input.lower() in ('quit', 'exit', 'q'):
                print("Goodbye!")
                break

            if not user_input:
                print("Please enter a valid URL.\n")
                continue

            raw_link = GitHubLinkConverter.convert_to_raw(user_input)

            if raw_link:
                print(f"\nRaw GitHub Link:\n{raw_link}\n")
            else:
                print(
                    "Error: Invalid GitHub URL format. "
                    "Please use a GitHub browser link.\n"
                )

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"An error occurred: {e}\n")


if __name__ == '__main__':
    main()
