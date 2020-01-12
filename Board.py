import requests
import numpy as np


class Board:
    def GetBoard(self):

        arr = np.zeros([9, 9], dtype=np.int)

        URL = "http://www.cs.utep.edu/cheon/ws/sudoku/new/?size=9&level=1"

        try:
            r = requests.get(url=URL)
        except requests.exceptions.ConnectionError:
            print('Error connecting to web')
            exit(1)
        except requests.exceptions.Timeout:
            print('Connection timeout')
            exit(1)
        except requests.exceptions.RequestException as e:
            print(e)
            exit(1)

        data = r.json()

        if data['response'] == "false":
            print('Some error. Retry.')
            exit()

        lst = data['squares']
        for i in lst:
            arr[i['x'], i['y']] = i['value']

        return arr
