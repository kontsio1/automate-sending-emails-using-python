import requests

dogRequest = requests.get('https://dog.ceo/api/breed/retriever/images/random')
catRequest = requests.get('https://cataas.com/cat/cute%2Cgif?position=center&html=false&json=false')

with open("catImage.gif", "wb") as file:
        file.write(catRequest.content)

# print(dogRequest.json())
# print(catRequest.content)

# doggo: https://i.pinimg.com/736x/2c/02/82/2c0282b3cd35a2602608cc39d75a40a2.jpg 