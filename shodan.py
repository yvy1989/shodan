import requests

API_KEY = input("Favor digite a sua API Key:\n")
query = input("Agora insira a sua pesquisa no shodan para receber os endereços IP's:\n")
ip_limit = int(input("Digite um numero inteiro de resultados que voce gostaria de obter:\n"))

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