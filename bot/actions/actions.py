from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random

class ActionAgendamento(Action):
   def name(self):
      return "action_agendamento"

   def run(self, dispatcher, tracker, domain):
        try:
          dispatcher.utter_message("Mensagem enviada por uma custom action.")
        except ValueError:
          dispatcher.utter_message(ValueError)

