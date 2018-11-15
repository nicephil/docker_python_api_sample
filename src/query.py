import requests

myurl="https://maps.googleapis.com/maps/api/place/autocomplete/json?input=Palo+Alto+California&key=AIzaSyC6JqDn7SObSOiywZ83_lMgGgZSlWLx4r4"
r = requests.get(myurl)
print r.json()

