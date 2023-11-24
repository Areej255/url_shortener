
import random
import string

# Dictionary to store the mapping of short URLs to original URLs
url_mapping = {}

# defining function to generate short url
def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(7))  # You can change the length as needed
    return short_url

# defining the func 
def shorten_url(original_url):
    # if orig url is in mapping
    if original_url in url_mapping:
        # return that url from the dictionary as a parameter
        return url_mapping[original_url]
    else:
        # otherwise jump to gen_shrt_url func
        short_url = generate_short_url()
        # in mapping dict, orig_url parameter has been passed
        url_mapping[original_url] = short_url
        return short_url
#  defining the func to generate expanded url from the shortened url exists in url mapping previously
def expand_url(short_url):
    for original_url, mapped_short_url in url_mapping.items():
        if short_url == mapped_short_url:
            return original_url
    return "URL not found"

while True:
    print("URL Shortening Service")
    print("1. Shorten URL")
    print("2. Expand URL")
    print("3. Quit")

    choice = input("Enter your choice (1 or 2 or 3): ")

    if choice == "1":
        original_url = input("Enter the original URL: ")
        short_url = shorten_url(original_url)
        print(f"Shortened URL: http://myshortener.com/{short_url}")  # Replace with your domain
    elif choice == "2":
        short_url = input("Enter the short URL: ")
        original_url = expand_url(short_url)
        print(f"Expanded URL: {original_url}")
    elif choice == "3":
        break
    else:
        print("Your choice is invalid. Please choose 1, 2, or 3.")