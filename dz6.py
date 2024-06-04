import pywebio
from pywebio.output import put_text, put_html, put_image

put_html('<h1>YAYY, ITS SUMMER!<h1>')
put_html('''<h2>Behind the steep banks
Hay smells like wormwood,
A bee sleeps on a daisy,
Blue is dripping from the sky.

Sycamores tickle the wind,
Unweaves vines with willows,
Summer whispers to the water:
- I will come here again.<h2>''')

plans_for_summer = pywebio.input.input('What are your plans fot the summer?')
count_of_simbols = len(plans_for_summer)
string = '<h2>count_of_simbols =' + str(count_of_simbols) + '<h2>'

put_html(string)

img = open('summer-beach-5.jpg', 'rb').read()
put_image(img, width='500px')
