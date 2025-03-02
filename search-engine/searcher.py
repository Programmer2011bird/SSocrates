from bs4 import BeautifulSoup
import requests
import json


def parse_json(json_file:str) -> list[dict[str,str]]:
    with open(json_file, "r+") as file:
        json_content: str = file.read()

    json_dict: list[dict[str, str]] = json.loads(json_content)
    return json_dict

def search_sites_by_category(category: str) -> list[str]:
    websites: list[dict[str,str]] = parse_json("websites.json")
    matching_websites: list[str] = []

    for website in websites:
        if website["category"] == "all" or website["category"] == category:
            matching_websites.append(website["url"])

    return matching_websites

def search_query(website:str):
    response: requests.Response = requests.get(website)
    soup = BeautifulSoup(response.text, "html.parser")
    inputs = soup.find_all("input")
    print(inputs[0])


if __name__ == "__main__":
    # print(parse_json("websites.json"))
    # print(search_sites_by_category(category="all"))
    search_query("https://coursera.org")

