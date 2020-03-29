PAV - P3: detección de pitch
============================

Esta práctica se distribuye a través del repositorio GitHub [Práctica 3](https://github.com/albino-pav/P3).
Siga las instrucciones de la [Práctica 2](https://github.com/albino-pav/P2) para realizar un `fork` de la
misma y distribuir copias locales (*clones*) del mismo a los distintos integrantes del grupo de prácticas.

Recuerde realizar el *pull request* al repositorio original una vez completada la práctica.

Ejercicios básicos
------------------

- Complete el código de los ficheros necesarios para realizar la detección de pitch usando el programa
  `get_pitch`.

   * Complete el cálculo de la autocorrelación e inserte a continuación el código correspondiente.
    	```.sh
      void PitchAnalyzer::autocorrelation(const vector<float> &x, vector<float> &r) const {
        for (unsigned int k = 0; k < r.size(); ++k) {
            for(unsigned int l=0; l < x.size()-1-k ; ++l ){
              r[k] = r[k] + (x[l]*x[l+k]);
            }
           r[k]=r[k]/x.size();
        }
            if (r[0] == 0.0F) //to avoid log() and divide zero 
             r[0] = 1e-10; 
      }
      ```

   * Inserte una gŕafica donde, en un *subplot*, se vea con claridad la señal temporal de un sonido sonoro
     y su periodo de pitch; y, en otro *subplot*, se vea con claridad la autocorrelación de la señal y la
	 posición del primer máximo secundario.

   <img src="img/Senyal_i_auto.png" width="640" align="center">

   Para la representación de las gráficas, hemos usado el siguiente código de Python:
      	```.sh
            import matplotlib.pyplot as plt
            import numpy as np
            import soundfile as sf

            senyal, fm = sf.read('pav_2181.wav')

            t = np.arange(0, len(senyal)) / fm

            plt.subplot(2,1,1)
            plt.title('Senyal en temps')
            plt.plot(t, senyal)

            plt.subplot(2,1,2)
            plt.title('Autocorrelació')
            plt.acorr(senyal, maxlags=20)

            plt.show()
        ```
        
	 NOTA: es más que probable que tenga que usar Python, Octave/MATLAB u otro programa semejante para
	 hacerlo. Se valorará la utilización de la librería matplotlib de Python.

   * Determine el mejor candidato para el periodo de pitch localizando el primer máximo secundario de la
     autocorrelación. Inserte a continuación el código correspondiente.
    ```c
      vector<float>::const_iterator iR= r.begin(), iRMax = iR;
      while(*iR>0){
        iR++;
      }
      if(iR<r.begin()+npitch_min)
       iR += npitch_min;
      iRMax= iR;
      while(iR != r.end()){
        if(*iR>*iRMax)
          iRMax=iR;
        ++iR;
      }
      unsigned int lag = iRMax - r.begin(); 
    ```


   * Implemente la regla de decisión sonoro o sordo e inserte el código correspondiente.
   	```c
      bool PitchAnalyzer::unvoiced(float pot, float r1norm, float rmaxnorm) const {
         bool unvoiced;
               if (pot < -50 || r1norm < 0.7 || rmaxnorm < 0.3 || (r1norm<0.9 && rmaxnorm<0.4) )
                    unvoiced=true;
               else
                   unvoiced=false;
         return unvoiced;
       }
    ```

- Una vez completados los puntos anteriores, dispondrá de una primera versión del detector de pitch. El 
  resto del trabajo consiste, básicamente, en obtener las mejores prestaciones posibles con él.

  * Utilice el programa `wavesurfer` para analizar las condiciones apropiadas para determinar si un
    segmento es sonoro o sordo. 
	
	  - Inserte una gráfica con la detección de pitch incorporada a `wavesurfer` y, junto a ella, los 
	    principales candidatos para determinar la sonoridad de la voz: el nivel de potencia de la señal
		(r[0]), la autocorrelación normalizada de uno (r1norm = r[1] / r[0]) y el valor de la
		autocorrelación en su máximo secundario (rmaxnorm = r[lag] / r[0]).


    <img src="img/recorte1.PNG" width="640" align="center">

		Puede considerar, también, la conveniencia de usar la tasa de cruces por cero.

	    Recuerde configurar los paneles de datos para que el desplazamiento de ventana sea el adecuado, que
		en esta práctica es de 15 ms.

      - Use el detector de pitch implementado en el programa `wavesurfer` en una señal de prueba y compare
	    su resultado con el obtenido por la mejor versión de su propio sistema.  Inserte una gráfica
		ilustrativa del resultado de ambos detectores.


     <img src="img/pitch_prog_wave_PROVA.PNG" width="640" align="center">

          Aquí podemos observar dos contornos de pitch:
          El primero es el obtenido con nuestra mejor versión del programa. 
          La segunda gráfica es la del detector de pitch de wavesurfer.
          Como podemos observas los contornos de pitch son muy parecidos pero a distintas escalas debido a la configuracion del wavesurfer. 
  
  * Optimice los parámetros de su sistema de detección de pitch e inserte una tabla con las tasas de error
    y el *score* TOTAL proporcionados por `pitch_evaluate` en la evaluación de la base de datos 
	`pitch_db/train`..

        ### Summary
        Num. frames:    11200 = 7045 unvoiced + 4155 voiced
        Unvoiced frames as voiced:      345/7045 (4.90 %)
        Voiced frames as unvoiced:      314/4155 (7.56 %)
        Gross voiced errors (+20.00 %): 69/3841 (1.80 %)
        MSE of fine errors:     2.29 %

        ===>    TOTAL:  91.22 %
        --------------------------


   * Ineserte una gráfica en la que se vea con claridad el resultado de su detctor de pitch junto al del
     detector de Wavesurfer. Aunque puede usarse Wavesurfer para obtener la representación, se valorará
	 el uso de alternativas de mayor calidad (particularmente Python).


     <img src="img/pitch_prog_wave.PNG" width="640" align="center">


Ejercicios de ampliación
------------------------

- Usando la librería `docopt_cpp`, modifique el fichero `get_pitch.cpp` para incorporar los parámetros del
  detector a los argumentos de la línea de comandos.
  
  Esta técnica le resultará especialmente útil para optimizar los parámetros del detector. Recuerde que
  una parte importante de la evaluación recaerá en el resultado obtenido en la detección de pitch en la
  base de datos.

  * Inserte un *pantallazo* en el que se vea el mensaje de ayuda del programa y un ejemplo de utilización
    con los argumentos añadidos.

- Implemente las técnicas que considere oportunas para optimizar las prestaciones del sistema de detección
  de pitch.

  Entre las posibles mejoras, puede escoger una o más de las siguientes:

  * Técnicas de preprocesado: filtrado paso bajo, *center clipping*, etc.
  * Técnicas de postprocesado: filtro de mediana, *dynamic time warping*, etc.
  * Métodos alternativos a la autocorrelación: procesado cepstral, *average magnitude difference function*
    (AMDF), etc.
  * Optimización **demostrable** de los parámetros que gobiernan el detector, en concreto, de los que
    gobiernan la decisión sonoro/sordo.
  * Cualquier otra técnica que se le pueda ocurrir o encuentre en la literatura.

  Encontrará más información acerca de estas técnicas en las [Transparencias del Curso](https://atenea.upc.edu/pluginfile.php/2908770/mod_resource/content/3/2b_PS Techniques.pdf)
  y en [Spoken Language Processing](https://discovery.upc.edu/iii/encore/record/C__Rb1233593?lang=cat).
  También encontrará más información en los anexos del enunciado de esta práctica.

  Incluya, a continuación, una explicación de las técnicas incorporadas al detector. Se valorará la
  inclusión de gráficas, tablas, código o cualquier otra cosa que ayude a comprender el trabajo realizado.

  También se valorará la realización de un estudio de los parámetros involucrados. Por ejemplo, si se opta
  por implementar el filtro de mediana, se valorará el análisis de los resultados obtenidos en función de
  la longitud del filtro.
   

Evaluación *ciega* del detector
-------------------------------

Antes de realizar el *pull request* debe asegurarse de que su repositorio contiene los ficheros necesarios
para compilar los programas correctamente ejecutando `make release`.

Con los ejecutables construidos de esta manera, los profesores de la asignatura procederán a evaluar el
detector con la parte de test de la base de datos (desconocida para los alumnos). Una parte importante de
la nota de la práctica recaerá en el resultado de esta evaluación.
