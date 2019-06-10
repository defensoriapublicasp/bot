from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import logging
from . import api

logger = logging.getLogger(__name__)

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
        except:
            dispatcher.utter_message(problem_message)

class ActionAgendamento(Action):
    def name(self):
        return "action_agendamento"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Ótimo.')
        place = tracker.get_slot('local')
        try:
            api_place = api.get_city_data(place)[0]
            logger.info(api_place)
            dispatcher.utter_message('Você pode ir na {} que fica na {}, número {} e telefone {}.'.format(api_place['nome'], api_place['endereco']['logradouro'], api_place['endereco']['numero'], api_place['telefoneOwner']['telefones'][0]['telefone']))
        except:
            dispatcher.utter_message(problem_message)

class ActionCejusc(Action):
    def name(self):
        return "action_cejusc"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Ótimo.')
        place = tracker.get_slot('local')
        try:
            api_place = api.get_cejusc_data()[0]
            logger.info(api_place)
            dispatcher.utter_message('Você pode ir na CEJUSC {}, que fica na {}, telefone {} e email {}.'.format(api_place['nome'], api_place['endereco'], api_place['telefone'], api_place['email']))
        except:
            dispatcher.utter_message(problem_message)
