import requests

class myslacker:
    def __init__(self):
        self.channel = '****************'
        self.token = '******************************'

    def post_message(self, text):
        response = requests.post("https://slack.com/api/chat.postMessage",
                                 headers={"Authorization": "Bearer " + self.token},
                                 data={"channel": self.channel, "text": text}
                                 )

if __name__ == '__main__':
    mySlack = myslacker()
    mySlack.post_message('slack test')