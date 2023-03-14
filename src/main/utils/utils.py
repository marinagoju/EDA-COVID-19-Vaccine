
import pandas as pd

dict_comunidades = {"Andalucía":"AN",
                    "Aragón":"AR",
                    "Asturias":"AS", 
                    "Canarias":"CN",
                    "Cantabria":"CB",
                    "Castilla - La Mancha":"CM",
                    "Castilla y León":"CL",
                    "Cataluña":"CT",
                    "Extremadura":"EX",
                    "Galicia":"GA",
                    "Baleares":"IB",
                    "La Rioja":"RI",
                    "Madrid":"MD",
                    "Murcia":"MC",
                    "Navarra":"NC",
                    "País Vasco":"PV",
                    "Comunidad Valenciana":"VC",
                    "Ceuta":"CE",
                    "Melilla":"ML"}

ISO = "ISO"  # cnt para nombrar al código identificador

def LoadVacunas(lista):
    '''Función que genera un unico dataframe resultante de la concatenacion de varios dataframes añadiendo una columna adicional con un
       codigo identificador de los datos. En este caso el código ISO de cada CC.AA de donde provienen los datos de cada dataframe.

    Input (lista): Lista de Tuplas (ruta del archivo excel, codigo identificador de los datos que se refiere al nombre de la hoja de excel)
        
    Output: pd.DataFrame
    
    '''  
    df = pd.DataFrame()    # Los DataFrames que se importan se van concatenando en esta variable.

    for i in lista:
        df_loaded = pd.read_excel(i[0], sheet_name = i[1])
        df_loaded[ISO] = i[1]
        df = pd.concat([df , df_loaded])
    return df

def ScrapISOdata():
    '''Función que scrapea un dataframe con los códigos ISO de todas las provincias de España y el correspondiente codigo ISO de su comunidad autónoma.
       Los códigos ISO son códigos estandarizados que identifican a las demarcaciones administrativa de cada país.

    Input: Ninguno
        
    Output: pd.DataFrame
    
    ''' 
    # Driver de Chrome de Selenium
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    # Herramientas para buscar elementos
    from selenium.webdriver.common.by import By
    service = Service(ChromeDriverManager().install())
    import time
    from bs4 import BeautifulSoup as bs

    # 1- Mi instancia del driver de Chrome para scrapear
    driver = webdriver.Chrome(service=service)
    # 2- Seleccionamos url de la que queremos obtener datos y la solicitamos al sitio web (se inician drivers -> abre el navegador)
    url = "https://www.iso.org/obp/ui/es/#iso:code:3166:ES"
    driver.get(url)
    # 3- Esperamos a que carge la pagina (10 segundos).
    time.sleep(10)
    # 4- Rescatamos el contenido html de la pagina web solicitada (codigo fuente)
    html = driver.page_source
    # 5- Buscamos los elementos 'table' (queremos obtener tabla de los codigos ISO de cada CC.AA y su correspondiente provincia)
    page = driver.find_elements(By.TAG_NAME, 'table')   
    # 6- Traduce o parsea el contenido html de la web. Devuelve un objeto bs donde buscaremos por etiqueta.
    soup = bs(html, "lxml")
    # 7- Buscamos las tablas que hay en la página con los atributos class e id. Nos devuelve una lista.
    table = soup.find("table", attrs = {'class':'tablesorter', 'id':'subdivision'})
    # 8- Seleccionamos la tabla que nos interesa de la lista y la cargamos con prettify de bs4 para que Pandas lo traduzca a df. https://stackoverflow.com/questions/41100451/load-scraped-table-via-bs4-into-pandas-dataframe
    ISO_CODE_DF = pd.read_html(table.prettify())[0]

    # 9- Aplicamos función Lambda para eliminar el "ES-" de los códigos ISO. 
    ISO_CODE_DF["Código 3166-2"] = ISO_CODE_DF["Código 3166-2"].apply( lambda x: str(x).replace("ES-", ""))
    ISO_CODE_DF["Subdivisión superior"] = ISO_CODE_DF["Subdivisión superior"].apply( lambda x: str(x).replace("ES-", ""))


    # Seleccionamos el contenido de la tabla que nos interesa (filas con el codigo ISO de las provincias y el de su equivalente CC.AA)
    ISO_DF = ISO_CODE_DF.loc[ ISO_CODE_DF["Categoría de la subdivisión"] == "province" ][["Código 3166-2", "Subdivisión superior" ]]\
        .drop_duplicates().reset_index().drop(columns="index")

    # Agregamos filas al df para Ceuta, Melilla y No Contesta (NC).
    row_1 = {"Código 3166-2": "CE", "Subdivisión superior": "CE"}
    row_2 = {"Código 3166-2": "ML", "Subdivisión superior": "ML"}
    row_3 = {"Código 3166-2": "NC", "Subdivisión superior": "NC"}
    ISO_DF = ISO_DF.append(row_1, ignore_index=True)
    ISO_DF = ISO_DF.append(row_2, ignore_index=True)
    ISO_DF = ISO_DF.append(row_3, ignore_index=True)

    return ISO_DF