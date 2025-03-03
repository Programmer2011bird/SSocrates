from bs4 import BeautifulSoup
import requests
import json

from requests.exceptions import SSLError


def parse_json(json_file:str) -> list[dict[str,str]]:
    with open(json_file, "r+") as file:
        json_content: str = file.read()

    json_dict: list[dict[str, str]] = json.loads(json_content)
    return json_dict

def search_sites_by_category(category: str) -> list[dict[str,str]]:
    websites: list[dict[str,str]] = parse_json("websites.json")
    matching_websites: list[dict[str,str]] = []

    for website in websites:
        if website["category"] == "all" or website["category"] == category:
            matching_websites.append(website)

    return matching_websites

def search_query(search_query: str, category: str):
    sites: list[dict[str,str]] = search_sites_by_category(category)
    passed_sites: list[str] = []
    
    for site in sites:
        search_url: str = site["search_url"]
        search_url = search_url.format(query=search_query)
        
        try:
            RESPONSE: requests.Response = requests.get(search_url, allow_redirects=False)
            requests.session().max_redirects = 100

            print(search_url, RESPONSE.status_code)

            if RESPONSE.status_code:
                passed_sites.append(search_url)

        except SSLError:
            pass
    
    return passed_sites


if __name__ == "__main__":
    # print(parse_json("websites.json"))
    # print(search_sites_by_category(category="all"))
    print(search_query(search_query="math", category="math"))

