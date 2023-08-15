import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Scopes required to access the YouTube API
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Scopes required to access the YouTube API
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def get_authenticated_service():
    creds = None

    # Load or create credentials
    if os.path.exists("token.json"):
        creds = InstalledAppFlow.from_client_secrets_file("client_secrets.json", SCOPES).run_local_server(port=0)
        # Save the credentials for future use
        with open("token.json", "w") as token:
            token.write(creds.to_json())  # Serialize the Credentials object to JSON
    else:
        flow = InstalledAppFlow.from_client_secrets_file("client_secrets.json", SCOPES)
        creds = flow.run_local_server(port=0)
        # Save the credentials for future use
        with open("token.json", "w") as token:
            token.write(creds.to_json())  # Serialize the Credentials object to JSON

    return build("youtube", "v3", credentials=creds)


def get_subscribed_channels(youtube):
    channels = []
    next_page_token = None

    while True:
        response = youtube.subscriptions().list(
            part="snippet",
            mine=True,
            maxResults=500,  # Adjust the number of results per page
            pageToken=next_page_token
        ).execute()

        for item in response.get("items", []):
            channels.append((item["snippet"]["title"], item["snippet"]["resourceId"]["channelId"]))

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    return channels

def unsubscribe_channel(youtube, subscription_id):
    youtube.subscriptions().delete(id=subscription_id).execute()


def main():
    youtube = get_authenticated_service()

    subscriptions = []
    nextPageToken = None

    while True:
        # Get the list of your subscriptions with pagination
        response = youtube.subscriptions().list(
            part="snippet",
            mine=True,
            maxResults=50,
            pageToken=nextPageToken
        ).execute()

        subscriptions.extend(response.get("items", []))
        nextPageToken = response.get("nextPageToken")

        if not nextPageToken:
            break  # Exit the loop if there are no more subscriptions

    if not subscriptions:
        print("You have no subscriptions.")
        return

    # Display the list of subscriptions and ask the user for the index range to unsubscribe
    for index, subscription in enumerate(subscriptions):
        print(f"{index + 1}. {subscription['snippet']['title']}")

    try:
        start_range = int(input("Enter the starting index (100): "))
        end_range = int(input("Enter the ending index (500): "))

        if 1 <= start_range <= end_range <= len(subscriptions):
            for i in range(start_range - 1, end_range):
                subscription_id = subscriptions[i]["id"]
                unsubscribe_channel(youtube, subscription_id)
                print(f"Successfully unsubscribed from {subscriptions[i]['snippet']['title']}.")
        else:
            print("Invalid index range. Please enter valid starting and ending indices within the allowed range.")
    except ValueError:
        print("Invalid input. Please enter valid starting and ending indices.")

if __name__ == "__main__":
    main()
