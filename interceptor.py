from remote  import http

def request(flow: http.HTTPFlow) -> None:
    # 1. Log the URL to the console
    print(f"Intercepted request to: {flow.request.pretty_url}")

    # 2. Modify the request on the fly
    if "google.com" in flow.request.pretty_host:
        flow.request.host = "bing.com"
        print("Scam alert! Redirecting Google to Bing.")

def response(flow: http.HTTPFlow) -> None:
    # 3. Modify the data coming back from the website
    # This replaces the word 'Google' with 'Python Proxy' in the HTML
    if flow.response and flow.response.content:
        flow.response.content = flow.response.content.replace(b"Google", b"Python Proxy")