import requests

def test_check_paths():
    # run the MCP server
    # python -u myapp_mcp_tools.py

    # check paths
    base_url = "http://127.0.0.1:8000"
    paths = ["/sse", "/mcp/sse", "/api/sse", "/v1/sse", "/messages", "/"]
    
    for path in paths:
        url = base_url + path
        try:
            print(f"Checking {url}...")
            response = requests.get(url, timeout=2)
            print(f"Status: {response.status_code}")
            if response.status_code != 404:
                print(f"Possible match: {url}")
        except Exception as e:
            print(f"Error connecting to {url}: {e}")
