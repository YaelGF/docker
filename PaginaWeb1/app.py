import web

urls = (
    '/', 'mvc.controllers.index.Index',
    '/docker','mvc.controllers.docker.Docker',
    '/ubuntu','mvc.controllers.ubuntu.Ubuntu'
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()
