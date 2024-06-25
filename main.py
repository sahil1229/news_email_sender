import requests
from send_email import send_email

api_key = "your_api_key"
url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}"


response = requests.get(url)


if response.status_code == 200:

    content = response.json()


    if "articles" in content:
        body = "Subject: Today's news" + "\n"
        for article in content["articles"][0:20]:
            title = article.get("title", "")
            description = article.get("description", "")
            url = article.get("url", "")

            if title is None:
                title = "No title available"
            if description is None:
                description = "No description available"
            if url is None:
                url = "No description available"

            body = body + title + "\n" + description + "\n" + url + 2 * "\n"

        print(body)

        body = body.encode("utf-8")
        send_email(message=body)
    else:
        print("No articles found in the response.")
else:
    print(f"Failed to retrieve news articles. Status code: {response.status_code}")
