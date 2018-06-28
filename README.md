# Primeros pasos como Data Scientist en Falabella .COM

## Primera parte

Falabella.COM cuenta con muchas fuentes de información distintas que se deben integrar para lograr la publicación de los productos en el sitio web. Estas fuentes de información combinadas con reglas de negocio indican si finalmente un producto debe ser publicado en un mosaico, y en qué posición debe ser mostrado.

Por otro lado, la tabla de descripción de productos es muchas veces llenada manualmente por proveedores o administrativos web de Falabella. Uno de los mayores desafíos enfrentados al momento de analizar los productos es el preprocesamiento de la información.

En este caso te pedimos que definas una **métrica de similaridad para productos de calzado**. Puedes utilizar el lenguaje (preferiblemente Python3.X) y las librerías que más te acomoden.

El objetivo de esta experiencia es entender tu forma de pensar y de resolver un problema de Data Mining.

El **entregable** consiste en:
   1. Informe en 1 plana explicando los pasos generales para resolver el problema. Además del porqué de la elección del entorno de desarrollo y modelos seleccionados.
   1. Código / Notebook autocontenido explicando las transformaciones y decisiones tomadas. Además de explicar cómo evaluaste tu métrica de similaridad.
   1. Si son N productos, se espera como output una matriz de NxN donde cada casillero contiene la similaridad de un producto a otro.
   1. Se debe entregar un script llamado get_distance.py que solo contenga una función que recibe dos índices y retorna la distancia entre esos productos.

## Segunda parte

En esta segunda parte te pedimos encontrar conjuntos de zapatos parecidos entre ellos, y distintos a los de los otros conjuntos. Para esto puedes utilizar cualquier técnica y librería.

El **entregable** consiste en:
   1. Informe en 0,5 planas explicando los pasos generales para resolver el problema. Además del porqué de la elección de los modelos seleccionados.
   1. Código / Notebook autocontenido explicando las transformaciones y decisiones tomadas. Además de explicar cómo evaluaste tu métrica de la segmentación.
   1. Si son N productos, se espera como output un archivo con N filas, donde el único valor por fila es el identificador de su conjunto.
   1. Se debe entregar un script llamado get_cluster.py que solo contenga una función que recibe un nuevo producto (representado como en la DB original)  y retorna su conjunto asignado.

## Preguntas

Para complementar tu experiencia debes agregar un archivo respondiendo las siguientes preguntas (no más de 5 líneas cada respuesta):

1. ¿Cómo harías la separación entre IA y ML?
1. ¿Cuáles son los pasos generales que habría que seguir en un lugar donde no se han desarrollado muchos proyectos de Machine Learning y se quiere resolver un problema se clustering de clientes?
1. ¿Cuál es la diferencia entre algoritmos supervisados y no supervisados?
1. ¿Para qué se utiliza el algoritmo Kmeans y cómo funciona?


**Referencias**: Puedes agregar referencia a bibliografía en cualquier parte de tu solución para soportar tus decisiones. 

**Consultas**: Ante cualquier consulta crear un Issue.
