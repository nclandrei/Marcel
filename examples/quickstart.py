import sys
from wit import Wit

if len(sys.argv) != 2:
    print('usage: python ' + sys.argv[0] + ' <wit-token>')
    exit(1)
access_token = sys.argv[1]

# Quickstart example
# See https://wit.ai/ar7hur/Quickstart

def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def send(request, response):
    print(response['text'])

def getForecast(request):
    context = request['context']
    entities = request['entities']

    loc = first_entity_value(entities, 'location')
    if loc:
        context['forecast'] = 'sunny in ' + loc
        if context.get('missingLocation') is not None:
            del context['missingLocation']
    else:
        context['missingLocation'] = True
        if context.get('forecast') is not None:
            del context['forecast']

    return context

actions = {
    'send': send,
    'getForecast': getForecast,
}

client = Wit(access_token=access_token, actions=actions)
client.interactive()
