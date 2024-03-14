
Algoritmo: max_subarray
Este script en Python encuentra la sublista contigua dentro de una lista que tiene la mayor suma de elementos.
Funcionamiento:

1. Inicialización de variables: Se inicializan varias variables para llevar un registro de la suma más grande encontrada (`max_sum`), los índices de inicio y fin de la sublista con la suma más grande (`start_index` y `end_index`), la suma actual de la sublista en consideración (`current_sum`) y el índice de inicio de la mejor sublista encontrada hasta el momento (`temp_start_index`).

2. Iteración a través de la lista: El script recorre cada elemento de la lista, realizando un seguimiento tanto del valor como del índice.

3. Actualización de la suma actual: Para cada elemento en la lista, se suma su valor a `current_sum`, actualizando la suma de la sublista actual en consideración.

4. Comparación con la suma más grande: Después de actualizar `current_sum`, el script la compara con `max_sum`. Si `current_sum` es mayor que `max_sum`, se actualiza `max_sum`, `start_index` y `end_index` para reflejar la nueva suma más grande y sus índices de sublista correspondientes.

5. Restablecimiento de la suma actual: Si `current_sum` se vuelve negativa durante la iteración, indica que la sublista actual no contribuye positivamente a la suma total. Por lo tanto, `current_sum` se restablece a 0 y `temp_start_index` se actualiza al índice del siguiente elemento.

6. Devolución de la sublista con la suma más grande: Una vez que se completa la iteración a través de la lista, el script devuelve la sublista con la suma más grande encontrada.

Uso:

Para utilizar el script, simplemente llame a la función `max_subarray()` y pase la lista de enteros como argumento. Por ejemplo:

```python
arr = [1, -3, 2, 1, -1]
print("Sublista con la mayor suma:", max_subarray(arr))
```

Esto devolverá la siguiente salida:

```
Sublista con la mayor suma: [2, 1]
```
```
