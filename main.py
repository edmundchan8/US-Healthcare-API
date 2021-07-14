import requests
from pprint import pprint

# ACCESSIBILITY_ENDPOINT = "https://www.healthcare.gov/accessibility.json"
HEALTHCARE_API_ENDPOINT = "https://www.healthcare.gov/api"
# ARTICLES_ENDPOINT = f"{HEALTHCARE_API_ENDPOINT}/articles.json"
INDEX_ENDPOINT = f"{HEALTHCARE_API_ENDPOINT}/index.json"

keep_running = True

banned_words = ["I", "am", "and", "what", "who", "you", "me", "they", "he", "him", "she", "her", "it", "or", "be",
                "so", "can", "could", "how", "where", "why", "when", "should", "shall", "do", "which", "would",
                "since", "here", "you", "what", "us", "the", "most", "of", "say", "is", "for", "a", "to", "have",
                "does", "anything", "make", "more", "less", "everything", "go", "get", "got", "my", "mine"]

while keep_running:
    search_params = input("Enter in something you want to know about US Healthcare: ")

    updated_search_params = search_params.split()

    final_search_params = [word for word in updated_search_params if word.lower() not in banned_words]
    index_response = requests.get(url=INDEX_ENDPOINT)
    index_response.raise_for_status()
    index_data = index_response.json()

    index_list = []

    for title in index_data:
        for word in final_search_params:
            if word.lower() in title['bite'].lower():
                index_list.append(title)

    for each_index in index_list:
        print(each_index['title'])
        print(f"https://www.healthcare.gov{each_index['url']}")
        print("")

    if len(index_list) < 1:
        print("No search results found, please try again")
    else:
        print(f"Number of results: {len(index_list)}")

    if search_params == "Exit":
        keep_running = False