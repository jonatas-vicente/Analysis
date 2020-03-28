import requests
import pandas as pd

##----------------------------------------------------------------------------Download de Tabela----------------------------------------##
url = 'https://www.fundamentus.com.br/resultado.php'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
print(df)

													###Critérios###
#Fómula de Grahan
#Fonte: https://www.fundamentus.com.br/pagina_do_ser/equacaoGrahan.htm
#P = EPS Proj* (8,5 + (2*G)) * (4,4/AAA yield)
#P = EPS Proj* (5,5 + (2*G)) * (4,4/Selic)??
#** Analisar os Índices corretos #

#-----------------------------------------------------------------------------------------------------------------------------------------#
#Critério do fluxo de caixa descontado

#-----------------------------------------------------------------------------------------------------------------------------------------#
#Basi
#Yield > 6%

#-----------------------------------------------------------------------------------------------------------------------------------------#
#Análise por indicadores
								#Receita/Lucro (Lucro Líquido)
#Setores Parentes (Resultados consistentes : baixa variação) [monopóloio ou oligopólio (Bancos, Seguro, Eletricidade, Saneamento)] {Dividendo Constante}
#Setores Cíclicos (Resultados inconsistentes : alta variação)[Mineração, Ciderurgia, Agricultura, Logística, Transporte, Varejo, Moda]

					##Formas de investir##
#Setores Perenes: (Sócio: Viés de longo prazo){Dividendos}
#Setores Cíclico: (Valor: Viés de Especulação)

##	Análise de Setores Perenes
#	-Lucro constante e positivo


#------------------------------------------------------------------------------------------------------------------------------------------#