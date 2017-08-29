# parserpostfix
English:It's a script to parser log of postfix services to extract the info to show by shell or web.

Spanish:Es un script  para analizar el log del servicio postfix para extraer la info para mostrar por la shell o por web. 

E:TODO

E: Will be develope on python-2.7 for a log's format used in my VPS Server from Comvive Servidores SL. After will be develope for an format's log for a installation from standard debian package of postfix.

S:Por Hacer

S:Se desarrollará en python-2.7 para el formato que se usa en mi servidor VPS de Comvive Servidores SL. Después se desarrollará para  el formato de log de un paquete de postfix standard de Debian. 

E: HOW TO WORK.

E:The script have two filter:
1. by time, we set time reference and one interval maybe 60 seconds search on log:
   a. sender,
   b. recipient.
2. by sender / recipient and show all traffic where two or on one is present, or both them are present. 

S:Cómo funciona:

S:Tiene dos modos de búsqueda:
1. por tiempo, en el cual le pasamos el tiempo de referencia, y en un intervalo de más/menos un minuto buscará los datos de:
   a. emisor
   b. receptor.
2. por emisor / receptor y se mostrarán todos el tráfico donde los dos correos o uno de ellos estén presentes.

comprobando.
