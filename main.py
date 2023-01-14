from dowloander import dowloander
from pesquisa import PesquisaBase

assunto = input('Digite o assunto: ')
contagem = input('Digite a quantidade de Videos: ')
site = PesquisaBase(assunto, contagem)

lista = site.pesquisar()    
dowloander(lista)
