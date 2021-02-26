import requests
response = requests.get("http://randomfox.ca/floof")
print(response.status_code)
print(response.text)
print(response.json())
randomfox=response.json()
print(randomfox['image'])
url=randomfox['image']
from PIL import Image   
from io import BytesIO
response2 = requests.get(url)
im = Image.open(BytesIO(response2.content))
im.show() 
