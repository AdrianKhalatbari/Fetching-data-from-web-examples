import requests

print('Welcome to Rick & Morty API')
while True:
    # api-endpoint
    URL = "https://rickandmortyapi.com/api/character/"
    print(
        'You have the following options\n0) Exit\n1) Get all dead characters\n2) Get characters by their name and living status')
    userInput = int(input('Enter your selection: \n'))
    if userInput == 0:
        break
    if userInput == 1:
        userNumberOfPages = int(input('Enter limit of pages: \n'))
        # ///////////////////Find number of pages
        PARAMS = {'page': 1, 'status': 'dead'}
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()
        realNumberOfPages = data['info']['pages']
        if userNumberOfPages > realNumberOfPages:
            numberOfPages = realNumberOfPages
        else:
            numberOfPages = userNumberOfPages
        # ////////////////////////////// Start to send requests
        for i in range(numberOfPages):
            if i == 0:
                print("Getting page 1 url: https://rickandmortyapi.com/api/character?status=dead")
            else:
                print('Getting page ' + str(i + 1) + ' url: https://rickandmortyapi.com/api/character?page=' + str(
                    i + 1) + '&status=dead')
        finalSize = 0
        for j in range(numberOfPages):
            # defining a params dict for the parameters to be sent to the API
            PARAMS = {'page': j + 1, 'status': 'dead'}
            # sending get request and saving the response as response object
            r = requests.get(url=URL, params=PARAMS)
            # extracting data in json format
            data = r.json()
            # extracting latitude, longitude and formatted address
            jsonSize = []
            for a in data['results']:
                jsonSize.append(a['id'])
            for i in range(len(jsonSize)):
                userId = data['results'][i]['id']
                name = data['results'][i]['name']
                status = data['results'][i]['status']
                userType = data['results'][i]['type']
                species = data['results'][i]['species']
                origin = data['results'][i]['origin']['name']
                print('ID:' + str(userId) + ' - name:' + name + ' - type:' + str(
                    userType) + ' species:' + species + ' - origin:' + origin + ' - status:' + status)
            finalSize = finalSize + len(jsonSize)
        print('Total number of ' + str(finalSize) + ' dead characters')

    if userInput == 2:
        character = input('Enter character to search for: \n')
        inputStatus = input('Enter living status (alive, dead, unknown): \n')
        userNumberOfPages = int(input('Enter limit of pages: \n'))
        # ///////////////////Find number of pages
        PARAMS = {'page': 1, 'status': inputStatus, 'name': character}
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()
        realNumberOfPages = data['info']['pages']
        if userNumberOfPages > realNumberOfPages:
            numberOfPages = realNumberOfPages
        else:
            numberOfPages = userNumberOfPages
        # ////////////////////////////// Start to send requests
        finalSize = 0
        for i in range(numberOfPages):
            if i == 0:
                print(
                    'Getting page 1 url: https://rickandmortyapi.com/api/character?name=' + character + '&status=' + inputStatus)
            else:
                print('Getting page ' + str(i + 1) + ' url: https://rickandmortyapi.com/api/character?page=' + str(
                    i + 1) + '&name=' + character + '&status=' + inputStatus)
        for j in range(numberOfPages):
            # defining a params dict for the parameters to be sent to the API
            PARAMS = {'page': j + 1, 'status': inputStatus, 'name': character}
            # sending get request and saving the response as response object
            r = requests.get(url=URL, params=PARAMS)
            # extracting data in json format
            data = r.json()
            # extracting latitude, longitude and formatted address
            jsonSize = []
            for a in data['results']:
                jsonSize.append(a['id'])
            for i in range(len(jsonSize)):
                userId = data['results'][i]['id']
                name = data['results'][i]['name']
                status = data['results'][i]['status']
                userType = data['results'][i]['type']
                species = data['results'][i]['species']
                origin = data['results'][i]['origin']['name']
                print('ID:' + str(userId) + ' - name:' + name + ' - type:' + str(
                    userType) + ' species:' + species + ' - origin:' + origin + ' - status:' + status)
            finalSize = finalSize + len(jsonSize)
        print('Total number of ' + str(finalSize) + ' ' + inputStatus + ' ' + character+"'s"+' found')
