class DirectMessageHandler():
    messages = {}

    def message_response_exists(message):
        if messages[message] != null:
            return True
        else:
            return False

    def get_message_response(message):
        if messages[message] != null:
            return messages[message]
        else:
            return False

    def set_message_response(message, response):
        messages[message] = response
        return True
