# Log Formatter
Herramienta para ordenar visualmente registros de datos en la consola.
Esta pequeña herramienta está escrita en Python 3.5

### Ejemplo
Esta herramienta realiza ordenaciones de listas como el ejemplo que se muestra en la siguiente imágen:
<img src="https://lh3.googleusercontent.com/7WfZLZF26s9-jKyBMr6PmhNXdVexF8uKDIJjaeCiwEDXr0rh6D-odZKtgO6LQCuAkfWEDpDqp6oTLAI=w1366-h705"><img>

### Importación de la librería
Se recomienda importar la librería en su totalidad de la siguiente forma:
```python
from log_formatter import *
```
### Funciones
La librería cuenta con las siguientes funciones:
- ```getFormattedLog(headers, content)```: Este método retorna ```string``` en caso de efectuar su tarea de forma adecuada, de lo contrario su valor de retorno será ```None```.
  Dispone de dos parámetros, ambos obligatorios.
  - ```headers```: Su tipo debe ser una lista, con cadenas de texto (```string```) en su interior.<br>
  Cada cadena de texto es un título para cada columna del contenido de la tabla.<br>
  Ejemplo: ```["Nombre", "Apellido", "Edad"]```.
  - ```content```: Su tipo debe ser una lista, a su vez, debe contener listas, las cuales contienen cadenas de texto, cada una de ellas es el equivalente a una fila de la tabla, cada valor equivale a un elemento de la tabla en relación a su cabecera, es decir, estos elementos deben ser ordenados de acuerdo a la posición de las cabeceras introducidas en el parámetro ```headers```. Cabe mencionar que la cantidad de valores en cada elemento debe ser idéntica al de la lista de las cabeceras, de lo contrario la función devolverá ```None```.<br>
  Ejemplo: ```[["Miguel", "Rivas", "18"], ["Daniela", "Vargas", "21"]]```.

### Código de ejemplo
El siguiente fragmento de código muestra un ejemplo de consumo de la herramienta:
```python
from log_formatter import *

myLog = getFormattedLog(["Libro", "Autor", "Precio"], [
 ["El cazador de sueños", "Stephen King", "$18"],
 ["Veinte mil leguas de viaje submarino", "Julio Verne", "$17"],
 ["Cosmos", "Carl Sagan", "$24"]])

print(myLog)

'''SALIDA
Libro                                Autor        Precio 
==================================== ============ ====== 
El cazador de sueños                 Stephen King $18    
Veinte mil leguas de viaje submarino Julio Verne  $17    
Cosmos                               Carl Sagan   $24    
'''```
