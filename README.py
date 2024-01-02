# -localisation_by_ip
# by cosmosse
import requests

def get_location(ip):
    url = f"http://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = response.json()

    # Extraire les informations de localisation
    city = data.get("city", "N/A")
    region = data.get("region", "N/A")
    country = data.get("country", "N/A")
    location = f"{city}, {region}, {country}"

    return location

def main():
    # Saisir l'adresse IP à localiser
    ip_address = input("Entrez l'adresse IP à localiser : ")

    # Obtenir la localisation
    location = get_location(ip_address)

    # Afficher les résultats
    print(f"Localisation approximative de l'adresse IP {ip_address} : {location}")

if __name__ == "__main__":
    main()
