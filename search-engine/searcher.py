from bs4 import BeautifulSoup
import requests
import json


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
    
    for site in sites:
        print(site["search_url"])


if __name__ == "__main__":
    # print(parse_json("websites.json"))
    # print(search_sites_by_category(category="all"))
    search_query(search_query="math", category="math")

