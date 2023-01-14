import re
import time

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright


class PesquisaBase:
    def __init__(self, assunto, quantidade):
        self.assunto = assunto
        self.quantidade = quantidade
        
    
    def __str__(self):
        return self.pesquisar()
        
    def pesquisar(self):
        with sync_playwright() as p:

            navegador = p.chromium.launch(headless=False) # headless
            pagina = navegador.new_page()
            pagina.set_default_navigation_timeout(100000)
            pagina.set_default_timeout(100000)
            pagina.goto(f"https://www.youtube.com/results?search_query=edit+{self.assunto}+short")

            pagina.dblclick('//*[@id="thumbnail"]/yt-image/img')
            pagina.locator('//*[@id="logo-icon"]')    
            time.sleep(1)
            lista = [pagina.url]
            for x in self.quantidade:
                for i in range(3):
                    pagina.keyboard.up("PageDown")
                    time.sleep(1)
                    pagina.keyboard.down("PageDown")
                    pagina.locator('//*[@id="logo-icon"]') 
                    pagina.url
                lista.append(pagina.url)


            print(lista)
            return lista
    
            #pesquisa site dps pega urls > abaixa os videos  >> colocar os videos na plataforma


if __name__ == "__main__":
    c = PesquisaBase('Madara Uchiha', 1)
    print(c.pesquisar())