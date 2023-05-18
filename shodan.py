import requests

api_key = input("Favor digite a sua API Key:\n")
search_query = input("Agora insira a sua pesquisa no shodan para receber os endereços IP's:\n")


# Send a request to the Shodan API
response = requests.get(f"https://api.shodan.io/shodan/host/search?key={api_key}&query={search_query}")

# Parse the JSON response and extract the IP addresses
data = response.json()
ip_addresses = [result['ip_str'] for result in data['matches']]

# Print the IP addresses
for ip in ip_addresses:
    print(ip)