from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests

problem_message = 'Desculpe tive um problema no agendamento, entre em contato '\
                  'com a defensoria em outro canal de comunicação ou tente '\
                  'novamente mais tarde.'

class ActionConfirmaAgendamento(Action):
    def name(self):
        return "action_confirma_agendamento"

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message('Ok, então você quer que eu procure '\
            'unidades em {}?'.format(tracker.get_slot('local')))
        except error:
            dispatcher.utter_message(problem_message)
            print(error)

class ActionAgendamento(Action):
    def name(self):
        return "action_agendamento"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Ótimo.')
        try:
            dispatcher.utter_message('Agendando em {}.'.format(tracker.get_slot('local')))
        except error:
            dispatcher.utter_message(problem_message)
            print(error)
