<?php

	/* Funciones */
	inlcude_once("funciones.php");

	/*Tomamos de la linea de comando las variables con la que vamos a buscar los correos.

	1. fecha de la busqueda, sino estÃ¡ establecida se toma la fecha del dÃa en curso

	*/

	$ARGUMENTOS=normaliza($ARGV);	

	if (is_null($ARGUMENTOS['fecha'])){

		/* buscamos en el dia actual*/

		$file="/var/log/mail.log";
	}else{
		/*Calculamos a partir de la fecha el dia
		y comprobamos que existe el archivo para 
		descomprimirlo y leerlo
		*/
		$file=calcularfecha($DATE);
		if (! is_file($file)){
			echo "El archivo no existe\n";
		}else{
			fopen($DESC,$file,"r");
			
		}
	}
?>		
	

