import faker

fake = faker.Faker()

def getFakeData():
    return {
        'name': fake.name(),
        'email': fake.email(),
        'password': fake.password(),
    }


# print(getFakeData())


import requests

url = "http://localhost:8000/"

for i in range(1000):
    data = getFakeData()
    response = requests.post(url, data=data)
    # print(response.status_code)
    # print(response.text)