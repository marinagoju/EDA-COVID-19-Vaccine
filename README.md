![imagen](https://github.com/marinagoju/EDA-COVID-19-Vaccine/blob/main/src/data/vacuna.jpg)
# <div align="center">**Efectividad de la vacuna de ARNm contra la COVID-19**:syringe:</div>

Este estudio tiene por objeto valorar la efectividad de la vacuna de ARN mensajero administrada contra el SARS-Cov-2. 
Para ello observaremos la evolucion de la COVID-19 en relación a la campaña de vacunación implementada en España.    
Nos preguntamos: *¿Cuáles son los cambios que se aprecian en la curva de evolución de la enfermedad desde que se introducen las nuevas vacunas de ARN mensajero?*<br></br> 

***¿Por qué un EDA sobre la efectividad de las vacuna contra la COVID-19?***<br></br>
Han pasado más de tres años desde que se diagnosticó el primer caso de COVID-19 en España, por aquel entonces no imaginábamos hasta qué punto se vería amenazado el funcionamiento normal del mundo. Había mucha incertidumbre al respecto, la población se enfrentaba a algo que no podía ver, y se plantearon muchas dudas acerca de su transmisibilidad, cómo evolucionaba y de las medidas sanitarias implantadas para frenar su avance. Incluso aún a día de hoy sigue habiendo cierta incertidumbre sobre la efectividad de las vacunas. 

Por ello, con motivo de arrojar un poco de luz sobre la cuestión y aprovechando la cantidad de datos epidemiológicos publicados por las instituciones de todo el mundo (al ser una enfermedad de declaración obligatoria: EDO), surgió la idea de iniciar este proyecto.<br></br>


## 🔎 1. Metodología de la investigación

El estudio que se expone es un estudio de tipo descriptivo retrospectivo, pues nos limitamos a recoger y analizar datos sin influir en el fenómeno de estudio. Asimismo, los datasets sobre los que trabajamos refieren información relativa a momentos anteriores al inicio de su análisis. La hipótesis preliminar que se planteó fue la siguiente:<br></br>
<div align="center"> ***H0: **La vacunación de ARNm es efectiva contra el SARS-Cov-2*** </div>

Los datos utilizados en esta investigación provienen de las estadísticas y reportes publicados por las instituciones oficiales de España. Trabajamos principalmente con cuatro datasets:

- **Datos relativos a la evolución de la crisis COVID-19** obtenidos a partir de la declaración individualizada de casos de COVID-19 por las CC.AA a la Red Nacional de Vigilancia Epidemiológica (RENAVE) a través de la plataforma informática SiViES que gestiona el Centro Nacional de Epidemiología (CNE). Recoge los casos confirmados, así como eventos de diferente nivel de gravedad, desde casos leves hasta hospitalizaciones, ingresos en UCI y fallecimientos.

- **Cifras oficiales de población** resultantes de la revisión del Padrón municipal a 1 de enero del 2021. Filtramos por comunidad autónoma y edad, considerando solamente a la población mayor de 12 años que es a la que va dirigida la campaña de vacunación.

- **Dataset de los datos de vacunación por comunidad autónoma** publicados con Power BI en la página web del Ministerio de Sanidad de España. Estos datos se obtuvieron mediante la captura de imagen de cada una de las tablas de datos de vacunación para cada CC.AA conjunto con un parser que nos reconvirtió la imagen en formato png a formato xlsx. Contempla a las personas vacunadas con al menos una dosis, personas con la pauta completa de vacunación, y personas vacunadas con dosis de recuerdo.

- **Datos de los tipos de vacunas administradas y entregadas a cada comunidad autónoma** ofrecidos por el Registro de vacunación frente a COVID-19 (REGVACU).<br></br>

La población de estudio abarca a toda la población residente en España en el periodo de tiempo comprendido desde la detección del primer caso COVID en el país (31/01/2020), hasta la entrada en vigor de la nueva estategia de vigilancia (01/04/2022) por la que solo se notifican casos en individuos de 60 años o más.<br></br>

## 📑 2. Análisis de datos

Los datos se han analizado en base series temporales (evolución) y diagramas de barras de frecuencias relativas o absolutas según ha sido conveniente.

**Indicadores  pronósticos** considerados para estudiar de la evolución y situación epidemiológica de la pandemia en consonancia para poder valorar la efectividad de la vacuna son:

- Incidencia acumulada a 14 días por cada 100.000 habitantes (pendiente)
- Número de casos nuevos confirmados
- Número de casos nuevos de hospitalizaciones por COVID-19.
- Número de ingresos nuevos en UCI.
- Número de defunciones nuevas. 

Se pueden apreciar las oleadas o periodos epidémicos vividos a lo largo de la pandemia en funcion del examen de estos indicadores.

**Fechas** a considerar en el análisis de los datos:
* **Inicio periodo de estudio** (31 de Enero de 2020). Marcado por la detección del primer caso COVID en España.
* **Fin periodo estudio** (28 de marzo de 2022). Actualización de la Estrategia de Vigilancia y Control de la COVID-19, por la que solo se notifican casos en personas de más de 60 años.  
* **Inicio de la campaña de vacunación** (20 de diciembre de 2021)  
* **Oleadas**: Hasta el 28 de marzo de 2022 se identificaron en España seis periodos epidémicos de COVID-19:
  - Primer periodo: Desde el 31 de enero hasta el 21 de junio de 2020.
  - Segundo periodo: Desde el 22 de junio hasta el 6 de diciembre de 2020.
  - Tercer periodo: Desde el 7 de diciembre de 2020 hasta el 14 de marzo de 2021.
  - Cuarto periodo: Desde el 15 de marzo de 2021 hasta el 19 de junio.
  - Quinto periodo: Desde el 20 de junio de 2021 hasta el 13 de octubre.
  - Sexto periodo: Desde el 14 de octubre de 2021 hasta el 27 de marzo de 2022.<br></br>
  
Para estudiar los datos de la población vacunada hemos tomado cifras de vacunas entregadas a las comunidades autónomas, pero como de acuerdo a los datos el porcentaje de vacunas administradas frente a las entregadas supera el 95% en España, los consideraremos equivalentes.

Los cálculos de las frecuencias relativas de población vacunada se han hecho sobre la población mayor de 12 años residente en España en 2021, que son los grupos de edad a los que fue dirigida a priori la campaña de vacunación.<br></br>

## 📋 3. Resultados generales

**Sobre la población vacunada**:
- Población vacunada predominantemente con vacunas de ARNm (Pfizer, Moderna). Con distribución no uniforme por grupos de edad.
- En los últimos estadíos de la campana de vacunación el porcentaje de vacunados alcanza cifras superiores al 95%, tanto en lo que respecta a aquellos con al menos una dosis y con la pauta completa.

**Sobre la efectividad de la vacunación**:
- Descenso de casos de hospitalización, ingresos en UCI y defunciones (casos graves) en las oleadas siguientes a la administración de la vacuna.
- Aumento de los casos de contagios (variante Ómicron).
- La mayoría de los casos confirmados son personas entre 40-49 años de edad.
- La mayoría de hospitalizados son personas mayores de 80 años de edad.
- La mayoría de los ingresos en UCI son personas entre 60-69 años de edad.
- La mayoría de los casos de defunciones son personas mayores de 80 años de edad.
<br></br>
## 📋 4. Conclusiones
A priori podemos aceptar nuestra hipótesis nula, dado que, de acuerdo con los datos, la vacunación ha llevado a un marcado descenso de casos graves (hospitalizados e ingresos en UCI) y de las defunciones entre los casos infectados.

Respecto al poco impacto de la vacuna en lo que respecta a la transmisibilidad de la enfermad, aún se está estudiando el por qué a pesar de la inmunización adquirida el agente logra traspasar las defensas del organismo. Pero todo apunta a que es una cuestión relacionada con los mecanismos de infección del virus.

Según los informes epidemiológicos, las variantes que terminan prevaleciendo son aquellas que presentan una mayor capacidad de escape inmune frente a otras, y por tanto aquellas que son más contagiosas. Pero también las que manifiestan menos gravedad de los casos que contagian, dado que para la propia preservación del agente infeccioso se prima la supervivencia del huésped.<br></br>

## 💬 5. Comentarios

Quedó pendiente estandarizar los datos mediante tasas de mortalidad o incidencia acumulada a 14 días por 100.000 habitantes para comparar entre distintas poblaciones. 
También para un futuro, sería un aspecto a considerar, estudiar la campaña de vacunación por grupos de edad y contrastarlo a su vez con la evolución de la COVID-19 por grupos de edad.

Entre los sesgos que se identifican en este estudio es que no se hace un análisis simultáneo de las muestras. Estudia la misma población en distintos momentos temporales. Es decir, el control de los casos lo representa la misma población, pero en un estado o momento temporal previo a la vacuna.

A su vez observamos un sesgo en lo que respecta a la detección de los casos dato que se utilizan metodologías de diagnóstico de diferente sensibilidad a lo largo del periodo de estudio. Aunque esto es comprensible dado que, por el carácter de nueva aparición del coronavirus, todos los métodos de diagnóstico se encontraban en proceso experimental.<br></br>

## ⚙️ 6. Librerías y recursos

- Tableau Public 2022.4
- Matplotlib
- Seaborn
- Pandas
- Selenium
- BeautifulSoup4
- Canvas
