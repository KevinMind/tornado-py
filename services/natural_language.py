import requests
import json

import services.py_scraper
scraper = services.py_scraper

from settings import meaning_cloud_key
KEY = meaning_cloud_key

print(KEY)




##############################################################################
# Takes input service and defines host url for api call                      #
##############################################################################

def service_url(service):
    base_url = "http://api.meaningcloud.com/"
    options = {
        "topics": "class-1.1",
        "sentiment": "sentiment-2.1",
        "summarize": "summarization-1.0",
        "cluster": "clustering-1.1"
    }
    url = base_url + options[service]
    return url

# Define Headers returns them to call function
def get_headers():
    return {'content-type': 'application/x-www-form-urlencoded'}

#############################################################################
##############################################################################

# Text structure
txtf = {
    "html" : "html",
    "plain": "plain"
}

##############################################################################
# Choose Model RIGHT NOW WE ONLY SUPPORT explicit statements of model
##############################################################################

def get_model(model):
    models = {
        "english": "IPTC_en", # IPTC_en: English IPTC model.
        "spanish": "IPTC_es", # IPTC_es: Spanish IPTC model.
        "french": "IPTC_fr", # IPTC_fr: French IPTC model.
        "italian": "IPTC_it", # IPTC_it: Italian IPTC model.
        "portuguese": "IPTC_pt", # IPTC_pt: Portuguese IPTC model.
        "catalan": "IPTC_ca", # IPTC_ca: Catalan IPTC model.
        "euro": "EUROVOC_es_ca", # EUROVOC_es_ca: EuroVoc EU's multilingual thesaurus (Spanish/Catalan).
        "business_rep_spanish": "BusinessRep_es", # BusinessRep_es: Business Reputation (Spanish).
        "iab_spanish": "IAB_es",  # IAB_es: Spanish IAB taxonomy model.
        "social_english": "SocialMedia_en", # SocialMedia_en: English Social Media modelself.
        "social_spanish": "SocialMedia_es", # SocialMedia_es: Spanish Social Media model
        "default": "general"
    }
    return models[model]

##############################################################################
# Choose Model
##############################################################################

lang = {
    "english": "en",
    "default": "auto"
}

##############################################################################
# BUILD PAYLOAD
##############################################################################

def get_payload(**kwargs):
    url = kwargs['url']
    service = kwargs['service']
    model = kwargs['model']

    # generate payload dictionary
    payload = {}

    # ALWAYS REQUIRED
    payload['key'] = KEY

    print(KEY)

    if service == "topics":
        payload['model'] = get_model(model)
        payload['url'] = url
    elif service == "sentiment":
        payload['lang'] = "auto"
        payload['url'] = url
    elif service == "summarize":
        # Soup for counting sentences
        sentences = scraper.count_sentences("http://vice.com/en_us/article/gy5mp3/its-time-to-take-down-statues-of-conquistadors")
        payload['sentences'] = sentences
        payload['url'] = url
    elif service == "cluster":
        payload['txt'] = scraper.return_text(url)
        payload['lang'] = "en"


    #############################
    return payload              #
    #############################


# payload = {
#     "model": get_model("default"),
#     "txtf": txtf['html'],
#     "lang": "auto"
# }

##############################################################################
# Build Request
# ##############################################################################
{
    "status": {
        "code":"0",
        "msg":"OK",
        "credits":"5",
        "remaining_credits":"39950"
    },
    "category_list": [
        {
        "code":"01018000",
        "label":"arts, culture and entertainment - monument and heritage site",
        "abs_relevance":"5.9928794",
        "relevance":"100"
        }
    ]
}
def find_meaning(**kwargs):
    service = kwargs['service']
    url = kwargs['url']
    model = kwargs['model']
    print("Model is {}.".format(model))
    # Define Headers
    headers = get_headers()
    # Define Host URL
    host = service_url(service)
    # Build Payload
    payload = get_payload(url=url, model=model, service=service)
    print(payload)
    response = requests.request("POST", host, data=payload, headers=headers)
    # status = response['status']
    # data = response['category_list'][0]
    return json.loads(response.text)
