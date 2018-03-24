# -*- coding: utf-8 -*-
"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function

import requests
from HTMLParser import HTMLParser
h = HTMLParser()

# Imports the Google Cloud client library
from google.cloud import translate

# Instantiates a client
translate_client = translate.Client()


# --------------- Helpers that build all of the responses ----------------------

def phonemes(text, language):
    payload = { "txt": text, "language": language, "alphabet": "IPA" }
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
     'Cache-Control': 'no-cache', 'Host': 'tom.brondsted.dk', 'Content-Type': 'application/x-www-form-urlencoded',
      'Referer': 'http://tom.brondsted.dk/text2phoneme/transcribeit.php'}

    r = requests.post("http://tom.brondsted.dk/text2phoneme/transcribeit.php", data=payload, headers=headers)


    second_half = r.text.split("<b>IPA transcription (phonemes):</b><br />")[1]
    phonemes = second_half.split("</p>")[0]
    phonemes = h.unescape(phonemes)
    phonemes = phonemes.replace(" ", "")

    return phonemes
 

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_phoneme_response(title, output, reprompt_text, should_end_session, original_output):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': '<speak><phoneme alphabet="ipa" ph="' + output + '">' + original_output + '</phoneme></speak>'
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response(locale):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    if locale == 'de-DE':
        speech_output = "Hallo"
    else:
        speech_output = "Hi"

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "what do you want to translate?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))
        
def set_language_in_session(intent, session, locale):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'language' in intent['slots']:
        language = intent['slots']['language']['value']
        session_attributes = { "language": language }
        if locale == 'de-DE':
            speech_output = "Ich übersetze jetzt nach " + language + "."
            reprompt_text = "Was möchtest du übersetzen?"
        else:
            speech_output = "Now translating to " + language + "."
            reprompt_text = "What would you like to translate?"

    else:
        speech_output = "Sorry. " \
                        "Please try again."
        reprompt_text = ""
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

language_codes = {
    "German": "de",
    "English": "en",
    "British English": "en-gb",
    "French": "fr",
    "Spanish": "es",
    "Russian": "ru",
    "Croatian": "hr",
    "Italian": "it",
    "Swedish": "se",
    "Arabic": "ar",
    "Deutsch": "de",
    "Englisch": "en",
    "Britisches Englisch": "en-gb",
    "Französisch": "fr",
    "Spanisch": "es",
    "Russisch": "ru",
    "Kroatisch": "hr",
    "Italienisch": "it",
    "Schwedisch": "se",
    "Arabisch": "ar",
    "Dänisch": "da",
    "Danish": "da",
    "en":"english",
    "de":"german",
    "da":"danish"
}


def translate(intent, session):
    session_attributes = {}
    reprompt_text = None

    if session.get('attributes', {}) and "language" in session.get('attributes', {}):
        language = session['attributes']['language']
        session_attributes = { "language": language }
        should_end_session = False
        
        if 'translateText' in intent['slots']:
            text = intent['slots']['translateText']['value']

            translation = translate_client.translate(text, target_language=language_codes[language])
            translationText = h.unescape(translation['translatedText'])

            languageCode = language_codes[language]
            if (languageCode in ["de", "en", "da"]):
                speech_output = phonemes(translationText, language_codes[languageCode])
                return build_response(session_attributes, build_phoneme_response(
                    intent['name'], speech_output, reprompt_text, should_end_session, translationText))
            
            speech_output = translation['translatedText']
            reprompt_text = ""
        else:
            speech_output = "Sorry. " \
                            "Please try again."
            reprompt_text = ""
        
    else:
        speech_output = "I'm not sure what your language is. " \
                        "You can say, set my language to German."
        should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response(launch_request['locale'])


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "SetLanguageIntent":
        return set_language_in_session(intent, session, intent_request['locale'])
    elif intent_name == "TranslateIntent":
        return translate(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response(intent_request['locale'])
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
