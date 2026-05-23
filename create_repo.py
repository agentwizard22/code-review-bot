import requests
import json

# GitHub credentials
username = "agentwizard22"
password = "agentbalon22"

# Repository details
repo_data = {
    "name": "code-review-bot",
    "description": "Multi-Agent AI Code Review System powered by Xiaomi MiMo V2.5 - Automated bug detection, style checking, and security scanning",
    "private": False,
    "has_issues": True,
    "has_projects": True,
    "has_wiki": True
}

print("🚀 Creating GitHub repository via API...")

# Create repository
response = requests.post(
    "https://api.github.com/user/repos",
    auth=(username, password),
    json=repo_data,
    headers={"Accept": "application/vnd.github.v3+json"}
)

if response.status_code == 201:
    repo = response.json()
    print(f"✅ Repository created successfully!")
    print(f"   Name: {repo['name']}")
    print(f"   URL: {repo['html_url']}")
    print(f"   Clone URL: {repo['clone_url']}")
    print(f"\n📦 Repository: {repo['html_url']}")
else:
    print(f"❌ Failed to create repository")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text}")

