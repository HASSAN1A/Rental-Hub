from flask import abort
import urllib.request,json
from .models import Quote

# Quotes api base url
quotes_base_url = "http://quotes.stormconsultancy.co.uk/random.json"

Quote=Quote


def get_quotes():

  count=0
  quotes=[]
  while count!=7:
    with urllib.request.urlopen(quotes_base_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)
    if get_quotes_response:
      quote_id=get_quotes_response['id']
      quote_text=get_quotes_response['quote']
      quote_author=get_quotes_response['author']
      quote_obj=Quote(quote_id,quote_text,quote_author)
      quotes.append(quote_obj)
    else:
      abort(500)       
    count=count+1
      

  return quotes