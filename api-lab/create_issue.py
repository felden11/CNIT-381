import os
import json
import os
import requests # type: ignore
from urllib import error, request

TOKEN = os.environ["GITHUB_TOKEN"]

USERNAME = "felden11"
REPO = "CNIT-381"

url = f"https://api.github.com/repos/{USERNAME}/{REPO}/issues"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "User-Agent": USERNAME,
    "Content-Type": "application/json",
}

payload = {
    "title": "Created from the CNIT 381 API lab",
    "body": "This issue was created with a POST request from Python.",
}

request_data = json.dumps(payload).encode("utf-8")
req = request.Request(url, data=request_data, headers=headers, method="POST")

try:
    with request.urlopen(req) as resp:
        issue = json.loads(resp.read().decode("utf-8"))
except error.HTTPError as exc:
    details = exc.read().decode("utf-8", errors="replace")
    raise RuntimeError(f"GitHub API request failed: {exc.code} {details}") from exc

print("Created issue #", issue["number"])
print("View it at:", issue["html_url"])


TOKEN = os.environ["GITHUB_TOKEN"]

USERNAME = "felden11"
REPO = "CNIT-381"

url = f"https://api.github.com/repos/{USERNAME}/{REPO}/issues"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "User-Agent": USERNAME,
}

payload = {
    "title": "Created from the CNIT 381 API lab",
    "body": "This issue was created with a POST request from Python.",
}

resp = requests.post(url, headers=headers, json=payload)
resp.raise_for_status()

issue = resp.json()

print("Created issue #", issue["number"])
print("View it at:", issue["html_url"])