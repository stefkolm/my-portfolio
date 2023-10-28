import requests

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = '5988213754:AAFvGC1e3bBG8OT_p5VDd8YPmuydPLVrgfw'
base_url = f'https://api.telegram.org/bot{bot_token}/'

def send_message(chat_id, text):
    url = f'{base_url}sendMessage'
    params = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, params=params)
    return response.json()

# Example usage
if __name__ == '__main__':
    # Replace 'USER_CHAT_ID' with the actual chat ID of the user you want to send a message to
    user_chat_id = '1090944878'
    message_text = 'Hello, this is a test message from your bot!'
    
    response = send_message(user_chat_id, message_text)
    print(response)