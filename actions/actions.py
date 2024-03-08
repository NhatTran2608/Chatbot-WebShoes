# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# actions.py

# actions.py

from typing import Any, Text, Dict, List
from pymongo import MongoClient
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionQueryMongoDB(Action):
    
    def name(self) -> Text:
        return "action_query_mongodb"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            client = MongoClient("mongodb://127.0.0.1/Shop")
            db = client["Shop"]
            collection = db["Products"]
            result = collection.find_one({"name": "Giày Nike Dunk High 'Hawaii' CZ2232-300"})
            if result:
                quantity_buy = result.get("quantity_buy")
                dispatcher.utter_message(text=f"Số lượng đã mua: {quantity_buy}")
            else:
                dispatcher.utter_message(text="Xin lỗi, không tìm thấy sản phẩm trong cơ sở dữ liệu.")
        except Exception as e:
            # Log any exceptions
            print(f"An error occurred: {e}")
            dispatcher.utter_message(text="Đã xảy ra lỗi khi truy vấn cơ sở dữ liệu.")
        return []






