from quickReplyHandler import QuickReplyHandler
from directMessageHandler import DirectMessageHandler

quickReplyHandler = QuickReplyHandler()
directMessageHandler = DirectMessageHandler()

class EventHandler():
    def manage(event):
        if event["direct_message_events"]:
            dmEvent = event["direct_message_events"]
            if dmEvent["type"] === "message_create":
                quickReply = dmEvent["message_create"]["message_data"]["quick_reply_response"]
                if quickReply:
                    quick_reply(quickReply)
                else:
                    direct_message(dmEvent["message_create"]["message_data"]["text"])

    def quick_reply(quickReply):
        metadata = quickReply["metadata"]
        if quickReplyHandler.action_exists(metadata):
            quickReplyHandler.get_action(metadata)
        else:
            return False

    def direct_message(directMessageText):
        text = directMessageText.lower().replace(" ", "_")
        if directMessageHandler.messsage_response_exists(text):
            directMessageHandler.get_message_response(text)
        else:
            return False
