class SelecaoOperacao:

    def __init__(self, page):
        self.page = page

    def EscolherCampos(self, valor):
        self.escolher_valor = self.page.locator(valor).click()

    def Digitar_Valor(self, valor):
        self.digitar_valor = self.page.get_by_role("option", name=valor).click()
        self.page.get_by_role("heading", name="Romaneio").click()