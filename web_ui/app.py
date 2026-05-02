from flask import Flask, request, render_template
import dns.resolver
import socket

app = Flask(__name__)

DNS_SERVER = "bind9_dns"

def dns_lookup(domain):
    try:
        resolver = dns.resolver.Resolver()
        
        # Resolve the Docker service name to its internal IP
        # Use the service name 'dns-server' from your yaml
        server_ip = socket.gethostbyname("dns-server") 
        
        resolver.nameservers = [server_ip]
        answer = resolver.resolve(domain, "A")
        return answer[0].to_text()
    except Exception as e:
        return f"Lookup failed: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    domain = ""

    if request.method == "POST":
        domain = request.form["domain"]
        result = dns_lookup(domain)

    return render_template("index.html", result=result, domain=domain)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)