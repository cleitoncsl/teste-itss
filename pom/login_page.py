class ExecuteLogin:
    def __init__(self, site):
        self.page = site


    def navigate(self, url_base):
        site = url_base
        self.page.goto(url_base)


    def submit_login(self, user_name, password):
        self.page.fill("[placeholder=\"Login\"]", user_name)
        self.page.fill("[placeholder=\"Senha\"]", password)
