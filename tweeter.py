from __future__ import print_function
import os
import tweepy

# TODO: Refactor and improve features. Consider adding a README.md with usage instructions, including how to add this script to the PATH for easier posting.


def get_status() -> str:
    """Prompt user for multi-line status input. End input with an empty line."""
    lines = []
    print("Enter your text (end with an empty line):")
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line:
            lines.append(line)
        else:
            break
    return "\n".join(lines)


def tweet_text(api: tweepy.API, user) -> None:
    """Prompt user for tweet text and post it."""
    tweet = get_status()
    try:
        api.update_status(tweet)
        print("\nTweet posted successfully!")
    except Exception as e:
        print(f"Error posting tweet: {e}")


def tweet_picture(api: tweepy.API, user) -> None:
    """Prompt user for picture path and status, then post tweet with image."""
    pic = os.path.abspath(input(f"Enter the picture path, {user.name}: "))
    title = get_status()
    try:
        api.update_with_media(pic, status=title)
        print("\nTweet with picture posted successfully!")
    except Exception as e:
        print(f"Error posting tweet with picture: {e}")


def initialize_api() -> tuple[tweepy.API, object]:
    """Initialize and return Tweepy API and user objects using environment variables for credentials."""
    ck = os.getenv("TWITTER_CONSUMER_KEY")
    cks = os.getenv("TWITTER_CONSUMER_SECRET")
    at = os.getenv("TWITTER_ACCESS_TOKEN")
    ats = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    if not all([ck, cks, at, ats]):
        raise RuntimeError("Twitter API credentials not set in environment variables.")

    auth = tweepy.OAuthHandler(ck, cks)
    auth.set_access_token(at, ats)
    api = tweepy.API(auth)
    user = api.me()
    return api, user


def main() -> None:
    """Main entry point for the tweeter script."""
    try:
        choice = input("\n1. Text\n2. Picture\nChoose option (1/2): ").strip()
        api, user = initialize_api()

        if choice == "1":
            tweet_text(api, user)
        elif choice == "2":
            tweet_picture(api, user)
        else:
            print("Invalid option. Please choose 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except RuntimeError as e:
        print(e)
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
