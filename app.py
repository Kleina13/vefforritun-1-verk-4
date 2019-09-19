# APP

from flask import Flask, render_template as rend

app = Flask(__name__)

lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem mollis aliquam ut porttitor leo a. Pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum. Nisl nunc mi ipsum faucibus vitae aliquet. Ultricies lacus sed turpis tincidunt id aliquet risus feugiat. Arcu ac tortor dignissim convallis aenean et tortor. Aliquam vestibulum morbi blandit cursus risus at. Feugiat in ante metus dictum at tempor commodo ullamcorper. Magnis dis parturient montes nascetur ridiculus mus. Sed libero enim sed faucibus turpis in eu. Sed tempus urna et pharetra. Tincidunt vitae semper quis lectus nulla at. Blandit massa enim nec dui nunc mattis enim. Amet commodo nulla facilisi nullam. Pulvinar elementum integer enim neque volutpat ac tincidunt vitae semper. Sodales ut eu sem integer. Viverra suspendisse potenti nullam ac tortor vitae purus. Sed risus pretium quam vulputate dignissim. Lobortis feugiat vivamus at augue eget arcu dictum. Pellentesque sit amet porttitor eget. Scelerisque eu ultrices vitae auctor eu augue ut lectus. Euismod elementum nisi quis eleifend quam adipiscing. Suspendisse ultrices gravida dictum fusce ut placerat orci. Sed odio morbi quis commodo odio aenean sed adipiscing. Rhoncus mattis rhoncus urna neque viverra justo nec ultrices. Bibendum ut tristique et egestas quis ipsum suspendisse ultrices gravida. At lectus urna duis convallis convallis. Adipiscing bibendum est ultricies integer. Pharetra vel turpis nunc eget. In massa tempor nec feugiat nisl. Lobortis feugiat vivamus at augue eget arcu dictum varius. Phasellus vestibulum lorem sed risus ultricies tristique nulla. Sed augue lacus viverra vitae.'

articles = [{'id': 1, 'author': "Noami Winters", 'title': "Rat poison in school's caffettiera food", 'content': lorem_ipsum},
			{'id': 2, 'author': "Sebastian Sanchez", 'title': "Video games bad!", 'content': lorem_ipsum},
			{'id': 3, 'author': "Carl Bowie", 'title': "Florida man steals baby to get free meth", 'content': lorem_ipsum},
			{'id': 4, 'author': "Rachel Kristen", 'title': "Football team discovers fire", 'content': lorem_ipsum},
			{'id': 5, 'author': "Samuel Jackson", 'title': "Donald Trump commits genocide", 'content': lorem_ipsum}]
people = [{'name': "Kalli B.", 'kt': "120703-2034"},
		  {'name': "Kalli D.", 'kt': "070100-3920"},
		  {'name': "Kalli G.", 'kt': "031104-1003"}]
lenA, lenB = len(articles), len(people)

@app.route('/')
def index():
	return '<h1>Velkominn</h1><a href="/mdl/article/1">Ýttu hérna fyrir MDL</a> | <a href="/kennitala/120703-2034">Ýttu hérna fyrir kennitölur</a>'

@app.route('/mdl/article/<ID>')
def article(ID):
	for x in range(lenA):
		if int(ID) == articles[x]['id']:
			d = articles[x]
			a, t, c = d['author'], d['title'], d['content']
	return rend('layout.html', author=a, title=t, content=c, articles=articles, len=lenA)

@app.route('/kennitala/<KT>')
def kennitala(KT):
	for x in range(lenB):
		if KT == people[x]['kt']:
			p = people[x]
			n, k = p['name'], p['kt']
	return rend('kennitala.html', name=n, kt=k, people=people, len=lenB)

@app.errorhandler(404)
def error404(error):
	return '<br><br><h1 style="text-align: center;">ERROR 404</h1><h2 style="text-align: center;">page not found<h2>'



if __name__ == "__main__":
	app.run(debug=True)