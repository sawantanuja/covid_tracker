from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "7efc1b07f0mshe06b8f3cb3918aap1af566jsn54b4c885d16d",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()


# Create your views here.
def index(request):
    mylist = []
    noofresults = int(response['results'])

    for x in range(0, noofresults):
        mylist.append(response['response'][x]['country'])

    if request.method == 'POST':
        selectedcountry = request.POST['selectedcountry']
        noofresults = int(response['results'])
        print(selectedcountry)
        for x in range(0,noofresults):
            if selectedcountry==response['response'][x]['country']:
                new = (response['response'][x]['cases']['new'])
                activate = (response['response'][x]['cases']['active'])
                critical =(response['response'][x]['cases']['critical'])
                recovered = (response['response'][x]['cases']['recovered'])
                total = (response['response'][x]['cases']['total'])
                deaths = int(total) - int(activate) - int(recovered)
        context = {'selectedcountry': selectedcountry,'mylist': mylist,'new': new,'activate': activate,'critical': critical,'recovered': recovered,'deaths': deaths,'total': total}
        return render(request,'index.html',context)

    context = {'mylist': mylist}
    return render(request,'index.html',context)


