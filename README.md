# Ejercicio módulo de funciones números primos
### El ejercicio
- Escriba la función es_divisible(n, d) que indique si n es divisible por d:
```sh
  > es_divisible(15, 5)
  > True
  > es_divisible(15, 6)
  > False
```

- Usando la función es_divisible, escriba una función es_primo(n) que determine si un número es primo o no:
```sh
  > es_primo(17)
  > True
  > es_primo(221)
  > False
```

- Usando la función es_primo, escriba la función i_esimo_primo(i) que entregue el i-ésimo número primo.
```sh
  > i_esimo_primo(1)
  > 2
  > i_esimo_primo(20)
  > 71
 ```

- Usando las funciones anteriores, escriba la función primeros_primos(m) que entregue una lista de los primeros m números primos:
 ```sh
  > primeros_primos(10)
  > [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
 ```

- Usando las funciones anteriores, escriba la función primos_hasta(m) que entregue una lista de los primos menores o iguales que m:
```sh
  > primos_hasta(19)
  > [2, 3, 5, 7, 11, 13, 17, 19]
```

- Cree un módulo llamado primos.py que contenga todas las funciones anteriores. Al ejecutar primos.py como un programa por sí solo, debe mostrar, a modo de prueba, los veinte primeros números primos. Al importarlo como un módulo, esto no debe ocurrir.


### Setup command
`sudo -H pip3 install pytest`

### Run command
`pytest`

### Notes
- pip's install path is not included in the PATH var by default, so without installing via `sudo -H`, pytest would be unaccessible.
