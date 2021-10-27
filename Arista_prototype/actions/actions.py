# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from .covid19 import Covid_19
from .disease_symptoms import symptom_prediction
from .hospital_booking import email_call_sms
# Covid_19 class #############
class ActionCovid19Place(Action):

    def name(self) -> Text:
        return "action_place"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        place= tracker.get_slot("place")
        full_details = tracker.get_slot("full_details")
        print(f'place=={place}')
        covid=Covid_19(str(place))

        dispatcher.utter_message(text=covid.covid_19_details_current())
        dispatcher.utter_message(text=covid.covid_19_details_total())
        dispatcher.utter_message(text=covid.total_covid_19())


        if full_details.lower() in ['yes','yea','ya','why not','oh ya']:
            dispatcher.utter_message(text=covid.kerala_total())



        return []
# Hospital Booking class
class ActionHospitalBooking(Action):

    def name(self) -> Text:
        return "action_hospital"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name=tracker.get_slot("name")
        age =tracker.get_slot("age")
        hospital_name=tracker.get_slot("hospital_name")
        place=tracker.get_slot("place1")
        dispatcher.utter_message(text=email_call_sms(name,age,hospital_name,place))

        return []
# Disease Symtom class
class ActionCovid19Place(Action):

    def name(self) -> Text:
        return "action_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name1=tracker.get_slot("name1")
        symptoms=tracker.get_slot("symptoms")
        other_symptoms=tracker.get_slot("any_other_symptoms")

        dispatcher.utter_message(text=symptom_prediction(str(name1),str(symptoms),str(other_symptoms)))

        return []

