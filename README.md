# News Email Sender

This project contains two Python scripts that fetch the latest business news from the NewsAPI and send it via email.

## Files

1. **send_email.py**
   - Contains the `send_email` function that sends an email using the Gmail SMTP server.

2. **main.py**
   - Fetches the latest business news from the NewsAPI.
   - Formats the news into an email-friendly format.
   - Sends the formatted news via email using the `send_email` function from `send_email.py`.

## Prerequisites

- Python 3.x
- `requests` library for making HTTP requests
- `smtplib` and `ssl` libraries for sending emails (part of Python's standard library)
- NewsAPI key (You can get one from https://newsapi.org/)
- A Gmail account with "Less secure app access" enabled or an App Password if two-factor authentication (2FA) is enabled.

## Setup

1. **Clone the repository**:

   ```sh
   git clone https://github.com/yourusername/news-email-sender.git
   cd news-email-sender
   ```

2. **Install dependencies**:

   ```sh
   pip install requests
   ```

3. **Update email credentials and NewsAPI key**:
   - Open `send_email.py` and update the `username`, `password`, and `receiver` variables with your Gmail credentials and the recipient's email address.
   - Open `main.py` and update the `api_key` variable with your NewsAPI key.

## Usage

You can run the script manually to fetch the latest news and send an email:

```sh
python main.py
```

This will fetch the latest business news and send an email to the specified recipient.



## License

This project is licensed under the MIT License.
