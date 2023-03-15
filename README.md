![imagen](https://github.com/marinagoju/EDA-COVID-19-Vaccine/blob/main/src/data/vacuna.jpg)
# <div align="center">**Efectividad de la vacuna de ARNm contra la COVID-19**:syringe:</div>

Este estudio tiene por objeto valorar la efectividad de la vacuna de ARN mensajero administrada contra el SARS-Cov-2. 
Para ello observaremos la evolucion de la COVID-19 en relación a la campaña de vacunación implementada en España.    
Nos preguntamos: *¿Cuáles son los cambios que se aprecian en la curva de evolución de la enfermedad desde que se introducen las nuevas vacunas de ARN mensajero?*<br></br> 

***¿Por qué un EDA sobre la efectividad de las vacuna contra la COVID-19?***<br></br>

Han pasado más de tres años desde que se diagnosticó el primer caso de COVID-19 en España, por aquel entonces no imaginábamos hasta qué punto se vería amenazado el funcionamiento normal del mundo. Había mucha incertidumbre al respecto, la población se enfrentaba a algo que no podía ver, y se plantearon muchas dudas acerca de su transmisibilidad, cómo evolucionaba y de las medidas sanitarias implantadas para frenar su avance. Incluso aún a día de hoy sigue habiendo cierta incertidumbre sobre la efectividad de las vacunas. 

Por ello, con motivo de arrojar un poco de luz sobre la cuestión y aprovechando la cantidad de datos epidemiológicos publicados por las instituciones de todo el mundo (al ser una enfermedad de declaración obligatoria: EDO), surgió la idea de iniciar este proyecto.<br></br>


## 1. Metodología de la investigación<br></br>

El estudio que se expone es un estudio de tipo descriptivo retrospectivo, pues nos limitamos a recoger y analizar datos sin influir en el fenómeno de estudio. Asimismo, los datasets sobre los que trabajamos refieren información relativa a momentos anteriores al inicio de su análisis.

La hipótesis preliminar que se plantea inicialmente es la siguiente:  
H0: La vacunación de ARNm es efectiva contra el SARS-Cov-2.

Los datos utilizados en esta investigación provienen de las estadísticas y reportes publicados por las instituciones oficiales de España. Trabajamos principalmente con cuatro datasets:

- Datos relativos a la evolución de la crisis COVID-19 obtenidos a partir de la declaración individualizada de casos de COVID-19 por las CC.AA a la Red Nacional de Vigilancia Epidemiológica (RENAVE) a través de la plataforma informática SiViES que gestiona el Centro Nacional de Epidemiología (CNE). Recoge los casos confirmados, así como eventos de diferente nivel de gravedad, desde casos leves hasta hospitalizaciones, ingresos en UCI y fallecimientos.

- Cifras oficiales de población resultantes de la revisión del Padrón municipal a 1 de enero del 2021. Filtramos por comunidad autónoma y edad, considerando solamente a la población mayor de 12 años que es a la que va dirigida la campaña de vacunación.

- Dataset de los datos de vacunación por comunidad autónoma publicados con Power BI en la página web del Ministerio de Sanidad de España. Estos datos se obtuvieron mediante la captura de imagen de cada una de las tablas de datos de vacunación para cada CC.AA conjunto con un parser que nos reconvirtió la imagen en formato png a formato xlsx. Contempla a las personas vacunadas con al menos una dosis, personas con la pauta completa de vacunación, y personas vacunadas con dosis de recuerdo.

- Datos de los tipos de vacunas administradas y entregadas a cada comunidad autónoma ofrecidos por el Registro de vacunación frente a COVID-19 (REGVACU).

La población de estudio abarca a toda la población residente en España en el periodo de tiempo comprendido desde la detección del primer caso COVID en el país (31/01/2020), hasta la entrada en vigor de la nueva estategia de vigilancia (01/04/2022) por la que solo se notifican casos en individuos de 60 años o más.<br></br>



## 2. Análisis de datos  
djsodada

### 3. Conclusiones  
djsodada

### 4. Recursos  
djsodada

