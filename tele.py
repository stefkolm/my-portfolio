import requests

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = '5988213754:AAFvGC1e3bBG8OT_p5VDd8YPmuydPLVrgfw'
base_url = f'https://api.telegram.org/bot{bot_token}/'

def send_message(text):
    chat_id = '1090944878'
    url = f'{base_url}sendMessage'
    params = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, params=params)
    return response.json()

# Example usage
