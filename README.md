# Automated-Instagram-Growth-Bot

The Automated Instagram Growth Bot is a Python-based project built using the Selenium library. It is designed to automate various tasks on the Instagram platform, enabling users to enhance their Instagram presence and grow their follower base more efficiently. This was built for learning purposes and not intended for use. 

The idea behind this bot is to interact with posts under specific hashtags such as "#Follow4Follow" or "#LikeforLike". When a user engages with posts under these hashtags, their interactions will be hypothetically reciprocated by other users.
## Prerequisites:

- **VPN Usage**: It is highly recommended to employ a VPN while using this code. Implementing a VPN helps to mitigate the risk of the Selenium web driver being detected as a bot, thus reducing the likelihood of restrictions or blocks from Instagram.

- **Instagram Limits**: It is crucial to be mindful of Instagram's usage limits to maintain a compliant and sustainable approach. These limits pertain to various actions such as likes, comments, and follows. Here are some guidelines to keep in mind, (the limits below are subject to updates):

     - **Likes**: Instagram imposes restrictions on the number of likes you can perform within an hour. For new accounts, it is advisable to limit likes to approximately 60 posts per hour. However, older accounts with a substantial follower base can extend this limit to around 120 likes per hour.

    - **Comments**: Instagram sets a daily limit for the number of comments you can post. Typically, this limit ranges from 180 to 200 comments per day, depending on the age of your account.

    - **Follows/Unfollows**: Instagram regulates the number of users you can follow or unfollow in a day. It is recommended to stay within the range of 150 to 200 follows or unfollows. 

## Usage:

- **Integrated ChatGPT**: As of now, OpenAi no longer provides free API credits. Consequently, the code has been updated to incorporate an alternative approach. It now randomly selects a friendly comment from an extensive array of pre-existing comments.

    - **Integrated ChatGPT (If Applicable)**: In case you have access to the OpenAi API, you can integrate the following code:<img src="images/OpenAiCode.png" width="800">

- **Handling User Credentials**: Currently, the project prompts users to enter their Instagram username and password directly in the terminal upon running the code. While this information is not stored, it is essential to prioritize security. To adopt a safer approach, it is recommended to store your Instagram username and password in a separate file called "secret.py" and make the following modifications in the "SeleniumAutomation.py" file (Add the green, remove the red):
     - <img src="images/UserCode.png" width="800">

## SeleniumAutomation.py

After the credentials are received:

- The code opens Instagram on the Chrome driver, logs in the user, and dismisses any pop-ups that may appear.

- It redirects the user to a specific hashtag page on Instagram.

- The bot proceeds to interact with the photos by liking them, following the user, and commenting (comments only take place 34% of the time)

- If any errors occur during the interaction process, the bot handles them gracefully and moves on to the next photo.

- The bot repeats the interaction cycle until the desired number of interactions is fulfilled.

https://github.com/haris-sujethan/Automated-Instagram-Growth-Bot/assets/96924701/63c38d9b-b523-4e7f-be76-21216a42c1ba

## unFollow.py

After the credentials are received:

- The code opens Instagram on the Chrome driver, logs in the user, and dismisses any pop-ups that may appear.

- It redirects the user to their following list

- Iterates through the users following list and unfollows other users

https://github.com/haris-sujethan/Automated-Instagram-Growth-Bot/assets/96924701/be324026-2453-4523-9751-9a205024ed56
