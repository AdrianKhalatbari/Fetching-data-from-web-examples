import requests

print('Welcome to Space X manned missions explorer')
try:
    year = int(input('Please, give the year to search for: \n'))
    launchesURL = "https://api.spacexdata.com/v5/launches"
    r = requests.get(url=launchesURL)
    launch = r.json()
    filteredList = []
    while True:

        counter = 0
        dicts = {}
        values = []
        print('Launch information descriptor')
        print('We have 3 launches to choose from.')
        print('-1) Exit')
        for i in range(len(launch)):
            dateStr = str(launch[i]['date_utc'])[0:4]
            if launch[i]['success'] is True and dateStr == str(year) and launch[i]['crew'] != []:
                print(str(counter) + ') ' + launch[i]['date_utc'] + ' - ' + launch[i]['name'])
                values.append(launch[i]['name'])
                dicts[int(counter)] = values[counter]
                counter = counter + 1

        selectedLaunch = int(input('Select launch to display more information: '))
        # selectedLaunch = 2
        if selectedLaunch == -1:
            break
        print('\n------------------\n')
        for i in range(len(launch)):
            if launch[i]['name'] == dicts.get(selectedLaunch):
                print('Name: ' + launch[i]['name'])
                print('Flight Number: ' + str(launch[i]['flight_number']))
                print('Date: ' + launch[i]['date_utc'])
                print('Mission: '+ launch[i]['details'])
                print('Mission status: Successful')
                print('Launch Wikipedia article: ' + launch[i]['links']['wikipedia'])
                print('The launch had a crew of ' + str(len(launch[i]['crew'])))
                print('\n::CREW MEMBERS::')
                idList = []
                for j in range(len(launch[i]['crew'])):
                    idList.append(launch[i]['crew'][j]['crew'])
                for x in range(len(idList)):
                    crewURL = 'https://api.spacexdata.com/v4/crew/'
                    crewURL = crewURL + str(idList.__getitem__(x))
                    v = requests.get(url=crewURL)
                    crewData = v.json()
                    print('  Crew member ' + str(x + 1))
                    print(' ',launch[i]['crew'][x]['role'],crewData['name'])
                    print('  Agency:'+crewData['agency'])
                    print('  Wikipedia page: '+crewData['wikipedia']+'\n')

except ValueError:
    print('Faulty input, please try again.')
