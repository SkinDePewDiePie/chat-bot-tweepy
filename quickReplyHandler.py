class QuickReplyHandler():
    actions = {}

    def actions_exists(metadata):
        if actions[metadata] != null:
            return True
        else:
            return False

    def get_action(metadata):
        if actions[metadata] != null:
            return actions[metadata]
        else:
            return False

    def set_message_response(metadata, action):
        actions[metadata] = action
        return True
