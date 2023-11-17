from playwright.sync_api import Playwright, sync_playwright, expect, Page
from pom.login_page import ExecuteLogin
from pom.acao_clicar import Clicar
from pom.camposSelecaoOperacao import SelecaoOperacao
from pom.campos_tela_romaneio import CamposRomaneio
import pytest
from time import sleep

site = 'http://10.1.1.28:1001/itss-agro/'
page_romaneio = 'paginas/romaneio/inicial.jsf'

def test_login_browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        color_scheme='dark'
    )
    page = context.new_page()

    log_in = ExecuteLogin(page)
    botao = Clicar(page)

    log_in.navigate(site)
    page.wait_for_load_state("networkidle")

    log_in.submit_login('cciliato', 'Alvorada@1234')
    botao.NomeBotao("Entrar", 3000)

    test_romaneio(page)


def test_romaneio(page):
    url = str(site + page_romaneio)
    page.goto(url)
    page.wait_for_load_state("networkidle")

    page.set_default_timeout(1000)

    print(f'-> Iniciando Operação')

    selecao_opr = SelecaoOperacao(page)
    sleep(2)
    print(f'-> Clica Operação')

    campos_opr = CamposRomaneio()
    sleep(2)

    texto_opera = campos_opr.selecao_operacao

    selecao_opr.EscolherCampos(texto_opera)
    sleep(2)

    print(f'-> Seleção Operação')

    selecao_opr.Digitar_Valor("700 - Entrada Spot")
    #page.pause()
    sleep(2)
    print(f'-> Fim Operação')



