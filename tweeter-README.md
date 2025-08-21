# Tweeter.py

A simple command-line tool to post tweets (text or image) to Twitter using the Tweepy library.

## Features
- Post a text tweet interactively
- Post a tweet with an image interactively
- Multi-line tweet input supported
- Uses Twitter API credentials from environment variables for security

## Requirements
- Python 3.7+
- [tweepy](https://www.tweepy.org/) (`pip install tweepy`)

## Setup
1. **Clone or copy `tweeter.py` to a directory of your choice.**
2. **Install dependencies:**
   ```bash
   pip install tweepy
   ```
3. **Set your Twitter API credentials as environment variables:**
   ```bash
   export TWITTER_CONSUMER_KEY=your_consumer_key
   export TWITTER_CONSUMER_SECRET=your_consumer_secret
   export TWITTER_ACCESS_TOKEN=your_access_token
   export TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
   ```
   You can add these lines to your `~/.bash_profile`, `~/.bashrc`, or `~/.zshrc` to make them permanent.

## Usage
Run the script from the command line:
```bash
python /path/to/tweeter.py
```
You will be prompted to choose between posting a text tweet or a tweet with an image, and then to enter your content.

## Adding to PATH for Easy Access
To run `tweeter.py` from anywhere, add its directory to your PATH:

1. Make the script executable and add a shebang:
   - Add the following as the first line in `tweeter.py`:
     ```python
     #!/usr/bin/env python3
     ```
   - Make it executable:
     ```bash
     chmod +x /path/to/tweeter.py
     ```
2. Add the script's directory to your PATH. For example, if you put it in `~/bin`:
   - Add this to your `~/.bash_profile`, `~/.bashrc`, or `~/.zshrc`:
     ```bash
     export PATH="$HOME/bin:$PATH"
     ```
3. Now you can run it from anywhere:
   ```bash
   tweeter.py
   ```

## Security Note
Never hardcode your API credentials in the script. Always use environment variables as shown above.

## License
MIT
