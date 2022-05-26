import web

render = web.template.render("mvc/views/")

class Ubuntu():
    def GET(self):
        try:
            return render.ubuntu()
        except Exception as e:
            return "Error" + str(e.args)