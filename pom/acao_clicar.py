class Clicar:
    def __init__(self, page):
        self.page = page

    def NomeBotao(self, btn_name, timeout):
        btn_name = btn_name
        timeout = timeout
        self.page.get_by_role("button", name=btn_name).click(timeout=timeout)