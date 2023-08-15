# Manage_Youtube_Subscriptions
This Python script interacts with the YouTube API to manage a user's subscribed channels. It uses OAuth 2.0 for authentication and provides functionality to unsubscribe from a range of subscribed channels. Here's a summarized explanation of the code and what it uses:

1. **Libraries Used:**
   - `os`: For file and directory operations.
   - `json`: For handling JSON data.
   - `google_auth_oauthlib.flow`: For OAuth 2.0 authentication flow.
   - `google.auth.transport.requests`: For making authenticated requests.
   - `googleapiclient.discovery`: For building the YouTube API service.

2. **Authentication:**
   - The script uses OAuth 2.0 to authenticate the user. It checks if there's a stored authentication token in "token.json". If not, it initiates the authentication flow using the "client_secrets.json" file, which contains your client ID and client secret.
   - Upon successful authentication, the credentials are stored in "token.json" for future use.

3. **Subscribed Channels Retrieval:**
   - The `get_subscribed_channels` function retrieves a list of subscribed channels. It repeatedly sends requests to the YouTube API's `subscriptions().list` endpoint with appropriate parameters to fetch the user's subscribed channels.
   - The retrieved channel data includes titles and channel IDs.

4. **Unsubscribe Functionality:**
   - The `unsubscribe_channel` function unsubscribes the user from a specified channel. It utilizes the YouTube API's `subscriptions().delete` endpoint with the provided subscription ID.

5. **Main Process:**
   - The `main` function is the core of the script's functionality.
   - It authenticates the user using OAuth.
   - It fetches the list of subscribed channels with pagination.
   - If there are no subscriptions, it informs the user.
   - It presents the user with a list of subscribed channels to choose from.
   - The user is prompted to enter a starting and ending index range to specify channels to unsubscribe from.
   - The script processes the unsubscribing based on the selected indices and provides success messages.

6. **Running the Script:**
   - The script should be executed in a terminal or command prompt.
   - Before running, ensure you have the necessary dependencies installed (`google-auth`, `google-auth-oauthlib`, `google-auth-httplib2`, `google-api-python-client`).
   - The "client_secrets.json" file should be set up correctly with your application's client ID and client secret.
   - The script guides the user through the process of unsubscribing from selected channels.

This script is a handy tool for managing your YouTube subscriptions programmatically, offering an alternative to manually unsubscribing from channels one by one.
