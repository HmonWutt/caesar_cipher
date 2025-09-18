class Message:
    def __init__(self,sender,receiver,text):
        self.sender = sender
        self.receiver = receiver
        self.text = text

    def __str__(self):
        return f'{self.sender} is sending "{self.text}" to {self.receiver}'
