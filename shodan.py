import requests

API_KEY = input("Enter your API Key:\n")
query = input("Now enter your search in shodan to receive IP addresses:\n")
ip_limit = int(input("Enter an integer number of results you would like to get:\n"))

url = f"https://api.shodan.io/shodan/host/search?key={API_KEY}&query={query}"

response = requests.get(url)
data = response.json()

# Extract the IP addresses from the response, limited by the variable
ip_addresses = [result['ip_str'] for result in data['matches'][:ip_limit]]

# Iterate over the IP addresses and fetch detailed information for each IP
for ip in ip_addresses:
    details_url = f"https://api.shodan.io/shodan/host/{ip}?key={API_KEY}"
    details_response = requests.get(details_url)
    details_data = details_response.json()

    # Extract the open ports from the detailed information
    open_ports = details_data.get('ports', [])

    # Print the IP address and its open ports
    print(f"IP: {ip}")
    print("Open Ports:")
    for port in open_ports:
        print(port)
    print("----------------------")
