from playwright.sync_api import Playwright, sync_playwright, expect
from pom.login_page import ExecuteLogin
from pom.acao_clicar import Clicar
from pom.camposSelecaoOperacao import SelecaoOperacao
from pom.campos_tela_romaneio import CamposRomaneio
from pom.campos_tela_romaneio import Operacao700


site = 'http://10.1.1.28:1001/itss-agro/'
url_romaneio = 'paginas/romaneio/inicial.jsf'
page_romaneio = f'{site}{url_romaneio}'

user_name = 'cciliato'
pass_word = 'Alvorada@1234'
texto_operacao = "700 - Entrada Spot"
nome_parceiro1 = "3000011"
nome_parceiro2 = "3000011 - TIAGO BOTTON"
nome_safra1 = "2022/2023"
nome_safra2 = "22/23-SAFRA"

def get_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        color_scheme='dark'
    )
    #context.tracing.start(screenshots=True, snapshots=True, sources=True)

    return context.new_page()

def abrirpagina(page, url_site):
    page.goto(url_site)
    page.wait_for_load_state("networkidle")


def execute_login(page, username, password):
    usuario = username
    senha = password

    log_in = ExecuteLogin(page)
    botao = Clicar(page)

    log_in.submit_login(usuario, senha)
    botao.NomeBotao("Entrar", 3000)
    page.wait_for_load_state("networkidle")


def start_romaneio(page, cod_operacao):

    botao = Clicar(page)
    selecao_opr = SelecaoOperacao(page)
    campos_opr = CamposRomaneio()


    texto_opera = campos_opr.selecao_operacao
    selecao_opr.EscolherCampos(texto_opera)
    selecao_opr.Digitar_Valor(cod_operacao)

    botao.NomeBotao("Incluir", 3000)
    page.wait_for_load_state("networkidle")


def start_opr_700(page):

    campo = Clicar(page)
    locator_name = Operacao700.campo_parceiro
    locator_safra = Operacao700.campo_safra

    campo.NomeCampo(locator_name, nome_parceiro1, nome_parceiro2, 3000)
    campo.NomeCampo(locator_safra, nome_safra1, nome_safra2, 3000)










if __name__ == "__main__":
    with sync_playwright() as playwright:
        page = get_page(playwright)

        abrirpagina(page, site)
        execute_login(page, user_name, pass_word)
        abrirpagina(page, page_romaneio)
        start_romaneio(page, texto_operacao)
        start_opr_700(page)

        #page.context.tracing.stop(path="trace.zip")
        #page.pause()

        page.close()