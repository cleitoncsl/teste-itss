from time import sleep

class Clicar:
    def __init__(self, page):
        self.page = page

    def NomeBotao(self, btn_name, timeout):
        btn_name = btn_name
        timeout = timeout
        self.page.get_by_role("button", name=btn_name).click(timeout=timeout)


    def NomeCampo(self, locator_name, input_text_name1, input_text_name2, timeout):
        locator_name = locator_name
        input_text_name1 = input_text_name1
        input_text_name2 = input_text_name2
        timeout = timeout
        self.page.locator(locator_name).press("Enter")
        sleep(0.5)

        self.page.locator(locator_name).fill(input_text_name1, timeout=timeout)
        sleep(0.5)

        self.page.locator(locator_name).fill(input_text_name2, timeout=timeout)
        sleep(0.5)