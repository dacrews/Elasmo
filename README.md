# Elasmo
I developed this web app to improve my understanding of, and skills related to, Django.

This web application features 6 pages, incoporates 3 web maps, and is fully responsive.

[Live Site](https://dacrews.pythonanywhere.com/index) deployed using [pythonanywhere](https://www.pythonanywhere.com/)

## Description
The main purpose of Elasmo is to provide site visitors with a deeper understanding of sharks. Visitors will discover 3 web maps which visualize tracker data collected by marine scientists, resources for several research studies and shark conservation organizations, and detailed descriptions for 10 common shark species.

This project was important to me because throughout my childhood, my dream was to work with sharks in some capacity. I had fun developing Elasmo since it felt as though I was combining an old passion with a more recent one: software development.

### Technologies Used
* Frameworks: Django, Bootstrap
* Libraries: Leaflet, jQuery
* Languages: HTML, CSS, JavaScript, Python
* Database: SQLite3
* Other: Wikipedia API

## Key Features
### Python and Wikipedia API
The Shark Species page was populated by adding a custom python script to my views.py file.
```python
def sharks(request):
    shark_list = [
        'Nurse Shark',
        'Whitetip Reef Shark',
        'Sandbar Shark',
        'Blacktip Reef Shark',
        'Galapagos Shark',
        'Whale Shark',
        'Great White Shark',
        'Thresher Shark',
        'Blue Shark',
        'Oceanic Whitetip Shark',
    ]

    wiki = wikipediaapi.Wikipedia(
        'en',
        extract_format = wikipediaapi.ExtractFormat.WIKI
    )

    data = []
    key = 0

    for shark in shark_list:
        page = wiki.page(shark)
        title = page.title
        content = page.summary
        result = {key: {'title': title, 'content': content}}
        key += 1

        data.append(result)

    return render(request, 'sharks.html', {'data': data})
```
This code utilized the [Wikipedia API](https://pypi.org/project/Wikipedia-API/) to extract text from the wikipedia pages of each shark species. Once extracted, I added the text to a table in my sharks.html template.
```html
<tr>
    <th class="tableHead" id="t1"><img class="img-fluid" src="static/img/sharks/nurse.jpg" height="400px" width="500px"></th>
    <td>
        {% for d in data %}
            <h4 class="sharkTitle" id="nurse">{{ d.0.title }}</h4>
            <p>{{ d.0.content }}</p>
        {% endfor %}
    </td>
</tr>
```
![elasmo_ss](https://user-images.githubusercontent.com/70422954/192132599-c12d24a4-c5c3-4c25-ae0a-f4ad9d40939f.PNG)

### Leaflet and SQLite3
On the Data and Research Page, users can interact with 3 web maps which visualize shark tracker data collected by credited marine scientists. Once I obtained the data, I cleaned and added it to my SQLite3 database. I then pulled the data from the SQLite tables to the leaflet maps in the form of map markers and popups.
```javascript
{% for point in porbblue %}
    // Markers
    markerPorblue = L.marker([{{ point.latitude }}, {{ point.longitude }}]).bindPopup(strPopup, {closeButton: false}); //.addTo(map_porblue);
    markersPorblue.addLayer(markerPorblue);

    // Popups
    strPopup = "<h4><center><b> {{ point.common_name }} </b></center><hr></h4>";
        strPopup += "<p>Scientific Name: {{ point.scientific_name }} </p>";
        strPopup += "<p>Sex: {{ point.sex }} </p>";
        strPopup += "<p>Life Stage: {{ point.life_stage }}</p>";
        strPopup += "<p>Length: {{ point.length_meters }}  meters</p>";
        strPopup += "<p>Locality: {{ point.locality }}</p>";
        strPopup += "<p>Collected by {{ point.collector }} on {{ point.date }}</p>";
{% endfor %}
```
![elasmo_ss_2](https://user-images.githubusercontent.com/70422954/192132918-9f696e87-5b78-4e97-8802-2fd4fa7b8b27.PNG)
