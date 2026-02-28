This is a Python-based Deep Packet Inspection (DPI) tool built using mitmproxy. It acts as a "Man-in-the-Middle" (MitM) service that intercepts, logs, and modifies network traffic (HTTP/HTTPS) in real-time.

🚀 Features
Real-time Interception: Captures every request sent from the browser/client.

Request Redirection: Automatically reroutes traffic (e.g., redirecting google.com to bing.com).

Deep Content Inspection: Scans the response body (HTML/Data) and modifies specific strings on the fly.

Byte-level Manipulation: Handles raw data streams to ensure compatibility with various web encodings.

🛠️ Prerequisites
Before running the script, ensure you have the following installed:

Python 3.8+

mitmproxy: The intercepting proxy engine.

```Bash
pip install mitmproxy
```



Project Structure
dpi_engine.py: The main Python logic for intercepting and modifying packets.

README.md: Project documentation and setup guide.

🚦 Getting Started
1. Run the Proxy
In your terminal, navigate to the project folder and run:

```Bash
mitmdump -s dpi_engine.py
```

The proxy will start listening on port 8080 by default.

2. Configure Your System
To allow the proxy to "open the envelope" of encrypted traffic, you must:

Set your browser or system proxy to 127.0.0.1 on port 8080.

Open your browser and visit mitm.it.

Download and install the CA Certificate for your Operating System.

3. Test the Script
Open your browser and go to google.com.

Observe the terminal: You will see "Scam alert! Redirecting Google to Bing."

Check the webpage: Any instance of the word "Google" will be replaced with "Python Proxy".

🧠 How it Works
Request Phase: The script checks flow.request.pretty_host. If it matches the target, it modifies the destination header.

Response Phase: The script waits for the server to send data back. It then performs a binary replace on flow.response.content before the data ever reaches your browser.
